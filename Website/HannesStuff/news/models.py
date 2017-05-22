from django.db import models

class Meldung(models.Model):
	titel = models.CharField(max_length=100)
	zeitstempel = models.DateTimeField()
	text = TextField('Meldungstext')

class Kommentar(models.Model):
	meldung = models.ForeignKey(Meldung)
	autor = models.CharField(max_length=70)
	text = TextField('Kommentartext')