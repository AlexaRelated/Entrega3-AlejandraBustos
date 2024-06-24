
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'category']
 

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile = Profile.objects.create(user=user, city=self.cleaned_data['city'])
            profile.save()
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
        }