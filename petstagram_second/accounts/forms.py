from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model


UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email',)


'''
We can override "AuthenticationForm" and add it to "LoginUserView" in "form_class" field to
set placeholders.
'''
# class LoginUserForm(auth_forms.AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "placeholder": "Username"}))
#     password = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "placeholder": "Password"}),
#     )


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender',)

        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Image',
            'gender': 'Gender',
        }
