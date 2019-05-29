def handle_error_by_throwing_exception():
    raise Exception("This is an exception.")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except ValueError:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        return (True, int(input_data))
    except ValueError:
        return (False, None)


def filelike_objects_are_closed_on_exception(f_obj):
    try:
        f_obj.open()
        f_obj.do_something()
        f_obj.close()
    except:
        f_obj.close()
        raise Exception("The program failed something!")
    
