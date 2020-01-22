from django.contrib.auth.forms import UserCreationForm
from ecommerce.models import MyUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = '__all__'
