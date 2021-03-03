# -*- coding: utf-8 -*-
{
    'name': "My Shop",  # Module title
    'summary': "Manage videogames easily",  # Module subtitle phrase
    'description': """Long description""",  # You can also rst format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/shop_videogame.xml',
        'views/shop_videogame_genre.xml',
        'views/shop_loan.xml',
        'views/shop_client.xml',
        'views/shop_videogame_creator.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
