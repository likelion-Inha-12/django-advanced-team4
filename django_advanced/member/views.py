import json
from django.http import JsonResponse
from .models import Member

def create_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)

		# 필드에 대한 값 추출
        email = data.get('email')
        password = data.get('password')
        is_leader = data.get('is_leader')
        hearts = data.get('hearts')
		
        # 추출한 값을 기반으로 Member 객체 생성하고 저장
        member = Member(
            email = email,
            password = password,
            is_leader = is_leader,
            hearts = hearts
        )

        member.save()
        return JsonResponse({'message' : 'success'})
    return JsonResponse({'message' : 'POST 요청만 허용됩니다.'})
