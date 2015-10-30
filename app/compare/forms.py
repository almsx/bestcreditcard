from django import forms

class Formulary(forms.Form):

	entity = forms.IntegerField(required=True)
	creditcard = forms.IntegerField(required=True)
	balance = forms.FloatField(required=True)