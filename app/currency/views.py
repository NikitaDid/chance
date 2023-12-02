from django.shortcuts import render
from app.currency.models import Rate, ContactUs, Source
from app.currency.forms import RateForm, MessageForms, SourceForm
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate_list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate_list')
    template_name = 'rate_update.html'


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('rate_list')
    template_name = 'rate_delete.html'


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


# --------------------------------------------------------


class MessageListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'message.html'


class MessageCreateView(CreateView):
    form_class = MessageForms
    success_url = reverse_lazy('message-list')
    template_name = 'message_create.html'


class MessageUpdateView(UpdateView):
    model = ContactUs
    form_class = MessageForms
    success_url = reverse_lazy('message-list')
    template_name = 'message_update.html'


class MessageDeleteView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy('message-list')
    template_name = 'message_delete.html'


class MessageDetailView(DetailView):
    model = ContactUs
    template_name = 'message_detail.html'


# --------------------------------------------------------

class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('source-list')
    template_name = 'source_delete.html'


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_details.html'


# --------------------------------------------------------



class IndexView(TemplateView):
    template_name = 'index.html'


def tets_templates(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }

    return render(request, 'test.html', context)
