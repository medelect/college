from django.shortcuts import render
from django.views import generic
from .models import Student, Group
from .forms import StudentForm, GroupForm

class StudentView(generic.ListView):
    template_name = 'students/student_tmpl.html'
    context_object_name = 'StudentList'

    def get_queryset(self):
        """Return students from group"""
        return Student.objects.filter(st_group=self.kwargs['grp_id'])


class GroupView(generic.ListView):
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


def actions(request, typ, act, obj_id):
    if typ == 'std':
        workForm = StudentForm
        workModel = Student
    elif typ == 'grp':
        workForm = GroupForm
        workModel = Group.objects.get(id=int(obj_id))
        print(workForm(workModel))
    if act == 'crt':
        form = workForm()
        return render(request, 'students/action_tmpl.html', 
                      {'form':form,'act':act})
    elif act == 'edt':
        form = workForm(workModel)
        return render(request, 'students/action_tmpl.html',
                      {'form':form,'act':act})
    elif act == 'dlt':
        form = workForm(workModel.objects.get(id=int(obj_id)))
        return render(request, 'students/action_tmpl.html', 
                      {'form':form,'act':act})

#    if request.method == 'POST':
#        form = StudentForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return render(request, 'students/action_tmpl.html')
#    else:
#         form = ForumUserForm()
#    return render(request, 'students/action.html', {'form':form})

