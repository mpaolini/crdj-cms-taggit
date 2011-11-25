from django import forms
from taggit.forms import TagField

class UpdateTagsForm(forms.Form):
    tags = TagField()
