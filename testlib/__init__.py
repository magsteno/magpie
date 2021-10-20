#### magpielib, tools for converting steno into shavian and shavian into latin

# used to get a list of active dictionaries to pull prefixed terms froms
from plover import config
from typing import Optional, Union, Tuple, List
currentconfig = config.Config(r'.\plover.cfg')

# each chord in the strokes dictionary is assigned a specific consonant cluster or vowel. sorted loosely based on standard shavian order
# rhotic clusters lack the letter 𐑮 because these already exist in the vowel. rhotic vowels lack the R in the chord because these already exist in the final
strokesDict = {
    'initials': {'': '', '𐑦': '𐑦',
        '𐑐': '𐑐', '𐑐𐑣𐑮': '𐑐𐑤', '𐑐𐑮': '𐑐𐑮', '𐑐𐑢': '𐑚', '𐑐𐑢𐑣𐑮': '𐑚𐑤', '𐑐𐑢𐑮': '𐑚𐑮',
        '𐑑': '𐑑', '𐑑𐑢': '𐑑𐑢', '𐑑𐑮': '𐑑𐑮', '𐑑𐑒': '𐑛', '𐑑𐑒𐑢': '𐑛𐑢', '𐑑𐑒𐑮': '𐑛𐑮',
        '𐑒': '𐑒', '𐑒𐑢': '𐑒𐑢', '𐑒𐑣𐑮': '𐑒𐑤', '𐑒𐑮': '𐑒𐑮', '𐑕𐑑𐑒': '𐑜', '𐑕𐑑𐑒𐑢': '𐑜𐑢', '𐑕𐑑𐑒𐑣𐑮': '𐑜𐑤', '𐑕𐑑𐑒𐑮': '𐑜𐑮',
        '𐑑𐑐': '𐑓', '𐑑𐑐𐑣𐑮': '𐑓𐑤', '𐑑𐑐𐑮': '𐑓𐑮', '𐑑𐑐𐑢': '𐑝', '𐑑𐑐𐑢𐑮': '𐑝𐑮',
        '𐑑𐑣': '𐑔', '𐑑𐑢𐑣': '𐑔𐑢', '𐑑𐑣𐑮': '𐑔𐑮', '𐑑𐑒𐑣': '𐑞',
        '𐑕': '𐑕', '𐑕𐑐': '𐑕𐑐', '𐑕𐑐𐑣𐑮': '𐑕𐑐𐑤', '𐑕𐑐𐑮': '𐑕𐑐𐑮', '𐑕𐑑': '𐑕𐑑', '𐑕𐑑𐑮': '𐑕𐑑𐑮', '𐑕𐑒': '𐑕𐑒', '𐑕𐑒𐑣𐑮': '𐑕𐑒𐑤', '𐑕𐑒𐑮': '𐑕𐑒𐑮', '𐑕𐑒𐑢': '𐑕𐑒𐑢', '𐑕𐑑𐑐': '𐑕𐑓', '𐑕𐑒𐑢𐑮': '𐑕𐑘', '𐑕𐑢': '𐑕𐑢', '𐑕𐑣𐑮': '𐑕𐑤', '𐑕𐑐𐑣': '𐑕𐑥', '𐑕𐑑𐑐𐑣': '𐑕𐑯', '𐑕𐑮': '𐑟',
        '𐑒𐑐': '𐑖', '𐑒𐑐𐑣𐑮': '𐑖𐑤', '𐑒𐑐𐑮': '𐑖𐑮', '𐑒𐑐𐑢': '𐑠',
        '𐑑𐑒𐑐': '𐑗', '𐑑𐑒𐑐𐑢': '𐑡',
        '𐑒𐑢𐑮': '𐑘', '𐑢': '𐑢',
        '𐑕𐑑𐑒𐑐𐑣': '𐑙', '𐑕𐑑𐑒𐑐𐑢𐑣': '𐑙𐑢',
        '𐑣': '𐑣', '𐑢𐑣': '𐑣𐑢',
        '𐑣𐑮': '𐑤', '𐑮': '𐑮',
        '𐑐𐑣': '𐑥', '𐑑𐑐𐑣': '𐑯'},
    'nonrhotic': {'': '',
        '𐑐': '𐑐', '𐑐𐑑': '𐑐𐑑', '𐑐𐑑𐑕': '𐑐𐑑𐑕', '𐑐𐑑𐑛': '𐑐𐑔', '𐑐𐑑𐑛𐑟': '𐑐𐑔𐑕', '𐑐𐑕': '𐑐𐑕', '𐑐𐑕𐑛': '𐑐𐑕𐑑', '𐑐𐑚𐑑': '𐑐𐑕𐑑',
        '𐑚': '𐑚', '𐑚𐑛': '𐑚𐑛', '𐑚𐑛𐑟': '𐑚𐑛𐑟', '𐑚𐑟': '𐑚𐑟',
        '𐑑': '𐑑', '𐑤𐑑𐑛': '𐑑𐑔', '𐑤𐑑𐑛𐑟': '𐑑𐑔𐑕', '𐑑𐑕': '𐑑𐑕', '𐑑𐑕𐑛': '𐑑𐑕𐑑',
        '𐑛': '𐑛', '𐑤𐑜': '𐑛', '𐑤𐑜𐑑𐑛': '𐑛𐑔', '𐑤𐑜𐑑𐑛𐑟': '𐑛𐑔𐑕', '𐑛𐑟': '𐑛𐑟', '𐑤𐑜𐑟': '𐑛𐑟', '𐑤𐑜𐑕𐑛': '𐑛𐑟𐑛',
        '𐑚𐑜': '𐑒', '𐑚𐑜𐑑': '𐑒𐑑', '𐑜𐑑': '𐑒𐑑', '𐑚𐑜𐑑𐑕': '𐑒𐑑𐑕', '𐑜𐑑𐑕': '𐑒𐑑𐑕', '𐑚𐑜𐑑𐑛': '𐑒𐑔', '𐑚𐑜𐑑𐑛𐑟': '𐑒𐑔𐑕', '𐑚𐑜𐑕': '𐑒𐑕', '𐑜𐑕': '𐑒𐑕', '𐑚𐑜𐑕𐑛': '𐑒𐑕𐑑', '𐑜𐑕𐑛': '𐑒𐑕𐑑', '𐑚𐑜𐑕𐑛𐑟': '𐑒𐑕𐑑𐑕', '𐑜𐑕𐑛𐑟': '𐑒𐑕𐑑𐑕', '𐑚𐑜𐑑𐑕𐑛': '𐑒𐑕𐑔', '𐑜𐑑𐑕𐑛': '𐑒𐑕𐑔', '𐑚𐑜𐑑𐑕𐑛𐑟': '𐑒𐑕𐑔𐑕', '𐑜𐑑𐑕𐑛𐑟': '𐑒𐑕𐑔𐑕',
        '𐑜': '𐑜', '𐑜𐑛': '𐑜𐑛', '𐑜𐑛𐑟': '𐑜𐑛𐑟', '𐑜𐑑𐑛': '𐑜𐑔', '𐑜𐑑𐑛𐑟': '𐑜𐑔𐑕', '𐑜𐑟': '𐑜𐑟',
        '𐑓': '𐑓', '𐑓𐑑': '𐑓𐑑', '𐑓𐑑𐑕': '𐑓𐑑𐑕', '𐑓𐑑𐑛': '𐑓𐑔', '𐑓𐑑𐑛𐑟': '𐑓𐑔𐑕', '𐑓𐑕': '𐑓𐑕', '𐑓𐑕𐑛': '𐑓𐑕𐑑',
        '𐑐𐑚𐑤': '𐑝', '𐑐𐑚𐑤𐑛': '𐑝𐑛', '𐑓𐑛': '𐑝𐑛', '𐑐𐑚𐑤𐑑𐑛': '𐑝𐑔', '𐑐𐑚𐑤𐑑𐑛𐑟': '𐑝𐑔𐑕', '𐑐𐑚𐑤𐑟': '𐑝𐑟', '𐑓𐑟': '𐑝𐑟',
        '𐑑𐑛': '𐑔', '𐑓𐑤𐑑': '𐑔𐑑', '𐑓𐑤𐑑𐑕': '𐑔𐑑𐑕', '𐑓𐑤𐑕': '𐑔𐑕', '𐑑𐑛𐑟': '𐑔𐑕', '𐑓𐑤𐑕𐑛': '𐑔𐑕𐑑',
        '𐑓𐑤𐑜': '𐑞', '𐑓𐑤𐑜𐑛': '𐑞𐑛', '𐑓𐑤𐑜𐑟': '𐑞𐑟',
        '𐑕': '𐑕', '𐑓𐑐': '𐑕𐑐', '𐑓𐑐𐑕': '𐑕𐑐𐑕', '𐑓𐑐𐑕𐑛': '𐑕𐑐𐑕𐑑', '𐑓𐑐𐑑': '𐑕𐑐𐑑', '𐑓𐑐𐑑𐑕': '𐑕𐑐𐑑𐑕', '𐑕𐑛': '𐑕𐑑', '𐑚𐑑': '𐑕𐑑', '𐑕𐑛𐑟': '𐑕𐑑𐑕', '𐑚𐑑𐑕': '𐑕𐑑𐑕', '𐑓𐑚𐑜': '𐑕𐑒', '𐑓𐑚𐑜𐑑': '𐑕𐑒𐑑', '𐑓𐑚𐑜𐑑𐑕': '𐑕𐑒𐑑𐑕', '𐑓𐑚𐑜𐑕': '𐑕𐑒𐑕', '𐑓𐑚𐑜𐑕𐑛': '𐑕𐑒𐑕𐑑', '𐑚𐑑𐑛': '𐑕𐑔', '𐑚𐑑𐑛𐑟': '𐑕𐑔𐑕',
        '𐑟': '𐑟', '𐑚𐑕': '𐑟', '𐑚𐑤𐑜': '𐑟𐑛', '𐑚𐑑𐑕𐑛': '𐑟𐑔', '𐑚𐑑𐑕𐑛𐑟': '𐑟𐑔𐑕',
        '𐑐𐑜': '𐑖', '𐑐𐑜𐑑': '𐑖𐑑', '𐑐𐑜𐑑𐑕': '𐑖𐑑𐑕', '𐑐𐑜𐑑𐑛': '𐑖𐑔', '𐑐𐑜𐑑𐑛𐑟': '𐑖𐑔𐑕',
        '𐑐𐑜𐑕': '𐑠', '𐑐𐑚𐑕𐑛': '𐑠𐑛', '𐑐𐑜𐑛': '𐑠𐑛', '𐑐𐑚𐑜𐑛': '𐑠𐑛', '𐑐𐑚𐑜𐑛𐑟': '𐑠𐑛𐑟', '𐑐𐑜𐑛𐑟': '𐑠𐑛𐑟',
        '𐑐𐑤𐑜': '𐑗', '𐑐𐑤𐑜𐑑': '𐑗𐑑', '𐑐𐑤𐑜𐑑𐑕': '𐑗𐑑𐑕', '𐑐𐑤𐑜𐑑𐑛': '𐑗𐑔', '𐑐𐑤𐑜𐑑𐑛𐑟': '𐑗𐑔𐑕',
        '𐑐𐑚𐑤𐑜': '𐑡', '𐑐𐑤𐑜𐑕': '𐑡', '𐑐𐑚𐑤𐑜𐑛': '𐑡𐑛', '𐑐𐑤𐑜𐑛': '𐑡𐑛', '𐑐𐑚𐑤𐑜𐑛𐑟': '𐑡𐑛𐑟', '𐑐𐑤𐑜𐑛𐑟': '𐑡𐑛𐑟', '𐑐𐑚𐑤𐑜𐑑𐑛': '𐑡𐑔', '𐑐𐑚𐑤𐑜𐑑𐑛𐑟': '𐑡𐑔𐑕',
        '𐑐𐑚': '𐑙', '𐑐𐑚𐑛': '𐑙𐑛', '𐑐𐑚𐑛𐑟': '𐑙𐑛𐑟', '𐑐𐑚𐑜': '𐑙𐑒', '𐑐𐑚𐑜𐑑': '𐑙𐑒𐑑', '𐑐𐑚𐑜𐑑𐑕': '𐑙𐑒𐑑𐑕', '𐑐𐑚𐑜𐑑𐑛': '𐑙𐑒𐑔', '𐑐𐑚𐑜𐑑𐑛𐑟': '𐑙𐑒𐑔𐑕', '𐑐𐑚𐑜𐑕': '𐑙𐑒𐑕', '𐑐𐑚𐑜𐑕𐑛': '𐑙𐑒𐑕𐑑', '𐑐𐑚𐑜𐑕𐑛𐑟': '𐑙𐑒𐑕𐑑𐑕', '𐑓𐑜': '𐑙𐑜', '𐑓𐑜𐑛': '𐑙𐑜𐑛', '𐑓𐑜𐑛𐑟': '𐑙𐑜𐑛𐑟', '𐑓𐑜𐑟': '𐑙𐑜𐑟', '𐑐𐑚𐑑𐑛': '𐑙𐑔', '𐑐𐑚𐑑𐑛𐑟': '𐑙𐑔𐑕', '𐑐𐑚𐑕': '𐑙𐑕', '𐑐𐑚𐑕𐑛': '𐑙𐑕𐑑', '𐑐𐑚𐑕𐑛𐑟': '𐑙𐑕𐑑𐑕', '𐑐𐑚𐑟': '𐑙𐑟',
        '𐑤': '𐑤', '𐑓𐑮𐑐': '𐑤𐑐', '𐑓𐑮𐑐𐑑': '𐑤𐑐𐑑', '𐑓𐑮𐑐𐑑𐑕': '𐑤𐑐𐑑𐑕', '𐑓𐑮𐑐𐑕': '𐑤𐑐𐑕', '𐑓𐑮𐑐𐑕𐑛': '𐑤𐑐𐑕𐑑', '𐑓𐑮𐑐𐑚': '𐑤𐑚', '𐑓𐑮𐑐𐑚𐑛': '𐑤𐑚𐑛', '𐑓𐑮𐑐𐑚𐑟': '𐑤𐑚𐑟',
        '𐑤𐑑': '𐑤𐑑', '𐑤𐑑𐑕': '𐑤𐑑𐑕', '𐑤𐑑𐑕𐑛': '𐑤𐑑𐑕𐑑', '𐑤𐑛': '𐑤𐑛', '𐑓𐑮𐑤𐑜': '𐑤𐑛', '𐑤𐑛𐑟': '𐑤𐑛𐑟', '𐑓𐑮𐑤𐑜𐑟': '𐑤𐑛𐑟',
        '𐑓𐑮𐑚𐑜': '𐑤𐑒', '𐑓𐑮𐑚𐑜𐑑': '𐑤𐑒𐑑', '𐑓𐑮𐑚𐑜𐑑𐑕': '𐑤𐑒𐑑𐑕', '𐑓𐑮𐑚𐑜𐑕': '𐑤𐑒𐑕', '𐑓𐑮𐑚𐑜𐑕𐑛': '𐑤𐑒𐑕𐑑', '𐑓𐑮𐑜': '𐑤𐑜', '𐑓𐑮𐑜𐑛': '𐑤𐑜𐑛', '𐑓𐑮𐑜𐑟': '𐑤𐑜𐑟',
        '𐑓𐑮𐑐𐑤': '𐑤𐑓', '𐑓𐑮𐑐𐑤𐑑': '𐑤𐑓𐑑', '𐑓𐑮𐑐𐑤𐑑𐑕': '𐑤𐑓𐑑𐑕', '𐑓𐑮𐑐𐑤𐑑𐑛': '𐑤𐑓𐑔', '𐑓𐑮𐑐𐑤𐑑𐑛𐑟': '𐑤𐑓𐑔𐑕', '𐑓𐑮𐑐𐑤𐑕': '𐑤𐑓𐑕', '𐑓𐑮𐑐𐑤𐑕𐑛': '𐑤𐑓𐑕𐑑', '𐑓𐑮𐑐𐑚𐑤': '𐑤𐑝', '𐑓𐑮𐑐𐑚𐑤𐑛': '𐑤𐑝𐑛', '𐑓𐑮𐑐𐑚𐑤𐑟': '𐑤𐑝𐑟',
        '𐑓𐑮𐑤': '𐑤𐑔', '𐑓𐑮𐑤𐑑': '𐑤𐑔𐑑', '𐑓𐑮𐑤𐑑𐑕': '𐑤𐑔𐑑𐑕', '𐑓𐑮𐑤𐑕': '𐑤𐑔𐑕', '𐑓𐑮𐑤𐑕𐑛': '𐑤𐑔𐑕𐑑',
        '𐑤𐑕': '𐑤𐑕', '𐑤𐑕𐑛': '𐑤𐑕𐑑', '𐑤𐑟': '𐑤𐑟', '𐑓𐑮𐑚𐑕': '𐑤𐑟', '𐑓𐑮𐑚𐑤𐑜': '𐑤𐑟𐑛', '𐑓𐑮𐑚𐑕𐑛': '𐑤𐑟𐑛',
        '𐑓𐑮𐑐𐑜': '𐑤𐑖', '𐑓𐑮𐑐𐑜𐑑': '𐑤𐑖𐑑', '𐑓𐑮𐑐𐑚𐑜': '𐑤𐑠', '𐑓𐑮𐑐𐑜𐑕': '𐑤𐑠', '𐑓𐑮𐑐𐑚𐑜𐑛': '𐑤𐑠𐑛',
        '𐑓𐑮𐑐𐑤𐑜': '𐑤𐑗', '𐑓𐑮𐑐𐑤𐑜𐑑': '𐑤𐑗𐑑', '𐑓𐑮𐑐𐑚𐑤𐑜': '𐑤𐑡', '𐑓𐑮𐑐𐑚𐑤𐑜𐑛': '𐑤𐑡𐑛',
        '𐑓𐑚𐑤': '𐑤𐑥', '𐑓𐑚𐑤𐑛': '𐑤𐑥𐑛', '𐑓𐑚𐑤𐑟': '𐑤𐑥𐑟', '𐑓𐑤': '𐑤𐑯', '𐑓𐑤𐑛': '𐑤𐑯𐑛', '𐑓𐑤𐑟': '𐑤𐑯𐑟',
        '𐑓𐑚': '𐑥', '𐑓𐑐𐑚': '𐑥𐑐', '𐑓𐑐𐑚𐑑': '𐑥𐑐𐑑', '𐑓𐑐𐑚𐑑𐑕': '𐑥𐑐𐑑𐑕', '𐑓𐑐𐑚𐑕': '𐑥𐑐𐑕', '𐑓𐑐𐑚𐑕𐑛': '𐑥𐑐𐑕𐑑', '𐑓𐑐𐑚𐑤': '𐑥𐑓', '𐑓𐑐𐑚𐑤𐑕': '𐑥𐑓𐑕', '𐑓𐑐𐑚𐑤𐑕𐑛': '𐑥𐑓𐑕𐑑', '𐑓𐑐𐑚𐑤𐑑': '𐑥𐑓𐑑', '𐑓𐑐𐑚𐑤𐑑𐑕': '𐑥𐑓𐑑𐑕', '𐑓𐑚𐑑': '𐑥𐑑', '𐑓𐑚𐑑𐑕': '𐑥𐑑𐑕', '𐑓𐑚𐑛': '𐑥𐑛', '𐑓𐑚𐑛𐑟': '𐑥𐑛𐑟', '𐑓𐑚𐑑𐑛': '𐑥𐑔', '𐑓𐑚𐑑𐑛𐑟': '𐑥𐑔𐑕', '𐑓𐑚𐑟': '𐑥𐑟',
        '𐑓𐑐𐑤': '𐑯', '𐑓𐑐𐑤𐑑': '𐑯𐑑', '𐑓𐑐𐑤𐑑𐑕': '𐑯𐑑𐑕', '𐑓𐑐𐑤𐑛': '𐑯𐑛', '𐑓𐑐𐑤𐑛𐑟': '𐑯𐑛𐑟', '𐑓𐑐𐑤𐑑𐑛': '𐑯𐑔', '𐑓𐑐𐑤𐑑𐑛𐑟': '𐑯𐑔𐑕', '𐑓𐑐𐑤𐑕': '𐑯𐑕', '𐑚𐑕𐑛': '𐑯𐑕𐑑', '𐑓𐑐𐑤𐑟': '𐑯𐑟', '𐑓𐑐𐑜': '𐑯𐑖', '𐑓𐑐𐑜𐑑': '𐑯𐑖𐑑', '𐑓𐑐𐑚𐑜': '𐑯𐑠', '𐑓𐑐𐑚𐑜𐑛': '𐑯𐑠𐑛', '𐑓𐑐𐑜𐑛': '𐑯𐑠𐑛', '𐑓𐑐𐑤𐑜': '𐑯𐑗', '𐑓𐑐𐑤𐑜𐑑': '𐑯𐑗𐑑', '𐑓𐑐𐑚𐑤𐑜': '𐑯𐑡', '𐑓𐑐𐑚𐑤𐑜𐑛': '𐑯𐑡𐑛',
        '𐑧𐑳': '𐑦', '𐑨𐑪𐑧𐑳': '𐑰', '𐑧': '𐑧', '𐑨𐑪𐑧': '𐑱', '𐑨': '𐑨', '𐑨𐑪𐑳': '𐑲', '*': '𐑩', '*𐑳': '𐑩', '𐑳': '𐑳', '𐑪': '𐑪', '𐑪𐑳': '𐑴', '𐑨𐑪': '𐑫', '𐑨𐑧': '𐑵', '𐑨𐑳': '𐑬', '𐑪𐑧': '𐑶', '𐑨𐑧𐑳': '𐑭', '𐑪𐑧𐑳': '𐑷', '*𐑧': '𐑧𐑩', '𐑨𐑪*𐑧𐑳': '𐑾', '*𐑧𐑳': '𐑾', '𐑨*𐑧': '𐑿', '𐑨𐑪*': '𐑘𐑩'},
    'rhotic': {'𐑮': '',
        '𐑮𐑐': '𐑐', '𐑮𐑐𐑑': '𐑐𐑑', '𐑮𐑐𐑑𐑕': '𐑐𐑑𐑕', '𐑮𐑐𐑕': '𐑐𐑕', '𐑮𐑐𐑕𐑛': '𐑐𐑕𐑑', '𐑮𐑚': '𐑚', '𐑮𐑚𐑛': '𐑚𐑛', '𐑮𐑚𐑟': '𐑚𐑟',
        '𐑮𐑑': '𐑑', '𐑮𐑑𐑕': '𐑑𐑕', '𐑮𐑑𐑕𐑛': '𐑑𐑕𐑑', '𐑮𐑛': '𐑛', '𐑮𐑤𐑜': '𐑛', '𐑮𐑛𐑟': '𐑛𐑟', '𐑮𐑤𐑜𐑟': '𐑛𐑟',
        '𐑮𐑚𐑜': '𐑒', '𐑮𐑚𐑜𐑑': '𐑒𐑑', '𐑮𐑚𐑜𐑑𐑕': '𐑒𐑑𐑕', '𐑮𐑚𐑜𐑕': '𐑒𐑕', '𐑮𐑚𐑜𐑕𐑛': '𐑒𐑕𐑑', '𐑮𐑜': '𐑜', '𐑮𐑜𐑛': '𐑜𐑛', '𐑮𐑜𐑟': '𐑜𐑟',
        '𐑓𐑮': '𐑓', '𐑓𐑮𐑑': '𐑓𐑑', '𐑓𐑮𐑑𐑕': '𐑓𐑑𐑕', '𐑓𐑮𐑕': '𐑓𐑕', '𐑓𐑮𐑕𐑛': '𐑓𐑕𐑑', '𐑮𐑐𐑚𐑤': '𐑝', '𐑮𐑐𐑚𐑤𐑛': '𐑝𐑛', '𐑓𐑮𐑛': '𐑝𐑛', '𐑮𐑐𐑚𐑤𐑟': '𐑝𐑟', '𐑓𐑮𐑟': '𐑝𐑟',
        '𐑮𐑑𐑛': '𐑔', '𐑓𐑮𐑤𐑜𐑑': '𐑔𐑑', '𐑮𐑑𐑛𐑟': '𐑔𐑕', '𐑓𐑮𐑤𐑜𐑕': '𐑔𐑕', '𐑓𐑮𐑤𐑜': '𐑞', '𐑓𐑮𐑤𐑜𐑛': '𐑞𐑛', '𐑓𐑮𐑤𐑜𐑟': '𐑞𐑟',
        '𐑮𐑕': '𐑕', '𐑮𐑕𐑛': '𐑕𐑑', '𐑮𐑚𐑑': '𐑕𐑑', '𐑮𐑕𐑛𐑟': '𐑕𐑑𐑕', '𐑮𐑚𐑑𐑕': '𐑕𐑑𐑕', '𐑮𐑟': '𐑟', '𐑮𐑚𐑕': '𐑟', '𐑮𐑚𐑤𐑜': '𐑟𐑛', '𐑮𐑚𐑕𐑛': '𐑟𐑛',
        '𐑮𐑐𐑜': '𐑖', '𐑮𐑚𐑜𐑑': '𐑖𐑑', '𐑮𐑐𐑚𐑜': '𐑠', '𐑮𐑐𐑜𐑕': '𐑠', '𐑮𐑐𐑚𐑜𐑛': '𐑠𐑛', '𐑮𐑐𐑜𐑛': '𐑠𐑛',
        '𐑮𐑐𐑤𐑜': '𐑗', '𐑮𐑐𐑤𐑜𐑑': '𐑗𐑑', '𐑮𐑐𐑚𐑤𐑜': '𐑡', '𐑮𐑐𐑚𐑤𐑜𐑛': '𐑡𐑛',
        '𐑮𐑤': '𐑤', '𐑮𐑤𐑛': '𐑤𐑛', '𐑮𐑤𐑛𐑟': '𐑤𐑛𐑟', '𐑮𐑤𐑟': '𐑤𐑟',
        '𐑓𐑮𐑚': '𐑥', '𐑓𐑮𐑚𐑛': '𐑥𐑛', '𐑓𐑮𐑚𐑟': '𐑥𐑟', '𐑮𐑐𐑚': '𐑯', '𐑮𐑐𐑚𐑑': '𐑯𐑑', '𐑮𐑐𐑚𐑑𐑕': '𐑯𐑑𐑕', '𐑮𐑐𐑚𐑛': '𐑯𐑛', '𐑮𐑐𐑚𐑕': '𐑯𐑕', '𐑮𐑐𐑚𐑟': '𐑯𐑟',
        '𐑨': '𐑸', '𐑪': '𐑹', '𐑧': '𐑺', '𐑳': '𐑻', '*': '𐑼', '*𐑳': '𐑼', '𐑨𐑪𐑧𐑳': '𐑽', '𐑧𐑳': '𐑽', '𐑨𐑪': '𐑫𐑼', '𐑨𐑪*': '𐑘𐑫𐑼', '*𐑧𐑳': '𐑘𐑼'}
}

