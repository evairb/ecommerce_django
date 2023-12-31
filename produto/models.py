from django.db import models
from utils.images import resize_image
from django.utils.text import slugify

# Create your models here
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0,verbose_name='Preço Promocional')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices = (
            ('V', 'Variavel'),
            ('S','Simples',),
        
        )
    )


    def get_preco_formatado(self):
        return f' R$ {self.preco_marketing:.2f}'.replace('.',',')
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return f' R$ {self.preco_marketing_promocional:.2f}'.replace('.',',')
    get_preco_promocional_formatado.short_description = 'Preço Promo'


    

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800
        
        if self.imagem:
            resize_image(self.imagem, max_image_size)

    def __str__(self) :
        return self.nome
    


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome
    

    class Meta:
        verbose_name = 'Variacao'
        verbose_name_plural = 'Variações'