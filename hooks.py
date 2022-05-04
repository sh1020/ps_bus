
import threading

_LOCK = threading.RLock()
_HOOKS = {}
_VERBOSE = True

def install_hook(name, fct):
    if _VERBOSE:
        print ("install_hook({0}, {1})".format(name, fct))
    with _LOCK:
        try:
            _HOOKS[name].append(fct)
        except KeyError:
            _HOOKS[name] = [fct]

def uninstall_hook(name, fct=None):
    if _VERBOSE:
        print ("uninstall_hook({0}, {1}".format(name, fct))
    with _LOCK:
        if fct:
            _HOOKS[name].remove(fct)
        else:
            del _HOOKS[name][:]

def call_hooks(name, args):
    if _VERBOSE:
        print ("call_hooks({0}, {1})".format(name, args))
    with _LOCK:
        try:
            if _VERBOSE:
                print ('_HOOKS[{0}]: {1}'.format(name, _HOOKS[name]))
            for fct in _HOOKS[name]:
                if _VERBOSE:
                    # print ('\t', t)pe(fct), fct, type(args), args)
                    print ('fct: {0}, args: {1}'.format(fct, args[:]))
                retval = fct(args)
                if retval is not None:
                    return retval
        except KeyError:
            pass
        return None

def show_hooks():
    for d in _HOOKS:
        print (d, ":\t", _HOOKS[d], end="\n")


if __name__ == "__main__":
    pass