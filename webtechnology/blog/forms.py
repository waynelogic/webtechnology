from django import forms
class UserForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Возраст клиента'}), label="Имя клиента")
    age=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Возраст клиента'}), label="Возраст клиента")
    email=forms.EmailField(widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'E-mail'}), label="E-mail")
    familyStatus = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), label="Женат/а?")

