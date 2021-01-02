from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="abjs",
                          email="itsmeabjs@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          )
        user.set_password("abjs")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
