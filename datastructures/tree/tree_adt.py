from abc import ABC, abstractmethod
from typing import Iterable, Optional


class Tree(ABC):
    """Abstract base class representing a tree structure."""

    class Position(ABC):
        """An abstraction representing the location of a single element."""

        @abstractmethod
        def element(self) -> object:
            pass

        @abstractmethod
        def __eq__(self, other: object) -> bool:
            pass

    @abstractmethod
    def root(self) -> Optional["Tree.Position"]:
        pass

    @abstractmethod
    def parent(self, p: "Tree.Position") -> Optional["Tree.Position"]:
        pass

    @abstractmethod
    def num_children(self, p: "Tree.Position") -> int:
        pass

    @abstractmethod
    def children(self, p: "Tree.Position") -> Iterable["Tree.Position"]:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    def is_root(self, p: "Tree.Position") -> bool:
        return self.root() == p

    def is_leaf(self, p: "Tree.Position") -> bool:
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        return len(self) == 0

    def depth(self, p: "Tree.Position") -> int:
        if self.is_root(p):
            return 0
        parent = self.parent(p)
        if parent is None:
            raise ValueError("Position has no parent but is not root")
        return 1 + self.depth(parent)

    def height(self, p: "Tree.Position") -> int:
        if self.is_leaf(p):
            return 0
        return 1 + max(self.height(c) for c in self.children(p))
