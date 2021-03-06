from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# Customizing the Admin interface
# https://docs.djangoproject.com/en/1.11/intro/tutorial07/

class ChoiceInline(admin.TabularInline): # or StackedInline
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_published_recently')

	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	
	list_filter = ['pub_date']
	search_fields = [
		'question_text',
		'choice__choice_text', # include related field into search-realm
		]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

