
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
		if semester.picture is None:
			image = ""
		else:
			image = "<img src='/media/%s' width=700px>" % semester.picture.docfile
		addon = """
			<h3><a href="semester/%s">%s</a></h3>
			%s
			<table class="rep">
			<tr class="tablehead">
				<th>Song</th>
				<th>Solosit</th>
				<th>Artist</th>
				<th>Arranger</th>
			</tr>
		""" % (semester.id,semester.name,image)
		addme = "%s%s" % (addme, addon)
		reps = Rep.objects.filter(semester=semester)
		for rep in reps:
			name = rep.song.name
			artist = rep.song.artist

			if(rep.song.arranger_text == ""):
				arrangers = rep.song.arranger.all()
				arrangers_string = ""
				for arranger in arrangers:
					arrangers_string = "<a href='singer/%s'>%s</a> %s" % (arranger.id,arranger.name,arrangers_string)
			else:
				arrangers_string = rep.song.arranger_text

			if(rep.soloist_text == ""):
				soloists = rep.soloist.all()
				soloist_string = ""
				for soloist in soloists:
					soloist_string = "<a href='singer/%s'>%s</a> %s" % (soloist.id,soloist.name,soloist_string)
			else:
				soloist_string = rep.soloist_text

			if rep.link == "":
				title = name;
			else:
				title = "<a href='%s'>%s</a>" % (rep.link,name)

			addon = """
			<tr>
			<td>%s</th>
			<td>%s</th>
			<td>%s</th>
			<td>%s</th>
			</tr>""" % (title,soloist_string,artist,arrangers_string)
			addme = "%s%s" % (addme, addon)

		addme = "%s</table>" % addme


	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': addme,'sidebar':sidebar_string})


def semester(Request,id):
	today = datetime.now().date()
	semester = get_object_or_404(Semester, id=id)

	addme = ""
	memberships = Membership.objects.filter(semester=semester).order_by('singer__name');
	singers = []
	for membership in memberships:
		singers.append([membership.singer,membership.officer]);

	text = "<br />"

	for item in singers:
		singer = item[0]
		if item[1] is None:
			officer = ""
		else:
			officer = item[1]
		
		grad = singer.graduation_semester.name;
		if singer.picture is None:
			image_url  = static('images/default_person.png');
		else:
			image_url  = "/media/%s" % singer.picture.docfile
		singer_info = "%s<br />%s<br />%s<br />%s" % (singer.name,grad,singer.voice_part,officer)
		text = "%s<div id ='member_sem'><a href='../singer/%s'><img height='130px' src='%s'><div id='memberinfo_sem'>%s</div></a></div>" % (text,singer.id,image_url,singer_info)

	if semester.picture is None:
		image = ""
	else:
		image = "<img src='/media/%s' width=700px>" % semester.picture.docfile

	addon = """
		<h2>%s</h2>
		%s
		<table class="rep">
		<tr class="tablehead">
			<th>Song</th>
			<th>Solosit(s)</th>
			<th>Artist</th>
			<th>Arranger(s)</th>
		</tr>
	""" % (semester.name,image)
	addme = "%s%s" % (addme, addon)
	reps = Rep.objects.filter(semester=semester)
	for rep in reps:
		name = rep.song.name
		artist = rep.song.artist

		if(rep.song.arranger_text == ""):
			arrangers = rep.song.arranger.all()
			arrangers_string = ""
			for arranger in arrangers:
				arrangers_string = "<a href='../singer/%s'>%s</a> %s" % (arranger.id,arranger.name,arrangers_string)
		else:
			arrangers_string = rep.song.arranger_text

		soloist_string = ""
		if(rep.soloist_text == ""):
			soloists = rep.soloist.all()
			for soloist in soloists:
				soloist_string = "<a href='../singer/%s'>%s</a> %s" % (soloist.id,soloist.name,soloist_string)
		else:
			soloist_string = rep.soloist_text

		if rep.link == "":
			title = name;
		else:
			title = "<a href='%s'>%s</a>" % (rep.link,name)

		addon = """
		<tr>
		<td>%s</th>
		<td>%s</th>
		<td>%s</th>
		<td>%s</th>
		</tr>""" % (title,soloist_string,artist,arrangers_string)
		addme = "%s%s" % (addme, addon)

	addme = "%s</table>" % addme


	addme = "%s%s" % (addme,text)

	events = Event.objects.filter(semester=semester).order_by('date');

	#events count 0
	text = "<div style='clear:both;'>"
	for event in events:
		if event.link == "":
			title = event.title;
		else:
			title = "<a href='%s'>%s</a>" % (event.link,event.title)

		text = "%s<div id='event'><b>%s</b><br /><span style='font-size:12px'>%s, %s</span><p style='font-size:14px'>%s</p></div>" % (text,title,event.date.strftime('%b, %d'),event.location,event.blurb)

	addme = "%s%s</div>" % (addme,text)


	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': addme,'sidebar':sidebar_string})

