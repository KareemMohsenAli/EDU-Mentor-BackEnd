from django.urls import path ,include


urlpatterns = [ 
  
    path('api/', include('blogs.api.urls'))
    ]
