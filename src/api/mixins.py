from rest_framework.permissions import AllowAny


class PublicApiViewPermissionsMixin(object):
    permission_classes = (AllowAny,)

class NoPaginateMixin(object):
    pagination_class = None

