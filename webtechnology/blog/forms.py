from django import forms
class UserForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Имя клиента")
    age=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Возраст клиента")
    # email=forms.EmailField(widget=forms.EmailField(attrs={'class': 'form-control'}), label="E-mail")
    familyStatus = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), label="Женат/а?")

