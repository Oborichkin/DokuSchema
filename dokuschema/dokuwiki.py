from abc import ABC, abstractmethod
from typing import Iterable, List, Tuple


class PageElementFactory(ABC):
    @abstractmethod
    def heading(self, text: str, level: int):
        pass

    @abstractmethod
    def text(self, text: str):
        pass

    @abstractmethod
    def table(self, rows: List[Tuple], heading: Iterable):
        pass


class DokuWikiFactory(PageElementFactory):
    def heading(self, text: str, level: int = 1):
        assert 1 <= level <= 5, "DokuWiki supports heading level between 1 and 5"
        return f"{'='*(7-level)} {text} {'='*(7-level)}\n\n"

    def text(self, text: str):
        return f"{text}\n\n"

    def table(self, rows: List[Tuple], heading: Iterable):
        res = [f"^ {' ^ '.join(heading)} ^"]
        for row in rows:
            res.append(f"| {' | '.join(row)} |")
        return "\n".join(res)
