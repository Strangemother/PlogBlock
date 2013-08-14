from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.edit import FormMixin
from forms import UploadFile, DeviceForm
from models import LogFile, Device, Parse
from plog.blocks import CDPBlock
from plog import Plog
import csv
from django.http import HttpResponse

class Index(FormView):
    template_name='cdp/index.html'
    success_url='/files/'
    form_class=UploadFile

    def form_valid(self, form):
        log_file = form.save()
        # import pdb; pdb.set_trace()
        self.success_url = '/parse/%s' % log_file.pk
        return super(Index, self).form_valid(form)

    def form_invalid(self, form):
        return super(Index, self).form_invalid(form)


class LogFileList(ListView):
    model = LogFile

class CsvView(TemplateView):
    template_name = 'cdp/csv.html'

    def post(self, request, *args, **kwargs):
        
        context = self.get_context_data(**kwargs)
        pid = kwargs['parse']
        parse = Parse.objects.get(pk=pid)
        fs = [x.name for x in parse.devices.model._meta.fields]
        fields = [x for x in self.request.POST]

        sf = []
        for field in fields:
            if field in fs: sf.append(field)
        
        devices = parse.devices.values(*sf)
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="parse.csv"'
        writer = csv.writer(response)

        
        writer.writerow(sf)
        for device in devices:    
            dd = [device[x] for x in device]
            writer.writerow(dd)
        return response

    def get(self, request, *args, **kwargs):
        
        context = self.get_context_data(**kwargs)
        pid = kwargs['parse']
        parse = Parse.objects.get(pk=pid)
        fs = parse.devices.model._meta.fields
        fields = []
        for field in fs:
            fields.append(field)
        context['object_list'] = fields
        
        return self.render_to_response(context)


class ParseView(TemplateView):
    template_name='cdp/parse_view.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        log_file_id = kwargs.get('file')
        log_file = LogFile.objects.get(id=log_file_id)

        f = log_file.log_file
        plog = Plog(f, whitespace='|', terminator=',')
        plog.add_blocks(CDPBlock)
        plog.run()

        p = Parse(log_file=log_file)
        added = 0
        p.save()

        # Blocks captured.
        invalid = {
            'forms': [],
            'blocks': [],
        }

        for block in plog.data_blocks:
            device = None
            
            if block.valid():
                device_form = DeviceForm(block.as_dict())  
                if device_form.is_valid():
                    mod = device_form._meta.model(**device_form.cleaned_data)
                    added += 1
                    mod.save()
                    p.devices.add(mod)
                else:
                    # Blocks failed to push into database
                    invalid['forms'].append(device_form)
            else:
                # Blocks failed in inital parsing
                invalid['blocks'].append(block)

        p.save()

        context['log_file'] = log_file
        context['parse'] = p
        context['added'] = added
        context['plog'] = plog
        context['invalid'] = invalid


        return self.render_to_response(context)