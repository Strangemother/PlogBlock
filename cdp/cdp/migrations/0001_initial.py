# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Device'
        db.create_table(u'cdp_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('entry_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('capabilities', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('interface', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('outgoing_port', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hold_time', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('duplex', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('power_drawn', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('Power_management_id', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('Power_request_levels', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Management_addresses', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal(u'cdp', ['Device'])


    def backwards(self, orm):
        # Deleting model 'Device'
        db.delete_table(u'cdp_device')


    models = {
        u'cdp.device': {
            'Management_addresses': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'Meta': {'object_name': 'Device'},
            'Power_management_id': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'Power_request_levels': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cdp']