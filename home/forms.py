from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import User



class ContactForms(ModelForm):
    class Meta:
        model = User
        fields = ("name", "email", "topic", "body")
        widgets = {
            "name": TextInput(attrs={"class":"form-control", "placeholder":"نام خانوادگی", "required":"required"}),
            "email": EmailInput(attrs={"class":"form-control", "placeholder":"ایمیل", "required":"required"}),
            "topic": TextInput(attrs={"class":"form-control", "placeholder":"موضوع", "required":"required"}),
            "body": Textarea(attrs={"class":"form-control", "placeholder":"پیام", "required":"required"}),
        }