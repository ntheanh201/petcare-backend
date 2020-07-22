from django.contrib.auth.models import User, AbstractUser
from django.db import models
from .enums import PostType, ReactionType, GenderType, NotificationType
from django.conf import settings
import uuid


def custom_media_path(instance, filename):
    file_ext = filename.split(".")[-1]
    return str(uuid.uuid4()) + "." + file_ext


class Image(models.Model):
    img_url = models.FileField(
        upload_to=custom_media_path, max_length=100, default="default.jpg"
    )



