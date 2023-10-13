from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(label="username",max_length=50)
    first_name=forms.CharField(label="first_name",max_length=50)
    last_name=forms.CharField(label="last_name",max_length=50)
    email=forms.CharField(label="email",max_length=50)
    password=forms.CharField(label="password",max_length=50)
    confirm_password=forms.CharField(label="confirm_password",max_length=50)

class LoginForm(forms.Form):
    username=forms.CharField(label='username',max_length=50)
    password=forms.CharField(label='password',max_length=50)

class AddTaskForm(forms.Form):
    task_name=forms.CharField(label='task_name',max_length=50)
    description=forms.CharField(label='description',max_length=200)

class UpdateTaskForm(forms.Form):
    task_name=forms.CharField(label='task_name',max_length=50)
    description=forms.CharField(label='description',max_length=200)
    status=forms.CharField(label='status',max_length=50)

class AddEventForm(forms.Form):
    event_name=forms.CharField(label='event_name',max_length=100)
    description=forms.CharField(label='description',max_length=200)
    event_date=forms.DateTimeField(label='event_date')

class UpdateEventForm(forms.Form):
    event_name=forms.CharField(label='event_name',max_length=100)
    description=forms.CharField(label='description',max_length=200)
    event_date=forms.DateTimeField(label='event_date')
    status=forms.CharField(label='status',max_length=50)
class UpdateProfile(forms.Form):
    previous_password=forms.CharField(label='previous_password',max_length=50)
    password=forms.CharField(label="password",max_length=50)
    confirm_password=forms.CharField(label="confirm_password",max_length=50)
