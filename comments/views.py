import json

from django.views import View
from django.http import JsonResponse

from .models import Comment

class Content(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            name       = data['name'],
            contents   = data['contents'],
        ).save()
        return HttpResponse(status=200)

    def get(self, request):
        return JsonResponse({'comment':list(Comment.objects.values())}, status=200)