# === dictionary functions ===
def comparejsons() -> None:
    import plover

    # reload and compare current plover config to 'briefsDict'
    currentconfig.load()
    enabledjsons = [path for (path, enabled) in currentconfig.__getitem__('dictionaries') if path.endswith('json') and enabled]
    if enabledjsons != currentjsons:
        reloadjsons(enabledjsons)

def reloadjsons(current: List[str] = [path for (path, enabled) in currentconfig.__getitem__('dictionaries') if path.endswith('json') and enabled]) -> None:
    import json, plover
    global currentjsons, briefsDict

    currentjsons = current
    # dictionary for holding briefs
    briefsDict = {}
    # import briefsDict entries from files listed in currentjsons
    for file in currentjsons[::-1]:
        with open(file, encoding='UTF8') as briefsfile:
            filedata = briefsfile.read()
            briefsPacked = json.loads(filedata)

            # extract from the file only keys beginning with a @, add them to briefsDict
            briefsPacked = list(filter(lambda k: k[0][:1] == '@', briefsPacked.items()))
            briefsDict = {**briefsDict, **{k[1:]: v.split(',,,') for k, v in briefsPacked}}
    del filedata, briefsPacked

def reloaddicts() -> None:
    import plover, os
    global latin, standardise

    # refresh list of jsons
    currentconfig.load()

    # dictionary to hold the necessary parts of the readlex (Shavian to orthodox dicitonary) in memory
    latin = {}
    # dictionary for correcting 'steno spellings' to readlex standard
    standardise = {}
    with open('.\\shavian\\tsv.cfg') as tsvcfg:
        list = tsvcfg.readlines()
        for tsvdir in list:
            if not os.path.isabs(tsvdir):
                tsvdir = '.\\shavian\\' + tsvdir.replace('\n', '')
            with open(tsvdir, encoding='UTF8') as file:
                for line in file.readlines():
                    line = line.replace('\n','')
                    #split lines and take word and frequency data
                    split = line.split("\t")
                    orth = split[0]
                    #entries in readlex marked with * are corrections of steno spelling
                    if orth[:1] == '*':
                        sten = split[1]
                        standardise[sten] = [orth[1:], sten]
                    else:
                        shav = split[1]
                        freq = int(split[2])
                        if shav not in latin:
                            latin[shav] = {orth: freq}
                        else:
                            latin[shav][orth] = freq
        for entry in latin:
            latin[entry] = [shav for shav, freq in sorted(latin[entry].items(), key=lambda freq: freq[1], reverse=True)]
    reloadjsons()

