from rest_framework import serializers

from .models import Projects

# class Projects_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = (


#         )




class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = (
			"name",
			"description",
			"video",
			"image",
			"slug",
			"image_path",
			"video_path"
        )