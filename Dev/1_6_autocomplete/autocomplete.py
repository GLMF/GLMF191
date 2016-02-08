import npyscreen
from MyTitleAutocomplete import MyTitleAutocomplete

class Window(npyscreen.NPSApp):
    def main(self):
        Form = npyscreen.Form(name="GNU/Linux Magazine")
        text = Form.add(MyTitleAutocomplete, name = "Texte :")

        Form.edit()

        npyscreen.notify_wait("Valeur saisie : " + text.value, title="Vérification")

if __name__ == "__main__":
    App = Window()
    App.run()

