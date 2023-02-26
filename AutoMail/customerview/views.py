# from django.shortcuts import render
import io

from customerview.models import CustomerInfo, CustomerPreview
from customerview.serializers import (CustomerInfoSerializer,
                                      CustomerPreviewSerializer)
from django.contrib.auth import get_user_model
from django.http import FileResponse
from django.template.loader import render_to_string
from django.utils import timezone
from reportlab.pdfgen import canvas
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def intro(request):
    return Response(data={"message": "Hello Consumer"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_customer_preview(request):
    data = request.data
    try:
        customer_preview = CustomerPreview.objects.create(
            order = data['order'],
            transaction = data['transaction'],
            initial_amount = data['initial_amount'],
            total_charges = data['total_charges'],
            payment_reference = data['payment_reference']
        )
    except:
        customer_preview = False
    
    if not customer_preview:
        return Response(data={"message": "There is an Error to add customer preview"}, status=status.HTTP_200_OK)
    serializer = CustomerPreviewSerializer(customer_preview, many=False)
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def customer_preview_list(request):
    try:
        customer_preview = CustomerPreview.objects.all()
    except:
        return Response(data={"message": "There is an Error to View List"}, status=status.HTTP_200_OK)
    serializer = CustomerPreviewSerializer(customer_preview, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def latest_preview_list(request):
    try:
        customer_preview = CustomerPreview.objects.latest('id')
    except:
        return Response(data={"message": "There is an Error to View List"}, status=status.HTTP_200_OK)
    serializer = CustomerPreviewSerializer(customer_preview, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def customer_preview_edit(request, preview_id):
    data = request.data
    qs = CustomerPreview.objects.filter(id=preview_id)
    if not qs.exists():
        return Response(data={"message": "Preview Not Exists"}, status=status.HTTP_200_OK)
    customer_preview = qs.first()
    customer_preview.order = data['order']
    customer_preview.transaction = data['transaction']
    customer_preview.initial_amount = data['initial_amount']
    customer_preview.total_charges = data['total_charges']
    customer_preview.payment_reference = data['payment_reference']
    customer_preview.save()
    serializer = CustomerPreviewSerializer(customer_preview, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def customer_preview_delete(request, preview_id):
    qs = CustomerPreview.objects.filter(id=preview_id)
    if not qs.exists():
        return Response({"message": "Customer Preview not exits"}, status=status.HTTP_404_NOT_FOUND)
    customer_preview = qs.first()
    customer_preview.delete()
    return Response({"message": "Customer Preview Removed"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def customerList(request):
    try:
        customerInfo = CustomerInfo.objects.all()
    except:
        return Response(data={"message": "There is an Error to See Customer List"}, status=status.HTTP_200_OK)
    serializer = CustomerInfoSerializer(customerInfo, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def customerInput(request):
    data = request.data
    print(data)
    try:
        customerInfo = CustomerInfo.objects.create(
        name = data['name'],
        address = data['address'],
        email = data['email'],
        phone = data['phone']
        )
    except:
        customerInfo = False
    if not customerInfo:
        return Response(data={"message": "There is an Error to create account"}, status=status.HTTP_200_OK)
    customerPreview = CustomerPreview.objects.latest('id')
    user_serializer = CustomerInfoSerializer(customerInfo, many=False)
    info_data = user_serializer.data
    serializer = CustomerPreviewSerializer(customerPreview, many=False)
    info_data.update(serializer.data)
    return Response(data=info_data, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
def generate_invoice(request):
    # Load the invoice data from the request
    data = request.data

    # Render the invoice template with the data
    rendered_html = render_to_string('invoice_template.html', {'data': data})

    # Create a PDF file from the HTML
    pdf_file = io.BytesIO()
    p = canvas.Canvas(pdf_file)
    p.drawString(100, 750, 'Invoice')
    p.drawString(100, 700, f"Order ID: {data['order']}")
    p.drawString(100, 650, f"Transaction ID: {data['transaction']}")
    p.drawString(100, 600, f"Initial Amount: {data['initial_amount']}")
    p.drawString(100, 550, f"Total Charges: {data['total_charges']}")
    p.drawString(100, 500, f"Payment Reference: {data['payment_reference']}")
    p.drawString(100, 450, f"Date: {timezone.now().strftime('%d/%m/%Y')}")
    p.drawString(100, 400, f"Customer Name: {data['name']}")
    p.drawString(100, 350, f"Address: {data['address']}")
    p.drawString(100, 300, f"Email: {data['email']}")
    p.drawString(100, 250, f"Phone: {data['phone']}")
    p.drawString(100, 200, 'Thank you for your business!')
    p.save()

    # Reset the PDF file pointer to the beginning
    pdf_file.seek(0)

    # Return the PDF as a downloadable response
    response = FileResponse(pdf_file, as_attachment=True, filename='invoice.pdf')
    return response