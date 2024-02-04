class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages
        super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError
        if 1 > new_pages:
            raise ValueError
        self.pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration
        super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, float):
            raise TypeError
        if 0 > new_duration:
            raise ValueError
        self.duration = new_duration
