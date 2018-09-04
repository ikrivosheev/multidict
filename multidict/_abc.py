import abc

from typing import (Mapping, MutableMapping, Generic, List, Union,
                    TypeVar, Optional, Dict, Iterable, Tuple)
from .istr import istr


_S = Union[str, istr]

_T = TypeVar('_T')


class MultiMapping(Mapping[_S, _T], Generic[_T]):

    @abc.abstractmethod
    def getall(self, key: _S, default: Optional[_T]=None) -> List[_T]:
        raise KeyError

    @abc.abstractmethod
    def getone(self, key: _S, default: Optional[_T]=None) -> _T:
        raise KeyError


_Arg = Union[Mapping[_S, _T],
             Dict[_S, _T],
             MultiMapping[_T],
             Iterable[Tuple[_S, _T]]]


class MutableMultiMapping(MultiMapping[_T], MutableMapping[_S, _T]):

    @abc.abstractmethod
    def add(self, key: _S, value: _T) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def extend(self, *args: _Arg, **kwargs: _T) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def popone(self, key: _S, default: Optional[_T]=None) -> _T:
        raise KeyError

    @abc.abstractmethod
    def popall(self, key: _S, default: Optional[_T]=None) -> List[_T]:
        raise KeyError
