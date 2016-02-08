import npyscreen
import curses

class BeautifulTheme(npyscreen.ThemeManager):
    _colors_to_define = (
        ('RED_BLUE', curses.COLOR_RED, curses.COLOR_BLUE),
        ('BLUE_YELLOW', curses.COLOR_BLUE, curses.COLOR_YELLOW),
    )

    default_colors = {
        'DEFAULT'     : 'RED_BLUE',
        'FORMDEFAULT' : 'RED_BLUE',
        'NO_EDIT'     : 'BLUE_YELLOW',
        'STANDOUT'    : 'BLUE_YELLOW',
        'CURSOR'      : 'RED_BLUE',
        'LABEL'       : 'RED_BLUE',
        'LABELBOLD'   : 'RED_BLUE',
        'CONTROL'     : 'BLUE_YELLOW',
        'IMPORTANT'   : 'RED_BLUE',
        'SAFE'        : 'BLUE_YELLOW',
        'WARNING'     : 'BLUE_YELLOW',
        'DANGER'      : 'RED_BLUE',
        'CRITICAL'    : 'RED_BLUE',
        'GOOD'        : 'RED_BLUE',
        'GOODHL'      : 'BLUE_YELLOW',
        'VERYGOOD'    : 'RED_BLUE',
        'CAUTION'     : 'BLUE_YELLOW',
        'CAUTIONHL'   : 'BLUE_YELLOW',
    }

    def __init__(self, *args, **kwargs):
        curses.use_default_colors()
        super(BeautifulTheme, self).__init__(*args, **kwargs)
