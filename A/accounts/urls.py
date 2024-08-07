from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('login/',auth_views.obtain_auth_token),
    path('logout/',views.UserLogout.as_view()),
    path('profiles/',views.ProfileView.as_view()),
    path('profile/create/<str:name>/',views.ProfileCreateView.as_view()),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

router = routers.SimpleRouter()
router.register('user',views.UserViewSet)

urlpatterns += router.urls

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTk5OTM5MywiaWF0IjoxNzE5OTEyOTkzLCJqdGkiOiI0MTQwY2UxM2U0ZWQ0MjAyOTk5Mjc1ZjU5NmM2MWU5MiIsInVzZXJfaWQiOjF9.DiwSiUb7xWymadDWyUgWE7fFYzJg-hP2H0HyiKIkOiI",
#     "access": ""eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5OTE0MDI0LCJpYXQiOjE3MTk5MTI5OTMsImp0aSI6IjBlMzNhMWQ5NzMxOTQxOTQ4MzljM2M5NGMyOGUwZmQwIiwidXNlcl9pZCI6MX0.LDlHmBPNU1tufnKuKsXwaB9bZ6x-PQoRJOeGH0CjoCo"
# }