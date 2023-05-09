from django.db import models

class Announcement(models.Model):
    title = models.CharField(verbose_name="Başlık",max_length=250,null=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True,null=True)
    image = models.ImageField(verbose_name="Görüntü",null=True,blank=True,upload_to="announcement",default="announcement.jpg")
    create_at = models.DateTimeField(verbose_name="Oluşturma Tarihi",auto_now_add=True)
    update_at =models.DateTimeField(verbose_name="Düzenleme Tarihi",auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.title()
        return super(Announcement, self).save(*args, **kwargs)
    class Meta:
      verbose_name = "Duyurular"
    
class Produck(models.Model):
    title = models.CharField(verbose_name="Başlık",max_length=250,null=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True,null=True)
    image = models.ImageField(verbose_name="Görüntü",null=True,blank=True,upload_to="produck",default="produck.png")
    create_at = models.DateTimeField(verbose_name="Oluşturma Tarihi",auto_now_add=True)
    update_at =models.DateTimeField(verbose_name="Düzenleme Tarihi",auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.title()
        return super(Produck, self).save(*args, **kwargs)
    class Meta:
      verbose_name = "Ürünler"