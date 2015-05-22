{
    'name': 'Email Template Time',
    'version': '0.1',
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Email Template',
    'description': 
    """
    This module adds an extra time filter in email templates

    Example: ${ '%m/%d/%Y'|time() }
    """,
    'depends': [
        'email_template',
    ],
    'data': [
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
