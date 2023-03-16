from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from .forms import getFlight
from .models import parametre_recherche, buckets, items, legs, segments

def flights(request):
    if request.method == 'POST':
        form = getFlight(request.POST)
        if form.is_valid():
            params = {
                'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiOGY3OWYxM2Y1MDIzZjQyNzM2YzQwZWUyNGZkOTYwNGYwMzZlMzlmMDMxOGQ0MjdkMjA4ZmQ0NjQyMzlmYWRkYzk0MjVjZDdlNTliMzg5ZmMiLCJpYXQiOjE2Nzc1NzI1NjcsIm5iZiI6MTY3NzU3MjU2NywiZXhwIjoxNzA5MTA4NTY3LCJzdWIiOiIyMDI3OCIsInNjb3BlcyI6W119.jjasqZn9GZfo7qcai4SWj-OnUeYpmcnObyByVLt2m1x_ajtrbCeGtawoezCnxFTqhZvPbN4AEC1e4FW2oI62rQ',
                'adults': form.cleaned_data['adults'],
                'origin' : form.cleaned_data['origin'],
                'destination': form.cleaned_data['destination'],
                'departureDate': form.cleaned_data['departureDate'],
                'returnDate': form.cleaned_data['returnDate'],
                'cabinClass': form.cleaned_data['cabinClass'],
                'currency': form.cleaned_data['currency'],
                'childAge1': form.cleaned_data['childAge1'],
                'childAge2': form.cleaned_data['childAge2'], 
                'childAge3': form.cleaned_data['childAge3'], 
                'childAge4': form.cleaned_data['childAge4'], 
                'childAge5': form.cleaned_data['childAge5'],
                'childAge6': form.cleaned_data['childAge6'],
                'childAge7': form.cleaned_data['childAge7'],
                'childAge8': form.cleaned_data['childAge8']
            }
            pr = parametre_recherche(origin = params['origin'],destination = params['destination']
            ,adults = params['adults']
            ,cabinClass = params['cabinClass']
            ,childAge1 = params['childAge1']
            ,childAge2 = params['childAge2']
            ,childAge3 = params['childAge3']
            ,childAge4 = params['childAge4']
            ,childAge5 = params['childAge5']
            ,childAge6 = params['childAge6']
            ,childAge7 = params['childAge7']
            ,childAge8 = params['childAge8']
            ,currency = params['currency']
            ,departureDate = params['departureDate']
            ,returnDate = params['returnDate'])
            pr.save()


            api_result = requests.get('https://app.goflightlabs.com/search-best-flights', params)
            api_response = api_result.json()
            bucketsdata = api_response['data']['buckets']

            for bucket in bucketsdata :
                bs = buckets(parametre_recherche = pr, name = bucket['name'], type = bucket['id'])
                bs.save()
                for item in bucket['items']:
                    its = items(buckets = bs,lien = item['deeplink'],prix = item['price']['formatted'] )
                    its.save()
                    for leg in item['legs']:
                        if leg == item['legs'] [0]:
                            typ = 'Aller'  
                        else:
                            typ = 'Retour' 
                        lgs = legs(items = its, aero_depart = leg['origin']['name'],aero_arrivee = leg['destination']['name'], 
                                   date_depart = leg['departure'], date_arrivee = leg['arrival'], nbre_escale = leg['stopCount'], 
                                   duree = leg['durationInMinutes'], type = typ)                        
                        lgs.save()
                        for segment in leg['segments']:
                            sgs = segments(legs = lgs, aero_depart = segment['origin']['name'], aero_arrivee = segment['destination']['name'],
                                          date_depart = segment['departure'],date_arrivee = segment['arrival'],duree = segment['durationInMinutes'],
                                          compagnie = segment['marketingCarrier']['name'], vol_operepar = segment['operatingCarrier']['name'] )
                            sgs.save()
            return HttpResponseRedirect('/resultats/')
    else:
        form = getFlight()

    context = {
            'form': form
    }

    return render(request, 'appone/appone.html', context)

def result(request):
    context = {
        'titre' : 'Résultats'
    }
    return render(request, 'appone/example.html', context)