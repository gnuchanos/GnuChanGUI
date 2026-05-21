"""Tutorial index - imports available tutorial scripts for easy discovery.
This file exposes a `tutorials` dict mapping short names to example modules/classes.
"""

from . import tutorial_button
from . import tutorial_checkbox
from . import tutorial_radio
from . import tutorial_selection
from . import tutorial_slider_progress
from . import tutorial_input
from . import tutorial_multiline
from . import tutorial_listbox
from . import tutorial_table
from . import tutorial_tree
from . import tutorial_canvas
from . import tutorial_frame
from . import tutorial_menubar
from . import tutorial_image
from . import tutorial_tabgroup
from . import tutorial_graph
from . import tutorial_output
from . import tutorial_pane
from . import tutorial_optionmenu
from . import tutorial_statusbar
from . import tutorial_buttonmenu
from . import tutorial_sizegrip
from . import tutorial_push_hvsep
from . import tutorial_titlebar
from . import tutorial_spin
from . import tutorial_imagegif
from . import tutorial_colors
from . import tutorial_column_pin
from . import tutorial_filedialogs
from . import tutorial_widget_helpers
from . import tutorial_message
from . import tutorial_timer
from . import tutorial_gamecanvas
from . import tutorial_font

# Map a short name to the module and main class to run
tutorials = {
    'button': (tutorial_button, 'ButtonTutorial'),
    'checkbox': (tutorial_checkbox, None),
    'radio': (tutorial_radio, None),
    'selection': (tutorial_selection, None),
    'slider_progress': (tutorial_slider_progress, None),
    'input': (tutorial_input, 'InputTutorial'),
    'multiline': (tutorial_multiline, 'MultilineTutorial'),
    'listbox': (tutorial_listbox, 'ListboxTutorial'),
    'table': (tutorial_table, 'TableTutorial'),
    'tree': (tutorial_tree, 'TreeTutorial'),
    'canvas': (tutorial_canvas, 'CanvasTutorial'),
    'frame': (tutorial_frame, 'FrameTutorial'),
    'menubar': (tutorial_menubar, 'MenuTutorial'),
    'image': (tutorial_image, 'ImageTutorial'),
    'tabs': (tutorial_tabgroup, 'TabTutorial'),
    'graph': (tutorial_graph, 'GraphTutorial'),
    'output': (tutorial_output, 'OutputTutorial'),
    'pane': (tutorial_pane, 'PaneTutorial'),
    'optionmenu': (tutorial_optionmenu, 'OptionMenuTutorial'),
    'statusbar': (tutorial_statusbar, 'StatusBarTutorial'),
    'buttonmenu': (tutorial_buttonmenu, 'ButtonMenuTutorial'),
    'sizegrip': (tutorial_sizegrip, 'SizegripTutorial'),
    'push_hvsep': (tutorial_push_hvsep, 'PushSepTutorial'),
    'titlebar': (tutorial_titlebar, 'TitlebarTutorial'),
    'spin': (tutorial_spin, 'SpinTutorial'),
    'imagegif': (tutorial_imagegif, 'ImageGifTutorial'),
    'colors': (tutorial_colors, 'ColorsTutorial'),
    'column_pin': (tutorial_column_pin, 'ColumnPinTutorial'),
    'filedialogs': (tutorial_filedialogs, 'FileDialogsTutorial'),
    'widget_helpers': (tutorial_widget_helpers, 'WidgetHelpersTutorial'),
    'message': (tutorial_message, 'MessageTutorial'),
    'timer': (tutorial_timer, 'TimerTutorial'),
    'gamecanvas': (tutorial_gamecanvas, 'GameCanvasTutorial'),
    'font': (tutorial_font, 'FontTutorial'),
}

__all__ = list(tutorials.keys())
