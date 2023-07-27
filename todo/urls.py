from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('maskAsDone/<int:pk>', views.maskAsDone, name='maskAsDone'),
    path('maskAsUndone/<int:pk>', views.maskAsUndone, name='maskAsUndone'),

    # Edit Mark
    path('editTask/<int:pk>', views.editTask, name='editTask'),

    path('deleteTask/<int:pk>', views.deleteTask, name='deleteTask'),
]