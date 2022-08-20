from django.contrib import admin
from .models import Candidate, Post, VoterList, Vote

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Post)
admin.site.register(VoterList)
admin.site.register(Vote)