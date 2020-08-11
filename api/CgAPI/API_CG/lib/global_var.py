def _init():
    if '_global_dict' not in globals().keys():
        global _global_dict
        _global_dict = {}
    if 'apis' not in _global_dict.keys():
        _global_dict['apis'] = []


def set_value(name, value):
    _global_dict[name] = value


def get_value(name):
    try:
        return _global_dict[name]
    except KeyError:
        return None


_init()
