from business.services.impl.command.previewing.to_markdown import FromMarkdown
from business.services.impl.command.previewing.to_plain import FromPlain
from business.services.previewing_service import PreviewingService


class PreviewingServiceImpl(PreviewingService):

    def __init__(self, connection):
        super().__init__(connection)

    def from_markdown(self, text, context=None):
        return FromMarkdown(self.connection, text, context).execute()

    def from_plain(self, text):
        return FromPlain(self.connection, text).execute()