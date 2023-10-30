from rest_framework.views import APIView
from django.http import JsonResponse
import io
import json
from rest_framework.parsers         import JSONParser
from rest_framework.exceptions      import (ParseError,
                                            ValidationError)
from rest_framework                     import status
from older.exception_response_string import bad_request

def BadRequestPayload(msg):
    return {
        "message": str(msg),
        "error": bad_request
    }

class MemoBaseAPIView(APIView):
    def fuck(self, error, message=None):
        resp = {"error" : error}
        if message:
            resp['message'] = message
        return JsonResponse(resp)

    def success(self, data):
        return JsonResponse({"error": None, "data" : data})

    def check_permissions(self, request):
        # Run serializer before permission check in case that the serialized data is necessary for permission checking.
        if hasattr(self, 'serializer_class'):
            serializer = self.serializer_class
            if request.method == 'POST':
                try:
                    if request.body:
                        stream = io.BytesIO(request.body)
                        data = JSONParser().parse(stream)
                    else:
                        data = None
                except ParseError as e:
                    raise ValidationError(detail=BadRequestPayload(e))
            else:
                data = request.GET
            if data != None:
                request.serializer = serializer(data=data)
                try:
                    request.serializer.is_valid(raise_exception=True)
                except Exception as e:
                    message = request.serializer.errors.get('non_field_errors', None)
                    if message:
                        e = ValidationError(detail={'error': str(message[0]), "message": str(request.serializer.errors)})
                        e.status_code = status.HTTP_200_OK
                        raise e
                    else:
                        raise ValidationError(detail=BadRequestPayload(request.serializer.errors))
        super().check_permissions(request)