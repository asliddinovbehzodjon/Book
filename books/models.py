from django.db import models
from readers.models import Kitobxon
DEFAULT = 'static/images/book.png'
# Create your models here.
class Category(models.Model):
        name = models.CharField(max_length=5000,help_text="Kategoriyaga nom bering...")
        def __str__(self):
                 return self.name
        class Meta:
                db_table = "Kategoriyalar"
                verbose_name = 'Kategoriya '
                verbose_name = 'Kategoriyalar '    
class Kitoblar(models.Model):
    
     category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='kitoblar',default=1)
     name = models.CharField(verbose_name="Kitob nomini kiriting",max_length=1000,help_text="Kitob nomini kiriting")
     author = models.TextField(verbose_name="Kitob muallifini yozing",help_text="Kitob muallifini yozing")
     description = models.TextField(verbose_name="Kitob haqida yozing",help_text="Kitob haqida yozing")
     image = models.ImageField(upload_to='images',default=DEFAULT)
     user = models.ForeignKey(Kitobxon,on_delete=models.SET_DEFAULT,default='Kitobxon',related_name='books')
     file = models.FileField(upload_to='books')
     uploaded = models.DateTimeField(auto_now_add=True)
     downloaded = models.IntegerField(default=1)
     size = models.CharField(max_length=500,null=True,blank=True)
     
     @property
     def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext
     def save(self,*args,**kwargs):
              if not self.size:
                       self.size = self.filesize
              return super().save(*args,**kwargs)
     def uploader(self):
          return self.user.name
     class Meta:
          db_table = "Kitoblar"
          verbose_name = "Kitob "
          verbose_name_plural = "Kitoblar "

     def __str__(self):
          return self.name
     
class Reklama(models.Model):
    link  = models.CharField(max_length=400,help_text="Telegram kanal linkini tashang")
    channel_id = models.IntegerField(help_text='Kanal ID sini kiriting')
    class Meta:
          db_table = "Kanallar"
          verbose_name = "Kanal "
          verbose_name_plural = "Kanallar "

    def __str__(self):
          return self.link