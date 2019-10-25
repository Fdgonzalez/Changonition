from rest_framework import routers
from ChangoFaceRec.views import PersonViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
