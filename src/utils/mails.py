from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template

def email_contact(email, content):
	template = get_template('email_contact.html')
	render = template.render({
		'content': content
		})

	reminder = "¡Tienes un nuevo email!"

	mail = EmailMultiAlternatives(reminder, from_email=[email], to=['antoniodegollado10@gmail.com'])
	mail.attach_alternative(render, 'text/html')
