from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Service for CRUD",
      default_version='v1.1',
      description='''
      Consider a store which has an inventory of boxes which are all 
      cuboid(which have length breadth and height). Each Cuboid has 
      been added by a store employee who is associated as the creator 
      of the box even if it is updated by any user later on.

      Admin panel : admin/

      Authentication System : Token based authentication\n


      Some More Info(Check the Side Bar for the rest) : \n
      Get All Boxes Created By Current User(Only for staff user): api/list?created-by=me\n
      Get All Boxes with volume more than X : GET api/list?volume-more-than=X\n
      Get All Boxes with volume less than X : GET api/list?volume-less-than=X\n
      Get All Boxes with area more than X : 'GET api/list?area-more-than=X\n
      Get All Boxes with area less than X : 'GET api/list?area-less-than=X\n
      Closing URL by / is mandatory for  : 'DELETE , PUT and PATCH\n
      ''',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="akashkumarsen4@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)