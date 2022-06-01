"""
File: testhashdict.py
A program for testing rehashing of as hash dictionary
"""

from hashdict import HashDict


def main(dictionaryType):
    d = dictionaryType()
    for key in range(1, 20):
        d[key] = "Value" + str(key)
        print("Length: %3d, Load factor: %5.3f" % (len(d), d.loadFactor()))
    while d.loadFactor() > 0.5:
        d.rehash()
        print("Load factor after rehash: %5.3f" % d.loadFactor())


if __name__ == "__main__":
    main(HashDict)
