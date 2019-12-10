from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views import generic

from . import models, forms


def index(request):
    # if request.method == 'POST':
    #     form = forms.ReceiverClassForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/collector/receivers/')

    RecyclingRequestFormSet = formset_factory(forms.RecyclingRequestClassForm)
    if request.method == 'POST':
        request_formset = RecyclingRequestFormSet(request.POST)
        if request_formset.is_valid():
            for form in request_formset:
                id = form.id
                status = form.status
                # models.RecyclingRequest.objects.filter(id=id).update(status=status)
                form.save()

    # else:
    #     number = models.RecyclingRequest.objects.filter(status="ثبت اطلاعات")
    #     return render(
    #         request,
    #         'index.html',
    #         context={'recycle_request': number},
    #     )

    else:
        request_formset = RecyclingRequestFormSet()
        items = models.RecyclingRequest.objects.filter(status="ثبت اطلاعات")
        request_formset = forms.RecyclingRequestModelFormset(
            queryset=models.RecyclingRequest.objects.filter(status="ثبت اطلاعات"))
        # for item in items:
        #     print(item)
        #     forms.RecyclingRequestClassForm(
        #         initial={'id': item.id, 'requester': item.requester.fullname, 'receiver': item.receiver.fullname,
        #                  'address': item.address, 'status': item.status, 'trash_type': item.trash_type})

    return render(request, 'index.html', {'formset': request_formset})


class RequestListView(generic.ListView):
    model = models.RecyclingRequest
    context_object_name = 'recycle_request'
    template_name = 'request_list.html'


class RequestDetailView(generic.ListView):
    model = models.RecyclingRequest
    context_object_name = 'recycle_request'
    template_name = 'request_detail.html'


class ReceiverListView(generic.ListView):
    model = models.Receiver
    context_object_name = 'receiver_list'
    template_name = 'receiver_list_table.html'


class ReceiverCreate(generic.CreateView):
    model = models.Receiver
    fields = {"fullname", "mobile_number"}
    # initial =
    template_name = 'receiver_create.html'


def receiver_create(request):
    if request.method == 'POST':
        form = forms.ReceiverClassForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collector/receivers/')

    else:
        form = forms.ReceiverClassForm()

    return render(request, 'receiver_create.html', {'form': form})


def receiver_detail(request, id):
    receiver = models.Receiver.objects.filter(id=id)
    context_object_name = receiver
    return render(
        request,
        'receiver_detail.html',
        context={'receiver': receiver},
    )


def receiver_edit(request, id):
    if request.method == 'POST':
        receiver = models.Receiver.objects.filter(id=id).update(request)
        request_formset = forms.RecyclingRequestModelFormset(
            queryset=models.RecyclingRequest.objects.filter(status="ثبت اطلاعات"))

        return render(request, 'index.html', {'formset': request_formset})


def receiver_delete(request, id):
    if request.method == 'POST':
        receiver = models.Receiver.objects.filter(id=id).delete()
        context_object_name = receiver
        return render(
            request,
            'receiver_detail.html',
            context={},
        )
    else:
        pass
