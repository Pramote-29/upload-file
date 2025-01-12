from django.db import models

class ImageUpload(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('id_card', 'สำเนาบัตรประชาชน'),
        ('house_registration', 'สำเนาทะเบียนบ้าน'),
        ('violator_id_card', 'บัตรประชาชนผู้กระทำ'),
        ('violator_house_registration', 'ทะเบียนบ้านผู้กระทำ'),
        ('injury_evidence', 'หลักฐานการบาดเจ็บ'),
    ]
    document_type = models.CharField(
        max_length=255,
        choices=DOCUMENT_TYPE_CHOICES,
        verbose_name="ประเภทเอกสาร"
    )
    image = models.BinaryField(
        verbose_name="ไฟล์รูปภาพ"
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="วันที่อัปโหลด"
    )

    def __str__(self):
        return f"Document: {self.document_type}, ID: {self.id}"