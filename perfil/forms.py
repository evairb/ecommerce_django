from django import forms
from django.contrib.auth.models import User
from perfil import models


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False, widget=forms.PasswordInput()  , label='Senha', help_text='Senha precisa ter 6 caracteres'
    )
    password2 = forms.CharField(
        required=False, widget=forms.PasswordInput()  , label='Confirmacao Senha'  
    )
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'username','password', 'email',
                  'password2')


    def clean(self, *args, **kwargs):
        data = self.data
        cleaned =self.cleaned_data
        validation_error_msgs = {}

        usuario_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()


        error_msg_user_exists = 'Usuario ja existe'
        error_msg_email_exists = 'Email ja existe'
        error_msg_password_math = 'As duas Senhas não conferem'
        error_msg_password_short = 'A senha contem menos de 6 caracteres'
        error_msg_required_field = 'Este campo e obrigatorio'
        
        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists
                
                if email_db:
                    if email_data != email_db.email:
                        validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_math
                    validation_error_msgs['password2'] = error_msg_password_math

                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_msg_password_short

                

        else:
            if usuario_db:
                validation_error_msgs['username'] = error_msg_user_exists
            
            if email_db:
                validation_error_msgs['email'] = error_msg_email_exists

            if password_data != password2_data:
                validation_error_msgs['password'] = error_msg_password_math
                validation_error_msgs['password2'] = error_msg_password_math

            if len(password_data) < 6:
                validation_error_msgs['password'] = error_msg_password_short

            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field

            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field

        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))