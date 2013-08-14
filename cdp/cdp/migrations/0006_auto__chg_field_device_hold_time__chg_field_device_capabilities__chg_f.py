# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Device.hold_time'
        db.alter_column(u'cdp_device', 'hold_time', self.gf('django.db.models.fields.CharField')(max_length=5, null=True))

        # Changing field 'Device.capabilities'
        db.alter_column(u'cdp_device', 'capabilities', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Device.outgoing_port'
        db.alter_column(u'cdp_device', 'outgoing_port', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Device.power_drawn'
        db.alter_column(u'cdp_device', 'power_drawn', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Device.management_addresses'
        db.alter_column(u'cdp_device', 'management_addresses', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Device.hold_time'
        raise RuntimeError("Cannot reverse this migration. 'Device.hold_time' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.capabilities'
        raise RuntimeError("Cannot reverse this migration. 'Device.capabilities' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.outgoing_port'
        raise RuntimeError("Cannot reverse this migration. 'Device.outgoing_port' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.power_drawn'
        raise RuntimeError("Cannot reverse this migration. 'Device.power_drawn' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Device.management_addresses'
        raise RuntimeError("Cannot reverse this migration. 'Device.management_addresses' and its values cannot be restored.")

    models = {
        u'cdp.device': {
            'Meta': {'object_name': 'Device'},
            'capabilities': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'duplex': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entry_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'hold_time': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'management_addresses': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'outgoing_port': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'power_drawn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
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