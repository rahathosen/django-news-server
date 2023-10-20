import os
import django
from django.core.management import call_command

# Get a list of all installed apps
from django.apps import apps

installed_apps = [app.name for app in apps.get_app_configs()]

# Create a directory to store the data files
os.makedirs('data_dump', exist_ok=True)

# Dump data from each model in each app
for app_name in installed_apps:
    app_data_file = f'data_dump/{app_name}.json'
    with open(app_data_file, 'w') as data_file:
        call_command('dumpdata', app_name, stdout=data_file)

print('Data has been dumped from all apps and models.')
