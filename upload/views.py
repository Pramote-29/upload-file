from django.shortcuts import render, redirect
from .models import ImageUpload
from base64 import b64encode

# Label ของช่องสำหรับอัปโหลด
UPLOAD_LABELS = {
    'id_card': 'สำเนาบัตรประชาชนของผู้ประสบปัญหาสังคม',
    'house_registration': 'สำเนาทะเบียนบ้านของผู้ประสบปัญหาสังคม',
    'violator_id_card': 'สำเนาบัตรประชาชนของผู้กระทำความรุนแรง',
    'violator_house_registration': 'สำเนาทะเบียนบ้านของผู้กระทำความรุนแรง',
    'injury_evidence': 'เอกสารแสดงรูปภาพที่บ่งบอกถึงการถูกทำร้ายร่างกาย หรือร่องรอยบาดแผล',
}

def upload_view(request):
    if request.method == "POST":
        uploaded_image_ids = []  # เก็บ ID รูปภาพที่อัปโหลดใน session
        for field_name, label in UPLOAD_LABELS.items():
            # สำหรับ "เอกสารแสดงรูปภาพที่บ่งบอกถึงการถูกทำร้ายร่างกาย..."
            if field_name == 'injury_evidence':
                files = request.FILES.getlist(field_name)
                for file in files:
                    if file:
                        try:
                            binary_data = file.read()
                            image_upload = ImageUpload.objects.create(
                                image=binary_data,
                                document_type=field_name
                            )
                            uploaded_image_ids.append(image_upload.id)
                        except Exception as e:
                            print(f"Error saving file {field_name}: {str(e)}")
            else:
                file = request.FILES.get(field_name)
                if file:
                    try:
                        binary_data = file.read()
                        image_upload = ImageUpload.objects.create(
                            image=binary_data,
                            document_type=field_name
                        )
                        uploaded_image_ids.append(image_upload.id)
                    except Exception as e:
                        print(f"Error saving file {field_name}: {str(e)}")
        
        # เก็บ ID ของรูปภาพใน session
        request.session['uploaded_image_ids'] = uploaded_image_ids
        return redirect('check_data')
    
    return render(request, 'upload/upload.html', {'upload_labels': UPLOAD_LABELS})

def check_data_view(request):
    # ดึง ID ของรูปภาพที่ถูกอัปโหลดใน session
    uploaded_image_ids = request.session.get('uploaded_image_ids', [])
    
    # ดึงข้อมูลเฉพาะรูปภาพที่มี ID ใน session
    uploaded_images = ImageUpload.objects.filter(id__in=uploaded_image_ids)
    
    # เตรียมข้อมูลรูปภาพสำหรับแสดงใน template
    images = [
        {
            'field_name': image.document_type,
            'image_data': b64encode(image.image).decode('utf-8'),
        }
        for image in uploaded_images
    ]
    
    return render(request, 'upload/check_data.html', {
        'images': images,
        'upload_labels': UPLOAD_LABELS
    })

def add_data(request):
    return render(request, 'upload/add_data.html')


def mainpage_view(request):
    return render(request, 'upload/main-page.html')