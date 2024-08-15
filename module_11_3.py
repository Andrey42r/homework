import inspect


def introspection_info(obj):
    _type = type(obj)
    _dir = dir(obj)
    _method = inspect.ismethod(obj)
    _module = inspect.getmodule(obj)
    return _type, _dir, _module, _method


number_info = introspection_info(42)
print(number_info)
