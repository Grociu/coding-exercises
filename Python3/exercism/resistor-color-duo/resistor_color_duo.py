ordered_colors = [
    "black", "brown", "red", "orange", 
    "yellow", "green", "blue", "violet", 
    "grey", "white"
    ]
def code(color):
    return ordered_colors.index(color)

def value(colors):
    return 10*code(colors[0]) + code(colors[1])