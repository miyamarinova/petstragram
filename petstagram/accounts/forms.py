
from django.contrib.auth import forms as auth_forms,get_user_model

UserModel = get_user_model()
class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    user = None
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )

# change te user from django/admin
class PetstagramChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel

