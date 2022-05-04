
import threading

_LOCK = threading.RLock()
_HOOKS = {}
_VERBOSE = True

def install_hooks(name, fct):
	if _VERBOSE:
		print ("install_hook({0}, {1})".format(name, fct))
	with _LOCK:
		try:
			_HOOKS[name].append(fct)
		except KeyError:
			_HOOKS[name] = [fct]

def uninstall_hooks(name, fct=None):
	with _LOCK:
		if fct:
			_HOOKS[name].remove(fct)
		else:
			del _HOOKS[name][:]

def call_hooks(name, args):

	if _VERBOSE:
		print ("uninstall_hook({0}, {1}".format(name, fct))
	with _LOCK:
		try:
			for fct in _HOOKS[name]:
				retval = fct(args)
				if retval is not None:
					return retval
		except KeyError:
			pass
		return None


def show_hooks():
	print (_HOOKS)
	# for d in _HOOKS:
		# print (d, ":\t", _HOOKS[d], end=",\t")
		# print (d, end=",\t")


if __name__ == "__main__":
	names = ("CMD1", "CMD2", "CMD3", "CMD4", "CMD5", "CMD6")
	fcts = ("ADD", "DEL", "EDIT", "MODIFY", "REFRESH", "COMMIT")
	for name in names:
		for fct in fcts:
			install_hook(name, fct)
		show_hooks()
	print ('\n')