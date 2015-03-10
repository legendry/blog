from django import template
from blog.models import Category
from django.core.urlresolvers import reverse

register=template.Library()

@register.tag(name='showcategory')
def showcategory(parser,token):
    return categories()

class categories(template.Node):
    def __init__(self):
        self.categoryList= Category.objects.all()
    def render(self, context):
        if self.categoryList:
            ct=''
            for category in self.categoryList:
                ct = ct + "<li><a href=\""+reverse("blog.views.searchbycategory")+"?categoryid="+str(category.id)+"\">"+category.category_name+"</a></li>"
                print (ct)
            return ct