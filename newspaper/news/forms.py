from django import forms
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['author', 'categories', 'title', 'content']


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        Common_group = Group.objects.get(name='common')
        Common_group.user_set.add(user)
        return user