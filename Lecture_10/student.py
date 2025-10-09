
from start_compiler.import_start import *



class numbers(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

class student(start):
    def __init__(self, *args):
        self.name = args[0] if len(args) > 0 else start()
        self.grades = args[1] if len(args) > 1 else start()

    def avg_grade(self, *args):
        local_vars = {}
        local_vars['person'] = args[0] if len(args) > 0 else start()
        local_vars['counter'] = start()
        StartError.lineNumber = 14
        check_events()
        _set('counter', local_vars, None)['counter'] = number(0)
        local_vars['sum'] = start()
        StartError.lineNumber = 16
        check_events()
        _set('sum', local_vars, None)['sum'] = number(0)
        StartError.lineNumber = 18
        check_events()
        
        while _lt(_get('counter', local_vars, None)['counter'], _len(_get(to_key(text('grades')), local_vars, _get('person', local_vars, None)['person'])[to_key(text('grades'))])): 
            StartError.lineNumber = 19
            check_events()
            _set('sum', local_vars, None)['sum'] = _add(_get('sum', local_vars, None)['sum'], _get(to_key(_get('counter', local_vars, None)['counter']), local_vars, _get(to_key(text('grades')), local_vars, _get('person', local_vars, None)['person'])[to_key(text('grades'))])[to_key(_get('counter', local_vars, None)['counter'])])
            StartError.lineNumber = 20
            check_events()
            _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1))

        return _div(_get('sum', local_vars, None)['sum'], _len(_get(to_key(text('grades')), local_vars, _get('person', local_vars, None)['person'])[to_key(text('grades'))]))
try:
    local_vars['person'] = start()
    StartError.lineNumber = 28
    check_events()
    _set('person', local_vars, None)['person'] = student(text("Dummy"), numbers(number(5), number(7), number(3), number(8), number(9)))
    StartError.lineNumber = 29
    check_events()
    _print(text("student:"), _get('person', local_vars, None)['person'], text("has an average grade of"), student.avg_grade(None, _get('person', local_vars, None)['person']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
