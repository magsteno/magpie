#test shavian dictionary

from testlib import briefsDict_search, steno_to_shav, reloaddicts

LONGEST_KEY = 6

def lookup(chords):
    assert len(chords) <= LONGEST_KEY, '%d/%d' % (len(chords), LONGEST_KEY)

    outline = []
    numbers = ['𐑪', '𐑕', '𐑑', '𐑐', '𐑣', '𐑨', '𐑓', '𐑐', '𐑤', '𐑑']
    for stroke in chords:
        outline = [''.join(outline), '']
        for key in stroke:
            if key.isnumeric():
                outline[1] = '#'
                outline.append(numbers[int(key)])
            else:
                outline.append('#𐑕𐑑𐑒𐑐𐑢𐑣𐑮𐑨𐑪-𐑧𐑳𐑓𐑚𐑤𐑜𐑛𐑟*'['#STKPWHRAO-EUFBLGDZ*'.index(key)])
        outline.append('/')

    outline = ''.join(outline[:-1])

    #reloads all dictionaries
    if outline == '𐑑𐑒-𐑮𐑐𐑤':
        reloaddicts()
        return '{PLOVER:SET_CONFIG}'

    #toggles between shavian and orthodox output
    if outline == '𐑧𐑳𐑓𐑜𐑑':
        return r'{PLOVER:TOGGLE_DICT:+testlib\testlatin.py,-testlib\testshav.py}'

    output = briefsDict_search(outline)
    if output is None:
        (output, variant) = steno_to_shav(outline.split('/'), standard = True)
        if output is None:
            raise KeyError('Empty stroke')
        if variant:
            raise KeyError('no known variant')

    return output
