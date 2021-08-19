from django.forms import ModelForm
from .models import ThemSuaXoa

class ThemForm(ModelForm):
    class Meta:
        model = ThemSuaXoa
        fields = '__all__'
