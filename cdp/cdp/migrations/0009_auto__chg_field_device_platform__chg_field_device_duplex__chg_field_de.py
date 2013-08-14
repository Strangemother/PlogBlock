# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Device.platform'
        db.alter_column(u'cdp_device', 'platform', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Device.duplex'
        db.alter_column(u'cdp_device', 'duplex', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Device.interface'
        db.alter_column(u'cdp_device', 'interface', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'Device.version'
        db.alter_column(u'cdp_device', 'version', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Device.entry_address'
        db.alter_column(u'cdp_device', 'entry_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True))

        # Changing field 'Device.device_id'
        db.alter_column(u'cdp_device', 'device_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Device.power_request_id'
        db.alter_column(u'cdp_device', 'power_request_id', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Device.platform'
        raise RuntimeError("Cannot reverse this migration. 'Device.platform' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.duplex'
        raise RuntimeError("Cannot reverse this migration. 'Device.duplex' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.interface'
        raise RuntimeError("Cannot reverse this migration. 'Device.interface' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.version'
        raise RuntimeError("Cannot reverse this migration. 'Device.version' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.entry_address'
        raise RuntimeError("Cannot reverse this migration. 'Device.entry_address' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.device_id'
        raise RuntimeError("Cannot reverse this migration. 'Device.device_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.power_request_id'
        raise RuntimeError("Cannot reverse this migration. 'Device.power_request_id' and its values cannot be restored.")

    models = {
        u'cdp.device': {
            'Meta': {'object_name': 'Device'},
            'capabilities': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'duplex': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'entry_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hold_time': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'management_addresses': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'outgoing_port': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'power_drawn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'power_management_id': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'power_request_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'power_request_levels': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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