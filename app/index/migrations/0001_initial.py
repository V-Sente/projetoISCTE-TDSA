# Generated by Django 4.1.1 on 2022-09-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('n_telemovel', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1)),
            ],
        ),

        migrations.CreateModel(
            name='Criador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('email_organizacao', models.EmailField(max_length=254)),
                ('organizacao', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
    ]