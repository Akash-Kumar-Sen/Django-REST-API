# Rest framework imports
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Django filter import
from django_filters import rest_framework as filters

# My Imports
from datetime import datetime
from .models import BoxItem
from .serializers import BoxItemSerializer,StaffBoxItemSerializer


# List View
class BoxItemList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)

    filter_fields = {
        'length': ['gt', 'lt'],
        'width': ['gt', 'lt'],
        'height': ['gt', 'lt'],
        'creation_date':['gt','lt'],
        'creator':['exact']
    }

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StaffBoxItemSerializer
        return BoxItemSerializer

    def get_queryset(self):
        queryset = BoxItem.objects.all()
        queryset=self.filter_by_area(queryset)
        queryset=self.filter_by_volume(queryset)
        queryset=self.filter_for_own_objects(queryset)
        return queryset

    #Filter By Area
    def filter_by_area(self,queryset):
        area_more_than = self.request.query_params.get('area-more-than')
        area_less_than = self.request.query_params.get('area-less-than')

        if (not area_less_than) and (not area_more_than):
            return queryset 

        empty_queryset =BoxItem.objects.none()

        if area_less_than is not None:
            for query in queryset:
                if query.get_area()<=float(area_less_than):
                    empty_queryset|=BoxItem.objects.filter(id=query.id)

        if area_more_than is not None:
            for query in queryset:
                if query.get_area()>=float(area_more_than):
                    empty_queryset|=BoxItem.objects.filter(id=query.id)

        return empty_queryset

    #Filter By Volume
    def filter_by_volume(self,queryset):
        volume_more_than = self.request.query_params.get('volume-more-than')
        volume_less_than = self.request.query_params.get('volume-less-than')

        if (not volume_less_than) and (not volume_more_than):
            return queryset 

        empty_queryset =BoxItem.objects.none()

        if volume_less_than is not None:
            for query in queryset:
                if query.get_volume()<=float(volume_less_than):
                    empty_queryset|=BoxItem.objects.filter(id=query.id)

        if volume_more_than is not None:
            for query in queryset:
                if query.get_volume()>=float(volume_more_than):
                    empty_queryset|=BoxItem.objects.filter(id=query.id)

        return empty_queryset

    #Filter for own objects
    def filter_for_own_objects(self,queryset):
        username = self.request.query_params.get('created-by')

        #Own username feature for staff user        
        if username == "me" and self.request.user.is_staff:
            queryset=queryset.filter(creator=self.request.user)

        return queryset

# Create View
class CreateBoxItem(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    permission_classes = (IsAdminUser, )
    serializer_class = StaffBoxItemSerializer

    def get_queryset(self):
        queryset = BoxItem.objects.filter(creator=self.request.user)
        return queryset

    def perform_create(self, serializer):     
        serializer.save(creator=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Update View
class UpdateBoxItem(mixins.UpdateModelMixin,generics.GenericAPIView):
    permission_classes = (IsAdminUser, )
    queryset = BoxItem
    serializer_class = StaffBoxItemSerializer

    def perform_update(self, serializer):
        serializer.save(last_updated=datetime.now())
        #return super().perform_update(serializer)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

# Delete View
class DeleteBoxItem(mixins.DestroyModelMixin,generics.GenericAPIView):
    permission_classes = (IsAdminUser, )
    queryset = BoxItem
    serializer_class = StaffBoxItemSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)