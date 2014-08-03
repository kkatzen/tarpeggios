
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
			image = "<a href='semester/%s'><img src='/media/%s' width=700px></a>" % (semester.id, semester.picture.docfile)
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
				arranger_count = 0;
				for arranger in arrangers:
					if(arranger_count > 0):
						arrangers_string = "%s<br />" % arrangers_string
					arranger_count = arranger_count +1
					arrangers_string = "<a href='singer/%s'>%s</a> %s" % (arranger.id,arranger.name,arrangers_string)
			else:
				arrangers_string = rep.song.arranger_text

			if(rep.soloist_text == ""):
				soloists = rep.soloist.all()
				soloist_string = ""
				singer_count = 0;
				for soloist in soloists:
					if(singer_count > 0):
						soloist_string = "%s<br />" % soloist_string
					singer_count = singer_count + 1
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
			arranger_count = 0
			for arranger in arrangers:
				if(arranger_count > 0):
					arrangers_string = "%s<br />" % arrangers_string
				arranger_count = arranger_count +1
				arrangers_string = "<a href='../singer/%s'>%s</a> %s" % (arranger.id,arranger.name,arrangers_string)
		else:
			arrangers_string = rep.song.arranger_text

		soloist_string = ""
		if(rep.soloist_text == ""):
			soloists = rep.soloist.all()
			soloist_count = 0;
			for soloist in soloists:
				if(soloist_count > 0):
					soloist_string = "%s<br />" % soloist_string
				soloist_count = soloist_count +1
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
		if event.blurb == "":
			blurb = "";
		else:
			blurb = "<p style='font-size:12px'>%s</p>" % (event.blurb)

		text = "%s<div id='event'><b>%s</b><br /><span style='font-size:13px'>%s, %s</span>%s</div>" % (text,title,event.date.strftime('%B %d'),event.location,blurb)

	addme = "%s%s</div>" % (addme,text)


	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': addme,'sidebar':sidebar_string})

def contact(Request):
	today = datetime.now().date()
	semester = Semester.objects.all().order_by('-date').filter(date__lte=today)[:1]

	president_pos = Officer.objects.all().filter(name="President")[:1]
	presidents = Membership.objects.all().filter(officer=president_pos,semester=semester[0])

	music_dirs_pos = Officer.objects.all().filter(name="Music Director")[:1]
	music_dirs = Membership.objects.all().filter(officer=music_dirs_pos,semester=semester[0])

	business_pos = Officer.objects.all().filter(name="Business Manager")[:1]
	business = Membership.objects.all().filter(officer=business_pos,semester=semester[0])

	social_pos = Officer.objects.all().filter(name="Social Chair")[:1]
	socials = Membership.objects.all().filter(officer=social_pos,semester=semester[0])

	text = ""
	if(len(business) > 0):
		text = "%s<h4>Business Manager</h4>" % (text)
		names = ""
		i = 0
		for business_m in business:
				i = i +1
				if i < 2:
					names = "%s<a href='singer/%s'>%s</a>  " % (names,business_m.singer.id,business_m.singer.name)
				else:
					names = "%s or <a href='singer/%s'>%s</a>  " % (names,business_m.singer.id,business_m.singer.name)
		text = "%sTo book the Tarpeggios for a performance, contact %sat unctarpeggios@gmail.com." % (text,names)

	if(len(music_dirs) > 0):
		text = "%s<br /><h4>Music Director</h4>" % (text)
		names = ""
		i = 0
		for music_dir in music_dirs:
				i = i +1
				if i < 2:
					names = "%s<a href='singer/%s'>%s</a>  " % (names,music_dir.singer.id,music_dir.singer.name)
				else:
					names = "%s or <a href='singer/%s'>%s</a>  " % (names,music_dir.singer.id,music_dir.singer.name)
		text = "%sFor information about auditions and questions about the Tarpeggios' music, contact %sat music.tarpeggios@gmail.com." % (text,names)

	if(len(socials) > 0):
		text = "%s<br /><h4>Social Chair</h4>" % (text)
		names = ""
		i = 0
		for social in socials:
				i = i +1
				if i < 2:
					names = "%s<a href='singer/%s'>%s</a>  " % (names,social.singer.id,social.singer.name)
				else:
					names = "%s or <a href='singer/%s'>%s</a>  " % (names,social.singer.id,social.singer.name)
		text = "%sFor social concerns, contact %sat unctarpeggios@gmail.com." % (text,names)

	if(len(presidents) > 0):
		text = "%s<br/><h4>President</h4>" % (text)
		names = ""
		i = 0
		for president in presidents:
				i = i +1
				if i < 2:
					names = "%s<a href='singer/%s'>%s</a>  " % (names,president.singer.id,president.singer.name)
				else:
					names = "%s or <a href='singer/%s'>%s</a>  " % (names,president.singer.id,president.singer.name)
				
		text = "%sFor any other questions, contact %sat unctarpeggios@gmail.com." % (text,names)


	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': text,'sidebar':sidebar_string})

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
		text = "%s<div id ='member_sem'><a href='singer/%s'><img src='%s'><div id='memberinfo_sem'>%s</div></a></div>" % (text,singer.id,image_url,singer_info)

	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': text,'sidebar':sidebar_string})

