from django.http import HttpResponse, JsonResponse
def home_page(request):
    friends=['sam',
             'vis']
    return HttpResponse(friends)
