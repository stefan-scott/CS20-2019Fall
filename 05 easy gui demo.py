import easygui_qt as easy

first_name = easy.get_string("Enter a name", "Question One")
if first_name == None:
    easy.show_message("That's a boring name", " ")
else:
    easy.show_message(first_name, " ")
