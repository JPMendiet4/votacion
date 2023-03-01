from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Municipality(models.Model):
    name = models.CharField('Nombre', max_length=100, null=False, blank=False)
    active = models.BooleanField('Activo', default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        
    def __str__(self):
        return self.name


class PollingStations(models.Model):
    name = models.CharField('Nombre', max_length=150, null=False, blank=False)
    address = models.CharField('Dirección', max_length=100, null=False, blank=False)
    municipality_id = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Puesto de votacion'
        verbose_name_plural = 'Puestos de votacion'
        
    def __str__(self):
        return self.name


class Captains(models.Model):
    name = models.CharField('Nombres', max_length=150, null=False, blank=False)
    surnames = models.CharField('Apellidos', max_length=250, null=False, blank=False)
    phone = models.CharField('Celular', max_length=10, null=False, blank=False)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Capitan"
        verbose_name_plural = "Capitanes"
        
    def __str__(self):
        return self.name


class Leader(models.Model):
    name = models.CharField('Nombres', max_length=150, null=False, blank=False)
    surnames = models.CharField('Apellidos', max_length=250, null=False, blank=False)
    phone = models.CharField('Celular', max_length=10, null=False, blank=False)
    captains_id = models.ForeignKey(Captains, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Lider"
        verbose_name_plural = "Lideres"

    def __str__(self):
        return self.name
    

class Commune(models.Model):
    name = models.CharField('Nombre', max_length=150, null=False, blank=False)
    municipality_id = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"

    def __str__(self):
        return self.name
    

class Neighborhoods(models.Model):
    name = models.CharField('Nombre', max_length=150, null=False, blank=False)
    commune_id = models.ForeignKey(Commune, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Barrio"
        verbose_name_plural = "Barrios"
    
    def __str__(self):
        return self.name


class VoterData(models.Model):
    name = models.CharField('Nombres',max_length=150, null=False, blank=False)
    surnames = models.CharField('Apellidos', max_length=250, null=False, blank=False)
    address = models.CharField('Dirección',max_length=100, null=False, blank=False)
    phone = models.CharField('Telefono', max_length=8, null=False, blank=False)
    Identification_card = models.CharField('Cédula', max_length=10, unique=True, null=False, blank=False)
    leader_id = models.ForeignKey(Leader, on_delete=models.PROTECT)
    neighborhoods_id = models.ForeignKey(Neighborhoods, on_delete=models.PROTECT)
    pollingStations_id = models.ForeignKey(PollingStations, on_delete=models.PROTECT)
    polling_station = models.CharField('Mesa',max_length=50, null=False, blank=False)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Datos del votante"
        verbose_name_plural = "Datos de los votantes"
    
    def __str__(self):
        return self.name
    

class LeaderRespNeighborhoods(models.Model):
    leader_id = models.ForeignKey(Leader, on_delete=models.PROTECT)
    captains_id = models.ForeignKey(Captains, on_delete=models.PROTECT)
    neighborhoods_id = models.ForeignKey(Neighborhoods, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Lider_Resp_barrio"
        verbose_name_plural = "Lideres_Resp_barrios"

    def __str__(self):
        return self.name
    

class CaptainCommune(models.Model):
    commune_id = models.ForeignKey(Commune, on_delete=models.PROTECT)
    captains_id = models.ForeignKey(Captains, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Capitan_Comuna'
        verbose_name_plural = 'Capitanes_Comunas'
        
    def __str__(self):
        return self.name