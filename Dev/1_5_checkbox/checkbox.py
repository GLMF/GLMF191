import npyscreen

class Window(npyscreen.NPSApp):
    def main(self):
        Form = npyscreen.Form(name="GNU/Linux Magazine")
        cbox_values = ["Option 1", "Option 2", "Option 3"]
        cbox = Form.add(npyscreen.TitleMultiSelect, max_height=len(cbox_values), value = [1,], name="Choix :",
                values = cbox_values, scroll_exit=True)

        Form.edit()

        npyscreen.notify_wait("Valeur saisie : " + str(cbox.get_selected_objects()), title="Vérification")

if __name__ == "__main__":
    App = Window()
    App.run()

