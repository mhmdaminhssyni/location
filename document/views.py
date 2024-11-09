
from rest_framework import generics
from .models import Document
from .serializers import DocumentSerializer
from .permissions import IsAuthenticatedOrRedirect


class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.live.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticatedOrRedirect] 


class DocumentDetailView(generics.RetrieveAPIView):
    queryset = Document.live.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticatedOrRedirect] 
