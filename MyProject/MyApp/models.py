from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=12)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
         return f"{self.name} {self.lastname}"
    class Meta:
        db_table = 'asma'
         
class AsmaEmail(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email         
        

   