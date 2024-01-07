from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    address = models.TextField()
    phone = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
    