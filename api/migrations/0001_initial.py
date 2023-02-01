# Generated by Django 4.0.2 on 2022-03-16 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0008_alter_article_hits'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.article')),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=('blog.article',),
        ),
    ]
