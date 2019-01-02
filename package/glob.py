"""
Global variables module
"""


class Glob:
    """
    List of variables used by different Python script
    """

    # Path for the configuration file
    confDbFile = 'database_conf'

    # Constants for SQL requests
    tabAssocCat = "app_product AS p, app_category_products AS a, app_category AS c"
    condAssocCat = "p.id=a.product_id AND c.id=a.category_id"
    tabBackProd = "app_backup AS b, app_product AS p"
    condBackProd = "b.product_id=p.id"

    # Information for the OpenFoodFacts API
    infoApi = {
        'https': 'https://fr.openfoodfacts.org/cgi/search.pl?search_simple=1&action=process',
        'action': 'process',
        'sort_by': 'unique_scans_n',
        'page_size': '20',
        'json': '1',
        'tagtype_0': 'categories',
        'tag_contains_0': 'contains',
    }

    # Parameters for inserting data into the database
    converDb = {
        'app_product': [
            ('name', 'product_name'),
            ('nutrition_grades', 'nutrition_grades'),
            ('url', 'url'),
            ('picture', 'image_front_url'),
            ('nutrition_picture', 'image_nutrition_url')
        ],
        'app_category': (
            'soda', 'jus', 'café', 'chocolat', 'lait', 'yaourt', 'fromage', 'Biscuit', 'gateau', 'dessert',
            'épicerie', 'jambon', 'poisson', 'apéritif', 'Surgelé', 'conserve', 'légume',
            'petit-déjeuner', 'sauce', 'Produit de la mer', 'condiment', 'viande', 'bonbon', 'vin',
            'charcuterie',
        ),
        'app_category_products': (
            'category_id',
            'product_id'
        ),
        'app_backup': (
            'id',
            'product'
        )
    }
