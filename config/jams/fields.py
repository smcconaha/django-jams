from rest_framework import serializers

class NameListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title
        # if value.tile:
        #     return value.title
        # else:
        #     return value.name
