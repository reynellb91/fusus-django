from django.contrib.auth.models import Group

from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_nested.viewsets import NestedViewSetMixin

from .models import User, Organization
from .serializers import UserModelSerializer, OrganizationModelSerializer, GroupModelSerializers

class UserViewSet(RetrieveModelMixin,
                  ListModelMixin,
                  CreateModelMixin,
                  UpdateModelMixin, 
                  DestroyModelMixin,
                  NestedViewSetMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'email']
    filterset_fields = ['phone']
    parent_lookup_kwargs = {'organization_pk': 'organization'}


class OrganizationViewSet(RetrieveModelMixin, 
                          UpdateModelMixin, 
                          GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class InfoApiView(GenericAPIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        resp = {
            'user_name': request.user.name,
            'id': request.user.id,
            'organization': getattr(request.user.organization, 'name', None),
            'public_ip': request.META.get('REMOTE_ADDR')
        }
        return Response(resp)


class GroupsViewSet(ListModelMixin, GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializers