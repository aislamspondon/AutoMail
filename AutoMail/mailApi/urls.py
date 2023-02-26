from django.urls import path
from mailApi import views

urlpatterns = [
    path('', views.intro, name="mailApi"),
    path('mailsend/', views.mail_send, name='mail_send'),
    
]