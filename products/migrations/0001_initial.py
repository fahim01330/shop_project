from django.db import migrations, models
from django.core.validators import MinValueValidator
class Migration(migrations.Migration):
 initial=True
 dependencies=[]
 operations=[migrations.CreateModel(name="Product",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("name",models.CharField(max_length=100)),("description",models.TextField()),("price",models.DecimalField(decimal_places=2,max_digits=10,validators=[MinValueValidator(0.01,message="Price must be greater than zero.")])),("stock",models.IntegerField(validators=[MinValueValidator(0,message="Stock cannot be negative.")]))])]
