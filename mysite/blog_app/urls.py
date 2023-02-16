from django.urls import path
from .views import register_view, AnotherLoginView, AccountView, UserUpdateView, upload_files, BlogListView, BlogDetailsView, create_file_blog


app_name = 'blog_app'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', AnotherLoginView.as_view(), name='another_login'),
    path('account/', AccountView.as_view(), name='account'),
    path('account/<int:pk>/update/', UserUpdateView.as_view(), name='account_update'),
    path('account/<int:pk>/create_post/', upload_files, name='create_post'),
    path('blogs_list/', BlogListView.as_view(), name='blogs_list'),
    path('blogs_list/<int:pk>/', BlogDetailsView.as_view(), name='blogs_details'),
    path('create_file_blog/', create_file_blog, name='create_file_blog'),
    ]

