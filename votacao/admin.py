from django.contrib import admin
from .models import Proposed_law, Voting, Comment

class AuthorAdmin(admin.ModelAdmin):
	pass

admin.site.register(Proposed_law)
admin.site.register(Voting)
admin.site.register(Comment)
