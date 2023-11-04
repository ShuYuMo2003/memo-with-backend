from django.shortcuts import render
from .basic_class import MemoBaseAPIView
from .serializer import    (GetPersonInfoRequestSerializer,
                            SaveOrUpdatePersonInfoRequestSerializer,
                            PersonModelSerializer,
                            SetPublicRequestSerializer,
                            GetAllPersonRequestSerializer)
from .models import Person
from .exception_response_string import *
from django.http import JsonResponse

from django.conf import settings

from django import forms

from uuid import uuid1 as g_uuid

class UploadPhotoForm(forms.Form):
    photo = forms.FileField()

def savePhoto(file):
    photo_uuid = g_uuid()
    orignal_name = file.name
    file_extension = orignal_name.split('.')[-1]
    file_name = f'{photo_uuid}.{file_extension}'

    with open(f'./static/photo/{file_name}', 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_name

def upload_file(request):
    if request.method == "POST":
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            file_handler = request.FILES["photo"]
            if file_handler.size > 10 * 1024 * 1024: # 10 MiB.
                return JsonResponse({"error": bad_photo, "data": "File too large."})
            if file_handler.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp', 'tiff']:
                return JsonResponse({"error": bad_photo, "data": "File type not supported."})
            uuid = savePhoto(file_handler)
            return JsonResponse({"error": None, "data": uuid})
        else:
            return JsonResponse({"error": bad_request, "data": "Invalid form."})
    else:
        return JsonResponse({"error" : bad_request, "data" : "POST method only."})

class ShowPersonInfo(MemoBaseAPIView):
    serializer_class = GetPersonInfoRequestSerializer
    def post(self, request):
        name = request.serializer.data['name']
        instances = Person.objects.filter(name__icontains=name, is_public=True)

        if not instances:
            return self.fuck(no_such_person_name, f'\'{name}\' is not in the database.')

        serializer = PersonModelSerializer(instances, many=True)

        return self.success(serializer.data)

class SetPublic(MemoBaseAPIView):
    serializer_class = SetPublicRequestSerializer

    def post(self, request):
        d = request.serializer.data

        if d['token'] != settings.MANAGE_TOKEN:
            return self.fuck(bad_token, 'Your token is not correct.')

        try:
            instance = Person.objects.get(id=d['id'])
        except Person.DoesNotExist:
            return self.fuck(no_such_person_id, "No such person in database.")

        instance.is_public = d['is_public']
        instance.save()

        return self.success('success')

class GetAllPerson(MemoBaseAPIView):
    serializer_class = GetAllPersonRequestSerializer

    def post(self, request):
        d = request.serializer.data

        if d['token'] != settings.MANAGE_TOKEN:
            return self.fuck(bad_token, 'Your token is not correct.')

        ser = PersonModelSerializer(Person.objects.all(), many=True)
        return self.success(ser.data)


class SaveOrUpdatePersonInfo(MemoBaseAPIView):
    serializer_class = SaveOrUpdatePersonInfoRequestSerializer

    def post(self, request):
        d = request.serializer.data

        if d['token'] != settings.MANAGE_TOKEN:
            return self.fuck(bad_token, 'Your token is not correct.')

        if d.get('id'):
            try:
                personInstance = Person.objects.get(id=d['id'])
            except Person.DoesNotExist:
                return self.fuck(no_such_person_id, 'qaq')
            if not d.get('is_public'):
                d['is_public'] = False

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