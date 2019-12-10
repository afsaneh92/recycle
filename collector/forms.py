from django import forms
from django.forms import ModelForm, modelformset_factory
from . import models


# class ReceiverForm(forms.Form):
#     fullname = forms.CharField(label='fullname', max_length=40)
#     mobile_number = forms.CharField(label='mobile_number', max_length=40)

class ReceiverClassForm(ModelForm):
    class Meta:
        model = models.Receiver
        fields = ['fullname', 'mobile_number', 'manager']


class RecyclingRequestClassForm(ModelForm):
    class Meta:
        model = models.RecyclingRequest
        fields = ['requester', 'receiver', 'address', 'status', 'trash_type']


RecyclingRequestModelFormset = modelformset_factory(
    models.RecyclingRequest,
    fields=('requester', 'receiver', 'address', 'status', 'trash_type' ),
    extra=1,
    # widgets={'name': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter Book Name here'
    #     })
    # }
)