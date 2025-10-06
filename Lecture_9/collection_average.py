
from start_compiler.import_start import *



class numbers(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

def collection(*args):
    local_vars = {}
    local_vars['grades'] = args[0] if len(args) > 0 else start()
    local_vars['counter'] = start()
    local_vars['sum'] = start()
    StartError.lineNumber = 20
    check_events()
    _set('counter', local_vars, None)['counter'] = number(0)
    StartError.lineNumber = 21
    check_events()
    _set('sum', local_vars, None)['sum'] = number(0)
    StartError.lineNumber = 23
    check_events()
    
    while _lt(_get('counter', local_vars, None)['counter'], _len(_get('grades', local_vars, None)['grades'])): 
        StartError.lineNumber = 24
        check_events()
        _set('sum', local_vars, None)['sum'] = _add(_get('sum', local_vars, None)['sum'], _get(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('grades', local_vars, None)['grades'])[to_key(_get('counter', local_vars, None)['counter'])])
        StartError.lineNumber = 25
        check_events()
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))

    return _div(_get('sum', local_vars, None)['sum'], _len(_get('grades', local_vars, None)['grades']))
try:
    local_vars['grades'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('grades', local_vars, None)['grades'] = numbers().clone()
    StartError.lineNumber = 7
    check_events()
    _set(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))] = number(6)
    StartError.lineNumber = 8
    check_events()
    _set(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))] = number(3)
    StartError.lineNumber = 9
    check_events()
    _set(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))] = number(6)
    StartError.lineNumber = 10
    check_events()
    _set(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))] = number(8)
    StartError.lineNumber = 11
    check_events()
    _set(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))] = number(10)
    local_vars['average'] = start()
    StartError.lineNumber = 31
    check_events()
    _set('average', local_vars, None)['average'] = collection(_get('grades', local_vars, None)['grades'])
    StartError.lineNumber = 32
    check_events()
    _print(text("The grades"), _get('grades', local_vars, None)['grades'], text("have an average grade of"), _get('average', local_vars, None)['average'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
