from django import forms
from .models import ImageUpload

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['document_type', 'image']
        labels = {
            'image': 'เลือกไฟล์รูปภาพ',
            'document_type': 'ประเภทเอกสาร',
        }