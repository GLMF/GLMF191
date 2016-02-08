import npyscreen

class MyTitleAutocompleter(npyscreen.Autocomplete):
    possibilities = ['Abba', 'Benabar', 'Cranberries']

    def auto_complete(self, input):
        choices = []

        for word in MyTitleAutocompleter.possibilities:
            if word.startswith(self.value):
                choices.append(word)

        self.value = choices[self.get_choice(choices)]

class MyTitleAutocomplete(npyscreen.TitleText):
    _entry_type = MyTitleAutocompleter
