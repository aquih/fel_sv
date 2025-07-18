# -*- encoding: utf-8 -*-

{
    'name': 'FEL El Salvador',
    'version': '2.0',
    'category': 'Custom',
    'description': """ Campos y funciones base para la facturación electrónica en El Salvador """,
    'author': 'aquíH',
    'website': 'http://aquih.com/',
    'depends': ['l10n_sv'],
    'data': [
        'views/account_views.xml',
        'views/res_company_views.xml',
        'views/partner_views.xml',
        'views/res_country_views.xml',
    ],
    'demo': [],
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
