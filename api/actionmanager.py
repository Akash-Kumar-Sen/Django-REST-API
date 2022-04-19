from .models import BoxItem,RestrictionModel
from datetime import datetime,timedelta

# Global Variables for restriction, fixed by admin
try:
    only_restriction_object=RestrictionModel.objects.get(id=1)
    A1=only_restriction_object.A1
    V1=only_restriction_object.V1
    L1=only_restriction_object.L1
    L2=only_restriction_object.L2
except:
    A1=100
    V1=1000
    L1=100
    L2=50

def _get_total_area():
    items=BoxItem.objects.all().order_by('id')
    area=0
    for item in items:
        area+=(item.length*item.width)
    return area


def _get_total_volume():
    items=BoxItem.objects.all().order_by('id')
    volume=0
    for item in items:
        volume+=(item.length*item.width*item.height)
    return volume

def _get_object_cnt():
    return BoxItem.objects.count()



# For area and volume not exceeding A1/V1
def _check_validity_area_volume(length,width,height):
    curr_area=length*width
    curr_volume=curr_area*height

    avg_area=(_get_total_area()+curr_area)/(_get_object_cnt()+1)
    avg_volume=(_get_total_volume()+curr_volume)/(_get_object_cnt()+1)

    if length<=0 or height<=0 or width<=0:
        return [False,"Length , Height or Width Cannot be Negative"]

    if avg_area>A1:
        return [False,"Average area exceeds the given mark for this entry"]

    if avg_volume>V1:
        return [False,"Average volume exceeds the given mark for this entry"]

    return [True,"0"]

# For overall object creation and that by a single user dont exceed L1/L2
def _check_validity_count(user):
    cnt_user=BoxItem.objects.filter(creator=user,creation_date__gt=datetime.now()-timedelta(days=7)).count()
    cnt_all=BoxItem.objects.filter(creation_date__gt=datetime.now()-timedelta(days=7)).count()

    if cnt_all+1>L1:
        return [False,"The weekly quota of adding boxes by all users is full"]
    
    if cnt_user+1>L2:
        return [False,"The weekly quota of adding boxes for this user is full"]
    
    return [True,"0"]
