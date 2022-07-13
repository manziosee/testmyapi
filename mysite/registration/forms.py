from django import forms

from student.models import Student


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student  
        fields = "__all__"  