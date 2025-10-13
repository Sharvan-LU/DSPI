
from start_compiler.import_start import *



class words(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

def search(*args):
    local_vars = {}
    local_vars['n'] = args[0] if len(args) > 0 else start()
    local_vars['word'] = args[1] if len(args) > 1 else start()
    local_vars['counter'] = start()
    StartError.lineNumber = 10
    check_events()
    _set('counter', local_vars, None)['counter'] = number(0)
    StartError.lineNumber = 12
    check_events()
    
    while _lt(_get('counter', local_vars, None)['counter'], _len(_get('n', local_vars, None)['n'])): 
        StartError.lineNumber = 13
        check_events()
        
        if _eql_val(_get(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get('n', local_vars, None)['n'])[to_key(_get('counter', local_vars, None)['counter'])], _get('word', local_vars, None)['word']): 
            StartError.lineNumber = 14
            check_events()
            
            return number(1)

        StartError.lineNumber = 16
        check_events()
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))

    return number(0)
try:
    local_vars['sentence'] = start()
    StartError.lineNumber = 22
    check_events()
    _set('sentence', local_vars, None)['sentence'] = words().clone()
    StartError.lineNumber = 23
    check_events()
    _set(to_key(number(0)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(0))] = text("Let").clone()
    StartError.lineNumber = 24
    check_events()
    _set(to_key(number(1)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(1))] = text("us").clone()
    StartError.lineNumber = 25
    check_events()
    _set(to_key(number(2)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(2))] = text("look").clone()
    StartError.lineNumber = 26
    check_events()
    _set(to_key(number(3)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(3))] = text("for").clone()
    StartError.lineNumber = 27
    check_events()
    _set(to_key(number(4)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(4))] = text("specific").clone()
    StartError.lineNumber = 28
    check_events()
    _set(to_key(number(5)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(5))] = text("words").clone()
    StartError.lineNumber = 29
    check_events()
    _set(to_key(number(6)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(6))] = text("in").clone()
    StartError.lineNumber = 30
    check_events()
    _set(to_key(number(7)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(7))] = text("a").clone()
    StartError.lineNumber = 31
    check_events()
    _set(to_key(number(8)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(8))] = text("for").clone()
    StartError.lineNumber = 33
    check_events()
    _print_raw(text("What word are you looking for? "))
    local_vars['word'] = start()
    StartError.lineNumber = 35
    check_events()
    _set('word', local_vars, None)['word'] = _input_text()
    StartError.lineNumber = 37
    check_events()
    _print(text("Does the sentence,"), _get('sentence', local_vars, None)['sentence'], text("contain the word"), _get('word', local_vars, None)['word'], text(":"), search(_get('sentence', local_vars, None)['sentence'], _get('word', local_vars, None)['word']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
