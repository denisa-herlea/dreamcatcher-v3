from django.urls import path

from . import views

app_name = 'dreamcatcher'

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('rating', views.rating, name='rating'),
    path('login_view', views.login_view, name='login_view'),
    path('login_register_view', views.login_register_view, name='login_register_view'),
    path('login_register', views.login_register, name='login_register'),
    path('descriere_categorie', views.descriere_categorie, name='descriere_categorie'),
    path('statistici', views.statistici_view, name='statistici_view'),
    path('statistici_stres_week', views.statistici_view_stres_week, name='statistici_view_stres_week'),
    path('statistici_stres_month', views.statistici_view_stres_month, name='statistici_view_stres_month'),
    path('statistici_energie_week', views.statistici_view_energie_week, name='statistici_view_energie_week'),
    path('statistici_energie_month', views.statistici_view_energie_month, name='statistici_view_energie_month'),
    path('statistici_durata_week', views.statistici_view_durata_week, name='statistici_view_durata_week'),
    path('statistici_durata_month', views.statistici_view_durata_month, name='statistici_view_durata_month'),
    path('back', views.back_to_statistici_view, name='back_to_statistici_view'),

]