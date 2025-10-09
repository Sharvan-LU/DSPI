
from start_compiler.import_start import *



class list(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

    def append(self, *args):
        local_vars = {}
        local_vars['l'] = args[0] if len(args) > 0 else start()
        local_vars['n'] = args[1] if len(args) > 1 else start()
        StartError.lineNumber = 8
        check_events()
        _set(to_key(_len(_get('l', local_vars, None)['l'])), local_vars, _get('l', local_vars, None)['l'])[to_key(_len(_get('l', local_vars, None)['l']))] = _get('n', local_vars, None)['n']
        return

    def remove(self, *args):
        local_vars = {}
        local_vars['l'] = args[0] if len(args) > 0 else start()
        local_vars['n'] = args[1] if len(args) > 1 else start()
        local_vars['l2'] = start()
        StartError.lineNumber = 18
        check_events()
        _set('l2', local_vars, None)['l2'] = list()
        local_vars['counter'] = start()
        StartError.lineNumber = 21
        check_events()
        _set('counter', local_vars, None)['counter'] = number(0)
        StartError.lineNumber = 23
        check_events()
        
        while _lt(_get('counter', local_vars, None)['counter'], _len(_get('l', local_vars, None)['l'])): 
            StartError.lineNumber = 24
            check_events()
            
            if _not(_eql_val(_get(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('l', local_vars, None)['l'])[to_key(_get('counter', local_vars, None)['counter'])], _get('n', local_vars, None)['n'])): 
                StartError.lineNumber = 25
                check_events()
                list.append(None, _get('l2', local_vars, None)['l2'], _get(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('l', local_vars, None)['l'])[to_key(_get('counter', local_vars, None)['counter'])])

            StartError.lineNumber = 27
            check_events()
            _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))

        StartError.lineNumber = 29
        check_events()
        _get('l2', local_vars, None)['l2'].copy(_set('l', local_vars, None)['l'])
        return
try:
    local_vars['grades'] = start()
    StartError.lineNumber = 35
    check_events()
    _set('grades', local_vars, None)['grades'] = list()
    StartError.lineNumber = 37
    check_events()
    list.append(None, _get('grades', local_vars, None)['grades'], number(4))
    StartError.lineNumber = 38
    check_events()
    list.append(None, _get('grades', local_vars, None)['grades'], number(5))
    StartError.lineNumber = 39
    check_events()
    list.append(None, _get('grades', local_vars, None)['grades'], number(2))
    StartError.lineNumber = 40
    check_events()
    list.append(None, _get('grades', local_vars, None)['grades'], number(10))
    StartError.lineNumber = 41
    check_events()
    list.append(None, _get('grades', local_vars, None)['grades'], number(9))
    StartError.lineNumber = 42
    check_events()
    list.append(None, _get('grades', local_vars, None)['grades'], number(5))
    StartError.lineNumber = 43
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
    StartError.lineNumber = 45
    check_events()
    list.append(None, _get('grades', local_vars, None)['grades'], number(8))
    StartError.lineNumber = 46
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
    StartError.lineNumber = 48
    check_events()
    list.remove(None, _get('grades', local_vars, None)['grades'], number(5))
    StartError.lineNumber = 49
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
