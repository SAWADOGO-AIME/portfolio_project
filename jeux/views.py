from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib import messages
from .models import Jeu, Post, Commentaire, Like
from .forms import CommentaireForm, LikeForm, JeuAdminForm, PostAdminForm

# Views pour la partie publique
def index(request):
    jeux = Jeu.objects.all()
    return render(request, 'jeux/index.html', {'jeux': jeux})

def detail_jeu(request, jeu_id):
    jeu = get_object_or_404(Jeu, id=jeu_id)
    posts = jeu.posts.all()
    commentaires = jeu.commentaire_set.all()
    
    # Formulaires pour commenter et liker
    commentaire_form = CommentaireForm()
    like_form = LikeForm()
    
    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            commentaire_form = CommentaireForm(request.POST)
            if commentaire_form.is_valid():
                commentaire = commentaire_form.save(commit=False)
                commentaire.jeu = jeu
                commentaire.save()
                messages.success(request, "Votre commentaire a été ajouté avec succès!")
                return redirect('detail_jeu', jeu_id=jeu.id)
        
        elif 'like_submit' in request.POST:
            like_form = LikeForm(request.POST)
            if like_form.is_valid():
                try:
                    like = like_form.save(commit=False)
                    like.jeu = jeu
                    like.save()
                    messages.success(request, "Merci pour votre like!")
                except IntegrityError:
                    messages.warning(request, "Vous avez déjà liké ce jeu.")
                return redirect('detail_jeu', jeu_id=jeu.id)
    
    context = {
        'jeu': jeu,
        'posts': posts,
        'commentaires': commentaires,
        'commentaire_form': commentaire_form,
        'like_form': like_form,
        'total_likes': jeu.total_likes(),
    }
    
    return render(request, 'jeux/detail_jeu.html', context)

# Views pour la partie admin (interface personnalisée)
@login_required
def admin_dashboard(request):
    jeux = Jeu.objects.all()
    return render(request, 'jeux/admin/dashboard.html', {'jeux': jeux})

@login_required
def admin_jeu_list(request):
    jeux = Jeu.objects.all()
    return render(request, 'jeux/admin/jeu_list.html', {'jeux': jeux})

@login_required
def admin_jeu_create(request):
    if request.method == 'POST':
        form = JeuAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Jeu créé avec succès!")
            return redirect('admin_jeu_list')
    else:
        form = JeuAdminForm()
    
    return render(request, 'jeux/admin/jeu_form.html', {'form': form, 'action': 'Créer'})

@login_required
def admin_jeu_edit(request, jeu_id):
    jeu = get_object_or_404(Jeu, id=jeu_id)
    
    if request.method == 'POST':
        form = JeuAdminForm(request.POST, request.FILES, instance=jeu)
        if form.is_valid():
            form.save()
            messages.success(request, "Jeu modifié avec succès!")
            return redirect('admin_jeu_list')
    else:
        form = JeuAdminForm(instance=jeu)
    
    return render(request, 'jeux/admin/jeu_form.html', {'form': form, 'jeu': jeu, 'action': 'Modifier'})

@login_required
def admin_jeu_delete(request, jeu_id):
    jeu = get_object_or_404(Jeu, id=jeu_id)
    
    if request.method == 'POST':
        jeu.delete()
        messages.success(request, "Jeu supprimé avec succès!")
        return redirect('admin_jeu_list')
    
    return render(request, 'jeux/admin/jeu_confirm_delete.html', {'jeu': jeu})

@login_required
def admin_post_list(request):
    posts = Post.objects.all()
    return render(request, 'jeux/admin/post_list.html', {'posts': posts})

@login_required
def admin_post_create(request):
    if request.method == 'POST':
        form = PostAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post créé avec succès!")
            return redirect('admin_post_list')
    else:
        form = PostAdminForm()
    
    return render(request, 'jeux/admin/post_form.html', {'form': form, 'action': 'Créer'})

@login_required
def admin_post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = PostAdminForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post modifié avec succès!")
            return redirect('admin_post_list')
    else:
        form = PostAdminForm(instance=post)
    
    return render(request, 'jeux/admin/post_form.html', {'form': form, 'post': post, 'action': 'Modifier'})

@login_required
def admin_post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post supprimé avec succès!")
        return redirect('admin_post_list')
    
    return render(request, 'jeux/admin/post_confirm_delete.html', {'post': post})


from django.contrib.auth.views import LoginView

class AdminLoginView(LoginView):
    template_name = 'admin/login.html'  # Assurez-vous que ce fichier existe