from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		# do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['paddynino@gmail.com'], # to email
			fail_silently = False,
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		# return the page
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def blog_details(request):
	return render(request, 'blog_details.html', {})

def service(request):
	return render(request, 'service.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

