from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_category():
        with open('category.json') as file:
            category_data = json.load(file)
        return category_data

    @staticmethod
    def json_read_product():
        with open('product.json') as file:
            product_data = json.load(file)
        return product_data

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category_data in Command.json_read_category():
            category_for_create.append(
                Category(
                    id=category_data['pk'],
                    category_name=category_data['fields']['category_name'],
                    category_description=category_data['fields']['category_description']
                )
            )

        Category.objects.bulk_create(category_for_create)

        for product_data in Command.json_read_product():
            product_for_create.append(
                Product(
                    id=product_data['pk'],
                    product_category_id=product_data['fields']['product_category'],
                    product_name=product_data['fields']['product_name'],
                    product_description=product_data['fields']['product_description'],
                    product_picture=product_data['fields']['product_picture'],
                    product_price=product_data['fields']['product_price'],
                    create_at=product_data['fields']['create_at'],
                    updated_at=product_data['fields']['updated_at']
                )
            )

        Product.objects.bulk_create(product_for_create)