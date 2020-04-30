from django.db import models

# Create your models here.
class Nav(models.Model):
	title = models.CharField(max_length=200)
	thumb = models.ImageField(upload_to="media")





	def _str_(self):
		return self.title
    
