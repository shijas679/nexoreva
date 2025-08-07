from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sub_course',
            field=models.CharField(max_length=255, choices=[('', '---------')], blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, choices=[('IT', 'IT'), ('Engineering', 'Engineering'), ('Medical', 'Medical')]),
        ),
    ]
