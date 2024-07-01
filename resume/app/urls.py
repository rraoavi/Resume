from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("", views.home),
    path('create/', views.resume_form, name='resume_create'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
    path('<int:pk>/download_jpg/', views.download_jpg, name='download_jpg'),
    # path('<int:pk>/print/', views.print_resume, name='print_resume'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)