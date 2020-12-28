from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class MembershipCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/memberships"

    @abstractmethod
    def execute(self): raise NotImplementedError