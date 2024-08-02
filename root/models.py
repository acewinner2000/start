from django.db import models

class service(models.Model):
    name1 = models.CharField(max_length=100,default="برای سرویس هااین فیلد را پر کنید")
    content1 = models.TextField(default="برای سرویس هااین فیلد را پر کنید")  
    
    created_at1 = models.DateTimeField(auto_now_add=True)
    updated_at1 = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=False)
    def __str__(self):
        return self.name1
class so(models.Model):   
    name2 = models.CharField(max_length=100,default="برای سرویس های ویژه این فیلد را پر کنید")
    content2 = models.TextField(default="برای سرویس های ویژه این فیلد را پر کنید.")  
    
    created_at2 = models.DateTimeField(auto_now_add=True)
    updated_at2 = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=False)
    
    def __str__(self):
        return self.name2
