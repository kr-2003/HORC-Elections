import csv
from django.shortcuts import render, redirect, reverse
from .models import Vote, VoterList, Candidate, Post
from django.contrib import messages
from django.http import HttpResponse
from .middleware import ManageVotingMiddleware
from django.utils.decorators import decorator_from_middleware
from django.db.models import Count

@decorator_from_middleware(ManageVotingMiddleware)
def index(request):
    voter = VoterList.objects.get(email=request.user.email)
    if request.method == "POST":
        post_ids = Post.objects.filter(hostel=voter.hostel).values_list("id", flat=True)

        for post_id in post_ids:
            vote_casted = request.POST.get(
                str(post_id), f"nota_{voter.hostel}@iiti.ac.in"
            )
            vote = Vote(user=voter, post_id_id=post_id, vote_casted_id=vote_casted)
            vote.save()

        voter.voted = True
        voter.save(update_fields=["voted"])
        messages.success(request, "You have successfully casted your vote")
        return redirect(reverse("account_logout"))

    posts = Post.objects.filter(hostel=voter.hostel)

    for post in posts:
        print(type(post), post, post.post_name)

    context = {
        "posts": posts,
        "page_title": "HORC Elections",
        "hostel": voter.hostel,
    }
    return render(request, "ballot.html", context)

def generateCSV(writer):
    votes = Vote.objects.values('post_id','vote_casted').annotate(num_votes=Count('user'))
    
    writer.writerow(["PostName", "Hostel", "Name","Email","NumVotes"])

    voted_for = dict()

    for vote in votes:
        post_id = vote['post_id']
        email = vote['vote_casted']
        num_votes = vote['num_votes'] 

        post = Post.objects.get(id = post_id)
        candidate = Candidate.objects.get(email = email)

        voted_for[email] = True

        writer.writerow([post.post_name,post.hostel,candidate.name,candidate.email,num_votes])

    posts = Post.objects.all()

    for post in posts:
        candidates = post.candidates.all()

        for candidate in candidates:
            if candidate.email not in voted_for:
                writer.writerow([post.post_name,post.hostel,candidate.name,candidate.email,0])

def getResult(request):
    if not request.user.is_staff:
        return redirect(reverse("home"))

    if request.method == "POST":
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="results.csv"'},
        )

        writer = csv.writer(response)
        generateCSV(writer)
        # writer.writerow(["First row", "Foo", "Bar", "Baz"])
        # writer.writerow(["Second row", "A", "B", "C", '"Testing"', "Here's a quote"])
        return response
    
    return render(request, "result.html")
