#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
word frequency
==============

Figure out the word frequency in the text (TEXT) below and print the
result in the following form:
word_1  frequency_1
word_2  frequency_2
...

Let the output be sorted by the words. Every word should be in lower case,
thus for instance the words 'The' and 'the' must be treated as same words.

Use the str.split() function (without parameters) for splitting up the
text by words.

Don't bother about the punctuation parks (. , " ? etc.).

Don't try to write the whole program in one session. First write just one
part of it, then try it to see if it works. If everything is OK, go on to
the next part.
"""

############################################################################

from errno import WSAECONNREFUSED
from unittest import TestCase


TEXT = """The Old Sea-dog at the Admiral Benbow

SQUIRE TRELAWNEY, Dr. Livesey, and the rest of these gentlemen having
asked me to write down the whole particulars about Treasure Island, from
the beginning to the end, keeping nothing back but the bearings of the
island, and that only because there is still treasure not yet lifted,
I take up my pen in the year of grace 17__ and go back to the time when
my father kept the Admiral Benbow inn and the brown old seaman with the
sabre cut first took up his lodging under our roof.

I remember him as if it were yesterday, as he came plodding to the inn
door, his sea-chest following behind him in a hand-barrow--a tall, strong,
heavy, nut-brown man, his tarry pigtail falling over the shoulder of his
soiled blue coat, his hands ragged and scarred, with black, broken nails,
and the sabre cut across one cheek, a dirty, livid white. I remember him
looking round the cover and whistling to himself as he did so, and then
breaking out in that old sea-song that he sang so often afterwards:

"Fifteen men on the dead man's chest-- Yo-ho-ho, and a bottle of rum!"

in the high, old tottering voice that seemed to have been tuned and
broken at the capstan bars. Then he rapped on the door with a bit of
stick like a handspike that he carried, and when my father appeared,
called roughly for a glass of rum. This, when it was brought to him,
he drank slowly, like a connoisseur, lingering on the taste and still
looking about him at the cliffs and up at our signboard.

"This is a handy cove," says he at length; "and a pleasant sittyated
grog-shop. Much company, mate?"

My father told him no, very little company, the more was the pity.

"Well, then," said he, "this is the berth for me. Here you, matey," he
cried to the man who trundled the barrow; "bring up alongside and help
up my chest. I'll stay here a bit," he continued. "I'm a plain man; rum
and bacon and eggs is what I want, and that head up there for to watch
ships off. What you mought call me? You mought call me captain. Oh, I see
what you're at-- there"; and he threw down three or four gold pieces on
the threshold. "You can tell me when I've worked through that," says he,
looking as fierce as a commander."""

def onlyAlpha(str):
    """
    Elt??vol??tja a nem bet??ket.
    """
    res = str.replace('.', '').replace(',', '').replace('"', '').replace('-', '').replace("'", "").replace(';', '').replace('?', '').replace('!', ''). replace('_', '')
    return res


def kisBetu_lista(str):
    """
    A sztringet kisbet??ss?? alak??tja ??s list??zza a szavakat.
    Megh??vja az onlyAlpha f??ggv??nyt.
    """
    words = onlyAlpha(str).lower().split()
    return words


def rendezettLista(li):
    """
    Sorba rendez ??s a sz??ism??tl??d??st megsz??nteti.
    """
    res = sorted(set(kisBetu_lista(li)))
    return res


def wordCount(words, li):
    """
    ??sszehasonl??tja a sz??list??t a sz??veggel
    """
    d = {}
    for w in li: # v??gigmegy a sz??lista szavain
        cnt = 0             # ind??tja a sz??ml??l??t
        for word in words:  # v??gigmegy a sz??veg szavain
            if w == word:   # ha egyez??s van, a sz??ml??l??t n??veli egyel
                cnt += 1
        d[w] = str(cnt)     # a sz??t??r kulcsot elnevezi az adott sz??ra, az ??rt??ket be??ll??tja a sz??ml??l?? ??rt??k??re ??s sztringre alak??tja
    
    return d


def szotarNyomtat(dict):
    for d in dict:
        print(d, dict[d])


def main():
    # print(kisBetu_lista(TEXT))
    # print(rendezettLista(TEXT))

    szotarNyomtat(wordCount(kisBetu_lista(TEXT), rendezettLista(TEXT)))

#############################################################################

if __name__ == '__main__':
    main()
