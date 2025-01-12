from django.shortcuts import render, redirect
from .models import ImageUpload
from base64 import b64encode

UPLOAD_LABELS = {
    'id_card': 'สำเนาบัตรประชาชนของผู้ประสบปัญหาสังคม',
    'house_registration': 'สำเนาทะเบียนบ้านของผู้ประสบปัญหาสังคม',
    'violator_id_card': 'สำเนาบัตรประชาชนของผู้กระทำความรุนแรง',
    'violator_house_registration': 'สำเนาทะเบียนบ้านของผู้กระทำความรุนแรง',
    'injury_evidence': 'เอกสารแสดงรูปภาพที่บ่งบอกถึงการถูกทำร้ายร่างกาย หรือร่องรอยบาดแผล',
}

def upload_view(request):
    if request.method == "POST":
        for field_name in UPLOAD_LABELS.keys():
            file = request.FILES.get(field_name)
            if file:
                print(f"Uploading file for {field_name}: {file.name}")
                binary_data = file.read()
                print(f"File size: {len(binary_data)} bytes")
                ImageUpload.objects.create(
                    image=binary_data,
                    document_type=field_name
                )
        return redirect('check_data')
    return render(request, 'upload/upload.html', {'upload_labels': UPLOAD_LABELS})


def add_data(request):
    return render(request, 'upload/add_data.html')

def check_data_view(request):
    uploaded_images = ImageUpload.objects.all()
    
    # เตรียมข้อมูลรูปภาพให้เป็น Base64 เพื่อแสดงใน HTML
    images = [
        {
            'field_name': image.document_type,
            'image_data': b64encode(image.image_data).decode('utf-8'),  # แปลงเป็น Base64
        }
        for image in uploaded_images
    ]

    return render(request, 'upload/check_data.html', {'images': images, 'upload_labels': UPLOAD_LABELS})