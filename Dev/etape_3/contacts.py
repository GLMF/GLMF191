"""
    Annuaire avec envoi de mails pour GNU/Linux Magazine

    Author: Tristan Colombo <tristan@gnulinuxmag.com>
                            (@TristanColombo)

    Date: 20-08-2014

    Last modification: 20-08-2014

    Licence: GNU GPL v3 (voir fichier gpl_v3.txt joint)
"""

import argparse
import DB
from Contact import Contact
from TextUI import TextUI


def cli_mode(args):
    person = Contact(args.name, (args.base, args.cursor))
    forename = person.forename
    name = person.name
    mail = person.mail

    if mail == None:
        print('Nouveau contact')
        mail = input('Veuillez saisir le mail: ')
        person.mail = mail

    person.generateDoc(args.sun)
    person.sendMail()

    print('Le mail a été envoyé à', forename, name)

def text_mode(args):
    app = TextUI()
    app.run()

def gui_mode(args):
    print('Interface graphique')


if __name__ == '__main__':
    """
        Création du parser d'arguments pour la ligne
        de commandes
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='Commandes')

    # Mode CLI
    cli_parser = subparsers.add_parser('cli', help='Mode ligne de commandes')
    cli_parser.add_argument('name', help='Prénom et nom du contact')
    cli_parser.add_argument('-s', '--soleil', action='store_true',
                            default=False, dest='sun',
                            help='Temps à insérer dans le fichier pdf')
    cli_parser.set_defaults(func=cli_mode)

    # Mode texte
    text_parser = subparsers.add_parser('text',
                                        help="Mode interface textuelle")
    text_parser.set_defaults(func=text_mode)

    # Mode graphique
    gui_parser = subparsers.add_parser('gui', help="Mode interface graphique")
    gui_parser.set_defaults(func=gui_mode)

    args = parser.parse_args()
    args.base, args.cursor = DB.create_db()
    args.func(args)
    DB.close_db(args.base, args.cursor)

    """try:
        args = parser.parse_args()
        args.base, args.cursor = create_db()
        args.func(args)
        close_db(args)
    except:
        parser.print_help()
        exit(1)"""
