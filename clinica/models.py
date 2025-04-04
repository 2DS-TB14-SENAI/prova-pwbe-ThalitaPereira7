from django.db import models

escolhas = [
    ("PED", "Pediatria"),
    ("GIN", "Ginecologia "),
    ("OFT", "Oftalmologia")
]

escolhaStatus = [
    ("AGE", "agendado"),
    ("REAL", "realizado"),
    ("CANCEL", "cancelado")

]

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=30, choices=escolhas)
    crm = models.CharField(max_length=5)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    paciente = models.CharField(max_length=50)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=escolhaStatus)

# Create your models here.
