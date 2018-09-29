from django.http import HttpResponse
from django.shortcuts import render
from main.models import Email
from utils.mails import email_contact

def main(request):
	template_name = 'main.html'

	return render(request, template_name)


def new_project(request):
	template_name = 'main.html'
	email = request.POST.get('email')
	content = request.POST.get('content')

	email_created = Email()
	email_created.email = email
	email_created.text = content
	email_created.save()

	email_contact(email_created.email, email_created.text)

	try:
		return render(request, template_name)
	except Exception as e:
		message = 'Ocurrio un error'
		return render(request, template_name)
		
		