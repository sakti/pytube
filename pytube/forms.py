import floppyforms as forms
import os
from .models import Video

EXT_WHITELIST = (".mp4", ".ogv", ".webm")


class VideoForm(forms.ModelForm):

    def clean_raw(self):
        data = self.cleaned_data["raw"]
        filename = data.name
        ext = os.path.splitext(filename)[1]
        ext = ext.lower()
        if ext not in EXT_WHITELIST:
            raise forms.ValidationError("Not Allowed filetype!")

        return data

    class Meta:
        exclude = ("user")
        model = Video
