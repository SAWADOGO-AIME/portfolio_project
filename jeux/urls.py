from django.urls import path
from . import views
from .views import AdminLoginView


urlpatterns = [
    # URLs pour la partie publique
    path('', views.index, name='index'),
    path('jeu/<int:jeu_id>/', views.detail_jeu, name='detail_jeu'),
    
    # URLs pour la partie admin personnalisée
    path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/jeux/', views.admin_jeu_list, name='admin_jeu_list'),
    path('admin/jeux/create/', views.admin_jeu_create, name='admin_jeu_create'),
    path('admin/jeux/<int:jeu_id>/edit/', views.admin_jeu_edit, name='admin_jeu_edit'),
    path('admin/jeux/<int:jeu_id>/delete/', views.admin_jeu_delete, name='admin_jeu_delete'),
    path('admin/posts/', views.admin_post_list, name='admin_post_list'),
    path('admin/posts/create/', views.admin_post_create, name='admin_post_create'),
    path('admin/posts/<int:post_id>/edit/', views.admin_post_edit, name='admin_post_edit'),
    path('admin/posts/<int:post_id>/delete/', views.admin_post_delete, name='admin_post_delete'),
]