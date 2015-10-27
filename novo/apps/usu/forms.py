from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=30,
        required=False)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=30,
        required=False)
    job_title = forms.CharField(label='Empresa', widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=50,
        required=False)
    email = forms.CharField( label='Email',widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=75,
        required=False)
    url = forms.CharField(label='URL', widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=50,
        required=False)
    location = forms.CharField(label='lugar', widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=50,
        required=False)
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=50,
        required=False)
    nit = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}), 
        required=False)
    fax = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=50,
        required=False)
    fecha_fun = forms.DateField(input_formats=['%Y-%m-%d'],widget=forms.TextInput(attrs={'class':'form-control'}), 
        required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'job_title', 'email', 'url', 'location', 'titulo', 'nit', 'fecha_fun', 'fax',]




class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), 
        label="Old password",
        required=True)

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), 
        label="New password",
        required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), 
        label="Confirm new password",
        required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']



    def clean(self):
        super(ChangePasswordForm, self).clean()
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        id = self.cleaned_data.get('id')
        user = User.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class(['Old password don\'t match'])
        if new_password and new_password != confirm_password:
            self._errors['new_password'] = self.error_class(['Passwords don\'t match'])
        return self.cleaned_data