
from django.urls import path
from document.views import DocumentListCreateView, DocumentDetailView

urlpatterns = [
    path('api/list/', DocumentListCreateView.as_view(), name='api_document_list'),
    path('api/detail/<int:pk>/', DocumentDetailView.as_view(), name='api_document_detail'),
]
