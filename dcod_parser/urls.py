from django.conf.urls import url
from django.contrib import admin

from main.views import UploadFileView, ParsedDataView, get_chart_data

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^parsed_data/$', ParsedDataView.as_view(), name='parsed_data'),
    url(r'^chart/(?P<region>[-\w]+)/$', get_chart_data, name='chart_data'),
    url(r'^$', UploadFileView.as_view(), name='upload_file'),
]
