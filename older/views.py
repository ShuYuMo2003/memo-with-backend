from django.shortcuts import render
from .basic_class import MemoBaseAPIView
from .serializer import    (GetPersonInfoSerializer,
                            SaveOrUpdatePersonInfoRequestSerializer,
                            PersonModelSerializer)
from .models import Person
from .exception_response_string import bad_request, no_such_person_id

# Create your views here.

class ShowPersonInfo(MemoBaseAPIView):
    serializer_class = GetPersonInfoSerializer
    def post(self, request):
        d = request.serializer.data
        return self.success(d)

class SaveOrUpdatePersonInfo(MemoBaseAPIView):
    serializer_class = SaveOrUpdatePersonInfoRequestSerializer

    def post(self, request):
        d = request.serializer.data
        if d.get('id'):
            try:
                personInstance = Person.objects.get(id=d['id'])
            except Person.DoesNotExist:
                return self.fuck(no_such_person_id, 'qaq')

            person = PersonModelSerializer(instance=personInstance, data=d)
            try:
                person.is_valid(raise_exception=True)
            except Exception as e:
                return self.fuck(bad_request, str(e))
            person.save()
            return self.success(person.data)
        else:
            # create
            newInstance = PersonModelSerializer(data=d)
            try:
                newInstance.is_valid(raise_exception=True)
            except Exception as e:
                return self.fuck(bad_request, str(e))
            newInstance.save()
            return self.success(newInstance.data)