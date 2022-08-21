from allauth.socialaccount.forms import SignupForm
from .models import VoterList
from django.contrib import messages

class MyCustomSocialSignupForm(SignupForm):

    def save(self, request):

        print(self.socialaccount)
        email = self.socialaccount.email
        print("Dekho kon aaya hai: ", email)
        try:
            voter = VoterList.objects.get(email=email)
        except VoterList.DoesNotExist:
            messages.error(request, "User not in the Voter's List")
        else:
            user = super(MyCustomSocialSignupForm, self).save(request)

        return user