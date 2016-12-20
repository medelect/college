from django.shortcuts import render
from django.views import generic
from .models import Student, Group
from .forms import StudentForm, GroupForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


#@login_required
class GroupView(LoginRequiredMixin, generic.ListView):
    login_url = '../../students/login/'
#    redirect_field_name = 'group_tmpl'
    template_name = 'students/group_tmpl.html'
    context_object_name = 'GroupList'
    
    #find easier way
    def get_queryset(self):
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
    template_name= 'smetudents/dlt_std.html'
#    fields = ['full_name','birthday', 'student_card', 'st_group']
    success_url = reverse_lazy('../group_tmpl')


def new_tag(request, pk):
    
    if pk == '1': 
        lst = Group.objects.all()
    else:
        lst = Student.objects.all()
    context = {'obj_lst': lst }
    return render(request, 'students/new_tag.html', context)


def index(request):
    return render(request, 'students/index.html')


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "../login/"
    template_name = "students/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)



class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "students/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
#    success_url = "students/logout.html"
    def get(self, request):
        request.path_info = '/'
        logout(request)
        return render(request, 'students/logout.html')


def common_act(request, way, pk):
    types = {'grp':[10,'Group'],'std':[20,'Student']}
    events = {'crt':[1,'Create'], 'edt':[2,'Edit'], 'dlt':[3,'Delete']}
    ress = way.split('_')
    act_code = types[ress[0]][0] + events[ress[1]][0]

    action_way = {
            '11': 'CrtGroup'
            '12': 'EdtGroup'
            '12': 'DltGroup'
            '21': 'CrtStudent'
            '22': 'EdtStudent'
            '23': 'DltStudent'
            }

