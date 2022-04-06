from django.db import models
'''
    As you all known to customizing User model of django auth app.
    we use 2 classes 
        1.AbstractUser
            IT used add some extra fields into User model.
        2.AbstractBaseUser
            It used create User model with all user define fields.
            It never user any built-in fields of Django user model.

            when use AbstractBaseUser for customizing we need 
            create our own UserManager

'''

from django.contrib.auth.models import BaseUserManager
class MyUserManager(BaseUserManager):
    def create_user(self,mobile_Number,password,**extra_fields):
        if not mobile_Number:
            raise ValueError('Users must have an Mobile Number')
        user = self.model(mobile_Number=mobile_Number,**extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user;


    def create_superuser(self,mobile_Number,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('user_Role','owner')
        return self.create_user(mobile_Number,password,**extra_fields)



from django.contrib.auth.models import AbstractBaseUser
class MyUser(AbstractBaseUser):
    userId = models.BigAutoField(primary_key=True)
    first_Name  = models.CharField(max_length=30)
    last_Name  = models.CharField(max_length=30)
    mobile_Number = models.BigIntegerField(unique=True)
    user_Role = models.CharField(max_length=10)
    is_superuser = models.BooleanField(default=False)
    address = models.TextField()

    objects = MyUserManager()
    
    USERNAME_FIELD="mobile_Number"
    REQUIRED_FIELDS=['first_Name','last_Name']
    