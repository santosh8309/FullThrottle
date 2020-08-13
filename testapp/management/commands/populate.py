from django.core.management.base import BaseCommand
from django.utils import timezone

from testapp.management.commands.util import populate_database

class Command(BaseCommand):
    help = 'Populate Models with random data'

    def add_arguments(self, parser):
        parser.add_argument('dp')
        parser.add_argument('ap')
        parser.add_argument('year')

    def handle(self, *args, **kwargs):
        # populate database with random data
        # print('kwargs', kwargs)
        data_points = int(kwargs['dp'])
        activity_period_number = int(kwargs['ap'])
        year = int(kwargs['year'])
        populate_database(data_points, activity_period_number, year)
