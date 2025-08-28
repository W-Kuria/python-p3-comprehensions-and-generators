#!/usr/bin/env python3


def return_evens(sequence):
    """
    Takes a sequence of integers and returns only the even ones.
    Example: return_evens([0, 1, 3, 5, 7, 8, 9]) -> [0, 8]
    """
    return [n for n in sequence if n % 2 == 0]


def make_exclamation(sentences):
    """
    Takes a list of sentences and returns them with '!' at the end.
    Example: make_exclamation(["Hello", "Python is fun"]) -> ["Hello!", "Python is fun!"]
    """
    return [sentence + "!" for sentence in sentences]