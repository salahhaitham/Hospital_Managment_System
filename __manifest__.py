{
    'name': 'Hospital Management',
    'version': '19.0',
    'category': 'Healthcare',
    'summary': 'Hospital Management System',
    'description': 'Complete Hospital Management Module for Odoo 15',
    'author': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'depends': ['base','mail','product','base_setup'],

    'data': [

        'security/ir.model.access.csv',
'data/hospital_tag.xml'  ,
'data/patient_sequence.xml'  ,
'wizards/cancel_appointment.xml',
        'views/hospital_menu.xml',
        'views/hospital_appointment.xml',
        'views/hospital_patient_views.xml',
   'views/res_config_settings_view.xml',


        'views/hospital_tag.xml',

    ],

    'images': ['static/description/icon.svg'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
