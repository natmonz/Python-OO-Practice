"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Finds randomized words from given dictionary

    >>> wf = WordFinder('words.txt')
    235886 words read

    >>> wf.random()
    'isolative'

    >>> wf.random()
    'cliack'
    """

    def __init__(self, path):
        """Reads dictionary and reports # of items read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)

        print(f'{len(self.words)} words read')

    def parse(self, dict_file):
        """Parses dict_file into list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Returns random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Word finder that will exclude blank lines.


    >>> swf = SpecialWordFinder("random_word.txt")

    >>> swf.random() in ['kale', 'apple', 'mango']
    True


    """

    def parse(self, dict_file):
        """Parses df into lists of words and will skip blank lines"""
        return [w.strip() for w in dict_file if w.strip() and not w.startswith('#')]
