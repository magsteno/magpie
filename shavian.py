#Ruma's Shavian syllable dictionary
import re

LONGEST_KEY = 6

#each chord in the dictionary is assigned a specific consonant cluster or vowel. sorted loosely based on standard shavian order
#rhotic clusters lack the letter 𐑮 because these already exist in the vowel. rhotic vowels lack the R in the chord because these already exist in the final
strokesDict = {
    'initials': {'': '', 'YAE': '𐑿', 'EU': '𐑦',
        'P': '𐑐', 'PHR': '𐑐𐑤', 'PR': '𐑐𐑮', 'PW': '𐑚', 'PWHR': '𐑚𐑤', 'PWR': '𐑚𐑮',
        'T': '𐑑', 'TW': '𐑑𐑢', 'TR': '𐑑𐑮', 'TK': '𐑛', 'TKW': '𐑛𐑢', 'TKR': '𐑛𐑮',
        'K': '𐑒', 'KW': '𐑒𐑢', 'KHR': '𐑒𐑤', 'KR': '𐑒𐑮', 'STK': '𐑜', 'STKW': '𐑜𐑢', 'STKHR': '𐑜𐑤', 'STKR': '𐑜𐑮',
        'TP': '𐑓', 'TPHR': '𐑓𐑤', 'TPR': '𐑓𐑮', 'TPW': '𐑝', 'TPWR': '𐑝𐑮',
        'TH': '𐑔', 'THR': '𐑔𐑮', 'TKH': '𐑞',
        'S': '𐑕', 'SP': '𐑕𐑐', 'SPHR': '𐑕𐑐𐑤', 'SPR': '𐑕𐑐𐑮', 'ST': '𐑕𐑑', 'STR': '𐑕𐑑𐑮', 'SK': '𐑕𐑒', 'SKHR': '𐑕𐑒𐑤', 'SKR': '𐑕𐑒𐑮', 'SKW': '𐑕𐑒𐑢', 'STP': '𐑕𐑓', 'SW': '𐑕𐑢', 'SHR': '𐑕𐑤', 'SPH': '𐑕𐑥', 'STPH': '𐑕𐑯', 'SR': '𐑟',
        'KP': '𐑖', 'KPHR': '𐑖𐑤', 'KPR': '𐑖𐑮', 'KPW': '𐑠',
        'TKP': '𐑗', 'TKPW': '𐑡',
        'KWR': '𐑘', 'W': '𐑢',
        'H': '𐑣', 'WH': '𐑣𐑢',
        'HR': '𐑤', 'R': '𐑮',
        'PH': '𐑥', 'TPH': '𐑯'},
    'nonrhotic': {'': '', 'TZ': '',
        'P': '𐑐', 'PT': '𐑐𐑑', 'PTS': '𐑐𐑑𐑕', 'PTD': '𐑐𐑔', 'PTDZ': '𐑐𐑔𐑕', 'PS': '𐑐𐑕', 'PSD': '𐑐𐑕𐑑', 'PBT': '𐑐𐑕𐑑',
        'B': '𐑚', 'BD': '𐑚𐑛', 'BDZ': '𐑚𐑛𐑟', 'BZ': '𐑚𐑟',
        'T': '𐑑', 'LTD': '𐑑𐑔', 'LTDZ': '𐑑𐑔𐑕', 'TS': '𐑑𐑕', 'TSD': '𐑑𐑕𐑑',
        'D': '𐑛', 'LG': '𐑛', 'LGTD': '𐑛𐑔', 'LGTDZ': '𐑛𐑔𐑕', 'DZ': '𐑛𐑟', 'LGZ': '𐑛𐑟', 'LGSD': '𐑛𐑟𐑛',
        'BG': '𐑒', 'BGT': '𐑒𐑑', 'GT': '𐑒𐑑', 'BGTS': '𐑒𐑑𐑕', 'GTS': '𐑒𐑑𐑕', 'BGTD': '𐑒𐑔', 'BGTDZ': '𐑒𐑔𐑕', 'BGS': '𐑒𐑕', 'GS': '𐑒𐑕', 'BGSD': '𐑒𐑕𐑑', 'GSD': '𐑒𐑕𐑑', 'BGSDZ': '𐑒𐑕𐑑𐑕', 'GSDZ': '𐑒𐑕𐑑𐑕', 'BGTSD': '𐑒𐑕𐑔', 'GTSD': '𐑒𐑕𐑔', 'BGTSDZ': '𐑒𐑕𐑔𐑕', 'GTSDZ': '𐑒𐑕𐑔𐑕',
        'G': '𐑜', 'GD': '𐑜𐑛', 'GDZ': '𐑜𐑛𐑟', 'GTD': '𐑜𐑔', 'GTDZ': '𐑜𐑔𐑕', 'GZ': '𐑜𐑟',
        'F': '𐑓', 'FT': '𐑓𐑑', 'FTS': '𐑓𐑑𐑕', 'FTD': '𐑓𐑔', 'FTDZ': '𐑓𐑔𐑕', 'FS': '𐑓𐑕', 'FSD': '𐑓𐑕𐑑',
        'PBL': '𐑝', 'PBLD': '𐑝𐑛', 'FD': '𐑝𐑛', 'PBLTD': '𐑝𐑔', 'PBLTDZ': '𐑝𐑔𐑕', 'PBLZ': '𐑝𐑟', 'FZ': '𐑝𐑟',
        'TD': '𐑔', 'FLT': '𐑔𐑑', 'FLTS': '𐑔𐑑𐑕', 'FLS': '𐑔𐑕', 'TDZ': '𐑔𐑕', 'FLSD': '𐑔𐑕𐑑',
        'FLG': '𐑞', 'FLGD': '𐑞𐑛', 'FLGZ': '𐑞𐑟',
        'S': '𐑕', 'FP': '𐑕𐑐', 'FPS': '𐑕𐑐𐑕', 'FPSD': '𐑕𐑐𐑕𐑑', 'FPT': '𐑕𐑐𐑑', 'FPTS': '𐑕𐑐𐑑𐑕', 'SD': '𐑕𐑑', 'BT': '𐑕𐑑', 'SDZ': '𐑕𐑑𐑕', 'BTS': '𐑕𐑑𐑕', 'FBG': '𐑕𐑒', 'FBGT': '𐑕𐑒𐑑', 'FBGTS': '𐑕𐑒𐑑𐑕', 'FBGS': '𐑕𐑒𐑕', 'FBGSD': '𐑕𐑒𐑕𐑑', 'BTD': '𐑕𐑔', 'BTDZ': '𐑕𐑔𐑕',
        'Z': '𐑟', 'BS': '𐑟', 'BLG': '𐑟𐑛', 'BSD': '𐑟𐑛', 'BTSD': '𐑟𐑔', 'BTSDZ': '𐑟𐑔𐑕',
        'PG': '𐑖', 'PGT': '𐑖𐑑', 'PGTS': '𐑖𐑑𐑕', 'PGTD': '𐑖𐑔', 'PGTDZ': '𐑖𐑔𐑕',
        'PGZ': '𐑠', 'PBGD': '𐑠𐑛', 'PGD': '𐑠𐑛', 'PBGDZ': '𐑠𐑛𐑟', 'PGDZ': '𐑠𐑛𐑟',
        'PLG': '𐑗', 'PLGT': '𐑗𐑑', 'PLGTS': '𐑗𐑑𐑕', 'PLGTD': '𐑗𐑔', 'PLGTDZ': '𐑗𐑔𐑕',
        'PBLG': '𐑡', 'PLGZ': '𐑡', 'PBLGD': '𐑡𐑛', 'PLGD': '𐑡𐑛', 'PBLGDZ': '𐑡𐑛𐑟', 'PLGDZ': '𐑡𐑛𐑟', 'PBLGTD': '𐑡𐑔', 'PBLGTDZ': '𐑡𐑔𐑕',
        'PB': '𐑙', 'PBD': '𐑙𐑛', 'PBDZ': '𐑙𐑛𐑟', 'PBG': '𐑙𐑒', 'PBGT': '𐑙𐑒𐑑', 'PBGTS': '𐑙𐑒𐑑𐑕', 'PBGTD': '𐑙𐑒𐑔', 'PBGTDZ': '𐑙𐑒𐑔𐑕', 'PBGS': '𐑙𐑒𐑕', 'PBGSD': '𐑙𐑒𐑕𐑑', 'PBGSDZ': '𐑙𐑒𐑕𐑑𐑕', 'FG': '𐑙𐑜', 'FGD': '𐑙𐑜𐑛', 'FGDZ': '𐑙𐑜𐑛𐑟', 'FGZ': '𐑙𐑜𐑟', 'PBTD': '𐑙𐑔', 'PBTDZ': '𐑙𐑔𐑕', 'PBS': '𐑙𐑕', 'PBSD': '𐑙𐑕𐑑', 'PBSDZ': '𐑙𐑕𐑑𐑕', 'PBZ': '𐑙𐑟',
        'L': '𐑤', 'FRP': '𐑤𐑐', 'FRPT': '𐑤𐑐𐑑', 'FRPTS': '𐑤𐑐𐑑𐑕', 'FRPS': '𐑤𐑐𐑕', 'FRPSD': '𐑤𐑐𐑕𐑑', 'FRPB': '𐑤𐑚', 'FRPBD': '𐑤𐑚𐑛', 'FRPBZ': '𐑤𐑚𐑟',
        'LT': '𐑤𐑑', 'LTS': '𐑤𐑑𐑕', 'LTSD': '𐑤𐑑𐑕𐑑', 'LD': '𐑤𐑛', 'FRLG': '𐑤𐑛', 'LDZ': '𐑤𐑛𐑟', 'FRLGZ': '𐑤𐑛𐑟',
        'FRBG': '𐑤𐑒', 'FRBGT': '𐑤𐑒𐑑', 'FRBGTS': '𐑤𐑒𐑑𐑕', 'FRBGS': '𐑤𐑒𐑕', 'FRBGSD': '𐑤𐑒𐑕𐑑', 'FRG': '𐑤𐑜', 'FRGD': '𐑤𐑜𐑛', 'FRGZ': '𐑤𐑜𐑟',
        'FRPL': '𐑤𐑓', 'FRPLT': '𐑤𐑓𐑑', 'FRPLTS': '𐑤𐑓𐑑𐑕', 'FRPLTD': '𐑤𐑓𐑔', 'FRPLTDZ': '𐑤𐑓𐑔𐑕', 'FRPLS': '𐑤𐑓𐑕', 'FRPLSD': '𐑤𐑓𐑕𐑑', 'FRPBL': '𐑤𐑝', 'FRPBLD': '𐑤𐑝𐑛', 'FRPBLZ': '𐑤𐑝𐑟',
        'FRL': '𐑤𐑔', 'FRLT': '𐑤𐑔𐑑', 'FRLTS': '𐑤𐑔𐑑𐑕', 'FRLS': '𐑤𐑔𐑕', 'FRLSD': '𐑤𐑔𐑕𐑑',
        'LS': '𐑤𐑕', 'LSD': '𐑤𐑕𐑑', 'LZ': '𐑤𐑟', 'FRBS': '𐑤𐑟', 'FRBSD': '𐑤𐑟𐑛',
        'FRPG': '𐑤𐑖', 'FRPGT': '𐑤𐑖𐑑', 'FRPBG': '𐑤𐑠', 'FRPBGD': '𐑤𐑠𐑛',
        'FRPLG': '𐑤𐑗', 'FRPLGT': '𐑤𐑗𐑑', 'FRPBLG': '𐑤𐑡', 'FRPBLGD': '𐑤𐑡𐑛',
        'FBL': '𐑤𐑥', 'FBLD': '𐑤𐑥𐑛', 'FBLZ': '𐑤𐑥𐑟', 'FL': '𐑤𐑯', 'FLD': '𐑤𐑯𐑛', 'FLZ': '𐑤𐑯𐑟',
        'FB': '𐑥', 'FPB': '𐑥𐑐', 'FPBT': '𐑥𐑐𐑑', 'FPBTS': '𐑥𐑐𐑑𐑕', 'FPBS': '𐑥𐑐𐑕', 'FPBSD': '𐑥𐑐𐑕𐑑', 'FPBL': '𐑥𐑓', 'FPBLS': '𐑥𐑓𐑕', 'FPBLSD': '𐑥𐑓𐑕𐑑', 'FPBLT': '𐑥𐑓𐑑', 'FPBLTS': '𐑥𐑓𐑑𐑕', 'FBT': '𐑥𐑑', 'FBTS': '𐑥𐑑𐑕', 'FBD': '𐑥𐑛', 'FBDZ': '𐑥𐑛𐑟', 'FBTD': '𐑥𐑔', 'FBTDZ': '𐑥𐑔𐑕', 'FBZ': '𐑥𐑟',
        'FPL': '𐑯', 'FPLT': '𐑯𐑑', 'FPLTS': '𐑯𐑑𐑕', 'FPLD': '𐑯𐑛', 'FPLDZ': '𐑯𐑛𐑟', 'FPLTD': '𐑯𐑔', 'FPLTDZ': '𐑯𐑔𐑕', 'FPLS': '𐑯𐑕', 'FPLSD': '𐑯𐑕𐑑', 'FPLZ': '𐑯𐑟', 'FPG': '𐑯𐑖', 'FPGT': '𐑯𐑖𐑑', 'FPBG': '𐑯𐑠', 'FPBGD': '𐑯𐑠𐑛', 'FPGD': '𐑯𐑠𐑛', 'FPLG': '𐑯𐑗', 'FPLGT': '𐑯𐑗𐑑', 'FPBLG': '𐑯𐑡', 'FPBLGD': '𐑯𐑡𐑛',
        'EU': '𐑦', 'AOEU': '𐑰', 'E': '𐑧', 'AOE': '𐑱', 'A': '𐑨', 'AOU': '𐑲', '*': '𐑩', '*R': '𐑼', '*U': '𐑩', 'U': '𐑳', 'O': '𐑪', 'OU': '𐑴', 'AO': '𐑫', 'AE': '𐑵', 'AU': '𐑬', 'OE': '𐑶', 'AEU': '𐑭', 'OEU': '𐑷', '*E': '𐑧𐑩', 'AO*EU': '𐑾', '*EU': '𐑾', 'A*E': '𐑿', 'AO*': '𐑘𐑩'},
    'rhotic': {'RTZ': '',
        'R': '', 'RP': '𐑐', 'RPT': '𐑐𐑑', 'RPTS': '𐑐𐑑𐑕', 'RPS': '𐑐𐑕', 'RPSD': '𐑐𐑕𐑑', 'RB': '𐑚', 'RBD': '𐑚𐑛', 'RBZ': '𐑚𐑟',
        'RT': '𐑑', 'RTS': '𐑑𐑕', 'RTSD': '𐑑𐑕𐑑', 'RD': '𐑛', 'RLG': '𐑛', 'RDZ': '𐑛𐑟', 'RLGZ': '𐑛𐑟',
        'RBG': '𐑒', 'RBGT': '𐑒𐑑', 'RBGTS': '𐑒𐑑𐑕', 'RBGS': '𐑒𐑕', 'RBGSD': '𐑒𐑕𐑑', 'RG': '𐑜', 'RGD': '𐑜𐑛', 'RGZ': '𐑜𐑟',
        'FR': '𐑓', 'FRT': '𐑓𐑑', 'FRTS': '𐑓𐑑𐑕', 'FRS': '𐑓𐑕', 'FRSD': '𐑓𐑕𐑑', 'RPBL': '𐑝', 'RPBLD': '𐑝𐑛', 'FRD': '𐑝𐑛', 'RPBLZ': '𐑝𐑟', 'FRZ': '𐑝𐑟',
        'RTD': '𐑔', 'FRLGT': '𐑔𐑑', 'RTDZ': '𐑔𐑕', 'FRLGS': '𐑔𐑕', 'FRLG': '𐑞', 'FRLGD': '𐑞𐑛', 'FRLGZ': '𐑞𐑟',
        'RS': '𐑕', 'RSD': '𐑕𐑑', 'RBT': '𐑕𐑑', 'RSDZ': '𐑕𐑑𐑕', 'RBTS': '𐑕𐑑𐑕', 'RZ': '𐑟', 'RBS': '𐑟', 'RBSD': '𐑟𐑛',
        'RPG': '𐑖', 'RBGT': '𐑖𐑑', 'RPBG': '𐑠', 'RPBGD': '𐑠𐑛', 'RPGD': '𐑠𐑛',
        'RPLG': '𐑗', 'RPLGT': '𐑗𐑑', 'RPBLG': '𐑡', 'RPBLGD': '𐑡𐑛',
        'RL': '𐑤', 'RLD': '𐑤𐑛', 'RLDZ': '𐑤𐑛𐑟', 'RLZ': '𐑤𐑟',
        'FRB': '𐑥', 'FRBD': '𐑥𐑛', 'FRBZ': '𐑥𐑟', 'RPB': '𐑯', 'RPBT': '𐑯𐑑', 'RPBTS': '𐑯𐑑𐑕', 'RPBD': '𐑯𐑛', 'RPBS': '𐑯𐑕', 'RPBZ': '𐑯𐑟',
        'A': '𐑸', 'O': '𐑹', 'E': '𐑺', 'U': '𐑻', '*': '𐑼', '*U': '𐑼', 'AOEU': '𐑽', 'EU': '𐑽', 'AO': '𐑫𐑼', 'AO*': '𐑘𐑫𐑼', '*EU': '𐑘𐑼'}
    }

