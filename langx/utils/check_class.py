class CheckClass:
    def __init__(self, *args, **kwargs):
        for arg in args:
            assert arg != None

            if isinstance(arg, list) and kwargs.get('check_empty_list') == True:
                assert len(arg) > 0
            elif isinstance(arg, str) and kwargs.get('check_empty_str') == True:
                assert len(arg) > 0

        for _, value in kwargs.items():
            assert value != None

            if isinstance(value, list) and kwargs.get('check_empty_list') == True:
                assert len(value) > 0
            elif isinstance(value, str) and kwargs.get('check_empty_str') == True:
                assert len(value) > 0