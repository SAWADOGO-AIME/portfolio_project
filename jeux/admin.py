from django.contrib import admin
from .models import Jeu, Post, Commentaire, Like

@admin.register(Jeu)
class JeuAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'total_likes', 'total_comments')
    search_fields = ('titre', 'description')
    list_filter = ('date_creation',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'jeu', 'type', 'date_creation')
    search_fields = ('titre', 'description', 'jeu__titre')
    list_filter = ('jeu', 'type', 'date_creation')

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'jeu', 'date_creation')
    search_fields = ('nom', 'email', 'contenu', 'jeu__titre')
    list_filter = ('jeu', 'date_creation')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'jeu', 'date_creation')
    search_fields = ('nom', 'email', 'jeu__titre')
    list_filter = ('jeu', 'date_creation')