
from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.shortcuts import render_to_response


def rep(Request):
	semesters = Semester.objects.all()
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
		songs = Song.objects.all()
		for song in songs:
			addon = """
			<tr>
			<td>%s</th>
			<td>%s</th>
			<td>%s</th>
			<td>%s</th>
			</tr>""" % (song.name,song.artist,song.soloist,song.arranger)
			addme = "%s%s" % (addme, addon)

		
	derp = """
	<h2>Spring 2014</h2>
	<div id ="cover">
	
	</div>
	<table>
		<tr class="tablehead">
			<th>Song</th>
			<th>Solosit</th>
			<th>Artist</th>
			<th>Arranger</th>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>


	</table>
<h2>Spring 2013</h2>
<div id ="cover2">

</div>
	<table>
		<tr class="tablehead">
			<th>Song</th>
			<th>Solosit</th>
			<th>Artist</th>
			<th>Arranger</th>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>


	</table>
	<h2>Spring 2013</h2>
<div id ="cover3">

</div>
	<table>
		<tr class="tablehead">
			<th>Song</th>
			<th>Solosit</th>
			<th>Artist</th>
			<th>Arranger</th>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>
		<tr>
			<td>Back to Black</th>
			<td>Amy Winehouse</th>
			<td>Lauren</th>
			<td>Eddie</th>
		</tr>
		<tr>
			<td>Can't Help Falling Love</td>
			<td>Ingrid Michaelson</td>
			<td>Mary Hannah</td>
			<td>Blake and Dyson</td>
		</tr>


	</table>"""
	derp = "%s%s" % (addme, derp)

	return render_to_response('app/index.html', {'text': derp})


def contact(Request):
	tests = Semester.objects.all()
	derp = """
		test contact
		"""
	return render_to_response('app/index.html', {'text': derp})

def members(Request):
	tests = Semester.objects.all()
	derp = """
		test members
		"""
	return render_to_response('app/index.html', {'text': derp})

def index(Request):
	tests = Semester.objects.all()
	derp = """
		test rep
		"""
	return render_to_response('app/index.html', {'text': derp})

def gallery(Request):
	tests = Semester.objects.all()
	derp = """
		test gallery
		"""
	return render_to_response('app/index.html', {'text': derp})

def events(Request):
	tests = Semester.objects.all()
	derp = """
		test events
		"""
	return render_to_response('app/index.html', {'text': derp})


