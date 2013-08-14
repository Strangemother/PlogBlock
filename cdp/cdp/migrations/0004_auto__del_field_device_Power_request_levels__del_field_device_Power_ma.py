# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Device.Power_request_levels'
        db.delete_column(u'cdp_device', 'Power_request_levels')

        # Deleting field 'Device.Power_management_id'
        db.delete_column(u'cdp_device', 'Power_management_id')

        # Adding field 'Device.power_management_id'
        db.add_column(u'cdp_device', 'power_management_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3),
                      keep_default=False)

        # Adding field 'Device.power_request_levels'
        db.add_column(u'cdp_device', 'power_request_levels',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Device.Power_request_levels'
        raise RuntimeError("Cannot reverse this migration. 'Device.Power_request_levels' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.Power_management_id'
        raise RuntimeError("Cannot reverse this migration. 'Device.Power_management_id' and its values cannot be restored.")
        # Deleting field 'Device.power_management_id'
        db.delete_column(u'cdp_device', 'power_management_id')

        # Deleting field 'Device.power_request_levels'
        db.delete_column(u'cdp_device', 'power_request_levels')


    models = {
        u'cdp.device': {
            'Management_addresses': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'Meta': {'object_name': 'Device'},
            'capabilities': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'duplex': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entry_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'hold_time': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'outgoing_port': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'power_drawn': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'power_management_id': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'power_request_levels': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cdp.logfile': {
            'Meta': {'object_name': 'LogFile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'cdp.parse': {
            'Meta': {'object_name': 'Parse'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'devices': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cdp.Device']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cdp.LogFile']"})
        }
    }

    complete_apps = ['cdp']