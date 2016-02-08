import npyscreen
from BeautifulTheme import BeautifulTheme

class Window(npyscreen.NPSApp):
    def main(self):
        npyscreen.setTheme(BeautifulTheme)
        Form = npyscreen.Form(name="GNU/Linux Magazine")
        text = Form.add(npyscreen.FixedText, value="Exemple de formulaire minimal")
        user_text = Form.add(npyscreen.TitleText, name="Saisir texte:")

        Form.edit()

        npyscreen.notify_wait("Valeur saisie : " + user_text.value, title="Vérification")

if __name__ == "__main__":
    App = Window()
    App.run()

