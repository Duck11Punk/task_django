from django.conf.urls import url
from json_app.views import show_spares_json, show_alt_json, show_json_table, show_json


urlpatterns = [ 
    # django_json/
    url(r'^spares_json/$', show_spares_json, name='show_spares_json' ),

    # django_json/alt_json/
    url(r'^alt_json/$', show_alt_json, name='show_alt_json' ),

    # django_json/json_table/
    url(r'^json_table/$', show_json_table, name='show_json_table' ),

    # django_json/json_file/
    url(r'^json_file/$', show_json, name='show_json' ),

    

    ]

  