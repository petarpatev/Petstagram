from django.urls import path, include

from petstagram_second.accounts.views import user_details, user_edit, user_delete, \
    RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='user register'),
    path('login/', LoginUserView.as_view(), name='user login'),
    path('logout/', LogoutUserView.as_view(), name='user logout'),
    path('profile/', include([
        path('<int:pk>/', user_details, name='user details'),
        path('<int:pk>/edit/', user_edit, name='user edit'),
        path('<int:pk>/delete/', user_delete, name='user delete'),
    ]))
)
