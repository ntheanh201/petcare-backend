from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PetcareUser


class PetcareMemberSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(source="assigned_user.id", read_only=True)
    # username = serializers.CharField(source="assigned_user.username", read_only=True)
    # participating_group = serializers.SerializerMethodField()

    # def get_participating_group(self, obj):
        # result_set = GroupPro.objects.filter(members=obj).values("id", "cover", "name")
        # # result_set = GroupPro.objects.filter(members=obj)
        # group_admin_set = GroupPro.objects.filter(admins=obj)
        # response_list = list()
        # for result in result_set:
        #     response = dict(result)
        #     response["is_admin"] = False
        #     for group_obj in group_admin_set:
        #         if group_obj.id == response["id"]:
        #             response["is_admin"] = True
        #     response["cover"] = "http://103.130.218.26:6960/media/" + result["cover"]
        #     response_list.append(response)
        # # return id, "http://103.130.218.26:6960/media/" + cover, name
        # return response_list

    class Meta:
        model = PetcareUser
        # fields = [
        #     "avatar",
        #     "url",
        #     "id",
        #     "username",
        #     "gender",
        #     "fullname",
        #     "phone",
        #     "address",
        #     "email",
        #     "dateOfBirth"
        # ]
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data["validate_data"] = False
