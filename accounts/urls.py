from django.urls import path

from accounts.views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileView, UserListView, \
    UpdateUserView, \
    DeleteUserView

urlpatterns = [
    path('register/', UserRegisterView.UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.UserProfileView.as_view(), name='profile'),
    path('list/', UserListView.UserListView.as_view(), name='list'),
    path('<pk>/update/', UpdateUserView.UpdateUserView.as_view(), name='update'),
    path('<pk>/delete/', DeleteUserView.DeleteUserView.as_view(), name='delete'),

]
