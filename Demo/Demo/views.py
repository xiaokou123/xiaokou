from django.http import HttpResponse
import datetime,time


def about(request):
    # return HttpResponse(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return HttpResponse(time.strftime('%Y-%m-%d %H:%M:%S'))


def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)
def sss(request,b,a):
    c='我%s年在%s'%(a,b)
    return HttpResponse (c)
from django.template.loader import get_template
def getindex(request):
    template_obj=get_template('index.html')
    result=template_obj.render()
    print(result)
    return HttpResponse(result)


from django.template import Template,Context