# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Talk(models.Model):
    TYPES = (
        ('talk', _(u'Palestra')),
        ('tutorial', _(u'Tutorial')),
    )

    LEVELS = (
        ('beginner', _(u'Iniciante')),
        ('intermediate', _(u'Intermediário')),
        ('advanced', _(u'Avançado')),
    )

    BOOL = (
        (0, _(u'Não')),
        (1, _(u'Sim')),
    )

    THEMES = (
        ('web', _(u'Desenvolvimento Web')),
        ('sci', _(u'Desenvolvimento Científico')),
        ('mobile', _(u'Mobile')),
        ('edu', _(u'Educação')),
        ('emp', _(u'Empreendedorismo')),
        ('adm', _(u'Administraçao de Sistemas')),
        ('hardware', _(u'Hardware, Robótica')),
        ('utils', _(u'Software Utilitários')),
        ('core', _(u'Core Python')),
        ('other', _(u'Outro')),
    )


    name = models.CharField(_(u'Nome'), max_length=150)
    email = models.EmailField(_(u'E-Mail'), max_length=254)
    phone = models.CharField(_(u'Telefone'), max_length=14)
    talk_once = models.BooleanField(_(u'Já paletrou'), choices=BOOL)
    macro_theme = models.CharField(
        _(u'MacroTema'), max_length=80, choices=THEMES,
    )
    title = models.CharField(_(u'Título'), max_length=80)
    type = models.CharField(
        _(u'Tipo'), max_length=20, choices=TYPES, blank=True,
    )
    level = models.CharField(_(u'Nível'), max_length=20, choices=LEVELS)
    summary = models.TextField(_(u'Resumo'))
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _(u'Palestra')
        verbose_name_plural = _(u'Palestras')

    def __unicode__(self):
        return u'{0} | {1}'.format(self.name, self.title)
