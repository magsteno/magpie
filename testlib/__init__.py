#### magpielib, tools for converting steno into shavian and shavian into latin

# used to get a list of active dictionaries to pull prefixed terms froms
from plover import config
from typing import Tuple
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
        '𐑕': '𐑕', '𐑕𐑐': '𐑕𐑐', '𐑕𐑐𐑣𐑮': '𐑕𐑐𐑤', '𐑕𐑐𐑮': '𐑕𐑐𐑮', '𐑕𐑑': '𐑕𐑑', '𐑕𐑑𐑮': '𐑕𐑑𐑮', '𐑕𐑒': '𐑕𐑒', '𐑕𐑒𐑣𐑮': '𐑕𐑒𐑤', '𐑕𐑒𐑮': '𐑕𐑒𐑮', '𐑕𐑒𐑢': '𐑕𐑒𐑢', '𐑕𐑑𐑐': '𐑕𐑓', '𐑕𐑢': '𐑕𐑢', '𐑕𐑣𐑮': '𐑕𐑤', '𐑕𐑐𐑣': '𐑕𐑥', '𐑕𐑑𐑐𐑣': '𐑕𐑯', '𐑕𐑮': '𐑟',
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
        '𐑐𐑜𐑟': '𐑠', '𐑐𐑚𐑜𐑛': '𐑠𐑛', '𐑐𐑜𐑛': '𐑠𐑛', '𐑐𐑚𐑜𐑛𐑟': '𐑠𐑛𐑟', '𐑐𐑜𐑛𐑟': '𐑠𐑛𐑟',
        '𐑐𐑤𐑜': '𐑗', '𐑐𐑤𐑜𐑑': '𐑗𐑑', '𐑐𐑤𐑜𐑑𐑕': '𐑗𐑑𐑕', '𐑐𐑤𐑜𐑑𐑛': '𐑗𐑔', '𐑐𐑤𐑜𐑑𐑛𐑟': '𐑗𐑔𐑕',
        '𐑐𐑚𐑤𐑜': '𐑡', '𐑐𐑤𐑜𐑟': '𐑡', '𐑐𐑚𐑤𐑜𐑛': '𐑡𐑛', '𐑐𐑤𐑜𐑛': '𐑡𐑛', '𐑐𐑚𐑤𐑜𐑛𐑟': '𐑡𐑛𐑟', '𐑐𐑤𐑜𐑛𐑟': '𐑡𐑛𐑟', '𐑐𐑚𐑤𐑜𐑑𐑛': '𐑡𐑔', '𐑐𐑚𐑤𐑜𐑑𐑛𐑟': '𐑡𐑔𐑕',
        '𐑐𐑚': '𐑙', '𐑐𐑚𐑛': '𐑙𐑛', '𐑐𐑚𐑛𐑟': '𐑙𐑛𐑟', '𐑐𐑚𐑜': '𐑙𐑒', '𐑐𐑚𐑜𐑑': '𐑙𐑒𐑑', '𐑐𐑚𐑜𐑑𐑕': '𐑙𐑒𐑑𐑕', '𐑐𐑚𐑜𐑑𐑛': '𐑙𐑒𐑔', '𐑐𐑚𐑜𐑑𐑛𐑟': '𐑙𐑒𐑔𐑕', '𐑐𐑚𐑜𐑕': '𐑙𐑒𐑕', '𐑐𐑚𐑜𐑕𐑛': '𐑙𐑒𐑕𐑑', '𐑐𐑚𐑜𐑕𐑛𐑟': '𐑙𐑒𐑕𐑑𐑕', '𐑓𐑜': '𐑙𐑜', '𐑓𐑜𐑛': '𐑙𐑜𐑛', '𐑓𐑜𐑛𐑟': '𐑙𐑜𐑛𐑟', '𐑓𐑜𐑟': '𐑙𐑜𐑟', '𐑐𐑚𐑑𐑛': '𐑙𐑔', '𐑐𐑚𐑑𐑛𐑟': '𐑙𐑔𐑕', '𐑐𐑚𐑕': '𐑙𐑕', '𐑐𐑚𐑕𐑛': '𐑙𐑕𐑑', '𐑐𐑚𐑕𐑛𐑟': '𐑙𐑕𐑑𐑕', '𐑐𐑚𐑟': '𐑙𐑟',
        '𐑤': '𐑤', '𐑓𐑮𐑐': '𐑤𐑐', '𐑓𐑮𐑐𐑑': '𐑤𐑐𐑑', '𐑓𐑮𐑐𐑑𐑕': '𐑤𐑐𐑑𐑕', '𐑓𐑮𐑐𐑕': '𐑤𐑐𐑕', '𐑓𐑮𐑐𐑕𐑛': '𐑤𐑐𐑕𐑑', '𐑓𐑮𐑐𐑚': '𐑤𐑚', '𐑓𐑮𐑐𐑚𐑛': '𐑤𐑚𐑛', '𐑓𐑮𐑐𐑚𐑟': '𐑤𐑚𐑟',
        '𐑤𐑑': '𐑤𐑑', '𐑤𐑑𐑕': '𐑤𐑑𐑕', '𐑤𐑑𐑕𐑛': '𐑤𐑑𐑕𐑑', '𐑤𐑛': '𐑤𐑛', '𐑓𐑮𐑤𐑜': '𐑤𐑛', '𐑤𐑛𐑟': '𐑤𐑛𐑟', '𐑓𐑮𐑤𐑜𐑟': '𐑤𐑛𐑟',
        '𐑓𐑮𐑚𐑜': '𐑤𐑒', '𐑓𐑮𐑚𐑜𐑑': '𐑤𐑒𐑑', '𐑓𐑮𐑚𐑜𐑑𐑕': '𐑤𐑒𐑑𐑕', '𐑓𐑮𐑚𐑜𐑕': '𐑤𐑒𐑕', '𐑓𐑮𐑚𐑜𐑕𐑛': '𐑤𐑒𐑕𐑑', '𐑓𐑮𐑜': '𐑤𐑜', '𐑓𐑮𐑜𐑛': '𐑤𐑜𐑛', '𐑓𐑮𐑜𐑟': '𐑤𐑜𐑟',
        '𐑓𐑮𐑐𐑤': '𐑤𐑓', '𐑓𐑮𐑐𐑤𐑑': '𐑤𐑓𐑑', '𐑓𐑮𐑐𐑤𐑑𐑕': '𐑤𐑓𐑑𐑕', '𐑓𐑮𐑐𐑤𐑑𐑛': '𐑤𐑓𐑔', '𐑓𐑮𐑐𐑤𐑑𐑛𐑟': '𐑤𐑓𐑔𐑕', '𐑓𐑮𐑐𐑤𐑕': '𐑤𐑓𐑕', '𐑓𐑮𐑐𐑤𐑕𐑛': '𐑤𐑓𐑕𐑑', '𐑓𐑮𐑐𐑚𐑤': '𐑤𐑝', '𐑓𐑮𐑐𐑚𐑤𐑛': '𐑤𐑝𐑛', '𐑓𐑮𐑐𐑚𐑤𐑟': '𐑤𐑝𐑟',
        '𐑓𐑮𐑤': '𐑤𐑔', '𐑓𐑮𐑤𐑑': '𐑤𐑔𐑑', '𐑓𐑮𐑤𐑑𐑕': '𐑤𐑔𐑑𐑕', '𐑓𐑮𐑤𐑕': '𐑤𐑔𐑕', '𐑓𐑮𐑤𐑕𐑛': '𐑤𐑔𐑕𐑑',
        '𐑤𐑕': '𐑤𐑕', '𐑤𐑕𐑛': '𐑤𐑕𐑑', '𐑤𐑟': '𐑤𐑟', '𐑓𐑮𐑚𐑕': '𐑤𐑟', '𐑓𐑮𐑚𐑤𐑜': '𐑤𐑟𐑛', '𐑓𐑮𐑚𐑕𐑛': '𐑤𐑟𐑛',
        '𐑓𐑮𐑐𐑜': '𐑤𐑖', '𐑓𐑮𐑐𐑜𐑑': '𐑤𐑖𐑑', '𐑓𐑮𐑐𐑚𐑜': '𐑤𐑠', '𐑓𐑮𐑐𐑚𐑜𐑛': '𐑤𐑠𐑛',
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
        '𐑮𐑐𐑜': '𐑖', '𐑮𐑚𐑜𐑑': '𐑖𐑑', '𐑮𐑐𐑚𐑜': '𐑠', '𐑮𐑐𐑚𐑜𐑛': '𐑠𐑛', '𐑮𐑐𐑜𐑛': '𐑠𐑛',
        '𐑮𐑐𐑤𐑜': '𐑗', '𐑮𐑐𐑤𐑜𐑑': '𐑗𐑑', '𐑮𐑐𐑚𐑤𐑜': '𐑡', '𐑮𐑐𐑚𐑤𐑜𐑛': '𐑡𐑛',
        '𐑮𐑤': '𐑤', '𐑮𐑤𐑛': '𐑤𐑛', '𐑮𐑤𐑛𐑟': '𐑤𐑛𐑟', '𐑮𐑤𐑟': '𐑤𐑟',
        '𐑓𐑮𐑚': '𐑥', '𐑓𐑮𐑚𐑛': '𐑥𐑛', '𐑓𐑮𐑚𐑟': '𐑥𐑟', '𐑮𐑐𐑚': '𐑯', '𐑮𐑐𐑚𐑑': '𐑯𐑑', '𐑮𐑐𐑚𐑑𐑕': '𐑯𐑑𐑕', '𐑮𐑐𐑚𐑛': '𐑯𐑛', '𐑮𐑐𐑚𐑕': '𐑯𐑕', '𐑮𐑐𐑚𐑟': '𐑯𐑟',
        '𐑨': '𐑸', '𐑪': '𐑹', '𐑧': '𐑺', '𐑳': '𐑻', '*': '𐑼', '*𐑳': '𐑼', '𐑨𐑪𐑧𐑳': '𐑽', '𐑧𐑳': '𐑽', '𐑨𐑪': '𐑫𐑼', '𐑨𐑪*': '𐑘𐑫𐑼', '*𐑧𐑳': '𐑘𐑼'}
}

