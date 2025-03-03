KEYS = (
    '#',
    'X-', 'B-', 'D-', 'Z-', 'G-', 'W-', 'I-', 'U-', 'N-', 'E-', 'A-', 'O-',
    '-X', '-B', '-D', '-Z', '-G', '-W', '-I', '-U', '-N', '-E', '-A', '-O',
)

IMPLICIT_HYPHEN_KEYS = ()

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'A-': '5-',
    'N-': '4-',
    'I-': '3-',
    'G-': '2-',
    'D-': '1-',
    '-D': '-6',
    '-G': '-7',
    '-I': '-8',
    '-N': '-9',
    '-A': '-0',
}

UNDO_STROKE_STENO = "W-W"

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'keyboard': {
        '#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),

        'A-': 'q',
        'O-': 'a',
        'N-': 'w',
        'E-': 's',
        'I-': 'e',
        'U-': 'd',
        'G-': 'r',
        'W-': 'f',
        'D-': 't',
        'Z-': 'g',
        'B-': 'c',
        'X-': 'v',

        '-X': 'n',
        '-B': 'm',
        '-D': 'y',
        '-Z': 'h',
        '-G': 'u',
        '-W': 'j',
        '-I': 'i',
        '-U': 'k',
        '-N': 'o',
        '-E': 'l',
        '-A': 'p',
        '-O': ';',

        'arpeggiate': 'space',
        'no-op': ('b'),
    },
    'Gemini PR': {
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),

        'A-': 'S1-',
        'O-': 'S2-',
        'N-': 'T-',
        'E-': 'K-',
        'I-': 'P-',
        'U-': 'W-',
        'G-': 'H-',
        'W-': 'R-',
        'D-': '*1',
        'Z-': '*2',
        'B-': 'A-',
        'X-': 'O-',

        '-X': '-E',
        '-B': '-U',
        '-D': '*3',
        '-Z': '*4',
        '-G': '-F',
        '-W': '-R',
        '-I': '-P',
        '-U': '-B',
        '-N': '-L',
        '-E': '-G',
        '-A': '-T',
        '-O': '-S',

        'no-op': ('-D','-Z','res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = './dictionaries/'
DEFAULT_DICTIONARIES = (
	'temp_main.json'
)
