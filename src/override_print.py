import pprint
import yaml


def op(text_or_var, var=None, format=False, yml=False):  # pragma: no cover
    """
    short-hand override print() formatter

    @params
    text_or_var
    var=None
    format=False
    yml=False
    """
    try:
        if var and format:
            if yml:
                return print('\n[', text_or_var, ']\n', yaml.dump(var))
            return print('\n[', text_or_var, ']\n', pprint.pformat(var))
        if not var and format:
            if yml:
                return print('\n', yaml.dump(text_or_var))
            return print('\n', pprint.pformat(text_or_var))
        if var:
            return print('\n[', text_or_var, ']\n', var, '\n')
        return print('\n', text_or_var, '\n')
    except Exception as error:
        print('\n"op()" print override internal error...')
        print(error, '\n')
