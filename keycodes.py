BYTES_MAGNIFIER = 0x1
BYTES_SCREEN_OFF = 0x100
BYTES_WIRELESS = 0x200
BYTES_SCREEN_OUTPUT = 0x400
BYTES_HIBERNATE = 0x800
BYTES_BRIGHTNESS_UP = 0x1000
BYTES_BRIGHTNESS_DOWN = 0x2000
BYTES_ACCESS_IBM = 0x4000
BYTES_VOLUME_UP = 0x10000
BYTES_VOLUME_DOWN = 0x20000
BYTES_VOLUME_MUTE = 0x40000

# Modifier masks - used for the first byte in the HID report.
# NOTE: The second byte in the report is reserved, b'\x00'

KEY_MOD_LCTRL = b'\x01'
KEY_MOD_LSHIFT = b'\x02'
KEY_MOD_LALT = b'\x04'
KEY_MOD_LMETA = b'\x08'
KEY_MOD_RCTRL = b'\x10'
KEY_MOD_RSHIFT = b'\x20'
KEY_MOD_RALT = b'\x40'
KEY_MOD_RMETA = b'\x80'

# Scan codes - last N slots in the HID report (usually 6).
# b'\x00' if no key pressed.

# If more than N keys are pressed, the HID reports
# KEY_ERR_OVF in all slots to indicate this condition.

KEY_NONE = b'\x00'  # No key pressed
# Keyboard Error Roll Over - used for all slots if too many keys are pressed ("Phantom key")
KEY_ERR_OVF = b'\x01'
KEY_POST_FAIL = b'\x02'  # Keyboard POST Fail
KEY_ERROR_UNDEFINED = b'\x03'  # Keyboard Error Undefined
KEY_A = b'\x04'  # Keyboard a and A
KEY_B = b'\x05'  # Keyboard b and B
KEY_C = b'\x06'  # Keyboard c and C
KEY_D = b'\x07'  # Keyboard d and D
KEY_E = b'\x08'  # Keyboard e and E
KEY_F = b'\x09'  # Keyboard f and F
KEY_G = b'\x0a'  # Keyboard g and G
KEY_H = b'\x0b'  # Keyboard h and H
KEY_I = b'\x0c'  # Keyboard i and I
KEY_J = b'\x0d'  # Keyboard j and J
KEY_K = b'\x0e'  # Keyboard k and K
KEY_L = b'\x0f'  # Keyboard l and L
KEY_M = b'\x10'  # Keyboard m and M
KEY_N = b'\x11'  # Keyboard n and N
KEY_O = b'\x12'  # Keyboard o and O
KEY_P = b'\x13'  # Keyboard p and P
KEY_Q = b'\x14'  # Keyboard q and Q
KEY_R = b'\x15'  # Keyboard r and R
KEY_S = b'\x16'  # Keyboard s and S
KEY_T = b'\x17'  # Keyboard t and T
KEY_U = b'\x18'  # Keyboard u and U
KEY_V = b'\x19'  # Keyboard v and V
KEY_W = b'\x1a'  # Keyboard w and W
KEY_X = b'\x1b'  # Keyboard x and X
KEY_Y = b'\x1c'  # Keyboard y and Y
KEY_Z = b'\x1d'  # Keyboard z and Z

KEY_1 = b'\x1e'  # Keyboard 1 and !
KEY_2 = b'\x1f'  # Keyboard 2 and @
KEY_3 = b'\x20'  # Keyboard 3 and #
KEY_4 = b'\x21'  # Keyboard 4 and $
KEY_5 = b'\x22'  # Keyboard 5 and %
KEY_6 = b'\x23'  # Keyboard 6 and ^
KEY_7 = b'\x24'  # Keyboard 7 and &
KEY_8 = b'\x25'  # Keyboard 8 and *
KEY_9 = b'\x26'  # Keyboard 9 and (
KEY_0 = b'\x27'  # Keyboard 0 and )

KEY_ENTER = b'\x28'  # Keyboard Return (ENTER)
KEY_ESC = b'\x29'  # Keyboard ESCAPE
KEY_BACKSPACE = b'\x2a'  # Keyboard DELETE (Backspace)
KEY_TAB = b'\x2b'  # Keyboard Tab
KEY_SPACE = b'\x2c'  # Keyboard Spacebar
KEY_MINUS = b'\x2d'  # Keyboard - and _
KEY_EQUAL = b'\x2e'  # Keyboard = and +
KEY_LEFTBRACE = b'\x2f'  # Keyboard [ and {
KEY_RIGHTBRACE = b'\x30'  # Keyboard ] and }
KEY_BACKSLASH = b'\x31'  # Keyboard \ and |
KEY_HASHTILDE = b'\x32'  # Keyboard Non-US # and ~
KEY_SEMICOLON = b'\x33'  # Keyboard ; and :
KEY_APOSTROPHE = b'\x34'  # Keyboard ' and "
KEY_GRAVE = b'\x35'  # Keyboard ` and ~
KEY_COMMA = b'\x36'  # Keyboard , and <
KEY_DOT = b'\x37'  # Keyboard . and >
KEY_SLASH = b'\x38'  # Keyboard / and ?
KEY_CAPSLOCK = b'\x39'  # Keyboard Caps Lock

