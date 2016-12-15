from django.shortcuts import render
from django.views import generic
from .models import Student, Group
from .forms import StudentForm, GroupForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection

#@login_required
class GroupView(LoginRequiredMixin, generic.ListView):
    login_url = '/admin/login/'
    redirect_field_name = 'group_tmpl'
    template_name = 'students/group_tmpl.html'
    context_object_name = 'GroupList'
    
    #find easier way
    def get_queryset(self):
#        print(connection.queries[0]['time'],' | ',len(connection.queries))
        """Return group vs added field"""
        GroupList = Group.objects.all()
        for grp_obj in GroupList:
            grp_obj.st_cnt = len(Student.objects.filter(
                                   st_group=grp_obj.id))
        return GroupList
    # model = Group


class StudentView(generic.ListView):
    template_name = 'students/student_tmpl.html'
    context_object_name = 'StudentList'

    def get_queryset(self):
        """Return students from group"""
        return Student.objects.filter(st_group=self.kwargs['grp_id'])


class CrtGroup(generic.CreateView):
    model = Group
    template_name = 'students/crt_grp.html'
    fields = ['name', 'warden']
    success_url = '../group_tmpl'


class EdtGroup(generic.UpdateView):
    model = Group
    template_name= 'students/edt_grp.html'
    fields = ['name', 'warden']
    success_url = '../group_tmpl'


class DltGroup(generic.DeleteView):
#    context_object_name = 'obj'
    model = Group
    template_name= 'students/dlt_grp.html'
#   fields = ['name', 'warden']
    success_url = '../group_tmpl'
#    success_url = reverse_lazy('del_grp/')


class CrtStudent(generic.CreateView):
    model = Student
    template_name = 'students/crt_std.html'
    fields = ['full_name','birthday', 'student_card', 'st_group']
    success_url = '../group_tmpl'

class EdtStudent(generic.UpdateView):
    model = Student
    template_name= 'students/edt_std.html'
    fields = ['full_name','birthday', 'student_card', 'st_group']
    success_url = '../group_tmpl'


class DltStudent(generic.DeleteView):
    model = Student
    template_name= 'students/dlt_std.html'
#    fields = ['full_name','birthday', 'student_card', 'st_group']
    success_url = reverse_lazy('../group_tmpl')

