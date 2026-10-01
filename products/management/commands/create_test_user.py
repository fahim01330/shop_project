from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
class Command(BaseCommand):
 def handle(self,*args,**kwargs):
  User=get_user_model(); u,_=User.objects.get_or_create(username="testuser"); u.set_password("testpassword123"); u.save(); t,_=Token.objects.get_or_create(user=u); self.stdout.write(f"Username: {u.username}\nPassword: testpassword123\nToken: {t.key}")