# initial load of dictionaries
reloaddicts()



# === utilities ===
### returns a decimal value based on booleans values of items in tuple; big-endian
def binarybools(bools: tuple) -> int:
    val = 0
    for i, num in enumerate(reversed(bools)):
        val += 2**i * bool(num)
    return val

### returns $first, changing a final 𐑩 to an 𐑫 if $last starts with a vowel
def schwu(first: str, last: str) -> str:
    import re
    if first[-1:] == '𐑩' and re.match('[𐑦-𐑭,𐑰-𐑾]', last[:1]) is not None:
        return first[:-1] + '𐑫'
    else: return first

### returns $s, changing a final 𐑛 or 𐑟 with devoicing or schwa
def devoice(s: str, a: int) -> str:
    import re

    # a = 0 means no apostrophe,
    # = 1 means with apostrophe,
    # and = 2 means with apostrophe and schwa
    lb = max(0, a-1) * '(?:'
    rb = max(0, a-1) * "'?)"

    if s[-1] not in '𐑑𐑕𐑛𐑟' or not s:
        return s
    # voices 𐑕 and 𐑑 for the sake of testing
    if ord(s[-1]) < 66650:
        s = s[:-1] + chr(ord(s[-1]) + 10)

    # $vl marks exceptions to devoicing
    vl = {'𐑛': '𐑑', '𐑟': '𐑕-𐑗'}[s[-1]]
    # substitute 𐑛 or 𐑟 for 𐑑 or 𐑕 if previous letter is devoiced
    output = re.sub(f"(.+[𐑐-𐑗𐑣](?<![{vl}])'?){s[-1]}", f'\\1{vl[0]}', s)
    # remove apostrophe
    if not a and output[-2] == "'":
        output = output[:-2] + output[-1]
    # insert schwa where necessary
    output = re.sub(f'(.+?)({lb}([𐑑𐑛])|[𐑕-𐑗𐑟-𐑡]){rb}((?(3)𐑛|𐑟))$', r'\1\2𐑩\4', output)
    return output

