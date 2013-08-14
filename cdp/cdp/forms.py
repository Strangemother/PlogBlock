from django import forms
from models import LogFile, Device

class UploadFile(forms.ModelForm):
	class Meta:
		model = LogFile

class DeviceForm(forms.ModelForm):
	class Meta:
		model = Device
