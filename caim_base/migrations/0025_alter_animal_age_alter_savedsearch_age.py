# Generated by Django 4.1 on 2023-02-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caim_base", "0024_merge_20221102_1237"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="age",
            field=models.CharField(
                choices=[
                    ("BABY", "Baby (< 1 year)"),
                    ("YOUNG", "Young (1-3 years)"),
                    ("ADULT", "Adult (3-8 years)"),
                    ("SENIOR", "Senior (8+ years)"),
                ],
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="savedsearch",
            name="age",
            field=models.CharField(
                blank=True,
                choices=[
                    ("BABY", "Baby (< 1 year)"),
                    ("YOUNG", "Young (1-3 years)"),
                    ("ADULT", "Adult (3-8 years)"),
                    ("SENIOR", "Senior (8+ years)"),
                ],
                default=None,
                max_length=8,
                null=True,
            ),
        ),
    ]
