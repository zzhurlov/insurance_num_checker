from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from checker.serializers import InsuranceNumberSerializer
from checker.models import InsuranceNumber


class CheckInsuranceNumberView(APIView):
    serializer_class = InsuranceNumberSerializer

    @extend_schema(
        summary="Check the Ins. number",
        description="""
            This endpoint allows a user to check the insurance number            
        """,
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                insurance_number = InsuranceNumber.objects.get(number=data["number"])
            except InsuranceNumber.DoesNotExist:
                return Response(
                    data={"message": "This insurance number does not exists!"}
                )

            return Response(data={"message": "НАЙДЕН"}, status=200)
