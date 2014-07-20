from django.db import models
import datetime
#from tinymce import models as tinymce_models

class Sidebar(models.Model):
	name = models.CharField(max_length=30)
#	blurb = tinymce_models.HTMLField()

class Semester(models.Model):
	name = models.CharField(max_length=50)
	date = models.DateTimeField()

	def __unicode__(self):
		return self.name
		
class Song(models.Model):
	name = models.CharField(max_length=50)
	artist = models.CharField(max_length=50)
	soloist = models.CharField(max_length=50)
	arranger = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Singer(models.Model):
	name = models.CharField(max_length=100)
	blurb = models.TextField()
	voice_part = models.CharField(max_length=20)
	graduation_semester = models.ForeignKey(Semester)
	school_email = models.EmailField(null=True,blank=True)
	alumni_email = models.EmailField(null=True,blank=True)

	def __unicode__(self):
		return self.name
	
