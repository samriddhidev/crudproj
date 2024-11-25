from django.http import HttpResponse, JsonResponse
def home_page(request):
    friends=['sam',
             'vibs']
    return HttpResponse(friends)
