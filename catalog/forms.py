from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms, BooleanField


from catalog.models import Product, Version

WRONG_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('create_at', 'updated_at',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        for word in WRONG_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Слова паразиты')

        return cleaned_data


class VersionForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_current(self):
        is_current = self.cleaned_data['is_current']
        if not is_current:
            raise ValidationError('Выберите одну активную версию')
        return is_current


