from rest_framework import serializers


name = "DRF"


class SubM(serializers.Serializer):
    w = serializers.IntegerField()
    x = serializers.IntegerField()
    y = serializers.CharField()
    z = serializers.CharField()


class ComplexM(serializers.Serializer):
    foo = serializers.IntegerField()
    bar = serializers.CharField()
    sub = SubM()
    subs = serializers.ListField(child=SubM())


def serialization_func(obj, many):
    return ComplexM(instance=obj, many=many).data


def deserialzation_func(obj, many):
    return ComplexM(data=obj, many=many).initial_data
