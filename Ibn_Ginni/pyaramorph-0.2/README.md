# pyaramorph

*An Arabic morphological analyzer and lexicon*

## Introduction

**pyaramorph** is a morphological analyzer and lexicon for the Arabic
language. It is a loose port of the [Buckwalter Arabic Morphological
Analyzer Version
1.0](http://www.ldc.upenn.edu/Catalog/CatalogEntry.jsp?catalogId=LDC2002L49),
though it does not implement all of that program’s functionality.

This software is supposed to provide quick successive analyses of single
words or short phrases. Buckwalter’s original Perl script only supported
input in the `cp1256` encoding, and I really did not want to refit it
for UTF-8. (Also, given how long it has been since I worked with Perl
and my preference for Python, it seemed worth it to do a Python
rewrite.) The Java port of the same script,
[AraMorph](http://www.nongnu.org/aramorph/), does accept UTF-8, but it
only processes specified input files, and its dictionary loading is
quite slow. It’s great for analyzing full texts, but not so much for
interactive analysis.

That’s why I wrote this port. The script itself is quite simple – Tim
Buckwalter really did all the hard work by putting together the
dictionary and table files – so all credit for the functionality
provided by this program should go to him! I have simply re-written the
program to suit my own needs.

## Requirements

1. [python](http://www.python.org/). Currently you need Python 3.
2. A terminal emulator with UTF-8 and BiDi support. I use
   [mlterm](http://mlterm.sourceforge.net/) with
   [unifont](http://www.unifoundry.com/index.html) or
   [DejaVu Sans Mono](http://dejavu-fonts.org/wiki/Main_Page).
   (Here are some old though perhaps useful
   [setup instructions](http://lists.arabeyes.org/archives/general/2004/February/msg00004.html).)
3. Ability to type in UTF-8 Arabic text. Linux/Unix users can try the
   Arabic layout included in my
   [Classical Input Methods for M17N](https://bitbucket.org/alexlee/m17n-classical),
   which are intended for use with
   [IBus](https://github.com/ibus/ibus/wiki).

## Installation

You can install using `pip`, or from source with `python setup.py
install`.

## Usage

Once you have the software installed and your BiDi-enabled, UTF-8
capable terminal up and running, you simply need to run the `pyaramorph`
command. At the prompt, enter an Arabic word or phrase, using Unicode.
Words not written in the Arabic script will be ignored.

The session output below should give you an idea of how it works:

    alexlee@sartorius:~$ pyaramorph 
    loading dictPrefixes ... loaded 299 entries
    loading dictStems ... loaded 38600 lemmas and 82158 entries
    loading dictSuffixes ... loaded 618 entries
    Unicode Arabic Morphological Analyzer (press ctrl-d to exit)
    $ كتب كتابا في المكتب
    analysis for: كتب ktb
        solution: (كَتَبَ kataba) [katab-u_1]
             pos: katab/VERB_PERFECT+a/PVSUFF_SUBJ:3MS
           gloss: ___ + write + he/it <verb>

        solution: (كُتِبَ kutiba) [katab-u_1]
             pos: kutib/VERB_PERFECT+a/PVSUFF_SUBJ:3MS
           gloss: ___ + be written;be fated;be destined + he/it <verb>

        solution: (كُتُب kutub) [kitAb_1]
             pos: kutub/NOUN
           gloss: ___ + books + ___

    analysis for: كتابا ktAbA
        solution: (كِتاباً kitAbAF) [kitAb_1]
             pos: kitAb/NOUN+AF/NSUFF_MASC_SG_ACC_INDEF
           gloss: ___ + book + [acc.indef.]

        solution: (كِتابا kitAbA) [kitAb_1]
             pos: kitAb/NOUN+A/NSUFF_MASC_DU_NOM_POSS
           gloss: ___ + book + two

        solution: (كُتّاباً kut~AbAF) [kut~Ab_1]
             pos: kut~Ab/NOUN+AF/NSUFF_MASC_SG_ACC_INDEF
           gloss: ___ + kuttab (village school);Quran school + [acc.indef.]

        solution: (كُتّاباً kut~AbAF) [kAtib_1]
             pos: kut~Ab/NOUN+AF/NSUFF_MASC_SG_ACC_INDEF
           gloss: ___ + authors;writers + [acc.indef.]

    analysis for: في fy
        solution: (فِي fiy) [fiy_1]
             pos: fiy/PREP
           gloss: ___ + in + ___

        solution: (فِيَّ fiy~a) [fiy_1]
             pos: fiy/PREP+~a/PRON_1S
           gloss: ___ + in + me

        solution: (فِي fiy) [fiy_2]
             pos: Viy/ABBREV
           gloss: ___ + V. + ___

    analysis for: المكتب Almktb
        solution: (المَكْتَب Almakotab) [makotab_1]
             pos: Al/DET+makotab/NOUN
           gloss: the + bureau;office;department + ___

    $

## Todo

Diacritics are ignored for now. It would be nice to use the
user-supplied diacritics to filter through the generated solutions. That
way if you enter something like `dar~ast` (دَرَّست), it won’t return any
results from the `daras` (دَرَس) root.

In his original Perl script, Buckwalter applies a number of spelling
substitutions if a given word does not generate any solutions. This
functionality should be easy to add, but I didn’t get around to it.

A simple GUI would be nice, for a better choice of fonts (like the
[SIL Arabic fonts](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=ArabicFonts))
and for Windows support.

## Contact

If you have any comments, suggestions, fixes, contributions, etc., please
contact Alex Lee (alexlee at fastmail net). Thanks!
