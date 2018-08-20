from django.urls import path
from django.contrib import admin

from . import views

app_name = 'votacao'

urlpatterns = [
	
    # User
    path('admin/', admin.site.urls),
    path('newuser/', views.RegisterUser.as_view(), name='newuser'),
    #Proposed_law
    path('propostalista/', views.Proposed_lawListView.as_view(), name='propostalista'),
    path('proposta/<pk>', views.Proposed_lawDetailView.as_view(), name='propostadetalhes'),
    path('propostacreate/', views.Proposed_lawCreateView.as_view(), name='propostacadastro'),
    path('success/', views.Success.as_view(), name = 'success'),
    #Comment
    path('comment/', views.CommentCreateView.as_view(), name='comment'),
    path('comment/update/', views.CommentUpdateView.as_view(), name='updatecomment'),

]