### searches for $stroke in strokesDict, returning None if not found
# latinOut = True will return latin spelling if available
def briefsDict_search(stroke: str, latinOut: bool = False, standard: bool = False) -> Optional[str]:
    comparejsons()
    if stroke in briefsDict:
        output = briefsDict[stroke][-latinOut]
    else:
        output = None
    return output

### separates $shav into words and the joiners that surround them and returns them in a list
# '{^}cat{^} -> ['{^', '', '}', 'cat', '{^}']
# '{^cat}' -> ['{^', 'cat', '}', '', None]
# 'cat{^}' -> [None, None, None, 'cat', '{^}']
def parse_joiners(shav: Union[str, Tuple[str, ...]], groups: Tuple[str, ...] = ('0', '1', '2', '3', '4')) -> List[Union[str, None]]:
    import re

    # shav, if tuple or list, will be converted into a string, with None values ignored
    # the primary purpose of this is so the output can be fed back in
    if type(shav) != str:
        shav = ''.join([(i or '') for i in shav])
    dissect = re.match(r'^(?:({\^)([^\{\}]*)(}))?(?:{\^})*(.*?)(?:{\^})*(?<=({\^}))?$', shav).groups()
    sections = []
    # alternative groupings can be specified with $groups
    # parse_joiners('cat', ('012', '34')) == [None, 'cat']
    for combination in groups:
        sections.append(None)
        for part in combination:
            part = dissect[int(part)]
            if part is not None:
                sections[-1] = (sections[-1] or '') + part

    if len(sections) == 1:
        sections = ''.join(sections)
    return sections

