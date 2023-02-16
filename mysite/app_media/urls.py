from django.urls import path
from .views import upload_file, model_form_upload, upload_files


app_name = 'app_media'

urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
    path('model_form_upload_file/', model_form_upload, name='model_form_upload_file'),
    path('upload_files/', upload_files, name='upload_files'),
]
