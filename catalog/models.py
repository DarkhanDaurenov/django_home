from django.db import models

NULLABLE_FIELDS = {"blank": True, "null": True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name="название категорий")
    category_description = models.TextField(
        verbose_name="описание категорий", **NULLABLE_FIELDS
    )

    def __str__(self):
        return f"{self.category_name} - {self.category_description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("id",)


class Product(models.Model):
    product_category = models.ForeignKey(
        "catalog.Category", on_delete=models.CASCADE, related_name="products"
    )
    product_name = models.CharField(
        max_length=100, verbose_name="наименование продукта"
    )
    product_description = models.CharField(
        max_length=100, verbose_name="описание продукта"
    )
    product_picture = models.ImageField(
        upload_to="goods/", verbose_name="изображение продукта", **NULLABLE_FIELDS
    )
    product_price = models.IntegerField(verbose_name="цена продукта")
    create_at = models.DateTimeField(
        auto_now_add=True, verbose_name="дата создания записи"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата обновления записи"
    )

    def __str__(self):
        return (
            f"{self.product_category} - {self.product_name} - {self.product_description}\n"
            f"{self.product_picture} - {self.product_price} - {self.create_at} - {self.updated_at}"
        )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("product_name",)


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        verbose_name="Версия",
        **NULLABLE_FIELDS,
    )
    number_version = models.CharField(
        max_length=150, verbose_name="версия номера", unique=True
    )
    version_name = models.CharField(max_length=150, verbose_name="название версий")
    is_current = models.BooleanField(default=False, verbose_name="признак версий")

    def __str__(self):
        return f"{self.product} - {self.number_version} - {self.version_name} - {self.is_current}"

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версий"
