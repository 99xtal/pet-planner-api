# Generated by Django 4.0.4 on 2022-05-20 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('pet_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.petcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_units', models.CharField(choices=[('g', 'grams'), ('kg', 'kilograms'), ('cups', 'cups'), ('whole', 'whole')], max_length=10)),
                ('time', models.TimeField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.food')),
                ('pet', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
    ]
