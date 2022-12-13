from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
    