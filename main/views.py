from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import logging
import csv, io
from .models import experiments


# Create your views here.

#def index(request):

#   return render (request ,'main/index.html')

def index(request):
    template = "main/index.html"

    prompt = {
        'order': "Order of csv should be first_name, last_name, email, ip_address, message"
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This file is not a .csv file")

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';', quotechar="|"):
        _, created = experiments.objects.update_or_create(
            gene        =column[0],
            specie      =column[1],
            accession   =column[2],
            comparison  =column[3],
            foldchange  =column[4],
            p_value     =column[5],
            t_statistic =column[6],
        )

    context = {}
    return render(request, template, context)