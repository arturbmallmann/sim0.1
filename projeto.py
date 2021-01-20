#definicao dos dados e interfaces da aplicacao
from abc import ABCMeta, abstractmethod, abstractproperty
class IGen:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_rand(self):
        """gera num"""