from django.core.management.base import BaseCommand, CommandError
from app.models import Product

import logging as log

from package.apirest import ApiRest
from package.glob import Glob


class Command(BaseCommand):
    help = 'update database for app'

    def add_arguments(self, parser):
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
            help='Delete data in the database',
        )

    def handle(self, *args, **options):
        if options['update']:
            api = ApiRest(log)
            for cat_name in Glob.converDb["app_category"]:
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

        elif options['delete']:
            pass
