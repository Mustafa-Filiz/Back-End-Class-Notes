from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    GENDER = (
		("1", "Male"),
		("2", "Female"),
		("3", "Other"),
		("4", "Prefer not to say"),
	)
    gender = models.CharField(max_length=50, choices=GENDER)
    image = models.ImageField(upload_to="student/", default="default.png")
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
    