fingerspelling = {
    'righthand': ['𐑮𐑚𐑜', '𐑮', '𐑚', '𐑜', '𐑓𐑮', '𐑐𐑚', '𐑤𐑜', '𐑓', '𐑐', '𐑤', '𐑓𐑐𐑤', '𐑓𐑮𐑐𐑚', '𐑐𐑚𐑤𐑜'],
    'numbers': [
        [    '0',    '0s',   '0th',  '0ths',      'zero',    'zeroes',    'zeroth',   'zeroths',
             '0',    '0𐑟',    '0𐑔',   '0𐑔𐑕',       '𐑟𐑽𐑴',      '𐑟𐑽𐑴𐑟',      '𐑟𐑽𐑴𐑔',     '𐑟𐑽𐑴𐑔𐑕'],
        [    '1',    '1s',   '1st',  '1sts',       'one',      'ones',     'first',    'firsts',
             '1',    '1𐑟',   '1𐑕𐑑',  '1𐑕𐑑𐑕',       '𐑢𐑳𐑯',      '𐑢𐑳𐑯𐑟',      '𐑓𐑻𐑕𐑑',     '𐑓𐑻𐑕𐑑𐑕'],
        [    '2',    '2s',   '2nd',  '2nds',       'two',      'twos',    'second',   'seconds',
             '2',    '2𐑟',    '2𐑛',   '2𐑛𐑟',        '𐑑𐑵',       '𐑑𐑵𐑟',    '𐑕𐑧𐑒𐑩𐑯𐑛',   '𐑕𐑧𐑒𐑩𐑯𐑛𐑟'],
        [    '3',    '3s',   '3rd',  '3rds',     'three',    'threes',     'third',    'thirds',
             '3',    '3𐑟',    '3𐑛',   '3𐑛𐑟',       '𐑔𐑮𐑰',      '𐑔𐑮𐑰𐑟',       '𐑔𐑻𐑛',      '𐑔𐑻𐑛𐑟'],
        [    '4',    '4s',   '4th',  '4ths',      'four',     'fours',    'fourth',   'fourths',
             '4',    '4𐑟',    '4𐑔',   '4𐑔𐑕',        '𐑓𐑹',       '𐑓𐑹𐑟',       '𐑓𐑹𐑔',      '𐑓𐑹𐑔𐑕'],
        [    '5',    '5s',   '5th',  '5ths',      'five',     'fives',     'fifth',    'fifths',
             '5',    '5𐑟',    '5𐑔',   '5𐑔𐑕',       '𐑓𐑲𐑝',      '𐑓𐑲𐑝𐑟',      '𐑓𐑦𐑓𐑔',     '𐑓𐑦𐑓𐑔𐑕'],
        [    '6',    '6s',   '6th',  '6ths',       'six',     'sixes',     'sixth',    'sixths',
             '6',    '6𐑟',    '6𐑔',   '6𐑔𐑕',      '𐑕𐑦𐑒𐑕',    '𐑕𐑦𐑒𐑕𐑩𐑟',     '𐑕𐑦𐑒𐑕𐑔',    '𐑕𐑦𐑒𐑕𐑔𐑕'],
        [    '7',    '7s',   '7th',  '7ths',     'seven',    'sevens',   'seventh',  'sevenths',
             '7',    '7𐑟',    '7𐑔',   '7𐑔𐑕',     '𐑕𐑧𐑝𐑩𐑯',    '𐑕𐑧𐑝𐑩𐑯𐑟',    '𐑕𐑧𐑝𐑩𐑯𐑔',   '𐑕𐑧𐑝𐑩𐑯𐑔𐑕'],
        [    '8',    '8s',   '8th',  '8ths',     'eight',    'eights',    'eighth',   'eighths',
             '8',    '8𐑟',    '8𐑔',   '8𐑔𐑕',        '𐑱𐑑',       '𐑱𐑑𐑕',       '𐑱𐑑𐑔',      '𐑱𐑑𐑔𐑕'],
        [    '9',    '9s',   '9th',  '9ths',      'nine',     'nines',     'ninth',    'ninths',
             '9',    '9𐑟',    '9𐑔',   '9𐑔𐑕',       '𐑯𐑲𐑯',      '𐑯𐑲𐑯𐑟',      '𐑯𐑲𐑯𐑔',     '𐑯𐑲𐑯𐑔𐑕'],
        [   '10',   '10s',  '10th', '10ths',       'ten',      'tens',     'tenth',    'tenths',
            '10',   '10𐑟',   '10𐑔',  '10𐑔𐑕',       '𐑑𐑧𐑯',      '𐑑𐑧𐑯𐑟',      '𐑑𐑧𐑯𐑔',     '𐑑𐑧𐑯𐑔𐑕'],
        [   '11',   '11s',  '11th', '11ths',    'eleven',   'elevens',  'eleventh', 'elevenths',
            '11',   '11𐑟',   '11𐑔',  '11𐑔𐑕',    '𐑦𐑤𐑧𐑝𐑩𐑯',   '𐑦𐑤𐑧𐑝𐑩𐑯𐑟',   '𐑦𐑤𐑧𐑝𐑩𐑯𐑔',  '𐑦𐑤𐑧𐑝𐑩𐑯𐑔𐑕'],
        [   '12',   '12s',  '12th', '12ths',    'twelve',   'twelves',   'twelfth',  'twelfths',
            '12',   '12𐑟',   '12𐑔',  '12𐑔𐑕',     '𐑑𐑢𐑧𐑤𐑝',    '𐑑𐑢𐑧𐑤𐑝𐑟',    '𐑑𐑢𐑧𐑤𐑓𐑔',   '𐑑𐑢𐑧𐑤𐑓𐑔𐑕']],
    '𐑐':  'P', '𐑚':  'B', '𐑑':  'T', '𐑛':  'D', '𐑒':  'K',  '𐑜': 'G',
    '𐑓':  'F', '𐑝':  'V', '𐑔': 'TH', '𐑞': 'DH', '𐑕':  'S', '𐑟':  'Z',
    '𐑖': 'SH', '𐑠': 'ZH', '𐑗': 'CH', '𐑡':  'J', '𐑘':  'Y', '𐑢':  'W',
    '𐑙': 'NG', '𐑣':  'H', '𐑤':  'L', '𐑮':  'R', '𐑥':  'M', '𐑯':  'N',
    '𐑧𐑳': 'I', '𐑧':  'E', '𐑨':  'A', '':   'ə', '𐑳':  'U', '𐑪':  'O',
    'exceptions': {None: None, '𐑒𐑣': 'C', '𐑒𐑢': 'Q', '𐑑𐑒𐑣𐑮': 'X'}
}
### returns a string with a number or ordinal, or with letters for fingerspelling
# ('#-𐑜') -> '3' # ('#𐑑𐑐𐑣-𐑐𐑚𐑤𐑜𐑑') -> 'twelfth'
# ('𐑑𐑐-𐑐𐑤') -> 'f' # ('𐑕𐑑𐑒𐑐𐑣*𐑐𐑤') -> 'NG' # ('#𐑒𐑐-𐑐𐑤') -> '𐑖'
def deschiffresetdeslettres(stroke: Tuple[str], latinOut: bool = False) -> Optional[str]:
    import re
    # https://regex101.com/r/e8WjLD/1
    parts = re.match(r'^(#)?([𐑕𐑑𐑒𐑐𐑢𐑣𐑮]+(?=-|\*[^𐑮]))?(?:-|([𐑨𐑪*𐑧𐑳]+(?=(𐑮))?))([𐑓𐑮𐑐𐑚𐑤𐑜]+)(𐑑)?(𐑕)?$', stroke[0])
    # if no match or too many strokes
    if len(stroke) > 1 or not parts:
        return None
    # $hash takes #, $initial takes initial consonants
    # $vowel takes vowels and *, $r takes 'R' only if vowel is present
    # $final takes final consonants, $t takes 'T', $s takes 'S'
    (hash, initial, vowel, r, final, t, s) = parts.groups()

    # -𐑐𐑤 marks fingerspelling, using # to mark shavian and * to mark capitalisation
    if final.replace('𐑮', '') == '𐑐𐑤':
        letter = None
        # if initial is present, we are fingerspelling a consonant
        if initial:
            if initial in strokesDict['initials'] and len(strokesDict['initials'][initial]) == 1:
                # the consonant is valid for shavian fingerspelling (hash marks shavian)
                letter = strokesDict['initials'][initial]
                if not hash:
                    letter = fingerspelling[letter]

            elif initial in fingerspelling['exceptions']:
                # the consonant is an exception with no shavian equivalent
                if not hash:
                    letter = fingerspelling['exceptions'][initial]

            if letter and not vowel:
                # vowel represents the * key
                letter = f'{{>}}{letter.lower()}'

        # if vowel is present, we are fingerspelling a vowel
        elif vowel:
            # if r is present, rhotic (otherwise nonrhotic)
            rhoticity = (not bool(r)) * 'non' + 'rhotic'
            if hash:
                if vowel in strokesDict[rhoticity] and len(strokesDict[rhoticity][vowel]) == 1:
                    # the vowel is valid for shavian fingerspelling
                    letter = strokesDict[rhoticity][vowel]

            elif vowel.replace('*', '') in fingerspelling:
                # when not shavian, vowel must be present in fingerspelling dictionary
                # if rhotic, an r will be placed after the vowel
                letter = fingerspelling[vowel.replace('*', '')] + bool(r) * 'r'
                if not re.fullmatch(r'(.\*|\*.*)', vowel):
                    # vowel should be lowercase if no *
                    letter = f'{{>}}{letter.lower()}'

        # attempt to wrap letter in {&} glue, else if no letter, return None
        return re.sub('({>})?(.+)', r'\1{&\2}', letter or '') or None

    # #- marks a number, optionally with N- (𐑑𐑐𐑣-) marking that it should be spelt out
    # in adition to the numbers, -𐑑 and -𐑕 can be used for ordinals and plurals
    elif hash and (initial == '𐑑𐑐𐑣' or not initial) and not vowel:
        if final in fingerspelling['righthand']:
            number = fingerspelling['righthand'].index(final)
            number = fingerspelling['numbers'][number][binarybools((not latinOut, initial, t, s))]
            #marks only single digits with {&} glue
            if not binarybools((initial, t, s)):
                number = f'{{&{number}}}'
            return number

    return None



