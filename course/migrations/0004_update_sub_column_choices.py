# Generated manually on 2025-08-07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_add_sub_column_and_rename_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='sub_column',
            field=models.CharField(
                blank=True,
                choices=[
                    ('', '---------'),
                    ('Web Development', 'Web Development'),
                    ('Data Science', 'Data Science'),
                    ('Networking', 'Networking'),
                    ('Mechanical', 'Mechanical'),
                    ('Civil', 'Civil'),
                    ('Electrical', 'Electrical'),
                    ('MBBS', 'MBBS'),
                    ('Nursing', 'Nursing'),
                    ('Pharmacy', 'Pharmacy'),
                ],
                max_length=255,
            ),
        ),
    ]
