from django.db import models

class parametre_recherche(models.Model):
           origin = models.CharField(max_length=30)
           destination= models.CharField(max_length=30)
           departureDate= models.CharField(max_length=30)
           returnDate= models.CharField(max_length=30)
           cabinClass=models.CharField(max_length=30)
           currency=models.CharField(max_length=30)
           adults= models.CharField(max_length=30)
           childAge1= models.CharField(max_length=30)
           childAge2= models.CharField(max_length=30)
           childAge3= models.CharField(max_length=30)
           childAge4= models.CharField(max_length=30)
           childAge5= models.CharField(max_length=30)
           childAge6= models.CharField(max_length=30)
           childAge7= models.CharField(max_length=30)
           childAge8= models.CharField(max_length=30)
           dt_recherche= models.DateTimeField(auto_now=True)

           def __str__(self):
                   return '{}-{}|{}/{}'.format(self.origin, self.destination, self.departureDate, self.returnDate)


class buckets(models.Model):
           type = models.CharField(max_length=30) # rapide, moins chers et meilleurs
           name = models.CharField(max_length=30)
           parametre_recherche = models.ForeignKey(parametre_recherche, on_delete=models.CASCADE)

           def __str__(self):
                   return '{}-{}'.format(self.type, self.parametre_recherche.pk)

class items(models.Model):
           prix = models.CharField(max_length=30)
          # type = models.CharField(max_length=30) # items.tags
           lien = models.CharField(max_length=30)
           buckets = models.ForeignKey(buckets, on_delete=models.CASCADE) 

           def __str__(self):
                   return '{}-{}'.format(self.buckets.name, self.prix)

class legs(models.Model):
           type = models.CharField(max_length=30) # aller, retour
           aero_depart = models.CharField(max_length=30)
           aero_arrivee = models.CharField(max_length=30)
           #compagnie = models.CharField(max_length=30)
           duree = models.CharField(max_length=30)
           nbre_escale = models.CharField(max_length=30)
           date_depart = models.CharField(max_length=30)
           date_arrivee = models.CharField(max_length=30)
           items = models.ForeignKey(items, on_delete=models.CASCADE)

           def __str__(self):
                   return '{}, {}'.format(self.type, self.items.pk)

class segments(models.Model):
           aero_depart = models.CharField(max_length=30)
           aero_arrivee = models.CharField(max_length=30)
           duree = models.CharField(max_length=30)
           date_depart = models.CharField(max_length=30)
           date_arrivee = models.CharField(max_length=30)
           compagnie = models.CharField(max_length=30)
           vol_operepar = models.CharField(max_length=30)
           legs = models.ForeignKey(legs, on_delete=models.CASCADE)

           def __str__(self):
                   return '{}-{}|{}/{}|{}'.format(self.aero_depart, self.aero_arrivee, self.date_depart, self.date_arrivee, self.compagnie)
           

  