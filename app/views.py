
from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.templatetags.static import static
from datetime import datetime, timedelta, time


def rep(Request):
	today = datetime.now().date()
	semesters = Semester.objects.all().order_by('-date').filter(date__lte=today)
	addme = ""
	for semester in semesters:
		addon = """
			<h2>%s</h2>
			<div id ="cover">
	
			</div>
			<table>
			<tr class="tablehead">
				<th>Song</th>
				<th>Solosit</th>
				<th>Artist</th>
				<th>Arranger</th>
			</tr>
		""" % semester.name
		addme = "%s%s" % (addme, addon)
		reps = Rep.objects.filter(semester=semester)
		for rep in reps:
			name = rep.song.name
			artist = rep.song.artist
			arrangers = rep.arranger.all()
			arrangers_string = ""
			for arranger in arrangers:
				arrangers_string = "%s %s" % (arranger.name,arrangers_string)
			if(rep.soloist_text == ""):
				soloists = rep.soloist.all()
				soloist_string = ""
				for soloist in soloists:
					soloist_string = "%s %s" % (soloist.name,soloist_string)
			else:
				soloist_string = rep.soloist_text

			addon = """
			<tr>
			<td>%s</th>
			<td>%s</th>
			<td>%s</th>
			<td>%s</th>
			</tr>""" % (name,soloist_string,artist,arrangers_string)
			addme = "%s%s" % (addme, addon)

		addme = "%s</table>" % addme


	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3>%s" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': addme,'sidebar':sidebar_string})


def contact(Request):
	page = get_object_or_404(Page, name="contact")
	
	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3>%s" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': page.content,'sidebar':sidebar_string})

def members(Request):
	today = datetime.now().date()
	semester = Semester.objects.all().order_by('-date').filter(date__lte=today)[:1]

	memberships = Membership.objects.filter(semester=semester[0]);
	singers = []
	for membership in memberships:
		singers.append([membership.singer,membership.officer]);

	text = "<h1>%s</h1>" % semester[0].name;

	for item in singers:
		singer = item[0]
		if item[1] is None:
			officer = ""
		else:
			officer = item[1]
		
		grad = singer.graduation_semester.name;
		image_url  = static('images/hallie.png');
		singer_info = "%s<br />%s<br />%s<br />%s" % (singer.name,grad,singer.voice_part,officer)
		text = "%s<div id ='member'><a href='singer/%s'><img src='%s'><div id='memberinfo'>%s</div></a></div>" % (text,singer.id,image_url,singer_info)

	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3>%s" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': text,'sidebar':sidebar_string})

def singer(Request,id):
	singer = get_object_or_404(Singer, id=id)
	singer_string = """
	<h3>%s</h3><h4>%s, %s</h4>
	<p>%s</p>
	""" % (singer.name,singer.voice_part,singer.graduation_semester.name,singer.blurb)

	memberships = Membership.objects.filter(singer=singer);
	info = "";
	for membership in memberships:
		info = "%s<h3>%s</h3>" % (info,membership.semester.name)
		if membership.officer is not None:
			info = "%s<br />%s" % (info,membership.officer.name)

	singer_string = "%s%s" % (singer_string,info)

	sidebar_string = "";
	sidebars = Sidebar.objects.all()

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3>%s" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': singer_string,'sidebar':sidebar_string})


def index(Request):
	page = get_object_or_404(Page, name="home")
	
	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3>%s" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': page.content,'sidebar':sidebar_string})

def gallery(Request):
	page = get_object_or_404(Page, name="gallery")
	
	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3>%s" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': page.content,'sidebar':sidebar_string})

def events(Request):
	page = get_object_or_404(Page, name="events")
	
	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3>%s" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': page.content,'sidebar':sidebar_string})

