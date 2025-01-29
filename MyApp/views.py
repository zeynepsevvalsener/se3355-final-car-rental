from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from datetime import datetime
import math

from .models import Car, Order, Contact, UserProfile, Office
from .forms import RegisterForm, SearchForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            # UserProfile güncelle
            profile = user.userprofile  # create_user_profile sinyali ile oluşmuş olmalı
            profile.country = form.cleaned_data['country']
            profile.city = form.cleaned_data['city']
            if request.FILES.get('photo'):
                profile.photo = request.FILES['photo']
            profile.save()

            messages.success(request, _("Your account has been created! You can now sign in."))
            return redirect('signin')
        else:
            messages.error(request, form.errors)
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def signin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername', '')
        loginpassword = request.POST.get('loginpassword', '')

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, _("Successfully logged in!"))
            return redirect('home')
        else:
            messages.error(request, _("Invalid credentials"))
            return redirect('signin')

    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, _("Successfully logged out!"))
    return redirect('home')

def vehicles(request):
    cars = Car.objects.all()

    # Filtreleme parametreleri
    make = request.GET.get('make', '')
    transmission = request.GET.get('transmission', '')
    order_by_price = request.GET.get('order_by_price', '')

    if make:
        cars = cars.filter(car_name__icontains=make)
    if transmission:
        cars = cars.filter(transmission__iexact=transmission)
    if order_by_price == 'asc':
        cars = cars.order_by('cost_per_day')
    elif order_by_price == 'desc':
        cars = cars.order_by('-cost_per_day')

    context = {'cars': cars}
    return render(request, 'vehicles.html', context)

def bill(request):
    # Araç listesini form seçimi için gönderiyoruz
    cars = Car.objects.all()
    return render(request, 'bill.html', {'cars': cars})

def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname','')
        billemail = request.POST.get('billemail','')
        billphone = request.POST.get('billphone','')
        billaddress = request.POST.get('billaddress','')
        billcity = request.POST.get('billcity','')
        car_id = request.POST.get('cars11','')
        dayss = request.POST.get('dayss','0')
        date_str = request.POST.get('date','')
        fl = request.POST.get('fl','')
        tl = request.POST.get('tl','')

        selected_car = None
        if car_id.isdigit():
            try:
                selected_car = Car.objects.get(pk=int(car_id))
            except Car.DoesNotExist:
                selected_car = None

        new_order = Order(
            name=billname,
            email=billemail,
            phone=billphone,
            address=billaddress,
            city=billcity,
            car=selected_car,
            days_for_rent=int(dayss) if dayss.isdigit() else 0,
            loc_from=fl,
            loc_to=tl
        )

        if date_str:
            try:
                new_order.date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except:
                pass

        new_order.save()
        messages.success(request, _("Booking confirmed!"))
        return redirect('home')
    else:
        return render(request, 'bill.html')

def contact(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname','')
        contactemail = request.POST.get('contactemail','')
        contactnumber = request.POST.get('contactnumber','')
        contactmsg = request.POST.get('contactmsg','')

        new_contact = Contact(
            name=contactname,
            email=contactemail,
            phone_number=contactnumber,
            message=contactmsg
        )
        new_contact.save()
        messages.success(request, _("Your message has been sent successfully!"))

    return render(request, 'contact.html')

def search(request):
    """
    Ofis araması: office/date/time
    """
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            office_name = form.cleaned_data['office']
            date_val = form.cleaned_data['date']
            time_val = form.cleaned_data['time']

            offices = Office.objects.all()
            if office_name:
                offices = offices.filter(name__icontains=office_name)

            # Tarih ve saate göre ek mantık (örneğin müsaitlik) eklenebilir
            return render(request, 'search_results.html', {
                'offices': offices,
                'search_date': date_val,
                'search_time': time_val,
            })
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    2 koordinat arası km cinsinden mesafe
    """
    R = 6371  # Earth's radius (km)
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = (math.sin(dphi / 2) ** 2) + math.cos(phi1) * math.cos(phi2) * (math.sin(dlambda / 2) ** 2)
    distance = 2 * R * math.asin(math.sqrt(a))
    return distance

def nearest_offices(request):
    """
    Kullanıcı tarayıcı konumunu alıp ?lat=...&lng=... parametreleriyle buraya yönlendiriyor.
    30 km yakındaki ofisleri listeleyelim.
    """
    try:
        user_lat = float(request.GET.get('lat', 0))
        user_lng = float(request.GET.get('lng', 0))
    except:
        user_lat, user_lng = 0, 0

    max_distance_km = 30
    offices = Office.objects.all()
    nearby = []
    for off in offices:
        dist = haversine_distance(user_lat, user_lng, off.latitude, off.longitude)
        if dist <= max_distance_km:
            nearby.append((off, dist))

    # Mesafeye göre sırala
    nearby_sorted = sorted(nearby, key=lambda x: x[1])

    return render(request, 'search_results.html', {
        'offices': [n[0] for n in nearby_sorted],
        'distances': [n[1] for n in nearby_sorted],
        'user_lat': user_lat,
        'user_lng': user_lng,
    })
