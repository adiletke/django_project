from django import forms

class UserConfigForm(forms.Form):
    class Meta:
        model = forms
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'id': 'inputPassword', 'name': 'password', 'type': 'password', 'autocomplete': 'off'}),
        }


