from django.shortcuts import render
import pandas as pd
from pandas import date_range
from datetime import date, datetime, timedelta
from typing import List
from django.http import HttpResponseRedirect
import requests

def daterange(debut: date, fin: date, inter: int):
  end = datetime.strptime(fin, "%Y-%m-%d") - timedelta(days = inter)
  daterange = []
  datedebut: date
  datefin: date
  for element in pd.date_range(start= debut, end= end):
    datedebut= element
    datefin = datedebut + timedelta(days = inter)
    dateset = (datedebut.strftime("%Y-%m-%d"), datefin.strftime("%Y-%m-%d"))
    daterange.append(dateset)
  return daterange


def template(request):
  context = {
    'titre' : 'apptwo'
  }
  return render(request, 'apptwo/apptwo.html', context)