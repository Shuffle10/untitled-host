from django.shortcuts import render, HttpResponse
from home.models import Release, Subscriber, Quote, Event, Video, Artist
from blog.models import Blog
from django.contrib import messages
from django.http import HttpResponseRedirect 
# Create your views here.
def home(request):
    allReleases = Release.objects.all()
    allReleases = reversed(allReleases)
    allPosts = Blog.objects.all()
    allPosts = reversed(allPosts)
    context = {'posts' : allPosts,
    'releases' : allReleases}
    if request.method=='POST':
        subscriber_email = request.POST['email']
        sub = Subscriber(email = subscriber_email)
        sub.save()
        email = EmailMessage(
        'untitled.np Newsletter Subscription',
        'Thankyou for subscribing. You will be notified about our releases and other activities. Have a good day ahead!',
        settings.EMAIL_HOST_USER,
        [subscriber_email],
        )
        email.fail_silently=False
        email.send()
        messages.success(request, 'Success! Your information has been recorded')
        return HttpResponseRedirect("/home")

    return render(request, 'home.html', context)

def releases(request):
    allReleases = Release.objects.all()
    allReleases = reversed(allReleases)
    context = {'releases' : allReleases}
    return render(request, 'releases.html', context)

def artists(request):
    allArtists = Artist.objects.all()
    context = {'artists' : allArtists}
    return render(request,'artists.html', context)

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
        

def submitted(request):
    if request.method=='POST':
        name= request.POST['name']
        quote_email = request.POST['email']
        phone = request.POST['phone']
        details = request.POST['details']
        quote = Quote(name=name , email =quote_email, phone=phone, details=details)
        quote.save()
        email = EmailMessage(
        'untitled.np Quotation Request',
        'Thankyou for requesting a quote. We will get back to you as soon as possible. Have a good day ahead!',
        settings.EMAIL_HOST_USER,
        [quote_email],
        )
        email.fail_silently=False
        email.send()
        messages.success(request, 'Success! Your information has been recorded')
        return HttpResponseRedirect("/home")


def events(request):
    events = Event.objects.all()
    context = {'events' : events}
    return render(request, 'events.html', context)

def corporate(request):
    return render(request, 'corporate.html')

def videos(request):
    allVideos = Video.objects.all()
    allVideos = reversed(allVideos)
    context ={'videos': allVideos}
    return render(request,'videos.html', context)

def videoModal(request, slug):
    allVideos = Video.objects.all()
    allVideos = reversed(allVideos)
    modalVideo = Video.objects.filter(slug=slug).first()
    context ={'video': modalVideo,
    'allVideos': allVideos}
    return render(request,'videoModal.html', context)