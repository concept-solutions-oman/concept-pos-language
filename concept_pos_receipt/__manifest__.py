{
    'name': 'POS Custom Receipt & Bilingual Invoice - Dual Language (English/Arabic)',
    'version': '17.0.1.0.0',
    'summary': 'Professional bilingual (English/Arabic) POS receipts with custom shop branding and paper-saving design (no logo).',
    'description': """
POS Custom Receipt & Bilingual Invoice (English/Arabic)
======================================================
This module customizes the default Odoo POS Receipt to make it clean, professional, and GCC tax-compliant.

Key Features:
-------------
* Bilingual Tax Table: Adds English and Arabic labels for Tax, Amount, Base, and Total.
* Shop Branding: Replaces the generic database company name with the active POS Shop Name.
* Paper Saver: Removes the company logo placeholder to prevent distorted/blurry printouts and save paper.
* Zero Configuration: Ready to use immediately upon installation.
    """,
    'author': 'Concept Solutions LLC',
    'website': 'https://www.csloman.com/',
    'category': 'Sales/Point Of Sale',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            '/concept_pos_receipt/views/pos_order_receipt_inherit.xml',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
