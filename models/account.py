# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

import logging

class AccountMove(models.Model):
    _inherit = "account.move"

    firma_fel_sv = fields.Char('Firma FEL SV', copy=False)
    condicion_pago_fel_sv = fields.Selection([('1', 'Contado'), ('2', 'Crédito'), ('3', 'Otro')], 'Condicion de Pago FEL SV')
    forma_pago_fel_sv = fields.Selection([('01', 'Billetes y monedas'), ('02', 'Tarjeta Débito'), ('03', 'Tarjeta Crédito')], 'Forma de Pago FEL SV')
    motivo_fel_sv = fields.Char(string='Motivo FEL SV')
    tipo_anulacion_fel_sv = fields.Char(string='Tipo de Anulación FEL SV')
    factura_nueva_fel_sv_id = fields.Many2one('account.move', string="Factura Nueva FEL SV")
    factura_original_fel_sv_id = fields.Many2one('account.move', string="Factura Original FEL SV")
    responsable_fel_sv_id = fields.Many2one('res.partner', string="Responsable FEL SV")
    solicitante_fel_sv_id = fields.Many2one('res.partner', string="Solicitante FEL SV")
    documento_xml_fel_sv = fields.Binary('Documento XML FEL SV', copy=False)
    documento_xml_fel_sv_name = fields.Char('Nombre documento XML FEL SV', default='documento_xml_fel.xml', size=32)
    resultado_xml_fel_sv = fields.Binary('Resultado XML FEL SV', copy=False)
    resultado_xml_fel_sv_name = fields.Char('Nombre resultado XML FEL SV', default='resultado_xml_fel.xml', size=32)
    certificador_fel_sv = fields.Char('Certificador FEL SV', copy=False)

    def num_a_letras_sv(self, amount):
        return a_letras.num_a_letras(amount,completo=True)

    def error_certificador_sv(self, error):
        self.ensure_one()
        factura = self
        if factura.journal_id.error_en_historial_fel_sv:
            factura.message_post(body='<p>No se publicó la factura por error del certificador FEL:</p> <p><strong>'+error+'</strong></p>')
        else:
            raise UserError('No se publicó la factura por error del certificador FEL: '+error)

    def requiere_certificacion_sv(self, certificador=''):
        self.ensure_one()
        factura = self
        requiere = factura.is_invoice() and factura.journal_id.generar_fel_sv and factura.amount_total != 0 and factura.company_id.country_id.code == 'SV'
        if certificador:
            requiere = requiere and ( factura.company_id.certificador_fel_sv == certificador or not factura.company_id.certificador_fel_sv )
        return requiere

    def error_pre_validacion_sv(self):
        self.ensure_one()
        factura = self
        if factura.firma_fel_sv:
            factura.error_certificador_sv("La factura ya fue validada, por lo que no puede ser validada nuevamente")
            return True

        return False

class AccountJournal(models.Model):
    _inherit = "account.journal"

    generar_fel_sv = fields.Boolean('Generar FEL SV')
    tipo_documento_fel_sv = fields.Selection([('1', 'Factura'), ('3', 'Comprobante de crédito fiscal'), ('4', 'Nota de remisión'), ('5', 'Nota de crédito'), ('6', 'Nota de débito'), ('7', 'Comprobante de retención'), ('8', 'Comprobante de liquidación'), ('9', 'Documento contable de liquidación'), ('11', 'Facturas de exportación'), ('14', 'Factura de sujeto excluido'), ('15', 'Comprobante de donación')], 'Tipo de Documento FEL SV', copy=False)
    condicion_pago_fel_sv = fields.Selection([('1', 'Contado'), ('2', 'Crédito'), ('3', 'Otro')], 'Condicion de Pago por Defecto FEL SV')
    forma_pago_fel_sv = fields.Selection([('01', 'Billetes y monedas'), ('02', 'Tarjeta Débito'), ('03', 'Tarjeta Crédito')], 'Forma de Pago por Defecto FEL SV')
    codigo_establecimiento_sv = fields.Char('Código Establecimiento FEL SV')
    error_en_historial_fel_sv = fields.Boolean('Error FEL SV en historial', help='Los errores no se muestran en pantalla, solo se registran en el historial')
    enviar_lineas_en_cero_fel_sv = fields.Boolean('Enviar lineas en cero para FEL SV')

class AccountTax(models.Model):
    _inherit = 'account.tax'

    codigo_fel_sv = fields.Char('Código FEL SV')

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    codigo_unidad_medida_fel_sv = fields.Char('Código Unidad de Medida FEL SV')
