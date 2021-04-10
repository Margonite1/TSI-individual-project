from data import char_stub, loadchar, is_testing


def load_adapt():
    testing = is_testing.is_testing()
    if testing == True:
        loaded_data = char_stub.load()
        return loaded_data
    else:
        loaded_data = loadchar.load
        return loaded_data
