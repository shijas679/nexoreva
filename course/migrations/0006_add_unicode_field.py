# Generated manually on 2025-08-07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_update_sub_column_choices_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='unicode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
