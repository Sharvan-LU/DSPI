
from start_compiler.import_start import *



class words(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

    def search(self, *args):
        local_vars = {}
        local_vars['w1'] = args[0] if len(args) > 0 else start()
        local_vars['loop_up'] = args[1] if len(args) > 1 else start()
        StartError.lineNumber = 8
        check_events()
        
        if _eql_val(_len(_get('w1', local_vars, None)['w1']), number(0)): 
            StartError.lineNumber = 9
            check_events()
            
            return number(0)

        StartError.lineNumber = 12
        check_events()
        
        if _eql_val(_get(to_key(number(0)), local_vars, _get('w1', local_vars, None)['w1'])[to_key(number(0))], _get('loop_up', local_vars, None)['loop_up']): 
            StartError.lineNumber = 13
            check_events()
            
            return number(1)

        return words.search(None, words.helper(None, _get('w1', local_vars, None)['w1']), _get('loop_up', local_vars, None)['loop_up'])

    def helper(self, *args):
        local_vars = {}
        local_vars['w1'] = args[0] if len(args) > 0 else start()
        local_vars['new'] = start()
        StartError.lineNumber = 22
        check_events()
        _set('new', local_vars, None)['new'] = words()
        local_vars['i'] = start()
        StartError.lineNumber = 25
        check_events()
        _set('i', local_vars, None)['i'] = number(1)
        StartError.lineNumber = 27
        check_events()
        
        while _lt(_get('i', local_vars, None)['i'], _len(_get('w1', local_vars, None)['w1'])): 
            StartError.lineNumber = 28
            check_events()
            _set(to_key(_sub(_get('i', local_vars, None)['i'], number(1))), local_vars, _get('new', local_vars, None)['new'])[to_key(_sub(_get('i', local_vars, None)['i'], number(1)))] = _get(to_key(_get('i', local_vars, None)['i']), local_vars, _get('w1', local_vars, None)['w1'])[to_key(_get('i', local_vars, None)['i'])]
            StartError.lineNumber = 29
            check_events()
            _set('i', local_vars, None)['i'] = _add(_get('i', local_vars, None)['i'], number(1))

        return _get('new', local_vars, None)['new']
try:
    local_vars['phrase'] = start()
    StartError.lineNumber = 36
    check_events()
    _set('phrase', local_vars, None)['phrase'] = words(text("Hi"), text("there"))
    StartError.lineNumber = 38
    check_events()
    _print(words.search(None, _get('phrase', local_vars, None)['phrase'], text("kip")))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
