from data import char_stub, is_testing
from src import char_gen


def name():
    testing = is_testing.is_testing()
    if testing == True:
        name = char_stub.name()
        return name
    else:
        name =char_gen.char_name()
        return name
