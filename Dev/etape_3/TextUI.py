"""
    Interface textuelle pour envoi de mails

    Author: Tristan Colombo <tristan@gnulinuxmag.com>
                            (@TristanColombo)

    Date: 25-09-2014

    Last modification: 25-09-2014

    Licence: GNU GPL v3 (voir fichier gpl_v3.txt joint)
"""

import npyscreen
import DB
from Contact import Contact

class ContactAutocompleter(npyscreen.Autocomplete):
    def auto_complete(self, input):
        db_args = DB.create_db()
        Contact.setDB(db_args)

        choices = Contact.complete(self.value)

        self.value = choices[self.get_choice(choices)]



class ContactAutocomplete(npyscreen.TitleText):
    _entry_type = ContactAutocompleter



class TextUI(npyscreen.NPSApp):
    weather_values = ["Soleil", "Pluie"]

    def main(self, *args, **kwargs):
        form = npyscreen.Form(name="Agenda")
        contact = form.add(ContactAutocomplete, name="Contact:")
        mail = form.add(npyscreen.TitleText, name="Mail:")
        weather = form.add(npyscreen.TitleSelectOne, max_height=len(TextUI.weather_values), 
                value=[0], name="Temps:", values=TextUI.weather_values, scroll_exit=True)

        form.edit()

        (base, cursor) = DB.create_db()
        person = Contact(contact.value, (base, cursor))
        person.mail = mail.value

        npyscreen.notify_wait("Valeur saisie : " + contact.value, title="Vérification")

        DB.close_db(base, cursor)
