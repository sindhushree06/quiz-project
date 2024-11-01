from django.db import models
from django.contrib.auth.models import User
# Extending User Model Using a One-To-One Link

     
class QuestionModel(models.Model):
    question=models.TextField(max_length=200)
    op1=models.TextField()
    op2=models.TextField()
    op3=models.TextField()
    op4=models.TextField()
    ans=models.TextField()
    def __str__(self):
         return self.question

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,verbose_name='User Object')
    #email_adress=models.CharField(max_length=55,unique=True,null=True,verbose_name='Email')
    bio=models.TextField(blank=True,null=True)
    profile_img=models.ImageField(upload_to='profile_images',default='user.png',blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    gender=models.CharField(max_length=6,choices=GENDER,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
 



    




