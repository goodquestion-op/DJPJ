import csv
from itertools import count
from django.core.management import BaseCommand
from MyApp1.models import teacher,Areas,Courses
from django.db.models import Min
from django.db import transaction

class Command(BaseCommand):
    help = "python manage.py importCSV --path H:(The CSV file path that you want to import) \n python manage.py importCSV --list (will list all duplicates in the datatbase) \n python manage.py importCSV --del (delets all duplicates in the data base)"
    

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
        parser.add_argument('--path2', type=str)
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--del', action='store_true')

    def handle2(self,*args, **kwargs):

        path = kwargs['path2']
        duplicate_field = 'Course' 

        keep_ids = Courses.objects.values(duplicate_field).annotate(
            min_id=Min('id')
        ).values_list('min_id', flat=True)

        to_delete = Courses.objects.exclude(id__in=keep_ids)
        count = to_delete.count()

        if kwargs['list']:
            if to_delete:
                for i in to_delete:
                    print(Courses.Course)
            else:
                print('No duplicates found')
        if kwargs['del']:
            # Delete in an atomic transaction - Basically means do it all if it can, do nothing if it can't
            with transaction.atomic():
                to_delete.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} duplicate items.'))


        with open(path, 'rt', encoding='utf-8-sig') as f:
            reader = csv.reader(f, dialect='excel')

            for row in reader:
                Courses.objects.create(Course=row[0])
            print('Added' + row[0])

    def handle(self,*args, **kwargs):

        path = kwargs['path']
        duplicate_field = 'Name' 

        keep_ids = teacher.objects.values(duplicate_field).annotate(
            min_id=Min('id')
        ).values_list('min_id', flat=True)

        to_delete = teacher.objects.exclude(id__in=keep_ids)
        count = to_delete.count()

        if kwargs['list']:
            if to_delete:
                for teach in to_delete:
                    print(teach.Name)
            else:
                print('No duplicates found')
        if kwargs['del']:
            # Delete in an atomic transaction - Basically means do it all if it can, do nothing if it can't
            with transaction.atomic():
                to_delete.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} duplicate items.'))


        with open(path, 'rt', encoding='utf-8-sig') as f:
            reader = csv.reader(f, dialect='excel')

            for row in reader:
                teacher.objects.create(Name=row[0])
            print('Added' + row[0])

