from django.db import models

NULLABLE = {"blank": True, "null": True}


class Contacts(models.Model):
    email = models.EmailField(verbose_name="Электронная почта")
    country = models.CharField(max_length=50, verbose_name="страна")
    city = models.CharField(max_length=50, verbose_name="город")
    street = models.CharField(max_length=50, verbose_name="улица")
    house_number = models.CharField(max_length=5, verbose_name="номер дома")

    def __str__(self):
        return (
            f"{self.email} {self.country} {self.city} {self.street} {self.house_number}"
        )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ("city",)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    model = models.CharField(max_length=100, verbose_name="модель")
    release_date = models.DateField(
        auto_now_add=True, verbose_name="дата выхода продукта на рынок"
    )

    def __str__(self):
        return f"{self.name} {self.model} {self.release_date}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Network(models.Model):
    level = ((0, "Завод"), (1, "розничная сеть"), (2, "индивидуальный предприниматель"))

    name = models.CharField(max_length=100, verbose_name="Название")
    contacts = models.OneToOneField(
        "Contacts", on_delete=models.CASCADE, verbose_name="Контакты", **NULLABLE
    )
    product = models.ManyToManyField("Product", verbose_name="Продукт", blank=True)
    supplier = models.ForeignKey(
        "Network", on_delete=models.SET_NULL, verbose_name="Поставщик", **NULLABLE
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком",
    )
    created_at = models.TimeField(
        auto_now_add=True, **NULLABLE, verbose_name="Время создания"
    )
    level = models.IntegerField(
        choices=level, verbose_name="Уровень иерархии", default=0
    )

    def __str__(self):
        return f"{self.name} {self.contacts} {self.product} {self.supplier} {self.debt} {self.created_at}"

    class Meta:
        verbose_name = "Сеть"
        verbose_name_plural = "Сети"
        ordering = ("contacts",)
