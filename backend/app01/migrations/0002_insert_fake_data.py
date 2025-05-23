# Generated by Django 5.1.6 on 2025-05-23 08:04
from django.db import migrations
from faker import Faker
from django.utils import timezone


def create_fake_data(apps, schema_editor):
    Tag = apps.get_model('app01', 'Tag')
    User = apps.get_model('app01', 'User')
    Note = apps.get_model('app01', 'Note')

    fake = Faker()

    for _ in range(10):
        user = User.objects.create(username=fake.user_name(),
                                   email=fake.email(),
                                   password=fake.password(length=10))

        tags = []
        for i in range(3):
            tag = Tag.objects.create(name=fake.word(), user=user)
            tags.append(tag)

        for i in range(3):
            note = Note.objects.create(
                user=user,
                title=fake.sentence(),
                content=fake.text(),
                created_at=timezone.now(),
            )
            note.tags.add(tags[i])  # 每篇筆記對應一個標籤

    print("✅ 每位使用者皆有三篇筆記與三個對應的個人標籤")


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [migrations.RunPython(create_fake_data)]
