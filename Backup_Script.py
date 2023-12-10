import os
import django
import csv

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<Your Project Name>.settings") # Change to your Project Name

# Ensure Django is initialized
django.setup()

# Now you can import your models
from yourapp.models import yourModel # Change to your app name and your model name


# Export data to CSV
queryset = yourModel.objects.all()
with open('Render_Backup.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'email_id', 'description']  # Replace with your actual field names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for instance in queryset:
        writer.writerow({'id': instance.id, 'name': instance.name, 'email_id': instance.email_id, 'description': instance.description}) # Replace with your actual field names

print("Backup completed successfully.")