def singer(Request,id):
	singer = get_object_or_404(Singer, id=id)

	singer_string = """
	<p>%s</p>
	""" % (singer.blurb)

	if singer.picture is None:
		image_url  = "";
	else:
		image_url  = "<img width=180px style='float:center;border: 3px solid #101D30;' src='/media/%s'>" % singer.picture.docfile

	memberships = Membership.objects.filter(singer=singer).order_by('-semester__date');
	sidebar_string = "%s<h3 style='margin-bottom:0px;padding-bottom:0px;text-align:center;'>%s</h3><p style='margin-top:4px;font-size:15px;text-align:center;'>%s<br />%s</p><h3 style='margin-bottom:0px;padding-bottom:0px;text-align:center;'>Active Semesters:</h3><p style='text-align:center'>" % (image_url,singer.name,singer.voice_part,singer.graduation_semester.name)
	for membership in memberships:
		officer = ""
		if membership.officer is not None:
			officer = " (%s)" % (membership.officer.name)

		sidebar_string = "%s<a href='../semester/%s'>%s%s</a><br />" % (sidebar_string,membership.semester.id,membership.semester.name,officer)
	sidebar_string = "%s</p>"  % (sidebar_string)

	if singer.senior_solo is None:
		senior_solo  = "";
	else:
		senior_solo  = "<h3 style='margin-bottom:0px;padding-bottom:0px;text-align:center;'>Senior Solo:</h3><p style='text-align:center'>%s by %s</p>" % (singer.senior_solo.name,singer.senior_solo.artist)

	sidebar_string = "%s%s"  % (sidebar_string,senior_solo)


	reps = Rep.objects.filter(soloist=singer).order_by('-semester__date');
	reps_count = Rep.objects.filter(soloist=singer).order_by('-semester__date').count();

	if reps_count > 0:
		singer_string = "%s<h3>Solos</h3>"  % (singer_string)

		songs=[]
		for rep in reps:
			if rep.song not in songs:
				songs.append(rep.song)

		count = 0
		for song in songs:
			if count > 0:
				singer_string = "%s, %s"  % (singer_string,song)
			else:
				singer_string = "%s%s"  % (singer_string,song)
			count = count+1

	songs = Song.objects.filter(arranger=singer);
	songs_count = Song.objects.filter(arranger=singer).count();

	if songs_count > 0:
		singer_string = "%s<h3>Arrangements</h3>"  % (singer_string)
		count = 0
		for song in songs:
			if count > 0:
				singer_string = "%s, %s"  % (singer_string,song)
			else:
				singer_string = "%s%s"  % (singer_string,song)
			count = count+1

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
	text = "<div style='clear:both;width:600px'>"
	for event in events:
		if event.link == "":
			title = event.title;
		else:
			title = "<a href='%s'>%s</a>" % (event.link,event.title)
		if event.blurb == "":
			blurb = "";
		else:
			blurb = "<p style='font-size:12px'>%s</p>" % (event.blurb)
		text = "%s<div id='event'><b>%s</b><br /><span style='font-size:13px'>%s, %s</span>%s</div>" % (text,title,event.date.strftime('%B %d'),event.location,blurb)

	sidebar_string = "";
	sidebars = Sidebar.objects.all();

	for sidebar in sidebars:
		sidebar_string = "%s<h3>%s</h3><p>%s</p>" % (sidebar_string,sidebar.name,sidebar.content)

	return render_to_response('app/index.html', {'text': text,'sidebar':sidebar_string})
