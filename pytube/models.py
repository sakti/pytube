from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage
import mimetypes
import os

mimetypes.init()


class Video(models.Model):
    name = models.CharField(max_length=200,
            help_text="Video name",
            db_index=True)
    raw = models.FileField(upload_to="raw")
    video = models.FileField(upload_to="video",
            editable=False)
    desc = models.TextField()
    user = models.ForeignKey(User)
    created_time = models.DateTimeField(auto_now_add=True,
                    db_index=True,
                    editable=False)
    last_updated_time = models.DateTimeField(auto_now=True,
                    editable=False)
    view_count = models.BigIntegerField(default=0,
                    editable=False)

    def get_mimetype(self):
        file_ext = os.path.splitext(self.raw.name)[1]
        mimetype = mimetypes.types_map.get(file_ext)
        return mimetype

    def increment_view(self):
        self.view_count += 1
        self.save()

    def __unicode__(self):
        return "%s" % self.name


def delete_filefield(sender, **kwargs):
    video = kwargs.get("instance")
    default_storage.delete(video.raw.path)
    if video.video:
        default_storage.delete(video.video.path)

post_delete.connect(delete_filefield, Video)
