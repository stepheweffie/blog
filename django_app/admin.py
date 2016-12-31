from django.contrib import admin
from .models import Post
from django import forms
import mathfield

class LessonAdminForm(forms.ModelForm):

    class Meta:
        widgets = {
            'latex': mathfield.MathFieldWidget
        }


class LessonAdmin(admin.ModelAdmin):
    form = LessonAdminForm

admin.site.register(Post, LessonAdmin)