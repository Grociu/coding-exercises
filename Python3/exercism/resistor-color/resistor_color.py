ordered_colors = [
    "black", "brown", "red", "orange", 
    "yellow", "green", "blue", "violet", 
    "grey", "white"
    ]

def color_code(color):
    return ordered_colors.index(color.lower())

def colors():
    return ordered_colors
