import collections
import functools


def string_hash(s, modulus):
    mult = 997
    return functools.reduce(lambda v, c: (v * mult + ord(c)) % modulus, s, 0)


class ContactList:

    def __init__(self, names):
        """
        names is a list of strings.
        """
        self.names = names

    def __hash__(self):
        # conceptually we want to hash the set of names. since the set type is
        # mutable, it cannot be hashed. therefore we use frozenset
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)


def merge_contact_lists(contacts):
    """
    contacts is a list of ContactList
    """
    return list(set(contacts))


def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
        group for group in sorted_string_to_anagrams.values() if len(group) >= 2
    ]
