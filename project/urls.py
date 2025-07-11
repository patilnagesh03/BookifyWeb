"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.ResisterView, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-change/', views.ChangePasswordView, name='password-change'),
    path('english_version/', views.BookSummaryView, name='book-list'),
    path('hindi_version/', views.HindiBookSummaryView, name='hindi-book-list'),
    path('hindi_book_detail/<int:book_id>/', views.HindiBookDetailView, name='hindi-book-detail'),
    path('book-detail/<int:book_id>/', views.BookDetailView, name='book-summary'),
    path('useridentify/',views.UserIdentityView, name = 'user-identity'),
    path('reset-password/<str:en_uname>/', views.ResetPasswordView, name='reset-password'),
    path('search/', views.search_books, name='search_books'),
    path('',views.Dashboard_View, name='dashboard'),
    path('accounts/', include('allauth.urls')),
]
