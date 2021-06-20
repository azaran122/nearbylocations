from django.views import generic

from django.contrib.gis.geos import Point

from django.contrib.gis.db.models.functions import Distance

from .models import Shop
from .models import Post



longitude = 32.3528711

latitude = 35.7769423


 
"""user_location = Point(longitude, latitude, srid=4326)
"""





class Home(generic.ListView):

# srid stands for Spatial Reference System Identifier. It’s a unique value to identify #spatial reference systems (projection systems used for interpreting the data in the spatial #database). 
    user_location = Point(longitude, latitude, srid=4326)
    model = Shop

    context_object_name = "shops"

    queryset = Shop.objects.annotate(

        distance=Distance("location", user_location)

    ).order_by("distance")[0:6]

    template_name = "shops/index.html"





home = Home.as_view()





def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        
        user_location = Point(longitude, latitude, srid=4326)
        model = Shop

        context_object_name = "shops"      # shops used in index , location is inside model

        queryset = Shop.objects.annotate(

        distance=Distance("location", user_location)

                ).order_by("distance")[0:6]

        template_name = "shops/index.html"






        





