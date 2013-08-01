from django.db import models

# Create your models here.
class Device(models.Model):
	device_id = models.CharField(max_length=255)
	entry_address = models.IPAddressField()
	platform = models.CharField(max_length=255)
	capabilities = models.CharField(max_length=255)
	interface = models.CharField(max_length=255)
	outgoing_port = models.CharField(max_length=255)
	hold_time = models.IntegerField(max_length=5, help_text='seconds')
	version = models.CharField(max_length=255)
	duplex = models.CharField(max_length=200)
	power_drawn = models.DecimalField(max_digits=10, decimal_places=3)
	Power_request_id = models.IntegerField(max_length=10), 
	Power_management_id = models.IntegerField(max_length=3)
	Power_request_levels = models.CharField(max_length=255)
	Management_address(es) = models.IPAddressField()