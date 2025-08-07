# Generated manually on 2025-08-07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_update_sub_column_choices'),
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
                    ('Cyber Security', 'Cyber Security'),
                    ('Computer Science Engineering (CSE)', 'Computer Science Engineering (CSE)'),
                    ('Mechanical Engineering', 'Mechanical Engineering'),
                    ('Civil Engineering', 'Civil Engineering'),
                    ('Electrical Engineering', 'Electrical Engineering'),
                    ('MBBS (Bachelor of Medicine & Bachelor of Surgery)', 'MBBS (Bachelor of Medicine & Bachelor of Surgery)'),
                    ('BDS (Bachelor of Dental Surgery)', 'BDS (Bachelor of Dental Surgery)'),
                    ('BAMS (Ayurveda)', 'BAMS (Ayurveda)'),
                    ('BHMS (Homeopathy)', 'BHMS (Homeopathy)'),
                ],
                max_length=255,
            ),
        ),
    ]