# === conversion functions for steno dictionaries ===

### '𐑕𐑑𐑒𐑣𐑮𐑨𐑪𐑧𐑚𐑕' to '𐑜𐑤𐑱𐑟'
def stroke_to_shav(stroke: str) -> str:
    import re

    # === segmenting strokes for searching and parsing ===
    # to make 𐑒𐑢𐑮 pass the regex
    if stroke.replace('#', '') == '𐑒𐑢𐑮': stroke += '-'

    # the hash symbol is used to mark where two words join
    if stroke == '#': return '{^}'

    # split 'stroke' into syllable segments (initial, vowels, final) and if prefixed with #, mark for joining to next syllable
    dissect = re.fullmatch(r'(#?)([𐑕𐑑𐑒𐑐𐑢𐑣𐑮]*)([𐑨𐑪*𐑧𐑳-]+)([𐑓𐑮𐑐𐑚𐑤𐑜𐑑𐑕𐑛𐑟]*)', stroke)
    if dissect is None:
        raise KeyError(f'{stroke} is an nvalid stroke')
    (joinsNext, initial, vowel, final) = dissect.groups()


    # === preparation for conversion ===
    # A* = schwa attached to front of syllable
    if vowel.replace('𐑳','') == '𐑨*':
        joinsNext = True
        vowel = vowel.replace('𐑨','')

    # # -TZ - alternative joiner (like #)
    # if final.replace('𐑮','') == '𐑑𐑟':
    #     joinsNext = True
    #     final = final.replace('𐑑𐑟','')

    # determines rhoticity
    if final.replace('𐑟', '') in list(strokesDict['rhotic'].keys()):
        rhoticity = 'rhotic'
    else:
        rhoticity = 'nonrhotic'

    # converts Y- into schwi
    if initial == '𐑒𐑢𐑮' and (vowel == '-' or (rhoticity == 'nonrhotic' and vowel + strokesDict[rhoticity][final] == '*𐑕𐑑')):
        initial = '𐑦'
        if final == '𐑮':
            vowel = '*'
        elif rhoticity == 'rhotic':
            raise KeyError(f'{stroke} is an invalid stroke')
        elif vowel == '-':
            vowel = ''

    # rhotic compounds with long vowels
    compound = ''
    if rhoticity == 'rhotic' and vowel not in strokesDict['rhotic']:
        compound = strokesDict['nonrhotic'][vowel]
        vowel = '*'

    # schwaed plurals
    plural = ''
    if '𐑟' in final and final.replace('𐑟', '') in strokesDict[rhoticity]:
        pluralless = strokesDict[rhoticity][final.replace('𐑟', '')]
        if pluralless and pluralless[-1:] in '𐑕𐑟𐑖𐑠𐑗𐑡':
            final = final.replace('𐑟', '')
            plural = '𐑩𐑟'


    # === conversion from steno to raw shavian (illegal strokes will raise KeyError) ===
    shav = strokesDict['initials'][initial] + compound + strokesDict[rhoticity][vowel] + strokesDict[rhoticity][final]
    for i, j in {'𐑘𐑵': '𐑿', '𐑘𐑿': '𐑿', '𐑾𐑼': '𐑰𐑼'}.items():
        shav = shav.replace(i, j)


    # === determination of word boundaries ===
    #if vowel is schwa or schwi, or 𐑾/𐑽 as a suffix, then {^} at start of syllable
    if (
        any(s in shav for s in '𐑩𐑼𐑾𐑽')
        and not (
            any(v in shav for v in '𐑧𐑫')
            or (len(vowel) > 3)
            or (vowel == '*' and joinsNext)
        )
    ) and (not compound) or initial == '𐑦':
        if vowel == '*' and final == '':
            raise KeyError('* cannot end a word (try *U)')
        shav = '{^}' + shav

    # will except words that shouldn't be changed, like 𐑲𐑼𐑯 (𐑝· 𐑲𐑼𐑦𐑙) 𐑯 𐑚𐑶𐑙
    if shav not in latin:
        # 𐑯 to 𐑙 after rhotic compound
        shav = re.sub('(𐑽|[𐑬-𐑲𐑴-𐑷𐑿]𐑼)(𐑯)', r'\1𐑙', shav)

        # 𐑦 before 𐑙 after long vowel
        shav = re.sub('([𐑬-𐑲𐑴-𐑷𐑽𐑿]𐑼?)(𐑙)', r'\1𐑦\2', shav)

    if joinsNext:
        shav += '{^}'

    return shav + plural


