from django.conf.urls import url, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    url(r'^home', PostListView.as_view(), name='blog-home'),
    url(r'^post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^about', views.about, name='blog-about'),
    url(r'^register', user_views.register, name='register'),
    url(r'^login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^profile', user_views.profile, name='profile'),

    url(r'^password-reset', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    url(r'^password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    url(r'^password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

]


