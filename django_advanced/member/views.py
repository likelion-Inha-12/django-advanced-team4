import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Member

# 1. 회원 생성 - 김시원
def create_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)

		# 필드에 대한 값 추출
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        is_leader = data.get('is_leader')
        hearts = data.get('hearts')
		
        # 추출한 값을 기반으로 Member 객체 생성하고 저장
        member = Member(
            name = name, #대표 이름으로 출력하기 위해 추가
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
            'name' : member.name,
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

# 4. 회원 정보 삭제 - 최우진
def delete_member(request, id):
    if request.method=='DELETE':
        member = get_object_or_404(Member, id=id)
        member.delete()
        response_data = {
            "message": f"id: {id} 회원 정보가 삭제되었습니다."
        }
        return JsonResponse(response_data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

# 5. 하트 누르기 - 최우진
def add_heart_to_member(request, id):
    if request.method == 'PATCH':
        member = get_object_or_404(Member, id=id)
        member.hearts += 1
        member.save()
        response_data = {
            "message": f"id: {id} 회원의 하트 수가 업데이트되었습니다.",
            "hearts": member.hearts
        }
        return JsonResponse(response_data, status=200)
    return JsonResponse({'message': 'PATCH 요청만 허용됩니다.'})

# 6. 대표 임명하기 - 손가영
def appoint_leader(request, id):
    if request.method == 'POST':
        member = get_object_or_404(Member, pk=id)
        if Member.objects.filter(is_leader=True).exclude(pk=id).exists():
            return JsonResponse({"message":"대표는 2명 이상일 수 없습니다."}, status=400)
        if member.is_leader==True:
            member.is_leader=False
            member.save()
            return JsonResponse({"message":f"{member.name}(을)를 대표 자격을 박탈하였습니다."})
        else:
            member.is_leader = True
            member.save()
            return JsonResponse({"message":f"{member.name}(을)를 대표로 임명하였습니다."})
    else:
        return JsonResponse({"message":"POST 요청만 허용합니다."})
        
# 7. 모든 회원 정보 조회 - 손가영
def get_all(request):
    if request.method == 'GET':
        members = Member.objects.all()
        total_hearts = sum(member.hearts for member in members)
        data = {
            "message" : "전체 회원 수와 하트 수 입니다.",
            "member_count" : members.count(),
            "total_hearts" : total_hearts
        }      
        return JsonResponse(data)
    else:
        return JsonResponse({'message':'GET 요청만 허용됩니다.'})  