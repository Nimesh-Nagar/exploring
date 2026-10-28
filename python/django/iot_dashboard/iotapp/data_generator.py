from faker import Faker
import random
from datetime import datetime, timedelta

from .models import Device, Sensor     

def generate_fake_data(num_devices=10, num_sensors_per_device=3):

    fake = Faker()

    for i in range(num_devices):
        device = Device.objects.create(
            name=fake.word().title() + f" Device {i+1}", # Generate a random iot device name
            description=fake.sentence(nb_words=10),
            created_at=fake.date_time_between(start_date='-1y', end_date='now'), # Generate a random creation date within the last year
            is_online=random.choice([True, False])
        )

        for j in range(num_sensors_per_device):
            Sensor.objects.create(
                device=device,
                name=fake.word().title() + f" Sensor {j+1}", # Generate a random sensor name
                sensor_type=random.choice(["Temperature", "Humidity", "Pressure", "Motion"])
            )

if __name__ == "__main__":
    generate_fake_data()    


# to run this script, use the following command in your terminal:
# python manage.py shell
# from iotapp.data_generator import generate_fake_data
# generate_fake_data()  

# Note: Make sure to run this script in the Django shell to have access to the models and database.

'''
how to verify the generated data:   
1. Open the Django admin interface (usually at http://localhost:8000/admin/).
2. Log in with your admin credentials.
3. Navigate to the "Devices" section to see the list of generated devices.
4. Click on a device to view its details, including the associated sensors.
5. You should see the generated device names, descriptions, creation dates, and online status.
6. You can also check the "Sensors" section to see the list of generated sensors and their types.   


'''