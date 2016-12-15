from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=70)
    birthday = models.DateField()
    student_card = models.CharField(max_length=11)
    st_group = models.ForeignKey('Group',
                              default=None,
                              on_delete=models.SET_DEFAULT)

    def __str__(self):
        return '%s %s %s' % (self.full_name,
                             self.birthday,
                             self.student_card)


class Group(models.Model):
    name = models.CharField(max_length=20)
    warden = models.OneToOneField('Student',
                                   default=None,
                                   on_delete=models.SET_DEFAULT)

    def __str__(self):
        return '%s %s' % (self.name,
                          self.warden.full_name)




