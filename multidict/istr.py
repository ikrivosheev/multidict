import sys
from ._compat import USE_CYTHON_EXTENSIONS


class istr(str):

    """Case insensitive str."""

    __is_istr__ = True

    def __new__(cls, val='',
                encoding=sys.getdefaultencoding(), errors='strict'):
        if getattr(val, '__is_istr__', False):
            # Faster than instance check
            return val
        if type(val) is str:
            pass
        else:
            val = str(val)
        val = val.title()
        return str.__new__(cls, val)

    def title(self):
        return self


upstr = istr  # for relaxing backward compatibility problems

istr_py = istr


try:
    if not USE_CYTHON_EXTENSIONS:  # pragma: no cover
        raise ImportError
    from ._istr import istr  # type: ignore
    istr_c = istr
except ImportError:  # pragma: no cover
    pass
