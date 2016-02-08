import npyscreen

class Window(npyscreen.NPSApp):
    def main(self):
        Form = npyscreen.Form(name="GNU/Linux Magazine")
        radio_values = ["Option 1", "Option 2", "Option 3"]
        radio = Form.add(npyscreen.TitleSelectOne, max_height=len(radio_values), value = [0], name="Choix:",
                values = radio_values, scroll_exit=True)

        Form.edit()

        npyscreen.notify_wait("Valeur saisie : " + radio.get_selected_objects()[0], title="Vérification")

if __name__ == "__main__":
    App = Window()
    App.run()

