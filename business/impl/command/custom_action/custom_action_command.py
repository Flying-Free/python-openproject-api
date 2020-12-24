from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class CustomActionCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/custom_actions"

    @abstractmethod
    def execute(self): raise NotImplementedError