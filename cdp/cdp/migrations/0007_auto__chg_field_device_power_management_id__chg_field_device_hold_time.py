# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Device.power_management_id'
        db.alter_column(u'cdp_device', 'power_management_id', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Device.hold_time'
        db.alter_column(u'cdp_device', 'hold_time', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):

        # Changing field 'Device.power_management_id'
        db.alter_column(u'cdp_device', 'power_management_id', self.gf('django.db.models.fields.IntegerField')(max_length=3))

        # Changing field 'Device.hold_time'
        db.alter_column(u'cdp_device', 'hold_time', self.gf('django.db.models.fields.CharField')(max_length=5, null=True))

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
            'power_management_id': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
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