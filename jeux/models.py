from django.db import models
from django.utils import timezone

class Jeu(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    # Champ pour l'image ou la vidéo
    media_type = models.CharField(max_length=5, choices=[('IMAGE', 'Image'), ('VIDEO', 'Vidéo')], default='IMAGE')
    image = models.ImageField(upload_to='jeux/images/', null=True, blank=True)
    #video_url = models.VideoField(upload_to='jeux/videos/', null=True, blank=True, help_text="URL YouTube ou autre plateforme vidéo")
    #VideoField(upload_to='jeux/videos/', null=True, blank=True, help_text="URL YouTube ou autre plateforme vidéo")
    video_url = models.FileField(upload_to='jeux/videos/', null=True, blank=True, help_text="Téléchargez une vidéo")  # Champ pour les vidéos

    def total_likes(self):
        return self.like_set.count()
        
    def total_comments(self):
        return self.commentaire_set.count()
        
    def __str__(self):
        return self.titre
        
    class Meta:
        verbose_name = "Jeu"
        verbose_name_plural = "Jeux"
        ordering = ['-date_creation']

class Post(models.Model):
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE, related_name='posts')
    titre = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=5, choices=[('IMAGE', 'Image'), ('VIDEO', 'Vidéo'), ('TEXT', 'Texte')], default='TEXT')
    description = models.TextField()
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    video_url = models.FileField(upload_to='posts/videos/', null=True, blank=True, help_text="Téléchargez une vidéo")
    date_creation = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.titre} - {self.jeu.titre}"
        
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-date_creation']

class Commentaire(models.Model):
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    contenu = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Commentaire de {self.nom} sur {self.jeu.titre}"
        
    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
        ordering = ['-date_creation']

class Like(models.Model):
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    date_creation = models.DateTimeField(default=timezone.now)
    
    class Meta:
        # Pour éviter qu'un utilisateur puisse liker plusieurs fois le même jeu
        unique_together = ('email', 'jeu')
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        
    def __str__(self):
        return f"Like de {self.nom} sur {self.jeu.titre}"