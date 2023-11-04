from datetime import date
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Correspondencia(models.Model):
    AZ = [
        ('1. Vice Docencia',( 
            ('1.1. Oficios', '1.1. Oficios'),
            ('1.2. Citaciones-Circulares-Memorandos', '1.2. Citaciones-Circulares-Memorandos'),
            ('1.2. Certificados', '1.2. Certificados'),
        )),
        (
            '2. SecretarGeneral',(
            ('2.1. Oficios', '2.1. Oficios'),
            ('2.2. Comisiones', '2.2. Comisiones'),
            ('2.3. PQRS', '2.3. PQRS'),
        )),
        (
            '3. Consejos',(
            ('3.1. Acuerdo CS', '3.1. Acuerdo CS'),
            ('3.2. Resoluciones CS', '3.2. Resoluciones CS'),
            ('3.3. Acuerdos CA', '3.3. Acuerdos CA'),
            ('3.4. Resoluciones CA', '3.4. Resoluciones CA'),
            ('3.5. Actas CA', '3.5. Actas CA'),
        )),
        (
            '4. Oficinas Asesoras de Jur y Control Disciplinario',(
            ('4.1. Oficios Jur', '4.1. Oficios Jur'),
            ('4.2. Conceptos Jur', '4.2. Conceptos Jur'),
            ('4.3. Oficios CD ', '4.3. Oficios CD '),
        )),
        (
            '5. Oficina Asesora de GestiHumana y Desarrollo de Personal',(
            ('5.1. GestiHumana', '5.1. GestiHumana'),
            ('5.2. Personal', '5.2. Personal'),
            ('5.3. Desarrollo Organizacional', '5.3. Desarrollo Organizacional'),
        )),
        (
            '6. Rectory Vicerector',(
            ('6.1. Rector', '6.1. Rector'),
            ('6.2. Vice-Administrativa', '6.2. Vice-Administrativa'),
            ('6.3. Vice-Bienestar', '6.3. Vice-Bienestar'),
            ('6.4. Vice-Calidad', '6.4. Vice-Calidad'),
            ('6.5. Vice-Extension', '6.5. Vice-Extension'),
            ('6.6. Vice-Internacionalizaci', '6.6. Vice-Internacionalizaci'),
            ('6.7. Vice-Investigaci', '6.7. Vice-Investigaci'),
        )),
        (
            '7. Oficina Asesoras de Planeaci y Control Interno',(
            ('7.1. Oficios P', '7.1. Oficios P'),
            ('7.2. Oficios CI', '7.2. Oficios CI'),
        )),
        (
            '8. AuditorControl Interno',(
            ('8.1. AuditorCI', '8.1. AuditorCI'),
        )),
        (
            '9. Facultades Centro',(
            ('9.1. Fac. C. Humanas', '9.1. Fac. C. Humanas'),
            ('9.2. Fac. C. Sociales', '9.2. Fac. C. Sociales'),
            ('9.3. Fac. Derecho', '9.3. Fac. Derecho'),
        )),
        (
            '10. Facultades Piedra',(
            ('10.1. Fac. C. Econ', '10.1. Fac. C. Econ'),
            ('10.2. Fac. C. Exactas y Naturales', '10.2. Fac. C. Exactas y Naturales'),
            ('10.3. Fac. Ingenier', '10.3. Fac. Ingenier'),
        )),
        (
            '11. Facultades Salud',(
            ('11.1. Fac. C. Farmac', '11.1. Fac. C. Farmac'),
            ('11.2. Fac. Enfermer', '11.2. Fac. Enfermer'),
            ('11.3. Fac. Medicina', '11.3. Fac. Medicina'),
            ('11.4. Fac. Odontolog', '11.4. Fac. Odontolog'),
        )),
        (
            '12. Institutos',(
            ('12.1. Inst. Inmunolog', '12.1. Inst. Inmunolog'),
            ('12.2. Inst. Hidr', '12.2. Inst. Hidr'),
            ('12.3 Inst. Estudios del Caribe', '12.3 Inst. Estudios del Caribe'),
            ('12.4. Inst. MatemAplicada', '12.4. Inst. MatemAplicada'),
            ('12.5. Inst. PolPublicas IPREG', '12.5. Inst. PolPublicas IPREG'),
        )),
        (
            '13. Rutas Acad y Salidas de Campo',(
            ('13.1. Rutas Acad', '13.1. Rutas Acad'),
            ('13.2. Salidas de Campo', '13.2. Salidas de Campo'),
        )),
        ('14. Otras Oficinas Internas', '14. Otras Oficinas Internas'),
        ('15. Correspondencia Externa', '15. Correspondencia Externa'),
        ('16. Solicitud de Docentes', '16. Solicitud de Docentes'),
        ('17. Correos electr', '17. Correos electr'),
        ('18. Informe de gesti', '18. Informe de gesti'),
        (
            '19. Centros',(
            ('19.1. C. de admisiones', '19.1. C. de admisiones'),
            ('19.2. C. de autoevaluaci', '19.2. C. de autoevaluaci'),
            ('19.3  C. de informaciy D.', '19.3  C. de informaciy D.'),
            ('19.4. C. de inform', '19.4. C. de inform'),
            ('19.5. C. de postgrado', '19.5. C. de postgrado'),
            ))

    ]
    radicado = models.CharField(max_length=10, unique=True, blank=False, default="RVD")
    recibido_de = models.CharField(max_length=50, unique=False, blank=False, default="")
    fecha_recibido = models.DateField(default=now)
    asunto = models.CharField(max_length=100, blank=False, null=False)
    numero_folios = models.PositiveIntegerField(null=False, default=1)
    firmado_por = models.CharField(max_length=50, unique=False, blank=False)
    cargo_firmante = models.CharField(max_length=50, unique=False, blank=False)
    enviado_a = models.CharField(max_length=20, unique=False, blank=False, default="none")
    fecha_envio = models.DateField(default=now)
    almacenado_AZ = models.CharField(max_length=100, choices=AZ)
    observaciones = models.TextField(blank=False,)
    entrada = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return ("Correspondencia{radicado=" + self.radicado + ", recibido_de=" + self.recibido_de + ", fecha_recibido=" + self.fecha_recibido.__str__() + ", asunto=" + self.asunto + ", numero_folios=" + str(self.numero_folios) + ", firmado_por=" + self.firmado_por + ", cargo_firmante=" + self.cargo_firmante + ", enviado_a=" + self.enviado_a + ", fecha_envio=" + self.fecha_envio.__str__() + ", almacenado_AZ=" + self.almacenado_AZ + ", observaciones=" + self.observaciones + ", entrada=" + str(self.entrada) + '}')













