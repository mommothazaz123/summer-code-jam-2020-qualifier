"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import collections
import datetime
import re
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""
    _article_counter = 0

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content

        # static id counter
        self.id = Article._article_counter
        Article._article_counter += 1

        # last edited
        self.last_edited = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self.last_edited = datetime.datetime.now()

    def short_introduction(self, n_characters: int):
        considered = self.content[:n_characters + 1]
        short, _ = considered.rsplit(maxsplit=1)  # splits on any whitespace, not just space or newline (e.g. tab)
        return short

    def most_common_words(self, n_words: int):
        counter = collections.Counter(match.group(0).lower() for match in re.finditer(r'\w+', self.content))
        return dict(counter.most_common(n_words))

    def __repr__(self):
        return f"<Article title={self.title!r} author={self.author!r} " \
               f"publication_date={self.publication_date.isoformat()!r}>"

    def __len__(self):
        return len(self.content)

    def __lt__(self, other):
        return self.publication_date < other.publication_date
