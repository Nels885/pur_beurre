from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import no_style
from django.db.utils import IntegrityError
from django.db import connection
from app.models import Product, Backup

import logging as log

from ._apirest import ApiRest
from ._glob import Glob


class Command(BaseCommand):
    """
    Commands for integrating values from OpenFoodFacts
    """
    help = 'Update database for Pur Beurre'

    def add_arguments(self, parser):
        """
        Options for interactions with the database
        :param parser:
            Command Name
        """
        parser.add_argument(
            '--update',
            action='store_true',
            dest='update',
            help='Update database',
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete all data in the database',
        )

    def handle(self, *args, **options):
        """
        Method that executes the option chosen by the user
        :param args:
            Parameters for the execution of the command
        :param options:
            Command name
        :return:
            Integration or deletion of data in the database
        """
        if options['update']:
            api = ApiRest(log)
            for cat_name in Glob.categories:
                results = api.get_request(cat_name)
                for result in results:
                    try:
                        Product.objects.create(
                            name=result['product_name'],
                            nutrition_grades=result['nutrition_grades'],
                            url=result['url'],
                            front_picture=result['image_front_url'],
                            nutrition_picture=result['image_nutrition_url'],
                            category=cat_name
                        )
                    except KeyError as err:
                        log.error(f"Manque la valeur: {err}")
                    except IntegrityError as err:
                        log.error(f"{err}")

        elif options['delete']:
            Product.objects.all().delete()
            Backup.objects.all().delete()

            sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Product, Backup])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)


