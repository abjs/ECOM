# mv 0001_initial.py api/migrations
from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="abjs" ,#admin user name
                          email="itsmeabjs@gmail.com",#Enter The Email
                          is_staff=True,
                          is_superuser=True,
                          )
        user.set_password("password") #Enter Your Admin Password
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
