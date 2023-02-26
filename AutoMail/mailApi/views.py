# from django.shortcuts import render
from authentication.serializers import UserSerializerWithToken
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from mailApi.excelToJson import convertJson
from mailApi.models import MailInfo
from mailApi.serializers import MailSerializer
from mailApi.YCloudApi import YCloudAPI
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def intro(request):
    return Response(data={"message": "Hello Mail API"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mail_send(request):
    data = request.data
    sender_mail = data['sender_mail']
    subject = data['subject']
    content = data['content']
    file = request.FILES.get('excel_file')
    # print(sender_mail, subject, content, file)
    MailInfo.objects.create(
        sender_mail = sender_mail,
        subject = subject,
        content = content
    )
    missing = []
    file_data = convertJson(file)
    cloud_api = YCloudAPI()
    for i in file_data:
        name = f"{i['fname']} {i['lname']}"
        client_mail = i['email']
        address = f"{i['address']}, {i['city']}  {i['state']}"
        content = content.replace("NAMEOF", name)
        content = content.replace("ADDRESSOF", address)
        success_msg = cloud_api.mail_api(sendermail=sender_mail, receiver=client_mail, subject=subject, content=content)
        if not success_msg:
            missing.append(client_mail)

    missing_mail = {'missing_mail': missing}
    serializer = MailSerializer(missing_mail)
    return Response(serializer.data, status=status.HTTP_200_OK)




