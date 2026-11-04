# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class Partner(models.Model):
    _inherit = "res.partner"

    nombre_facturacion_fel_sv = fields.Char('Nombre facturación FEL SV')
    nombre_comercial_fel_sv = fields.Char('Nombre comercial FEL SV')
    nit_facturacion_fel_sv = fields.Char('NIT facturación FEL SV')
    tipo_documento_fel_sv = fields.Char('Tipo de documento FEL SV')
    departamento_fel_sv = fields.Char('Código departamente FEL SV')
    municipio_fel_sv = fields.Char('Código de municipio facturación FEL SV')
    distrito_fel_sv = fields.Char('Código de distrito facturación FEL SV')
    descripcion_actividad_fel_sv = fields.Char('Descripción actividad FEL SV')
