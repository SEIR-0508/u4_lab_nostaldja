# Generated by Django 4.2.3 on 2023-07-17 20:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0004_remove_fad_decade_alter_decade_end_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fad',
            name='decade',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.decade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fad',
            name='description',
            field=models.TextField(),
        ),
    ]
