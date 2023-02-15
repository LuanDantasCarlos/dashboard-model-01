from django.db import models

class DadosNF(models.Model):
    prestador = models.CharField(max_length=50)
    convenio = models.CharField(max_length=50)
    protocolo = models.CharField(max_length=12)
    remessa = models.CharField(max_length=20)
    classificacao = models.CharField(max_length=50)
    rps = models.CharField(max_length=20)
    nfe = models.CharField(max_length=20)
    emissao = models.CharField(max_length=20)
    vencimento = models.CharField(max_length=20)
    def __str__(self):
        return self.prestador