from django.db import models
from django.contrib.auth.models import User



class Services(models.Model):

    name = models.CharField(max_length=120)
    content = models.TextField(default="test service")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)
    


class ask(models.Model):

    name = models.CharField(max_length=120)
    content = models.TextField(default="test ask")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)

class Skills(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


        
    class Meta:
        ordering = ("created_at",)


    def __str__(self):
        return self.name




class Trainers(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to= "trainers" , default="static\img\hero-bg-light.webp")
    skills = models.ManyToManyField(Skills)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ("created_at",)


    def __str__(self):
        return self.user.username



class SpecialServices(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default="no content")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)




class Property(models.Model):
    name = models.TextField(default='test')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)




class Pricing(models.Model):
    
    name = models.CharField(max_length=120)
    content = models.TextField(default="test")
    fee = models.FloatField(default=0)
    questions = models.ManyToManyField(Property)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("created_at",)

