import inspect


def introspection_info(obj):
    _type = type(obj)
    _dir = dir(obj)
    _method = inspect.ismethod(obj)
    _module = inspect.getmodule(obj)
    print(f'type: {_type}, attributes: {_dir}, methods: {_method}, module: {_module}')


number_info = introspection_info(42)
print(number_info)
