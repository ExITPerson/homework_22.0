from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        models = Product
        fields = ['name', 'description', 'image', 'category', 'price',]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = [
            'казино', 'криптовалюта', 'крипта',
            'биржа', 'дешево', 'бесплатно',
            'обман', 'полиция', 'радар',
        ]

        for word in forbidden_words:
            if word.lower() in name.lower() or word.lower() in description.lower():
                self.add_error('name', f'Слово {word} не может содержаться в имени или описании')

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')