from MyApp.models import Office


office = Office.objects.create(
    name="Central Office",
    address="123 Main St, Example City",
    latitude=40.7128,
    longitude=-74.0060
)


print(Office.objects.all())
