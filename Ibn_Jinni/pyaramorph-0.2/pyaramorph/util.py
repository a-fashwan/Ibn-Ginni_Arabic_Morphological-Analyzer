# util.py
# Helpful functions.

import re
from pkg_resources import resource_filename

class DictionaryLoadError(Exception):
    """Indicates a problem while loading a dictionary"""

MAX_PREFIX_LENGTH = 4
MAX_SUFFIX_LENGTH = 6

def segment_indexes(wordlen):
    """Generate possible segment indexes.
    
    A word can be divided into three parts: prefix+stem+suffix. The
    prefix and suffix are optional, but the stem is mandatory.

    In this function we generate all the possible ways of breaking down
    a word of the given length. The generator returns a pair of values,
    representing the stem index and the suffix index.
    """
    prelen = 0
    suflen = 0

    while prelen <= MAX_PREFIX_LENGTH:
        stemlen = wordlen - prelen
        suflen = 0

        while stemlen >= 1 and suflen <= MAX_SUFFIX_LENGTH:
            # Cannot have zero-length stem.
            yield (prelen, prelen + stemlen)
            
            stemlen -= 1
            suflen += 1

        prelen += 1

def _data_file_path(filename):
    """ Return the path to the given data file """
    return resource_filename(__name__, filename)

def load_dict(filename, encoding='utf-8'):
    """Load and return the given dictionary"""
    dict = {}
    seen = set()
    lemmas = 0
    entries = 0
    lemmaID = ""
    spattern = ""
    root = ""

    p_AZ = re.compile('^[A-Z]')
    p_iy = re.compile('iy~$')

    infile = open(_data_file_path(filename), 'r', encoding=encoding)
    print("loading %s ... " % (filename), end='')

    for line in infile:
        #print(line)
        if line.startswith(';; '): # a new lemma
            m = re.search('^;; (.*)$', line)
            lemmaID = m.group(1)
            seen.add(lemmaID)
            lemmas += 1;
        
        elif line.startswith(';;;-- '): # stem pattern
            m = re.search('^;;;-- (.*)$', line)
            root = m.group(1)
        
        elif line.startswith(';--- '): # stem pattern
            m = re.search('^;--- (.*)$', line)
            spattern = m.group(1)    
        
        elif line.startswith(';'): # a comment
            continue

        else: 
            #print(line)
            line = line.strip(' \n')
            (entry, voc, cat, glossPOS) = re.split('\t', line)
            m = re.search('<pos>(.+?)</pos>', glossPOS)
            if m:
                POS = m.group(1)
                gloss = glossPOS
            else:
                gloss = glossPOS
                #voc = "%s (%s)" % (buckwalter.buck2uni(voc), voc)
                if cat.startswith('Pref-0') or cat.startswith('Suff-0'):
                    POS = "" # null prefix or suffix
                elif cat.startswith('F'):
                    POS = "%s/FUNC_WORD" % voc
                elif cat.startswith('IV_Pass'):
                    POS = "%s/IV" % voc
                elif cat.startswith('IV'):
                    POS = "%s/IV" % voc
                elif cat.startswith('PV_Pass'):
                    POS = "%s/PV_PASS" % voc
                elif cat.startswith('PV'):
                    POS = "%s/PV" % voc
                elif cat.startswith('CV'):
                    POS = "%s/CV" % voc
                elif cat.startswith('N') and "NOUN_PROP" in gloss:
                    POS = "%s/NOUN_PROP" % voc # educated guess
                elif cat.startswith('N') and "ADV_TIM" in gloss:
                    POS = "%s/ADV_TIME" % voc # educated guess
                elif cat.startswith('N') and "ADV_PLC" in gloss:
                    POS = "%s/ADV_PLACE" % voc # educated guess
                elif cat.startswith('N') and "ADV_TPL" in gloss:
                    POS = "%s/ADV_TIME_PLACE" % voc # educated guess
                elif cat.startswith('N') and "ADV_MNN" in gloss:
                    POS = "%s/ADV_MANNER" % voc # educated guess
                elif cat.startswith('N') and p_iy.search(voc):
                    POS = "%s/NOUN" % voc # (was NOUN_ADJ:
                            # some of these are really ADJ's
                            # and need to be tagged manually)
                elif cat.startswith('N'):
                    POS = "%s/NOUN" % voc
                elif cat.startswith('J'):
                    POS = "%s/ADJ" % voc
                else:
                    raise DictionaryLoadError(
                            "no POS can be deduced in %s: %s" % \
                            (filename, line))

            gloss = re.sub('<pos>.+?</pos>', '', gloss)
            gloss = gloss.strip()
            dict.setdefault(entry, []).append(
                (entry, voc, cat, gloss, POS, lemmaID, root, spattern))
            entries += 1

    infile.close()
    if not lemmaID == "":
        print("loaded %d lemmas and %d entries" % (lemmas, entries))
    else:
        print("loaded %d entries" % (entries))
    return dict

def load_table(filename, encoding='utf-8'):
    """Load and return the given table"""
    p = re.compile('\s+')
    table = {}
    infile = open(_data_file_path(filename), 'r', encoding=encoding)

    for line in infile:
        if line.startswith(';'): continue # comment line
        line = line.strip()
        p.sub(' ', line)
        table[line] = 1

    infile.close()
    return table

