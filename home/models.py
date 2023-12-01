from .manager import BaseModel
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# class OwnProfilePage(BaseModel):
#     name= models.CharField(max_length=255)
    
#     def __str__(self) -> str:
#         return self.name


class Category(BaseModel):
    name = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.name
    
class Tags(BaseModel):
    name = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model) :
    firstname = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField() 
    
    def __str__(self) -> str:
        return self.firstname


    
    

class News(BaseModel):
    title = models.CharField(max_length=255) #0
    img = models.ImageField(upload_to='news/') #1
    view_count = models.BigIntegerField(default=0, blank=True, null=True)#2
    body = RichTextField() #3
    slug = models.SlugField() #4
    user = models.ForeignKey( User ,on_delete= models.SET_NULL , null= True) #5
    category = models.ForeignKey(Category ,on_delete=models.CASCADE, null= True , related_name = 'category') #6
    tags = models.ManyToManyField(Tags, related_name="tags") #7
    is_active = models.BooleanField(default= True)
    
    def __str__(self) -> str:
        return self.title
    

