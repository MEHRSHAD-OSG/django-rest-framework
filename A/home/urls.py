from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    # path('', views.Home.as_view(), name='home'),
    path('', views.QuestionView.as_view(), name='question'),
    path('question/create/', views.QuestionCreateView.as_view(), name='question_create'),
    path('question/update/<int:pk>/', views.QuestionUpdateView.as_view(), name='question_update'),
    path('question/delete/<int:pk>/', views.QuestionDeleteView.as_view(), name='question_delete'),

]