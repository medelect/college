from django import template

register = template.Library()

@register.inclusion_tag('./students/ref.html')
def edit_tag(obj):
    class_name = str(obj.__doc__).split('(')[0].lower()
    obj_link = '../../admin/students/%s/%s/change/'%(class_name, obj.id)
    return {'obj':obj,'obj_link':obj_link}


#class EditTagNode(template.Node):
#    def __init__(self, obj):
#        self.obj = obj
#
#    def render(self, context):
#        return datetime.datetime.now().strftime(self.format_string)
