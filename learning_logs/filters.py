import django_filters

from . models import *

class TopicFilter(django_filters.FilterSet):


    class Meta:
        model = Topic
        fields = {
            'city': ['contains']
        }