#! /usr/bin/env python3
# coding: utf8
"""
Update database PostgreSQL with API OpenfoodFacts
"""

import os
import pickle
import logging as log
from getpass import getpass
import argparse

from package.database import Database
from package.glob import Glob
from package.apirest import ApiRest


def parse_arguments():
    """
    Arguments added to command line to get
    additional information
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true', help="""Display informations of use-OpenFoodFacts""")
    parser.add_argument("-d", "--debug", action='store_true', help="""Switch to debug mode!""")
    return parser.parse_args()


def header(msg=""):
    """
    Header of program
        :param msg: Show the menu name or detected errors
        :return: Show the program header
    """
    os.system("clear")
    print("\n   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "   ~~~           Mise à jour Base de données           ~~~\n"
          "   ~~~         pour l'application Pure Beurre          ~~~\n"
          "   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(msg)


def conf_database(msg=""):
    """
    Adding the parameters in the 'database_conf' file that
    allow you to connect to the database
        :param msg: Show the menu name or detected errors
        :return: dict of the parameters of the database
    """
    header(msg)
    print("Information de connection pour la base de données")
    db_name = input("  - Nom de la base de données : ")
    user = input("  - Compte propriétaire : ")
    password = getpass("  - Password du compte : ")
    port = str(input("  - port (5432 par défaut) : "))
    if port == "":
        port = "5432"
    host = input("  - Adresse base de données ('localhost' par défaut) : ")
    if host == "":
        host = "localhost"
    conf_db = {'dbname': db_name, 'user': user, 'password': password, 'port': port, 'host': host}
    pickle.dump(conf_db, open(Glob.confDbFile, 'wb'))

    print("\n## Ajout paramètres de la base de données terminée ##\n")


def data_create():
    """
    Adding data from OpenFoodFacts to the database using
    the OpenFoodFacts API and using SQL requests
        :return: Adding values in the different tables of the database
    """
    api = ApiRest(log)
    col = []
    data_off_name = []
    table_prod = "app_product"
    table_cat = "app_category"
    for colDb, name in Glob.converDb[table_prod]:
        if name is not None:
            data_off_name.append(name)
        col.append(colDb)
    col_product = ",".join(col)
    log.info(f"Colonnes : {col_product}\n"
             f"Valeurs  : {data_off_name}")

    nb_line_before = db.select("count(*)", table_prod)[0][0]

    for category in Glob.converDb[table_cat]:
        cond_cat = " name=%s"
        cat_id = db.select("id", table_cat, cond_cat, True, [category])
        if len(cat_id) == 0:
            id_category = db.insert(table_cat, [category], "name", True)
        else:
            id_category = cat_id[0][0]
            log.info(f"*** Categorie '{category}' existe avec l'ID : {id_category} ***")
        results = api.get_request(category)
        for nbProduct in range(len(results) - 1):
            result = results[nbProduct]
            val_product = api.convert_data(result, data_off_name)

            # Product information with verbose option
            log.info(f"*** PRODUIT N°{nbProduct + 1} CATEGORIE : '{category}' ***\n"
                     f"Product_name : {result['product_name']}\n")
            log.debug(f"Valeurs du produit : {val_product}\n")

            condition = " name=%s"
            list_id = db.select("id", table_prod, condition, True, [result['product_name']])
            if len(list_id) == 0:
                id_product = db.insert(table_prod, val_product, col_product, True)
            else:
                id_product = list_id[0][0]
                log.info(f"*** Produit '{result['product_name']}' existe avec l'ID : {id_product} ***")
            db.insert("app_category_products(product_id, category_id)", [id_product, id_category])

    nb_line_after = db.select("count(*)", table_prod)[0][0]
    print(f"  - {nb_line_after - nb_line_before} produits ajoutés\n"
          "\n## Insertion des données dans la base terminée ##\n")


def main():
    """
    Principal menu of the program
        :return: returns the number that the user has chosen
    """
    header()
    print("Listes des options:\n"
          "  1 - Paramètres base de données\n"
          "  2 - Effacez toutes les données\n"
          "  3 - Insérez les données dans la base de données\n")
    entry = input("Entrez le numéro de votre choix (ou <Enter> pour quitter) : ")
    return entry


if __name__ == '__main__':
    """
    Initialization of program
    """
    args = parse_arguments()
    if args.debug:
        log.basicConfig(level=log.DEBUG)
    elif args.verbose:
        log.basicConfig(level=log.INFO)
    while 1:
        try:
            confDb = pickle.load(open(Glob.confDbFile, 'rb'))
            db = Database(log, confDb)
            if not db.error:
                choice = main()
                if choice == "":
                    break
                elif choice == "1":
                    conf_database()
                elif choice == "2":
                    header("## Suppression des données dans la base de données ##\n")
                    db.sql_script('script_erase_DB.sql')
                elif choice == "3":
                    header("# Insertion des données dans la base de données en cours... #\n")
                    data_create()
                else:
                    print("\n*** Erreur de touche ***\n")
            else:
                conf_database("*** Erreur information de connection Base de données ***\n")
            input("Appuyez sur une touche pour revenir au menu principal... ")
            db.close()
        except FileNotFoundError:
            conf_database()
            continue
        except KeyboardInterrupt:
            log.warning("Fermeture du programme avec <Ctrl+C>")
            break
        else:
            db.close()