KEY_F1 = b'\x3a'  # Keyboard F1
KEY_F2 = b'\x3b'  # Keyboard F2
KEY_F3 = b'\x3c'  # Keyboard F3
KEY_F4 = b'\x3d'  # Keyboard F4
KEY_F5 = b'\x3e'  # Keyboard F5
KEY_F6 = b'\x3f'  # Keyboard F6
KEY_F7 = b'\x40'  # Keyboard F7
KEY_F8 = b'\x41'  # Keyboard F8
KEY_F9 = b'\x42'  # Keyboard F9
KEY_F10 = b'\x43'  # Keyboard F10
KEY_F11 = b'\x44'  # Keyboard F11
KEY_F12 = b'\x45'  # Keyboard F12

KEY_SYSRQ = b'\x46'  # Keyboard Print Screen
KEY_SCROLLLOCK = b'\x47'  # Keyboard Scroll Lock
KEY_PAUSE = b'\x48'  # Keyboard Pause
KEY_INSERT = b'\x49'  # Keyboard Insert
KEY_HOME = b'\x4a'  # Keyboard Home
KEY_PAGEUP = b'\x4b'  # Keyboard Page Up
KEY_DELETE = b'\x4c'  # Keyboard Delete Forward
KEY_END = b'\x4d'  # Keyboard End
KEY_PAGEDOWN = b'\x4e'  # Keyboard Page Down
KEY_RIGHT = b'\x4f'  # Keyboard Right Arrow
KEY_LEFT = b'\x50'  # Keyboard Left Arrow
KEY_DOWN = b'\x51'  # Keyboard Down Arrow
KEY_UP = b'\x52'  # Keyboard Up Arrow

KEY_NUMLOCK = b'\x53'  # Keyboard Num Lock and Clear
KEY_KPSLASH = b'\x54'  # Keypad /
KEY_KPASTERISK = b'\x55'  # Keypad *
KEY_KPMINUS = b'\x56'  # Keypad -
KEY_KPPLUS = b'\x57'  # Keypad +
KEY_KPENTER = b'\x58'  # Keypad ENTER
KEY_KP1 = b'\x59'  # Keypad 1 and End
KEY_KP2 = b'\x5a'  # Keypad 2 and Down Arrow
KEY_KP3 = b'\x5b'  # Keypad 3 and PageDn
KEY_KP4 = b'\x5c'  # Keypad 4 and Left Arrow
KEY_KP5 = b'\x5d'  # Keypad 5
KEY_KP6 = b'\x5e'  # Keypad 6 and Right Arrow
KEY_KP7 = b'\x5f'  # Keypad 7 and Home
KEY_KP8 = b'\x60'  # Keypad 8 and Up Arrow
KEY_KP9 = b'\x61'  # Keypad 9 and Page Up
KEY_KP0 = b'\x62'  # Keypad 0 and Insert
KEY_KPDOT = b'\x63'  # Keypad . and Delete

KEY_102ND = b'\x64'  # Keyboard Non-US \ and |
KEY_COMPOSE = b'\x65'  # Keyboard Application
KEY_POWER = b'\x66'  # Keyboard Power
KEY_KPEQUAL = b'\x67'  # Keypad =

KEY_F13 = b'\x68'  # Keyboard F13
KEY_F14 = b'\x69'  # Keyboard F14
KEY_F15 = b'\x6a'  # Keyboard F15
KEY_F16 = b'\x6b'  # Keyboard F16
KEY_F17 = b'\x6c'  # Keyboard F17
KEY_F18 = b'\x6d'  # Keyboard F18
KEY_F19 = b'\x6e'  # Keyboard F19
KEY_F20 = b'\x6f'  # Keyboard F20
KEY_F21 = b'\x70'  # Keyboard F21
KEY_F22 = b'\x71'  # Keyboard F22
KEY_F23 = b'\x72'  # Keyboard F23
KEY_F24 = b'\x73'  # Keyboard F24