### ('#𐑑𐑐*', '𐑑𐑐𐑣𐑧𐑑', '𐑒𐑢𐑮-𐑚𐑜𐑕') into '𐑓𐑩𐑯𐑧𐑑𐑦𐑒𐑕'
def steno_to_shav(steno: Tuple[str, ...], standard: bool = False) -> Tuple[Optional[str], int, bool]:
    output = None
    past = False

    # special exception for the 𐑳 -> 𐑩 brief
    if steno[-1] == '𐑳':
        raise KeyError('article, not part of stroke')

    # == separate variant markers from strokes ==
    for varindex in range(len(steno)):
        if steno[varindex] == '-𐑮𐑚' and all(chain == '-𐑮𐑚' for chain in steno[varindex:]):
            variant = len(steno) - varindex
            break
    else:
        variant = 0

    for stroke in steno[:-variant or None]:
        if output == '{^}{^}':
            raise KeyError(f'outline {steno} starts with no phonetic information')

        dz = False

        syllable = briefsDict_search(stroke)
        previous = parse_joiners(output or '{^}', ('0123','4'))

        # == convert stroke to dissected tuple ==
        # '𐑒𐑢𐑮-𐑚𐑜𐑕' to ('{^}', '𐑦𐑒𐑕', None)
        if syllable is not None: # if stroke is in strokesDict, split
            syllable = parse_joiners(syllable)
        # if stroke was not in strokesDict, or no joiners in output
        if syllable is None or syllable[0] == syllable[4]:
            stroke = stroke_to_shav(stroke)
            syllable = parse_joiners(stroke, ('012', '3', '4'))
        # else, if joiners in output (stroke is a prefix stroke)
        else:
            syllable = parse_joiners(syllable, ('02', '1', '34'))
            if any(x == syllable[1] for x in ['𐑛', '𐑟', "'𐑟"]):
                dz = True
                if syllable[1] == '𐑛':
                    past = True

        # == update previous and commit to output if strokes connect ==
        previous[0] = schwu(previous[0], syllable[1] or '')
        # if joiner at end of $previous or start of $syllable
        if previous[1] or syllable[0]:
            # adds syllable to output without intermediary joiners; None -> ''
            output = ''.join([(x or '') for x in previous[:bool(output)] + syllable[bool(output):]])
            if dz:
                output = devoice(output, 1)
        else:
            raise KeyError('Word boundary within outline')

    if standard and output is not None:
        output = parse_joiners(output, ('012', '3', '4'))
        if output[1] in standardise:
            output = standardise[output[1]][bool(variant)]
            if variant:
                variant -= 1
        output = ''.join([(x or '') for x in output])

    return output, variant, past