# === dictionary functions ===
def comparejsons():
    import plover

    # reload and compare current plover config to 'briefsDict'
    currentconfig.load()
    enabledjsons = [path for (path, enabled) in currentconfig.__getitem__('dictionaries') if path.endswith('json') and enabled]
    if enabledjsons != currentjsons:
        reloadjsons(enabledjsons)

def reloadjsons(current = [path for (path, enabled) in currentconfig.__getitem__('dictionaries') if path.endswith('json') and enabled]):
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

def reloaddicts():
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
                tsvdir = '.\\shavian\\' + tsvdir
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
### returns $first, changing a final 𐑩 to an 𐑫 if $last starts with a vowel
def schwu(first,last):
    import re
    if first[-1:] == '𐑩' and re.match('[𐑦-𐑭,𐑰-𐑾]', last[:1]) is not None:
        return first[:-1] + '𐑫'
    else: return first

### searches for $stroke in strokesDict, returning None if not found
# latinOut = True will return latin spelling if available
def briefsDict_search(stroke, latinOut = False, standard = False):
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
def parse_joiners(shav, groups = ('0', '1', '2', '3', '4')):
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
    return sections


# === conversion functions for steno dictionaries ===
### '𐑕𐑑𐑒𐑣𐑮𐑨𐑪𐑧𐑚𐑟' to '𐑜𐑤𐑱𐑟'
def stroke_to_shav(stroke: str) -> str:
    import re

    # === segmenting strokes for searching and parsing ===
    # to make 𐑒𐑢𐑮 pass the regex
    if stroke == '𐑒𐑢𐑮': stroke += '-'

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

    # -TZ - alternative joiner (like #)
    if final.replace('𐑮','') == '𐑑𐑟':
        joinsNext = True
        final = final.replace('𐑑𐑟','')

    # determines rhoticity
    if final in list(strokesDict['rhotic'].keys()):
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


    # === conversion from steno to raw shavian (illegal strokes will raise KeyError) ===
    shav = strokesDict['initials'][initial] + strokesDict[rhoticity][vowel] + strokesDict[rhoticity][final]


    # === determination of word boundaries ===
    #if vowel is schwa or schwi, or 𐑾/𐑽 as a suffix, then {^} at start of syllable
    if (
        any(s in shav for s in '𐑩𐑼𐑾𐑽')
        and not (
            any(v in shav for v in '𐑧𐑫')
            or (len(vowel) > 3)
            or (vowel == '*' and joinsNext)
        )
    ) or initial == '𐑦':
        if vowel == '*' and final == '':
            raise KeyError('* cannot end a word (try *U)')
        shav = '{^}' + shav

    if joinsNext:
        shav += '{^}'

    return(shav)