KEY_OPEN = b'\x74'  # Keyboard Execute
KEY_HELP = b'\x75'  # Keyboard Help
KEY_PROPS = b'\x76'  # Keyboard Menu
KEY_FRONT = b'\x77'  # Keyboard Select
KEY_STOP = b'\x78'  # Keyboard Stop
KEY_AGAIN = b'\x79'  # Keyboard Again
KEY_UNDO = b'\x7a'  # Keyboard Undo
KEY_CUT = b'\x7b'  # Keyboard Cut
KEY_COPY = b'\x7c'  # Keyboard Copy
KEY_PASTE = b'\x7d'  # Keyboard Paste
KEY_FIND = b'\x7e'  # Keyboard Find
KEY_MUTE = b'\x7f'  # Keyboard Mute
KEY_VOLUMEUP = b'\x80'  # Keyboard Volume Up
KEY_VOLUMEDOWN = b'\x81'  # Keyboard Volume Down
KEY_LOCKING_CAPSLOCK = b'\x82'  # Keyboard Locking Caps Lock
KEY_LOCKING_NUMLOCK = b'\x83'  # Keyboard Locking Num Lock
KEY_LOCKING_SCROLLLOCK = b'\x84'  # Keyboard Locking Scroll Lock
KEY_KPCOMMA = b'\x85'  # Keypad Comma
KEY_PAD_EQUAL = b'\x86'  # Keypad Equal Sign
KEY_RO = b'\x87'  # Keyboard International1
KEY_KATAKANAHIRAGANA = b'\x88'  # Keyboard International2
KEY_YEN = b'\x89'  # Keyboard International3
KEY_HENKAN = b'\x8a'  # Keyboard International4
KEY_MUHENKAN = b'\x8b'  # Keyboard International5
KEY_KPJPCOMMA = b'\x8c'  # Keyboard International6
KEY_INTERNATIONAL7 = b'\x8d'  # Keyboard International7
KEY_INTERNATIONAL8 = b'\x8e'  # Keyboard International8
KEY_INTERNATIONAL9 = b'\x8f'  # Keyboard International9
KEY_HANGEUL = b'\x90'  # Keyboard LANG1
KEY_HANJA = b'\x91'  # Keyboard LANG2
KEY_KATAKANA = b'\x92'  # Keyboard LANG3
KEY_HIRAGANA = b'\x93'  # Keyboard LANG4
KEY_ZENKAKUHANKAKU = b'\x94'  # Keyboard LANG5
KEY_LANG6 = b'\x95'  # Keyboard LANG6
KEY_LANG7 = b'\x96'  # Keyboard LANG7
KEY_LANG8 = b'\x97'  # Keyboard LANG8
KEY_LANG9 = b'\x98'  # Keyboard LANG9
KEY_ALTERNATE_ERASE = b'\x99'  # Keyboard Alternate Erase
KEY_SYSREQ_ATTENTION = b'\x9a'  # Keyboard SysReq/Attention
KEY_CANCEL = b'\x9b'  # Keyboard Cancel
KEY_CLEAR = b'\x9c'  # Keyboard Clear
KEY_PRIOR = b'\x9d'  # Keyboard Prior
KEY_RETURN = b'\x9e'  # Keyboard Return
KEY_SEPARATOR = b'\x9f'  # Keyboard Separator
KEY_OUT = b'\xa0'  # Keyboard Out
KEY_OPER = b'\xa1'  # Keyboard Oper
KEY_CLEAR_AGAIN = b'\xa2'  # Keyboard Clear/Again
KEY_CRSEL_PROPS = b'\xa3'  # Keyboard CrSel/Props
KEY_EXSEL = b'\xa4'  # Keyboard ExSel

