# Defining the varialbles as globals for ease of modification.
GARDEN_WIDTH = 50
GARDEN_LENGTH = 50
PATH_LENGTH = 3
HEIGHT_PERMIT = 20
DOOR_HEIGHT = 7
DOOR_WIDTH = 3
WINDOW_HEIGHT = 3
WINDOW_WIDTH = 4
NUMBER_OF_WINDOWS_PER_WALL = 2
EXTRA_SPACE = 1
RIM_HEIGHT = 2


def house_fits_in_garden(house_width, house_length):
    return house_width + 2 * PATH_LENGTH <= GARDEN_WIDTH and \
        house_length + 2 * PATH_LENGTH <= GARDEN_LENGTH


def we_have_permit(height):
    return height <= HEIGHT_PERMIT


def walls_sized_correctly(house_height, house_width, house_length):
    minimal_dimensions = DOOR_WIDTH + \
        NUMBER_OF_WINDOWS_PER_WALL * WINDOW_WIDTH + \
        (NUMBER_OF_WINDOWS_PER_WALL + 2) * EXTRA_SPACE
    return house_height >= DOOR_HEIGHT + EXTRA_SPACE and \
        house_width >= minimal_dimensions and \
        house_length >= minimal_dimensions - DOOR_WIDTH


def we_have_house(house_height, house_width, house_length, roof_height):
    if not house_fits_in_garden(house_width, house_length):
        return "House too big."
    if not we_have_permit(house_height + roof_height):
        return "No permission."
    if not walls_sized_correctly(house_height, house_width, house_length):
        return "House too small."
    grey_paint = (2 * house_width + 2 * house_length - DOOR_WIDTH) * RIM_HEIGHT
    yellow_paint = \
        2 * house_width * house_height + \
        2 * house_length * house_height + \
        roof_height * house_width - \
        DOOR_HEIGHT * DOOR_WIDTH - \
        WINDOW_HEIGHT * WINDOW_WIDTH * NUMBER_OF_WINDOWS_PER_WALL * 4 - \
        grey_paint
    return "Yellow: {}, Gray: {}".format(yellow_paint, grey_paint)
