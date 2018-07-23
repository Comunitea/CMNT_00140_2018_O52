# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    'name': 'o52 Custom',
    'version': '11.0.1.0.0',
    'summary': 'Adds customizations.',
    'author': 'Comunitea',
    'license': 'AGPL-3',
    'category': 'Custom',
    'depends': ['account', 'sales_team'],
    'data': [
        'views/report_invoice.xml',
        'views/partner_view.xml',
    ],
    'installable': True,
}
