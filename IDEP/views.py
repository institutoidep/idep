#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime 
from django.shortcuts import render 
 
def fecha_actual(request): 
    ahora = datetime.datetime.now() 
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora}) 
 
def horas_adelante(request, horas): 
    try: 
        horas = int(horas) 
    except ValueError: 
        raise Http404() 
    dt = datetime.datetime.now() + datetime.timedelta(hours=horas) 
    return render(request, 'horas_adelante.html', {'hora_siguiente': dt, 'horas': horas }) 