from django.shortcuts import render,render_to_response,RequestContext
from django.conf import settings
import datetime
from django.http import HttpResponseRedirect
from .forms import SignUpForm,ContactForm
from django.core.mail import send_mail
from models import SignUp
from ipware.ip import get_real_ip
# Create your views here.
def home(request):
	#hora = datetime.datetime.now()
	#hora = hora.strftime("%H:%M")
	title = 'Sign Up Now'
	#if request.user.is_authenticated():
	#	title = "SATHHHH %s" %(request.user)

	ip = get_real_ip(request)
        if ip is not None:
            ip = request.META["HTTP_X_FORWARDED_FOR"]
           



	form = SignUpForm(request.POST or None)

	context = {
		"template_title":title,
		"form":form
	}

	if form.is_valid():
		#----
		#form.save()
		#------
		#instance = form.save(commit=False)
		#print instance.email
		#print instance.fullname
		#if instance.fullname == None or instance.fullname == "" :
		#	instance.fullname = "Javier"		
		#instance.save()
		#-----
		#print request.POST['email'] not recomendado
		instance = form.save(commit=False)
		fullname =form.cleaned_data.get("fullname")
		if not fullname:
			fullname = "New full name"
		instance.fullname = fullname
		instance.save()


		context = {
		"template_title":ip,

		}

	if request.user.is_authenticated() and request.user.is_staff:
		#queryset = SignUp.objects.all().order_by('-email').filter(fullname__icontains="ed")
		queryset = SignUp.objects.all().order_by('-email').filter(fullname__iexact="isabel")


		context = {
		"queryset": queryset
		}
	
	#return render(request,"home.html",context = locals())
	return render(request,"home.html",context)

def contact(request):
	form = ContactForm(request.POST or None)
	title= "Holas a todos"
	title_align = True
	if form.is_valid():
		#for key,value in form.cleaned_data.iteritems():
		#	print key,value
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_fullname = form.cleaned_data.get("fullname")

		subject	= 'site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'edenluis.elae@gmail.com']
		contact_message = "%s: %s via %s" % (
				form_fullname,
				form_message,
				form_email)

		#send_mail(subject, contact_message, from_email,[to_email],fail_silently=False )
		send_mail(form_fullname, form_message, from_email, [form_email], fail_silently=False)

	context = {
		"form": form,
		"title":title,
		"title_align":title_align,
	}
	return render(request, "forms.html", context)
