# -*- coding: utf-8 -*-
from django.views.generic import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from myproject.myapp.models import Document


class FileManagerView(CreateView):
    model = Document
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Document.objects.all()
        kwargs['fava'] = 'rava'
        return super(FileManagerView, self).get_context_data(**kwargs)


class FileRemoveView(DeleteView):
    model = Document
    success_url = reverse_lazy('main')
