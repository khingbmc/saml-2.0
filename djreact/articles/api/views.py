from rest_framework.generics import ListAPIView, RetrieveAPIView

from articles.models import Articles
from .serializers import AriticlesSerializer


class ArticlesListView(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = AriticlesSerializer

class ArticlesDetailView(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = AriticlesSerializer
