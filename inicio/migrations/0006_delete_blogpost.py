# Generated by Django 5.0.6 on 2024-06-17 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_alter_post_author_alter_post_categories_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
