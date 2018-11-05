from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.db.models.signals import post_save
from django.dispatch import receiver

class Type(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50);

class Post(models.Model) :
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100, default='Non Title')

class Wysiwyg(summer_model.Attachment) :
    wysiwyg_field = summer_fields.SummernoteTextField(default='')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, default=None)

class Image(models.Model) :
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    img_file = models.ImageField(upload_to='file/image', blank=True, default='file/image/default_image.jpg')
