# Generated by Django 4.0.2 on 2024-04-27 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]
    operations = [
        migrations.RunSQL("""
            INSERT INTO product_product (
                id,
                name,
                category_id
            )
            SELECT
                id,
                name,
                category_id
            FROM
                catalog_product;
        """, reverse_sql="""
            INSERT INTO catalog_product (
                id,
                name,
                category_id
            )
            SELECT
                id,
                name,
                category_id
            FROM
                product_product;
        """)
    ]
