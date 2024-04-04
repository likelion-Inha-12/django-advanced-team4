import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Member

# 1. 회원 생성 - 김시원
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

# 2. 회원 정보 조회 - 김시원
def get_member(request, id):
    if request.method == 'GET':
        member = get_object_or_404(Member, id=id)

        data = {
            'id' : member.id,
            'email' : member.email,
            'is_leader' : member.is_leader,
            'hearts' : member.hearts
        }

        return JsonResponse(data, status=200)
    return JsonResponse({'message':'GET 요청만 허용됩니다.'})

# 3. 회원 정보 수정 - 김시원
def update_member_password(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        password = data.get('password')
        member = get_object_or_404(Member, id=id)
        member.password = password
        member.save()

        response_data = {
            "message": f"id: {id} 회원의 비밀번호가 업데이트되었습니다.",
            "password": password
        }

        return JsonResponse(response_data, status=200)
    return JsonResponse({'message': 'PUT 요청만 허용됩니다.'})