def contact(Request):
	page = get_object_or_404(Page, name="contact")
	
	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': page.content,'sidebar':sidebar_string})

def members(Request):
	today = datetime.now().date()
	semester = Semester.objects.all().order_by('-date').filter(date__lte=today)[:1]

	memberships = Membership.objects.filter(semester=semester[0]).order_by('singer__name');
	singers = []
	for membership in memberships:
		singers.append([membership.singer,membership.officer]);

	text = ""

	for item in singers:
		singer = item[0]
		if item[1] is None:
			officer = ""
		else:
			officer = item[1]
		
		grad = singer.graduation_semester.name;
		if singer.picture is None:
			image_url  = static('images/default_person.png');
		else:
			image_url  = "/media/%s" % singer.picture.docfile
		singer_info = "%s<br />%s<br />%s<br />%s" % (singer.name,grad,singer.voice_part,officer)
		text = "%s<div id ='member'><a href='singer/%s'><img src='%s'><div id='memberinfo'>%s</div></a></div>" % (text,singer.id,image_url,singer_info)

	text = "%s<p style='clear:both;'><a href='alumni'>View Tarpeggio Alumni</a></p>" % text
	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': text,'sidebar':sidebar_string})

def alumni(Request):
	#order these peeps by most recent grad semester than by name
	today = datetime.now().date()
	semesters = Semester.objects.all().order_by('-date').filter(date__lte=today)

	allmysingers = [];
	#first is to elimate current semester ppl who haven't graduated obvi
	first = True;
	for semester in semesters:
		if first == False:
			singers = Singer.objects.all().filter(graduation_semester=semester).order_by('name');
			for singer in singers:
					allmysingers.append(singer)
		else:
			first = False;

	text = ""
	for singer in allmysingers:

		grad = singer.graduation_semester.name;
		if singer.picture is None:
			image_url  = static('images/default_person.png');
		else:
			image_url  = "/media/%s" % singer.picture.docfile
		singer_info = "%s<br />%s<br />%s<br />" % (singer.name,grad,singer.voice_part)
		text = "%s<div id ='member'><a href='singer/%s'><img src='%s'><div id='memberinfo'>%s</div></a></div>" % (text,singer.id,image_url,singer_info)

	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': text,'sidebar':sidebar_string})

def singer(Request,id):
	singer = get_object_or_404(Singer, id=id)

	if singer.picture is None:
		image_url  = "";
	else:
		image_url  = "<img height=200px style='float:left;margin-right:20px;border: 3px solid #101D30;' src='/media/%s'>" % singer.picture.docfile

	singer_string = """
	%s<h3 style='margin-bottom:2px;'>%s</h3><h4 style='margin:0px;'>%s, %s</h4>
	<p>%s</p>
	""" % (image_url,singer.name,singer.voice_part,singer.graduation_semester.name,singer.blurb)

	sidebar_string = "";

	memberships = Membership.objects.filter(singer=singer).order_by('-semester__date');
	sidebar_string = "<h3>Active Semesters:</h3>";
	for membership in memberships:
		officer = ""
		if membership.officer is not None:
			officer = " (%s)" % (membership.officer.name)

		sidebar_string = "%s<a href='../semester/%s'>%s%s</a><br />" % (sidebar_string,membership.semester.id,membership.semester.name,officer)
	sidebar_string = "%s<p></p>"  % (sidebar_string)

	if singer.senior_solo is None:
		senior_solo  = "";
	else:
		senior_solo  = "<h3>Senior Solo:</h3>%s by %s</p>" % (singer.senior_solo.name,singer.senior_solo.artist)

	sidebar_string = "%s%s"  % (sidebar_string,senior_solo)


	return render_to_response('app/index.html', {'text': singer_string,'sidebar':sidebar_string})


def index(Request):
	page = get_object_or_404(Page, name="home")
	
	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': page.content,'sidebar':sidebar_string})

def gallery(Request):
	page = get_object_or_404(Page, name="gallery")
	
	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': page.content,'sidebar':sidebar_string})

def events(Request):
	today = datetime.now().date()
	semester = Semester.objects.all().order_by('-date').filter(date__lte=today)[:1]

	events = Event.objects.filter(semester=semester[0]).order_by('date');

	#events count 0
	text = ""
	for event in events:
		if event.link == "":
			title = event.title;
		else:
			title = "<a href='%s'>%s</a>" % (event.link,event.title)

		text = "%s<h2>%s</h2>%s %s<br />%s" % (text,title,event.date,event.location,event.blurb)

	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': text,'sidebar':sidebar_string})
