# Generated manually on 2025-08-07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_sub_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='payment_amount',
            new_name='fees',
        ),
        migrations.AddField(
            model_name='course',
            name='sub_column',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
