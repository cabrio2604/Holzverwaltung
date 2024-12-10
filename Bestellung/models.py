from django.db import models

# Create your models here.


class Lieferant(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.CharField(("E-Mail"), max_length=50)
    telefon = models.CharField(("Telefonnummer"), max_length=50)
    

    class Meta:
        verbose_name = ("Lieferant")
        verbose_name_plural = ("Lieferanten")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Lieferant_detail", kwargs={"pk": self.pk})


class Lieferung(models.Model):
    datum = models.DateField(("Lieferdatum"), auto_now=False, auto_now_add=False)
    lieferant = models.ForeignKey(Lieferant, verbose_name=("Lieferant"), on_delete=models.RESTRICT)

    class Meta:
        verbose_name = ("Lieferung")
        verbose_name_plural = ("Lieferungen")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Lieferung_detail", kwargs={"pk": self.pk})