KEY_KP00 = b'\xb0'  # KEYPAD 00 = b'\xb0' # Keypad 00
KEY_KP000 = b'\xb1'  # Keypad 000
KEY_THOUSANDS_SEPARATOR = b'\xb2'  # Thousands Separator
KEY_DECIMAL_SEPARATOR = b'\xb3'  # Decimal Separator
KEY_CURRENCY_UNIT = b'\xb4'  # Currency Unit
KEY_CURRENCY_SUB_UNIT = b'\xb5'  # Currency Sub-unit
KEY_KPLEFTPAREN = b'\xb6'  # Keypad (
KEY_KPRIGHTPAREN = b'\xb7'  # Keypad )
KEY_KPLEFTBRACKET = b'\xb8'  # Keypad {
KEY_KPRIGHTBRACKET = B'\xb9'  # KEYPAD } = b'\xb9' # Keypad }
KEY_KPTAB = b'\xba'  # KEYPAD TAB = b'\xba' # Keypad Tab
KEY_KPBACKSPACE = b'\xbb'  # Keypad Backspace
KEY_KPA = b'\xbc'  # Keypad A
KEY_KPB = b'\xbd'  # KEYPAD B = b'\xbd' # Keypad B
KEY_KPC = b'\xbe'  # KEYPAD C = b'\xbe' # Keypad C
KEY_KPD = b'\xbf'  # KEYPAD D = b'\xbf' # Keypad D
KEY_KPE = b'\xc0'  # KEYPAD E = b'\xc0' # Keypad E
KEY_KPF = b'\xc1'  # KEYPAD F = b'\xc1' # Keypad F
KEY_KPXOR = b'\xc2'  # KEYPAD XOR = b'\xc2' # Keypad XOR
KEY_KPOR = b'\xc3'  # Keypad ^
KEY_KPPERCENT = b'\xc4'  # KEYPAD % = b'\xc4' # Keypad %
KEY_KPLESS = b'\xc5'  # KEYPAD < = b'\xc5' # Keypad <
KEY_KPGREAT = b'\xc6'  # KEYPAD > = b'\xc6' # Keypad >
KEY_KPAND = b'\xc7'  # KEYPAD & = b'\xc7' # Keypad &
KEY_KPANDAND = b'\xc8'  # KEYPAD && = b'\xc8' # Keypad &&
KEY_KPOR = b'\xc9'  # Keypad |
KEY_KPOROR = b'\xca'  # KEYPAD || = b'\xca' # Keypad ||
KEY_KPCOLON = b'\xcb'  # Keypad :
KEY_KPHASHTAG = b'\xcc'  # KEYPAD # = b'\xcc' # Keypad #
KEY_KPSPACE = b'\xcd'  # KEYPAD SPACE = b'\xcd' # Keypad Space
KEY_KPAT = b'\xce'  # Keypad @
KEY_KPEXCLAIM = b'\xcf'  # KEYPAD ! = b'\xcf' # Keypad !
KEY_KPMEMORYSTORE = b'\xd0'  # KEYPAD MEMORY STORE = b'\xd0' # Keypad Memory Store
KEY_KPMEMORYRECALL = b'\xd1'  # Keypad Memory Recall
KEY_KPMEMORYCLEAR = b'\xd2'  # Keypad Memory Clear
KEY_KPMEMORYADD = b'\xd3'  # Keypad Memory Add
KEY_KPMEMORYSUBTRACT = b'\xd4'  # Keypad Memory Subtract
KEY_KPMEMORYMULTIPLY = b'\xd5'  # Keypad Memory Multiply
KEY_KPMEMORYDIVIDE = b'\xd6'  # Keypad Memory Divide
KEY_KPPLUSMINUS = b'\xd7'  # Keypad +/-
KEY_KPCLEAR = b'\xd8'  # Keypad Clear
KEY_KPCLEARENTRY = b'\xd9'  # Keypad Clear Entry
KEY_KPBINARY = b'\xda'  # Keypad Binary
KEY_KPOCTAL = b'\xdb'  # Keypad Octal
KEY_KPDECIMAL = b'\xdc'  # Keypad Decimal
KEY_KPHEXADECIMAL = b'\xdd'  # Keypad Hexadecimal

KEY_LEFTCTRL = b'\xe0'  # Keyboard Left Control
KEY_LEFTSHIFT = b'\xe1'  # Keyboard Left Shift
KEY_LEFTALT = b'\xe2'  # Keyboard Left Alt
KEY_LEFTMETA = b'\xe3'  # Keyboard Left GUI
KEY_RIGHTCTRL = b'\xe4'  # Keyboard Right Control
KEY_RIGHTSHIFT = b'\xe5'  # Keyboard Right Shift
KEY_RIGHTALT = b'\xe6'  # Keyboard Right Alt
KEY_RIGHTMETA = b'\xe7'  # Keyboard Right GUI

KEY_MEDIA_PLAYPAUSE = b'\xe8'
KEY_MEDIA_STOPCD = b'\xe9'
KEY_MEDIA_PREVIOUSSONG = b'\xea'
KEY_MEDIA_NEXTSONG = b'\xeb'
KEY_MEDIA_EJECTCD = b'\xec'
KEY_MEDIA_VOLUMEUP = b'\xed'
KEY_MEDIA_VOLUMEDOWN = b'\xee'
KEY_MEDIA_MUTE = b'\xef'
KEY_MEDIA_WWW = b'\xf0'
KEY_MEDIA_BACK = b'\xf1'
KEY_MEDIA_FORWARD = b'\xf2'
KEY_MEDIA_STOP = b'\xf3'
KEY_MEDIA_FIND = b'\xf4'
KEY_MEDIA_SCROLLUP = b'\xf5'
KEY_MEDIA_SCROLLDOWN = b'\xf6'
KEY_MEDIA_EDIT = b'\xf7'
KEY_MEDIA_SLEEP = b'\xf8'
KEY_MEDIA_COFFEE = b'\xf9'
KEY_MEDIA_REFRESH = b'\xfa'
KEY_MEDIA_CALC = b'\xfb'
