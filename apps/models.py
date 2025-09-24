from django.core.validators import FileExtensionValidator
from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE, TextField, ImageField, BooleanField, \
    SmallIntegerField


class Product(Model):
    name = CharField(max_length=255, verbose_name="Nomi")
    price = IntegerField(default=0)
    description = TextField(blank=True)
    is_premium = BooleanField(default=False)
    short_description = TextField(null=True)
    discount = SmallIntegerField(default=0, help_text='foizda hisoblanadi')
    image = ImageField(upload_to='products/%Y/%m/%d', validators=[FileExtensionValidator(['jpg', 'png'])],
                       help_text="faqat jpg yukla")
    category = ForeignKey('apps.Category', on_delete=CASCADE)

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return f"{self.id} - {self.name}"


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.name}"
