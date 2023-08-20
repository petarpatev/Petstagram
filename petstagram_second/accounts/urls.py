from django.urls import path, include

from petstagram_second.accounts.views import user_register, user_login, user_details, user_edit, user_delete

urlpatterns = (
    path('register/', user_register, name='user register'),
    path('login/', user_login, name='user login'),
    path('profile/', include([
        path('<int:pk>/', user_details, name='user details'),
        path('<int:pk>/edit/', user_edit, name='user edit'),
        path('<int:pk>/delete/', user_delete, name='user delete'),
    ]))
)
