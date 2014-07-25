from django.db import models
import datetime
#from tinymce import models as tinymce_models

class Document(models.Model):
	docfile = models.FileField(upload_to='%Y/%m/%d')
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Page(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField()

	def __unicode__(self):
		return self.name

class Sidebar(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField()

	def __unicode__(self):
		return self.name

class Semester(models.Model):
	name = models.CharField(max_length=50)
	date = models.DateField(help_text="date which this semester becomes the current semester")
	concert = models.CharField(max_length=100,null=True,blank=True)
	members = models.ManyToManyField('Singer', through='Membership')
	picture = models.ForeignKey(Document,null=True, blank=True, default = None)

	def __unicode__(self):
		return self.name

class Officer(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Song(models.Model):
	name = models.CharField(max_length=50)
	artist = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Singer(models.Model):
	name = models.CharField(max_length=100)
	blurb = models.TextField()
	voice_part = models.CharField(max_length=20)
	graduation_semester = models.ForeignKey(Semester,related_name="graduation_semester")
	school_email = models.EmailField(null=True,blank=True)
	alumni_email = models.EmailField(null=True,blank=True)

	senior_solo = models.ForeignKey(Song,null=True, blank=True, default = None)
	picture = models.ForeignKey(Document,null=True, blank=True, default = None)
	
	def __unicode__(self):
		return self.name

class Membership(models.Model):
	singer = models.ForeignKey(Singer)
	semester = models.ForeignKey(Semester)
	officer = models.ForeignKey(Officer,null=True, blank=True)

	def __unicode__(self):
		return "%s in %s" % (self.singer, self.semester)

class Rep(models.Model):
	semester = models.ForeignKey(Semester)
	song = models.ForeignKey(Song)
	soloist = models.ManyToManyField(Singer,related_name="soloist")
	arranger = models.ManyToManyField(Singer,related_name="arranger")
	soloist_text = models.CharField(max_length=100,null=True, blank=True)

	def __unicode__(self):
		return "%s in %s" % (self.song,self.semester)
