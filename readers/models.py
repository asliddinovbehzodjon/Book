from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

class Kitobxon(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     name = models.CharField("Kitobxon nomi",max_length=500,help_text="Kitobxon nomini kiriting",default="Kitobxon")
     starred = models.IntegerField(verbose_name="Kitobxonni bahosi",default=0)
     def image(self):
          width = 50
          height = 50
          image_url = "https://cdn-icons-png.flaticon.com/512/219/219983.png"
          html = '<img src="{url}" width="{width}" height="{height}" />'
          return format_html(
          html.format(url=image_url, width=width,
          height=height)
          )
     class Meta:
          db_table = "Kitobxonlar"
          verbose_name = "Kitobxon "
          verbose_name_plural = "Kitobxonlar "

     def __str__(self):
          return self.name
     
     