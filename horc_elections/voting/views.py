import email
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

    voter = VoterList.objects.get(email = user_email)
    if voter.voted:
        #maybe create a nice page for this or nvm
        return HttpResponse("<h1>User Already Voted</h1>")

    if request.method == "POST":

        post_ids = Post.objects.filter(hostel = voter.hostel).values_list('id', flat=True)
        
        for post_id in post_ids:
            vote_casted = request.POST.get(str(post_id))

            print("Creating vote ", user_email, post_id , vote_casted)

            user_obj = VoterList.objects.get(email = user_email)
            post_id_obj = Post.objects.get(id = post_id)
            vote_casted_obj = Candidate.objects.get(email = vote_casted)

            print(user_obj,post_id_obj , vote_casted_obj)

            
            vote = Vote.objects.create(user=user_obj,post_id=post_id_obj,vote_casted=vote_casted_obj)
            vote.save()

        VoterList.objects.filter(email = user_email).update(voted = True)
        # voter.update(voted=True)        
        messages.success(request, "Vote Casted successfully")

    posts = Post.objects.filter(hostel = voter.hostel)


    for post in posts:
        print(type(post),post,post.post_name)

    context = {
        "posts" : posts,
        "page_title" : "HORC Elections",
        "hostel" : voter.hostel,
    }
    return render(request, "voting/ballot.html" , context)