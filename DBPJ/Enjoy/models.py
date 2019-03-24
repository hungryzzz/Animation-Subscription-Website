from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=40, null=False)
    pw = models.CharField(max_length=20, null=False)
    email = models.EmailField(db_index=True, null=False)
    legal = models.BooleanField(null=False)


class Managers(models.Model):
    name = models.CharField(max_length=40, null=False)
    id_num = models.CharField(max_length=20, null=False)
    pw = models.CharField(max_length=20, null=False)


class Animation(models.Model):
    img = models.ImageField(upload_to='img', null=True)
    name = models.CharField(max_length=40, null=False)
    pub_time = models.DateField(null=False)
    update_time = models.CharField(max_length=60, null=False)
    style = models.CharField(max_length=30, null=True)
    tag1 = models.CharField(max_length=30, null=True)
    tag2 = models.CharField(max_length=30, null=True)
    va1 = models.CharField(max_length=40, null=True)
    va2 = models.CharField(max_length=40, null=True)
    va3 = models.CharField(max_length=40, null=True)
    va4 = models.CharField(max_length=40, null=True)
    state = models.CharField(max_length=40, null=False)
    link = models.URLField(null=True)


class Subscribe_Comment(models.Model):
    user_name = models.CharField(max_length=40, null=False)
    ani_name = models.CharField(max_length=40, null=False)
    comment = models.CharField(max_length=300, null=True)


class Not_sub(models.Model):
    user_name = models.CharField(max_length=40, null=False)
    ani_name = models.CharField(max_length=40, null=False)




