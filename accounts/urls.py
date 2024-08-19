from django.urls import path

from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileView, UserListView, UpdateUserView, \
    DeleteUserView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('list/', UserListView.as_view(), name='list'),
    path('<pk>/update/', UpdateUserView.as_view(), name='update'),
    path('<pk>/delete/', DeleteUserView.as_view(), name='delete'),

]
