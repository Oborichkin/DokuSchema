from abc import ABC, abstractmethod


class PageElementFactory(ABC):
    @abstractmethod
    def heading(self, text, level):
        pass

    @abstractmethod
    def text(self, text):
        pass


class DokuWikiFactory(PageElementFactory):
    def heading(self, text, level=1):
        assert 1 <= level <= 5, "DokuWiki supports heading level between 1 and 5"
        return f"{'='*(7-level)} {text} {'='*(7-level)}\n\n"

    def text(self, text):
        return f"{text}\n\n"
