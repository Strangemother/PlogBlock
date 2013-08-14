# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Parse'
        db.create_table(u'cdp_parse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('log_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cdp.LogFile'])),
        ))
        db.send_create_signal(u'cdp', ['Parse'])

        # Adding M2M table for field devices on 'Parse'
        m2m_table_name = db.shorten_name(u'cdp_parse_devices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('parse', models.ForeignKey(orm[u'cdp.parse'], null=False)),
            ('device', models.ForeignKey(orm[u'cdp.device'], null=False))
        ))
        db.create_unique(m2m_table_name, ['parse_id', 'device_id'])

        # Adding field 'LogFile.created'
        db.add_column(u'cdp_logfile', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 8, 11, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'LogFile.log_file'
        db.alter_column(u'cdp_logfile', 'log_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting model 'Parse'
        db.delete_table(u'cdp_parse')

        # Removing M2M table for field devices on 'Parse'
        db.delete_table(db.shorten_name(u'cdp_parse_devices'))

        # Deleting field 'LogFile.created'
        db.delete_column(u'cdp_logfile', 'created')


        # User chose to not deal with backwards NULL issues for 'LogFile.log_file'
        raise RuntimeError("Cannot reverse this migration. 'LogFile.log_file' and its values cannot be restored.")

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