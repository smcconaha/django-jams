from rest_framework import serializers

class NameListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title
    
#added this class to pull create an album list serializer that shows songs on each album
