from django.forms import ModelForm
from app.models import cadastro 
# Create the form class.
class cadastroForm(ModelForm):
    class Meta:
        model = cadastro
        fields = ['user_name', 'user_lastname', 'user_company', 'user_choices', 'user_text1','user_test' ]  