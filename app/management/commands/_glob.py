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
        'page_size': '100',
        'json': '1',
        'tagtype_0': 'categories',
        'tag_contains_0': 'contains',
    }

    # Parameters for inserting data into the database
    categories = (
        'Sodas', 'Jus de fruits', 'Cafés', 'Cacaos et chocolats en poudre', 'Chocolats au lait', 'Chocolats noirs',
        'Produits à tartiner sucrés', 'Laits UHT', 'Yaourts aux fruits', 'Yaourts natures', 'Fromages à tartiner',
        'Camemberts', 'Fromages double crème', 'Fromages blancs', 'Emmentals râpés', 'Munster', 'Fromages apéritif',
        'Biscuits au chocolat', 'Biscuits et gâteaux', 'Popcorn', 'Salades composées', 'Conserves', 'Salades',
        'Légumes frais', 'Sauces', 'Produits de la mer', 'Cornichons', 'Epices', 'Bonbons', 'Viandes surgelées',
        'Produits à tartiner salés', 'vin', 'Saucissons', 'Jambons', 'Pizzas', 'Chips', 'Apéritif',

    )
