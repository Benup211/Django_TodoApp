from django.urls import path
from . import views
app_name="todolist"
urlpatterns=[
    path('',views.index,name="index"),
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('logout',views.logout_view,name="logout"),
    path('add_task/',views.add_task_view,name="add_task"),
    path('task/<int:todoitem_id>/',views.todoitem_view,name="viewtodoitem"),
    path('task/<int:todoitem_id>/delete/',views.delete_todoitem,name="delete_task"),
    path('task/<int:todoitem_id>/edit/',views.update_todotask,name="update_task"),
    path('add_event/',views.add_event_view,name="add_event"),
    path('event/<int:eventitem_id>/',views.eventitem_view,name="vieweventitem"),
    path('event/<int:eventitem_id>/delete/',views.delete_eventitem,name="delete_event"),
    path('event/<int:eventitem_id>/edit/',views.update_eventtask,name="update_event"),
    path('updateprofile/',views.update_profile,name="update_profile"),
]