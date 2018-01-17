from django import forms
from models import Tasks, User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('title', 'start_date', 'details', 'image')

    def save(self, user=None):
        task_form = super(TaskForm, self).save(commit=False)
        if user:
            task_form.owner_id = user
        task_form.save()
        return task_form

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget = forms.widgets.SelectDateWidget()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username','email',  'first_name', 'last_name', 'password1', 'password2', )