### ('#𐑑𐑐*', '𐑑𐑐𐑣𐑧𐑑', '𐑒𐑢𐑮-𐑚𐑜𐑕') into '𐑓𐑩𐑯𐑧𐑑𐑦𐑒𐑕'
def steno_to_shav(steno: Tuple[str], standard = False) -> str:
    output = None

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

        # == update previous and commit to output if strokes connect ==
        previous[0] = schwu(previous[0], syllable[1] or '')
        # if joiner at end of $previous or start of $syllable
        if previous[1] or syllable[0]:
            # adds syllable to output without intermediary joiners; None -> ''
            output = ''.join([(x or '') for x in previous[:bool(output)] + syllable[bool(output):]])
        else:
            raise KeyError('Word boundary within outline')

    if standard:
        output = parse_joiners(output, ('012', '3', '4'))
        if output[1] in standardise:
            output = standardise[output[1]][bool(variant)]
            if variant:
                variant -= 1
        output = ''.join([(x or '') for x in output])

    return output, variant

def shav_to_latin(shav: str, variant: int = 0) -> str:
    output = parse_joiners(shav, ('012', '3', '4'))
    output[1] = latin[output[1]]
    if variant >= len(output[1]):
        raise KeyError('No such variant')
    output[1] = output[1][variant]
    return ''.join([(x or '') for x in output])
