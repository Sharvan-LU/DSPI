
from start_compiler.import_start import *



class numbers(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

def square(*args):
    local_vars = {}
    local_vars['list'] = args[0] if len(args) > 0 else start()
    local_vars['counter'] = start()
    StartError.lineNumber = 25
    check_events()
    _set('counter', local_vars, None)['counter'] = number(0)
    local_vars['squares'] = start()
    StartError.lineNumber = 27
    check_events()
    _set('squares', local_vars, None)['squares'] = numbers().clone()
    StartError.lineNumber = 29
    check_events()
    
    while _lt(_len(_get('squares', local_vars, None)['squares']), _len(_get('list', local_vars, None)['list'])): 
        StartError.lineNumber = 30
        check_events()
        _set(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('squares', local_vars, None)['squares'])[to_key(_get('counter', local_vars, None)['counter'])] = _mul(_get(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('list', local_vars, None)['list'])[to_key(_get('counter', local_vars, None)['counter'])], _get(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('list', local_vars, None)['list'])[to_key(_get('counter', local_vars, None)['counter'])])
        StartError.lineNumber = 31
        check_events()
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))

    return _get('squares', local_vars, None)['squares']
try:
    local_vars['list'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('list', local_vars, None)['list'] = numbers().clone()
    StartError.lineNumber = 7
    check_events()
    _set(to_key(number(0)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(0))] = number(1).clone()
    StartError.lineNumber = 8
    check_events()
    _set(to_key(number(1)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(1))] = number(2).clone()
    StartError.lineNumber = 9
    check_events()
    _set(to_key(number(2)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(2))] = number(3).clone()
    StartError.lineNumber = 10
    check_events()
    _set(to_key(number(3)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(3))] = number(4).clone()
    StartError.lineNumber = 11
    check_events()
    _set(to_key(number(4)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(4))] = number(5).clone()
    StartError.lineNumber = 12
    check_events()
    _set(to_key(number(5)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(5))] = number(6).clone()
    StartError.lineNumber = 13
    check_events()
    _set(to_key(number(6)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(6))] = number(7).clone()
    StartError.lineNumber = 14
    check_events()
    _set(to_key(number(7)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(7))] = number(8).clone()
    StartError.lineNumber = 15
    check_events()
    _set(to_key(number(8)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(8))] = number(9).clone()
    StartError.lineNumber = 16
    check_events()
    _set(to_key(number(9)), local_vars, _get('list', local_vars, None)['list'])[to_key(number(9))] = number(10).clone()
    local_vars['squares'] = start()
    StartError.lineNumber = 19
    check_events()
    _set('squares', local_vars, None)['squares'] = numbers().clone()
    StartError.lineNumber = 36
    check_events()
    _print(text("The squares of:"), _get('list', local_vars, None)['list'], text("are:"), square(_get('list', local_vars, None)['list']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
