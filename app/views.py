import re

from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView

from .models import Mapping


class Redirect(APIView):
    def get(self, request, path):
        url = get_object_or_404(Mapping, path=path).url
        if not re.match(r'https?:\/\/', url):
            url = 'http://' + url
        return redirect(url, permanent=True)
