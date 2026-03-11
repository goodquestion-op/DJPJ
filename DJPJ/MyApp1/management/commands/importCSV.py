import csv
from itertools import count
from django.core.management import BaseCommand
from MyApp1.models import teacher
from django.db.models import Min
from django.db import transaction

class Command(BaseCommand):
    help = "This is some help text"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--del', action='store_true')



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
                teacher.objects.create(Name=row[0], Area=row[1])
            print('Added' + row[0])

