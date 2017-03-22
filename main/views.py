import json

from django.views.generic import FormView, TemplateView
from django.http import JsonResponse

from main.forms import UploadFileForm
from main.models import DataValue, DataRegion


class UploadFileView(FormView):
    template_name = 'upload.html'
    form_class = UploadFileForm
    success_url = '/parsed_data'

    def form_valid(self, form):
        data = json.loads(form.cleaned_data['file'].read().decode('utf8'))

        for item in data['data']:
            region, created = DataRegion.objects.get_or_create(name=item['Регион'])
            DataValue.objects.create(country=item['Страна'], value=int(float(item['Значение'])), region=region)
        return super(UploadFileView, self).form_valid(form)


class ParsedDataView(TemplateView):
    template_name = 'parsed_data.html'

    def get(self, request, *args, **kwargs):
        region_id = request.GET.get('region', '')
        if region_id:
            self.region = DataRegion.objects.get(pk=region_id)
        else:
            self.region = DataRegion.objects.first()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()

        ctx['countries'] = list(DataValue.objects.values_list('country', flat=True))
        ctx['selected_region'] = self.region
        ctx['regions'] = DataRegion.objects.all()

        return ctx


def get_chart_data(request, region):
    if region:
        obj = DataRegion.objects.get(id=region)
    else:
        obj = DataRegion.objects.first()
    data = {
        'countries': list(DataValue.objects.filter(region=obj).values_list('country', flat=True)),
        'values': list(DataValue.objects.filter(region=obj).values_list('value', flat=True))
    }
    return JsonResponse(data)