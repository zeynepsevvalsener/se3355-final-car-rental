from MyApp.models import Office

# Yeni bir Office kaydı oluştur
office = Office.objects.create(
    name="Central Office",
    address="123 Main St, Example City",
    latitude=40.7128,
    longitude=-74.0060
)

# Veritabanına kaydedildiğini doğrula
print(Office.objects.all())
