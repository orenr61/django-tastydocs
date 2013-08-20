from django.conf.urls.defaults import patterns
from views import doc

 urlpatterns = patterns(                                                                            
     '',                                                                                            
     (r'^api/$', versions),                                                                         
     (r'^api/(?P<api_name>.+)$', doc),                                                              
     (r'^example/(?P<api_name>.+)/(?P<resource_name>.+)/', 'tastydocs.views.example_data'),         
 )                                                                                                  
