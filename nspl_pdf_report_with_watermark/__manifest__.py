# -*- coding: utf-8 -*-
{
    'name': 'Reports With Watermark',
    'version': '19.0.1',
    'category': 'Extra Tools',
    'summary': 'Add watermark to PDF reports',
    'description': """
Reports With Watermark
======================

This module allows you to include a watermark in PDF reports.

Key Features:
-------------
- Add text or image as watermark on PDF reports
- Configure watermark from company settings
- Useful for drafts, internal documents, or duplicates
- Automatically applies watermark on print
    """,
    'author': 'Namah Softech Private Limited',
    'company': 'Namah Softech Private Limited',
    'maintainer': 'Namah Softech Private Limited',
    'contributors': [
        'Vipul Sah',
    ],
    'website': 'https://www.namahsoftech.com',
    'support': 'support@namahsoftech.com',
    'license': 'LGPL-3',
    'price': 9.99,
    'currency': 'USD',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'views/res_company_views.xml',
        'report/pdf_with_watermark_template.xml',
        'views/base_document_layout.xml',
    ],
    'images': [
        'static/description/img/banner.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
