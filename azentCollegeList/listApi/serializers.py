from rest_framework import serializers
from listApi.models import CollegeList


class CollegeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollegeList
        fields = ('id',
                  'alpha_two_code',
                  'country',
                  'domain',
                  'name',
                  'web_page')
