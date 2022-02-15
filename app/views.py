from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView

from .models import Mapping


class Redirect(APIView):
    def get(self, request, path):
        return redirect(get_object_or_404(Mapping, path=path).url)
