from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponseRedirect
# Create your views here.

brief = '''Details here..
'''

a={
'next':'Hacker Space',
'date':"August 12' 2018",
'first_speaker_name':"Nupur Agrahari",
'first_speaker_info': "",
'first_speaker_twitter':"https://twitter.com/nupur493",
'first_speaker_git':"https://github.com/nupuragrahari",
'first_speaker_linkedin':"https://www.linkedin.com/in/nupur-agrahari-088b91a4/",
'second_speaker_name':"Ankit Giri",
'second_speaker_info': "",
'second_speaker_twitter':"",
'second_speaker_git':"",
'second_speaker_linkedin':"",
'third_speaker_name': "Shashank Kumar",
'third_speaker_git': "https://github.com/realslimshanky/",
'rsvp_link':"https://goo.gl/forms/mhWYyHiLhEttuwF33",
'gmaps_link':"https://goo.gl/maps/7fYcHR4EX3N2",
'how_to_get_here':"Walking distance from Noida Sector 15 metro station",
'venue_name':"Hacker Space",
'venue_add':"A-73 Sector 2, Near Sector 15 Metro Station, Noida, Uttar Pradesh 201301",
'brief': brief
}


def home(request):
    return render(request, 'root/index.html', a)

def about(request):
    return render(request, 'root/about.html')

def pastmeetups(request):
    return render(request, 'root/pastmeetups.html')

def contact(request):
    return render(request, 'root/contact.html')

def sponsor(request):
    return render(request, 'root/sponsors.html')

def subscribe(request):
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['subscribe']
            print(email)
            return HttpResponseRedirect('/subscribe/done')

def ucmp(request):
    return render(request, 'root/upcomingmeetups.html')

def community_partners(request):
    return render(request, 'root/communitypartners.html')
