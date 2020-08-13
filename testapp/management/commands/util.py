import names
import  pytz
import random
import uuid

from datetime import datetime
from pprint import pprint
from randomtimestamp import randomtimestamp
from testapp.models import *


def generate_random_timestamp(year):
    datetime = randomtimestamp(year, False)
    datetime_object = datetime.strftime('%b %d %Y %I:%M%p')
    return datetime_object

# generate dummy data
def generate_dummy_data(data_points, activity_period_number, year):
    data = []
    for i in range(data_points):
        # id = str(i+1)
        id = str(uuid.uuid1())
        real_name = names.get_full_name()
        tz = random.choice(pytz.all_timezones)

        activity_periods = []
        for i in range(activity_period_number):
            timestamp1 = generate_random_timestamp(year)
            timestamp2 = generate_random_timestamp(year)

            # sort the two time stamps
            t1 = datetime.strptime(timestamp1, "%b %d %Y %I:%M%p")
            t2 = datetime.strptime(timestamp2, "%b %d %Y %I:%M%p")
            start_time = t2.strftime('%b %d %Y %I:%M%p') if (t1-t2).days>0 else t1.strftime('%b %d %Y %I:%M%p')
            end_time = t1.strftime('%b %d %Y %I:%M%p') if (t1-t2).days>0 else t2.strftime('%b %d %Y %I:%M%p')

            activity_periods.append({'start_time': start_time, 'end_time': end_time})

        json = {'id': id, 'real_name': real_name, 'tz': tz, 'activity_periods': activity_periods}
        data.append(json)
    return data


def populate_database(data_points=2, activity_period_number=3, year=2020):
    # clear previous data
    User.objects.all().delete()
    ActivityPeriod.objects.all().delete()

    dummy_data = generate_dummy_data(data_points, activity_period_number, year)
    # insert data into the Models here
    for data in dummy_data:
        User.objects.create(
            uid = data['id'],
            real_name = data['real_name'],
            tz = data['tz']
        )
        ActivityPeriod.objects.create(
            uid = data['id'],
            activity_periods = data['activity_periods']
        )
