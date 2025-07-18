{
    'name': 'Open Academy',
    'version': '16.0.0',
    'summary': 'It include all the course available in Open Academy',
    'category': 'Tools',
    'author': 'You',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_res_partner.xml',
        'views/session_view.xml',
        'views/course_view.xml',
    ],
    'installable': True,
    'application': True,
}
