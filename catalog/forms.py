from django.forms import ModelForm, BooleanField
from catalog.models import Product
from django.core.exceptions import ValidationError


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                       "радар"]

    class Meta:
        model = Product
        exclude = ("updated_at",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        contains = any(word in name.lower() for word in self.FORBIDDEN_WORDS)
        if contains:
            raise ValidationError("В названии есть запрещенные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        contains = any(word in description.lower() for word in self.FORBIDDEN_WORDS)
        if contains:
            raise ValidationError("В описании есть запрещенные слова")
        return description

    def clean_purchase_price(self):
        price = self.cleaned_data.get("purchase_price")
        if price is not None and price <= 0:
            raise ValidationError("Цена не может быть отрицательной или равной 0.")
        return price
