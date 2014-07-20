from django.db import models
import datetime
#from tinymce import models as tinymce_models

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
	date = models.DateTimeField()
	concert = models.CharField(max_length=100,null=True,blank=True)

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
	active_semesters = models.ManyToManyField(Semester)

	senior_solo = models.ForeignKey(Song,null=True, blank=True, default = None)
	
	def __unicode__(self):
		return self.name
	
class Rep(models.Model):
	semester = models.ForeignKey(Semester)
	song = models.ForeignKey(Song)
	soloist = models.ManyToManyField(Singer,related_name="soloist")
	arranger = models.ManyToManyField(Singer,related_name="arranger")
	soloist_text = models.CharField(max_length=100,null=True, blank=True)

	def __unicode__(self):
		return "%s in %s" % (self.song,self.semester)
