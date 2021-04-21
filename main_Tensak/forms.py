from django import forms
from .models import UsersGuideRequests, Procreator, Model
from uuid import uuid4
import os


class UserGuideRequestsForm(forms.ModelForm):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                                             'placeholder': 'Имя', 'required': 'required'}))
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'id': 'email',
                                                                'class': 'form-control',
                                                                'placeholder': 'Електронная почта',
                                                                'required': 'required'}))
    user_number = forms.DecimalField(max_digits=10, decimal_places=0, widget=forms.NumberInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                                                                      'placeholder': 'Номер телефона', 'required': 'required'}))
    user_message = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'name': 'message', 'id': 'message', 'class': 'form-control',
               'rows': '1', 'placeholder': 'Сообщение',
               'required': 'required'}))

    class Meta():
        model = UsersGuideRequests
        fields = ('user_name', 'user_email', 'user_number', 'user_message')


class ProcreatorAddForm(forms.ModelForm):
    title = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type': 'text', 'id': 'title',
                                                                        'class': 'form-control',
                                                                        'placeholder': 'Название производителя',
                                                                        'required': 'required'}))
    is_visible = forms.BooleanField(initial=True, required=False)
    popular_level = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number', 'id': 'category_order',
                                                                        'class': 'form-control',
                                                                        'placeholder': 'Популярность производителя',
                                                                        'required': 'required'}))

    class Meta:
        model = Procreator
        fields = ('title', 'popular_level', 'is_visible')


class ModelAddForm(forms.ModelForm):
    def get_file_name_models(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/models/', filename)

    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'id': 'title',
                                                                         'class': 'form-control',
                                                                         'placeholder': 'Модель',
                                                                         'required': 'required'}))
    price = forms.DecimalField(max_digits=7, decimal_places=2, widget=forms.TextInput(attrs={'type': 'number', 'id': 'price',
                                                                        'class': 'form-control',
                                                                        'placeholder': 'Цена',
                                                                        'required': 'required'}))
    is_visible = forms.BooleanField(initial=True, required=False)
    description = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'type': 'text', 'id': 'description',
                                                                         'class': 'form-control',
                                                                         'placeholder': 'Описание/комментарий',
                                                                         'required': 'required'}))
    photo = forms.ImageField(widget=forms.ImageField)
    procreator = forms.Select()
    is_sale = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Model
        fields = ('title', 'price', 'is_visible', 'description', 'photo', 'procreator', 'is_sale')