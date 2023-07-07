from django.urls import path
from home import views


app_name = "home"

urlpatterns = [
    path('', views.index, name='home'),
    path('user/<int:id>', views.get_user, name='user'),
    path('user/<int:id>/edit', views.save_user, name='edit_user')
]

