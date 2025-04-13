from django import forms
from .models import Commentaire, Like, Jeu, Post

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['nom', 'email', 'contenu']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre commentaire', 'rows': 4}),
        }

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['email']
        widgets = {
            #'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}),
        }
        
class JeuAdminForm(forms.ModelForm):
    class Meta:
        model = Jeu
        fields = ['titre', 'description', 'media_type', 'image', 'video_url']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'media_type': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.FileInput(attrs={'class': 'form-control'})
        }
        
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['jeu', 'titre', 'type', 'description', 'image', 'video_url']
        widgets = {
            'jeu': forms.Select(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.FileInput(attrs={'class': 'form-control'})
        }
        
        
