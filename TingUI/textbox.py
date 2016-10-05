from .widget import Widget

class Label(Widget):
    """ Label type widget """

    def __init__(self):
        self.type = "LABEL"

    
    
class TextEdit(Widget):
    """ TextEdit type widget """

    def __init__(self):
        self.type = "TEXTBOX"
