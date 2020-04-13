import json

from django.views import View
from django.http  import JsonResponse, HttpResponse
from .models      import User

class Signup(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
                email = data['email'],
	        password = data['password'],
        ).save()
        return JsonResponse({'message':'회원가입이 완료되었습니다.'},status=200)

class Login(View):
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(email = data['email'])
        if User.objects.filter(email = data['email']).exists(): 
            if User.password == data['password']:
                return JsonResponse({'message':'로그인이 되었습니다.'},status=200) 
        else:
            return JsonResponse({'message':'INVALID_USER'},status=401)
