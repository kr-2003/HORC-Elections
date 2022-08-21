from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Candidate, Post, VoterList, Vote
from .resources import *

# Register your models here.
# admin.site.register(Candidate)
# admin.site.register(Post)
# admin.site.register(VoterList)
# admin.site.register(Vote)

@admin.register(Candidate)
class CandidateAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    model = Candidate
    resource_class = Candidate_Resource

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    model = Post
    resource_class = Post_Resource

@admin.register(VoterList)
class VoterListAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    model = VoterList
    resource_class = VoterList_Resource

@admin.register(Vote)
class VoteAdmi(ImportExportModelAdmin,admin.ModelAdmin):
    model = Vote
    resource_class = Vote_Resource