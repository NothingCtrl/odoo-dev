# -*- coding: utf-8 -*-
{
    'name': "My Module",
    'summary': "Short subtitle phrase",
    'description': """Long description""",
    'author': "Duong Bao Thang",
    'license': "AGPL-3",
    'website': "http://camratus.com",
    'category': "Library",
    'version': "9.0.1.0.0",
    'depends': ['base', 'decimal_precision'],
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/library_book.xml'
    ],
    #'demo': ['demo.xml'],
}
