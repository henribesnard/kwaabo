from django import forms

class getFlight(forms.Form):
           origin = forms.CharField(label='Départ', max_length=3)
           destination= forms.CharField(label='Arrivée', max_length=3)
           departureDate= forms.CharField(label='Date départ', max_length=100)
           returnDate= forms.CharField(label='Date arrivée', max_length=100)
           cabinClass=forms.CharField(label='Classe', max_length=100)
           currency=forms.CharField(label='Devise', max_length=3)
           adults= forms.CharField(label='Nombre adulte', max_length=100)
           childAge1= forms.CharField(label='Age enfant1', max_length=100, required=False)
           childAge2= forms.CharField(label='Age enfant2', max_length=100, required=False) 
           childAge3= forms.CharField(label='Age enfant3', max_length=100, required=False)
           childAge4= forms.CharField(label='Age enfant4', max_length=100, required=False)
           childAge5= forms.CharField(label='Age enfant5', max_length=100, required=False)
           childAge6= forms.CharField(label='Age enfant6', max_length=100, required=False)
           childAge7= forms.CharField(label='Age enfant7', max_length=100, required=False)
           childAge8= forms.CharField(label='Age enfant8', max_length=100, required=False)
           
