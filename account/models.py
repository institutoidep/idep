from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Area_Estudio(models.Model):
    area              = models.CharField(max_length=30)
    duracion          = models.CharField(max_length=20)
    costo_inscripcion = models.DecimalField(max_digits=6, decimal_places=2)
    costo_semanal     = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __unicode__(self):
        name = "%s - %s %s %s"%(self.area,self.duracion,self.costo_inscripcion,self.costo_semanal)
        return name

class Horario(models.Model):
    horario            = models.CharField(max_length=30)
    dias               = models.CharField(max_length=30)

    def __unicode__(self):
        name = "%s - %s"%(self.horario, self.dias)
        return name

class Alumno(models.Model):
    GRADO_ESCOLAR = (
                        ( 0, 'Primaria'),
                        ( 1, 'Secundaria'),
                        ( 2, 'Preparaoria'),
                        ( 3, 'Profecional'),
    )
    GENERO = ( (0,'Hombre'),
               (1,'Mujer'),
             )
    maricula           = models.PositiveSmallIntegerField(unique=True)
    fmatricula         = models.DateTimeField(auto_now_add=True)
    genero             = models.SmallIntegerField(choices = GENERO,) 
    apaterno           = models.CharField(max_length=60)
    amaterno           = models.CharField(max_length=60,blank=True,null=True)
    nombre             = models.CharField(max_length=60)
    fnacimiento        = models.DateField()
    grado_escolar      = models.SmallIntegerField(choices = GRADO_ESCOLAR,) 
    lugar_trabajo      = models.CharField(max_length=80,blank=True,null=True)
    puesto_trabajo     = models.CharField(max_length=40,blank=True,null=True)
    domicilio          = models.TextField()
    nombre_tutor       = models.CharField(max_length=80,blank=True,null=True)
    tel_celular        = models.CharField(max_length=20, null=True, blank=True)
    tel_casa           = models.CharField(max_length=20, null=True, blank=True)
    tel_trabajo        = models.CharField(max_length=20, null=True, blank=True)
    tel_tutor          = models.CharField(max_length=20, null=True, blank=True)
    area_estudios      = models.ForeignKey(Area_Estudio)
    horario            = models.ForeignKey(Horario)
    email_estudiante   = models.EmailField(blank=True,null=True)
    email_tutor1       = models.EmailField(blank=True,null=True)
    email_tutor2       = models.EmailField(blank=True,null=True)
    curp               = models.BooleanField()
    acta_nacimiento    = models.BooleanField()
    credencial_elector = models.BooleanField()
    boleta_certificado = models.BooleanField()
    comprobante_dom    = models.BooleanField()
    foto               = models.ImageField(blank=True,null=True)
    reg_curp           = models.CharField(max_length=18,unique=True) 
                   
    def __unicode__(self):
        name = "%s - %s - %s - %s - %s - %s"%(self.maricula,self.curp,self.apaterno+" "+self.amaterno+" "+self.nombre,self.tel_celular,self.area_estudios,self.horario)
        return name
        
    
    