def shav_to_latin(shav: str, variant: int = 0, past: bool = False) -> str:
    import re
    output = parse_joiners(shav, ('012', '3', '4'))
    shav = output[1]
    output[1] = []

    if shav in latin:
        output[1] += latin[shav]

    suffixsplit = re.fullmatch('(.*?[^𐑩])(𐑩?[𐑛𐑟]|[𐑑𐑕]|𐑼𐑟?|𐑦𐑙𐑟?)$', shav)
    if suffixsplit is not None:
        (shav, suffix) = suffixsplit.groups()
        for k, v in {'𐑩?[𐑑𐑛]': 'ed', '𐑩': 'e', '𐑼': 'er', '𐑦𐑙': 'ing', '[𐑕𐑟]': 's'}.items():
            suffix = re.sub(k, v, suffix)
        if shav in latin:
            for lat in latin[shav]:
                if any(suffix.startswith(v) for v in 'aeiou'):
                    lat = re.sub('(.+)e$', r'\1', lat)
                if not any(lat + suffix == word for word in output[1]):
                    output[1].append(f"{lat}{suffix}")

    output[1] = sorted(output[1], key = lambda k: k.endswith('ed'), reverse = past)

    if variant >= len(output[1]) or len(output[1]) == 0:
        raise KeyError('No such variant')
    output[1] = output[1][variant]
    return ''.join([(x or '') for x in output])
