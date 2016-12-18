from django.forms import ModelForm
from .models import Student, Group

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'birthday', 'student_card', 'st_group']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'warden']



