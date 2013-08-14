# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Device.power_request_id'
        db.add_column(u'cdp_device', 'power_request_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


        # Changing field 'Device.power_management_id'
        db.alter_column(u'cdp_device', 'power_management_id', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'Device.power_request_levels'
        db.alter_column(u'cdp_device', 'power_request_levels', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):
        # Deleting field 'Device.power_request_id'
        db.delete_column(u'cdp_device', 'power_request_id')


        # User chose to not deal with backwards NULL issues for 'Device.power_management_id'
        raise RuntimeError("Cannot reverse this migration. 'Device.power_management_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.power_request_levels'
        raise RuntimeError("Cannot reverse this migration. 'Device.power_request_levels' and its values cannot be restored.")

    models = {
        u'cdp.device': {
            'Meta': {'object_name': 'Device'},
            'capabilities': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'duplex': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entry_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'hold_time': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'management_addresses': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'outgoing_port': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'power_drawn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'power_management_id': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'power_request_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'power_request_levels': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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