shortcutsDict = {
    'U': '𐑩', '-FPL': '𐑩𐑯', '-LG': '𐑞', 'T': '𐑑', '-F': '𐑝', 'SKP': '𐑯', 'TP': '𐑓',
    'T-LG': '𐑑 𐑞', '-FLG': '𐑝 𐑞', 'SKP-LG': '𐑯 𐑞', 'TP-LG': '𐑓 𐑞',
    '-PB': '{^𐑦𐑙}', '-PBZ': '{^𐑦𐑙𐑟}', '-L': '{^𐑤𐑦}', '-PBL': '{^𐑦𐑙𐑤𐑦}', '*BL': '{^𐑩𐑚𐑩𐑤}', '*BLZ': '{^𐑩𐑚𐑩𐑤𐑟}', 'EUBL': '{^𐑩𐑚𐑤𐑦}', 'TPAO*U': '{^𐑦𐑓𐑲}',
    'TKAFB/TPH*BL': '𐑛𐑨𐑥𐑯𐑩𐑚𐑩𐑤'
    }

#i learnt some of this code from emily-symbols. thanks emily for commenting it so well and helping me learn

def lookup(chords):

    #apparently this is a failsafe for the longest key being no longer than the limit; i don't know what it does
    assert len(chords) <= LONGEST_KEY, '%d/%d' % (len(chords), LONGEST_KEY)

    #it is assumed we start on a new word, this {^} however ensures a first syllable can be placed
    output = ['{^}']
    joinsPrevious = False

    if '/'.join(chords) in shortcutsDict:
        return shortcutsDict['/'.join(chords)]

    for index, stroke in enumerate(chords):

        if stroke == '*':
            raise KeyError

        #this variable determines whether the following stroke explicitly continues
        joinsNext = False
        #converts from embedded-number format to standard printed steno order. marks for multiple syllables
        if any(k in stroke for k in '1234506789#'):
            stroke = list(stroke)
            joinsNext = True
            numbers = ['O', 'S', 'T', 'P', 'H', 'A', 'F', 'P', 'L', 'T']
            for key in range(len(stroke)):
                if stroke[key].isnumeric():
                    stroke[key] = numbers[int(stroke[key])]
            stroke = ''.join(stroke)

        if stroke == '#':
            if index != 0:
                output[index + joinsPrevious] = ''
            elif len(chords) != 1:
                raise KeyError
            output.append('{^}')
            continue
        if '#' in stroke:
            stroke = stroke.replace('#', '')

        #the following regex splits the stroke into 'initial' cluster, 'vowel', and 'final' cluster
        match = re.fullmatch(r'([STKPWHR]*)([AO*EU-]+)([FRPBLGTSDZ]*)', stroke)
        if match is None:
            raise KeyError
        (initial, vowel, final) = match.groups()

        if final in list(strokesDict['rhotic'].keys()):
            rhoticity = 'rhotic'
        else:
            rhoticity = 'nonrhotic'

        if initial == 'KWR' and (vowel == '-' or (rhoticity == 'nonrhotic' and vowel + strokesDict[rhoticity][final] == '*𐑕𐑑')):
            initial = 'EU'
            if final == 'R':
                vowel = '*'
            elif 'R' in final:
                raise KeyError
            elif vowel == '-':
                vowel = ''

        syllable = strokesDict['initials'][initial] + strokesDict[rhoticity][vowel] + strokesDict[rhoticity][final]

        #if vowel is schwa or schwi, or 𐑾/𐑽 as a suffix, connects with previous syllable
        if (any(s in syllable for s in '𐑩𐑼𐑾𐑽') and not(any(v in syllable for v in '𐑧𐑫') or (len(vowel) > 3) or (vowel == '*' and joinsNext))) or (vowel == 'EU' and (final == '' or 'R' in final)) or initial == 'EU':
            if vowel == '*' and final == '':
                raise KeyError
            if index == 0:
                joinsPrevious = True
                output.append('{^}')
            else:
                output[index + joinsPrevious] = '{^}'

        #alternative join next syllable
        if final == 'TZ' or final == 'RTZ':
            joinsNext = True

        #raises KeyError if this syllable should not connect to previous
        if output[index + joinsPrevious] != '{^}':
            raise KeyError

        #replaces schwa with schwu if it comes before a vowel
        schwu = output[index + joinsPrevious - 1]
        if schwu[len(schwu)-1:] == '𐑩' and initial == '':
            output[index + joinsPrevious - 1] = schwu[:len(schwu)-1] + '𐑫'

        if syllable == '𐑳' and final != '':
            syllable = '𐑩'

        output[index + joinsPrevious] = syllable

        #marks whether the next syllable will explicitly connect or not
        if joinsNext:
            output.append('{^}')
        else:
            output.append('')

    output = ''.join(output).replace('𐑘𐑵', '𐑿').replace('𐑘𐑿', '𐑿')

    return output
