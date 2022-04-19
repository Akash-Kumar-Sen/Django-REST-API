from rest_framework import serializers
from .models import BoxItem
from .actionmanager import _check_validity_area_volume,_check_validity_count


# Serializer for normal user
class BoxItemSerializer(serializers.ModelSerializer):
    volume = serializers.SerializerMethodField('_get_volume')
    area = serializers.SerializerMethodField('_get_area')

    def _get_volume(self,box_object):
        length = getattr(box_object, "length")
        width = getattr(box_object, "width")
        height = getattr(box_object, "height")

        return length*width*height

    def _get_area(self,box_object):
        length = getattr(box_object, "length")
        width = getattr(box_object, "width")

        return length*width

    
    class Meta:
        model = BoxItem
        fields = (
            'length', 
            'width',
            'height',
            'volume',
            'area',
        )


# Serializer for staff user
class StaffBoxItemSerializer(serializers.ModelSerializer):
    volume = serializers.SerializerMethodField('_get_volume')
    area = serializers.SerializerMethodField('_get_area')
    created_by = serializers.SerializerMethodField('_get_creator')

    def _get_volume(self,box_object):
        length = getattr(box_object, "length")
        width = getattr(box_object, "width")
        height = getattr(box_object, "height")

        return length*width*height

    def _get_area(self,box_object):
        length = getattr(box_object, "length")
        width = getattr(box_object, "width")

        return length*width

    def _get_creator(self,box_object):
        user=getattr(box_object,"creator")

        return str(user)

    def validate(self,data):

        # Limit the average length and volume
        try:
            length=data['length']
        except:
            length=self._args[0].length

        try:
            width=data['width']
        except:
            width=self._args[0].width

        try:
            height=data['height']
        except:
            height=self._args[0].height

        # Function from actionmanager
        validity_all=_check_validity_area_volume(length,width,height)

        is_valid=validity_all[0]
        error_msg=validity_all[1]

        if not is_valid:
            raise serializers.ValidationError(error_msg)

        # Limiting the total boxes added in a week, overall and by any user
        if self.context['request'].method == "POST":
            # Retrive the user
            user =  self.context['request'].user
            # Function from actionmanager
            validity_all=_check_validity_count(user)
            is_valid=validity_all[0]
            error_msg=validity_all[1]

            if not is_valid:
                raise serializers.ValidationError(error_msg)

        return data

    
    class Meta:
        model = BoxItem
        fields = (
            'length', 
            'width',
            'height',
            'volume',
            'area',
            'created_by',
            'last_updated',
        )

