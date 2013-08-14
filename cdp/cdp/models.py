from django.db import models

class LogFile(models.Model):
	'''
	A single log file loaded into the database
	'''
	created = models.DateTimeField(auto_now_add=True)
	log_file = models.FileField(upload_to='uploads', blank=True, null=True)

	def __unicode__(self):
		return '%s:%s' % (self.log_file, self.created)


class Device(models.Model):
	device_id = models.CharField(max_length=255, null=True, blank=True)
	entry_address = models.IPAddressField(null=True, blank=True)
	platform = models.CharField(max_length=255, null=True, blank=True)
	capabilities = models.CharField(max_length=255, null=True, blank=True)
	interface = models.CharField(max_length=25, null=True, blank=True)
	outgoing_port = models.CharField(max_length=255, null=True, blank=True)
	hold_time = models.CharField(max_length=20, help_text='seconds', null=True, blank=True)
	version = models.CharField(max_length=255, null=True, blank=True)
	duplex = models.CharField(max_length=200, null=True, blank=True)
	power_drawn = models.CharField(max_length=20, null=True, blank=True)
	power_request_id = models.CharField(max_length=10, null=True, blank=True) 
	power_management_id = models.CharField(max_length=3, null=True, blank=True)
	power_request_levels = models.CharField(max_length=255, null=True, blank=True)
	management_addresses = models.IPAddressField(null=True, blank=True)

	def __unicode__(self):
		return "%s %s" % (self.platform, self.entry_address)


class Parse(models.Model):
	'''
	A parse procedure coupling a file and parse data
	'''
	created = models.DateTimeField(auto_now_add=True,
		help_text="When the parse procedure took place")
	log_file = models.ForeignKey(LogFile,
		help_text="The log file associated with the parse procedure")
	devices = models.ManyToManyField(Device,
		help_text="Devices created and added to the database during the file parse")