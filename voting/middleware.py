from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from .models import VoterList
from django.core.exceptions import ObjectDoesNotExist


class ManageVotingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_superuser:
            return redirect(reverse("admin:index"))

        try:
            voter = VoterList.objects.get(email=request.user.email)
        except VoterList.DoesNotExist:
            messages.error(request, "User not in the Voter's List")
            return redirect("account_logout")
 
        if(voter.voted):
            messages.error(request, "User already Voted")
            return redirect(reverse("account_logout"))