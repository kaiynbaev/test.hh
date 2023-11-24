from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserModelManager
# from posts.models import Posts
 
class UserModel(AbstractUser):
    username = models.CharField(unique=True, default='', max_length=70)
    email = models.EmailField(db_index=True, unique=True, max_length=200, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)
    objects = UserModelManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
