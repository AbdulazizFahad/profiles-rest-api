from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test"""

    def get(self, request, Format=None):
        """Retrun a list of APIView features"""
        an_apiview = [
            "F1",
            "F2",
            "F3"
        ]

        return Response({"Message":"welcome","an_apiview":an_apiview}) 

