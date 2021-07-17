from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from listApi.models import CollegeList
from listApi.serializers import CollegeListSerializer


# Create your views here.


@api_view(['GET'])
def college_list(request):
    if request.method == "GET":
        colleges = CollegeList.objects.all()

        country_code = request.GET.get('code', None)
        if country_code is not None:
            colleges = colleges.filter(alpha_two_code__icontains=country_code)

        domain_check = request.GET.get('domain', None)
        if domain_check is not None:
            colleges = colleges.filter(domain__icontains=domain_check)

        name = request.GET.get('name', None)
        if name is not None:
            colleges = colleges.filter(name__icontains=name)

        colleges_serializer = CollegeListSerializer(colleges, many=True)
        return JsonResponse(colleges_serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
