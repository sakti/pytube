import floppyforms as forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        exclude = ("user")
        model = Video
