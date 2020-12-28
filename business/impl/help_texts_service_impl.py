from business.impl.command.help_texts.find_all import FindAll
from business.impl.command.help_texts.find import Find
from business.help_texts_service import HelpTextsService

class HelpTextsServiceImpl(HelpTextsService):

    def find(self, help_text):
        return Find(help_text).execute()

    def find_all(self):
        return FindAll().execute()