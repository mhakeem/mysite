from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3
	list_display = ('question', 'pub_date')

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hirarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)