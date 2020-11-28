from rest_framework import serializers
from person.models import Profile


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
       model = Profile
       exclude = ['hobbies','fav_movies']

    def create(self,validated_data):
        user= super(UserCreationSerializer,self).create(validated_data)
        return user


