from django.shortcuts import render, redirect, reverse
# from account.views import account_login
from .models import  Vote, VoterList, Candidate, Post

from django.utils.text import slugify
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse, HttpResponse
import requests
import json
# Create your views here.

def index(request):
    user_email = request.user.email
    print(request.user.first_name)
    print(request.user.socialaccount_set.filter())
    voter = VoterList.objects.get(email = user_email)
    if voter.voted:
        #maybe create a nice page for this or nvm
        return HttpResponse("<h1>User Already Voted</h1>")

    if request.method == "POST":
        post_ids = Post.objects.filter(hostel = voter.hostel).values_list('id', flat=True)
        
        for post_id in post_ids:
            vote_casted = request.POST.get(post_id)
            Vote.objects.create(user=user_email,post_id=post_id,vote_casted=vote_casted)

        voter.update(voted=True)        
        messages.success(request, "Vote Casted successfully")

    posts = Post.objects.filter(hostel = voter.hostel)
    print(voter.hostel)
    print(posts)

    context = {
        "posts" : posts,
        "page_title" : "HORC Elections",

    }
    return render(request, "voting/ballot.html" , context)