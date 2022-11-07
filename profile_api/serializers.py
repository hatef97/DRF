from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """ serializers a name field for testing our APIview """
    name = serializers.CharField(max_length=10)

