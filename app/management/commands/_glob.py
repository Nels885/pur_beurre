"""
Global variables module
"""


class Glob:
    """
    List of variables used by different Python script
    """

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
    categories = (
        'soda', 'jus', 'café', 'chocolat', 'lait', 'yaourt', 'fromage', 'Biscuit', 'gateau', 'dessert',
        'épicerie', 'jambon', 'poisson', 'apéritif', 'Surgelé', 'conserve', 'légume',
        'petit-déjeuner', 'sauce', 'Produit de la mer', 'condiment', 'viande', 'bonbon', 'vin',
        'charcuterie',
    )
