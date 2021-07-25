from django import forms
from django.core import validators


class CaputureInputForm(forms.Form):


        bcg =     forms.CharField(required=True, error_messages={'required': 'Please select bcg'})
        pent1 =   forms.CharField(required=True, error_messages={'required': 'Please select pent1'})
        pent2 =   forms.CharField(required=True, error_messages={'required': 'Please select pent2'})
        pent3 =   forms.CharField(required=True, error_messages={'required': 'Please select pent3'})
        rota1 =   forms.CharField(required=True, error_messages={'required': 'Please select rota1'})
        rota2 =   forms.CharField(required=True, error_messages={'required': 'Please select rota2'})
        polio1 =  forms.CharField(required=True, error_messages={'required': 'Please select polio1'})
        polio2 =  forms.CharField(required=True, error_messages={'required': 'Please select polio2'})
        pnuemo1 = forms.CharField(required=True, error_messages={'required': 'Please select pnuemo1'})
        pneumo2 = forms.CharField(required=True, error_messages={'required': 'Please select pnuemo2'})
        rtss1 =   forms.CharField(required=True, error_messages={'required': 'Please select rtss1'})














