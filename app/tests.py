from django.test import TestCase
from app.models import *
import datetime

def tests():
	semester = Semester("spring 2014", datetime.now())
