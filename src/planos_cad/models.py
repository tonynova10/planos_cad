from __future__ import unicode_literals

from django.db import models

class Emails(models.Model):
	email = models.EmailField(max_length=25, blank=True, null=True)
	text = models.TextField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=True)

	def __str__(self):
		return self.email
