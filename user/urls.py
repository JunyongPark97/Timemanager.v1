
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user import views
from user.views import ImportCSVView, ImportUserView

app_name='user'
urlpatterns = [
    path('', views.graph, name='graph'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout1/',LogoutView.as_view(),{'next_page':'/'},name='logout1'),
    path('request/<int:pk>', views.request_view, name='request'),
    path('password/',views.change_password, name='change_password'),
    path('gotohome/',views.gotohome, name='gotohome' ),
    path('request-list/',views.requestlist, name='requestlist'),
    path('request-list/<int:pk1>/<int:pk2>/',views.editrequest, name='editrequest'),
    path('list/', views.list, name='list'),
    path('api/import/', ImportCSVView.as_view(), name='import_csv'),
    path('api/import/user', ImportUserView.as_view(), name='import_Usercsv'),
    path('ex/', views.makeEach, name='ex'),

]