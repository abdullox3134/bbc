from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from about.models import About
from about.pagination import ResultsSetPagination
from about.serializers import AboutSerializer


class AboutListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AboutSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return About.objects.all()


@api_view(['GET'])
def aboutdetail(request, pk):
    about = get_object_or_404(About, pk=pk)
    serializer = AboutSerializer(about, context={'request': request})
    return Response(serializer.data)
