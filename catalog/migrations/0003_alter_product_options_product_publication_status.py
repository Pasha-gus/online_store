# Generated by Django 4.2.2 on 2025-01-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_created_at_alter_product_description_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "permissions": [("can_unpublish_product", "can unpublish product")],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="publication_status",
            field=models.BooleanField(default=False, verbose_name="Статус публикации"),
        ),
    ]