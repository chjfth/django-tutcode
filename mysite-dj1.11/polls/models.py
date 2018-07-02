from django.db import models

# Create your models here.

import datetime
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	# https://docs.djangoproject.com/en/1.11/intro/tutorial07/#customize-the-admin-change-list
	was_published_recently.admin_order_field = 'pub_date' # tell order rule of this column
	was_published_recently.boolean = True # tell datatype, boolean make the value display as a tick/cross
	was_published_recently.short_description = 'Published recently?' # customize column header text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

