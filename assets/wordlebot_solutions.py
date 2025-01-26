"""
Copied from view-source:https://www.nytimes.com/interactive/2022/upshot/wordle-bot.html
"""

SOLUTIONS = {
  "normal-simple": {
    "starting_word": "crane",
    "unsolved": [
      "dared",
      "dazed",
      "diked",
      "dozer",
      "eared",
      "gazed",
      "jibed",
      "lolly",
      "mixed",
      "waxed"
    ],
    "guesses": {
      "aback": [
        "plush",
        76
      ],
      "abase": [
        "sloth-usage",
        51
      ],
      "abash": [
        "spilt-awash",
        34
      ],
      "abate": [
        "sloth",
        67
      ],
      "abbey": [
        "petal-fades",
        38
      ],
      "abbot": [
        "toils-adopt",
        39
      ],
      "abhor": [
        "tyros-valor",
        42
      ],
      "abide": [
        "talus",
        59
      ],
      "abled": [
        "petal-alley-ailed",
        41
      ],
      "abode": [
        "talus-abide",
        42
      ],
      "aboil": [
        "toils",
        53
      ],
      "abort": [
        "tyros-ratio",
        42
      ],
      "about": [
        "toils-adopt",
        37
      ],
      "above": [
        "talus-abide",
        42
      ],
      "abuse": [
        "talus",
        64
      ],
      "abuzz": [
        "toils-dumpy",
        33
      ],
      "abyss": [
        "toils",
        53
      ],
      "ached": [
        "fecal-acted",
        38
      ],
      "achoo": [
        "hotly-macho",
        44
      ],
      "acing": [
        "",
        99
      ],
      "acorn": [
        "ranch",
        60
      ],
      "acrid": [
        "scram",
        70
      ],
      "acted": [
        "fecal",
        55
      ],
      "actor": [
        "scram",
        70
      ],
      "acute": [
        "sauce",
        61
      ],
      "adage": [
        "sloth-agave",
        43
      ],
      "adapt": [
        "spilt",
        73
      ],
      "added": [
        "petal-fades-aided",
        22
      ],
      "adder": [
        "tales-audit",
        53
      ],
      "addle": [
        "talus-imply",
        42
      ],
      "adept": [
        "petal",
        63
      ],
      "adieu": [
        "petal-fades",
        41
      ],
      "adios": [
        "toils",
        53
      ],
      "admin": [
        "natal-annoy",
        43
      ],
      "admit": [
        "toils-audit",
        36
      ],
      "adobe": [
        "talus-abide",
        42
      ],
      "adobo": [
        "toils-bayou",
        35
      ],
      "adopt": [
        "toils",
        49
      ],
      "adore": [
        "lairs",
        56
      ],
      "adorn": [
        "rayon",
        64
      ],
      "adult": [
        "toils-fault",
        37
      ],
      "aegis": [
        "petal-media",
        46
      ],
      "aerie": [
        "lairs",
        76
      ],
      "affix": [
        "toils-mafia",
        30
      ],
      "afire": [
        "lairs",
        76
      ],
      "afoot": [
        "toils-adopt-about",
        25
      ],
      "afore": [
        "lairs-adore",
        40
      ],
      "afoul": [
        "toils-allow",
        32
      ],
      "after": [
        "tales",
        71
      ],
      "again": [
        "slain",
        61
      ],
      "agape": [
        "sloth-agave",
        43
      ],
      "agate": [
        "sloth-abate",
        50
      ],
      "agave": [
        "sloth",
        56
      ],
      "agent": [
        "",
        91
      ],
      "agile": [
        "talus-imply",
        42
      ],
      "aging": [
        "tings",
        63
      ],
      "agita": [
        "toils",
        54
      ],
      "aglow": [
        "toils-allow",
        32
      ],
      "agony": [
        "tings-along",
        43
      ],
      "agora": [
        "tyros-amour",
        40
      ],
      "agree": [
        "lairs",
        76
      ],
      "ahead": [
        "petal",
        59
      ],
      "ahold": [
        "toils",
        53
      ],
      "aided": [
        "petal-fades",
        35
      ],
      "aider": [
        "tales-audit",
        53
      ],
      "ailed": [
        "petal-alley",
        54
      ],
      "aimed": [
        "petal-fades-adieu",
        29
      ],
      "aioli": [
        "toils-viola",
        38
      ],
      "aired": [
        "tales-audit",
        53
      ],
      "aisle": [
        "talus",
        72
      ],
      "alarm": [
        "midst",
        66
      ],
      "album": [
        "toils-allay",
        28
      ],
      "alder": [
        "tales",
        71
      ],
      "alert": [
        "tales",
        71
      ],
      "algae": [
        "talus-imply",
        42
      ],
      "alias": [
        "toils",
        53
      ],
      "alibi": [
        "toils",
        56
      ],
      "alien": [
        "sleep",
        72
      ],
      "align": [
        "natal",
        73
      ],
      "alike": [
        "talus-imply",
        37
      ],
      "alive": [
        "talus-imply-alike",
        25
      ],
      "allay": [
        "toils",
        42
      ],
      "alley": [
        "petal",
        63
      ],
      "allot": [
        "toils-float",
        43
      ],
      "allow": [
        "toils",
        45
      ],
      "alloy": [
        "toils-allow",
        32
      ],
      "aloft": [
        "toils-float",
        43
      ],
      "aloha": [
        "toils-allow-aloud",
        19
      ],
      "alone": [
        "",
        86
      ],
      "along": [
        "tings",
        59
      ],
      "aloof": [
        "toils-allow",
        32
      ],
      "aloud": [
        "toils-allow",
        32
      ],
      "alpha": [
        "toils-allay",
        28
      ],
      "altar": [
        "tyros",
        60
      ],
      "alter": [
        "tales",
        71
      ],
      "amaro": [
        "midst-alarm",
        50
      ],
      "amass": [
        "spilt-awash",
        34
      ],
      "amaze": [
        "sloth-agave-awake",
        27
      ],
      "amber": [
        "tales-audit",
        53
      ],
      "ambit": [
        "toils-audit",
        36
      ],
      "amble": [
        "talus-imply",
        42
      ],
      "amend": [
        "agent",
        66
      ],
      "amigo": [
        "toils-axiom",
        37
      ],
      "amino": [
        "tings",
        79
      ],
      "amiss": [
        "toils",
        53
      ],
      "amity": [
        "toils-agita",
        37
      ],
      "among": [
        "tings-along",
        43
      ],
      "amour": [
        "tyros",
        56
      ],
      "amped": [
        "petal-gaped",
        43
      ],
      "ample": [
        "talus-imply",
        42
      ],
      "amply": [
        "toils-madly",
        34
      ],
      "amuck": [
        "hotly-basic",
        40
      ],
      "amuse": [
        "talus-abuse",
        48
      ],
      "ancho": [
        "panic",
        74
      ],
      "angel": [
        "sleep-laden",
        46
      ],
      "anger": [
        "ramen",
        67
      ],
      "angle": [
        "gloms",
        69
      ],
      "angry": [
        "rayon",
        71
      ],
      "angst": [
        "natal",
        63
      ],
      "anime": [
        "gloms",
        69
      ],
      "anise": [
        "gloms",
        69
      ],
      "ankle": [
        "gloms",
        69
      ],
      "annal": [
        "natal",
        73
      ],
      "annex": [
        "sleep-known",
        49
      ],
      "annoy": [
        "natal",
        60
      ],
      "annul": [
        "natal-anvil",
        50
      ],
      "anode": [
        "gloms",
        69
      ],
      "anole": [
        "gloms",
        69
      ],
      "antic": [
        "panic",
        74
      ],
      "antsy": [
        "natal",
        73
      ],
      "anvil": [
        "natal",
        67
      ],
      "aorta": [
        "tyros",
        65
      ],
      "apace": [
        "scale-peace",
        45
      ],
      "apart": [
        "midst",
        64
      ],
      "aphid": [
        "toils-mafia",
        30
      ],
      "aping": [
        "tings-aging",
        53
      ],
      "apnea": [
        "sleep",
        72
      ],
      "apple": [
        "talus-imply",
        42
      ],
      "apply": [
        "toils-madly",
        34
      ],
      "apron": [
        "rayon",
        71
      ],
      "aptly": [
        "toils-fault",
        37
      ],
      "arbor": [
        "armor-ardor",
        40
      ],
      "arced": [
        "",
        99
      ],
      "ardor": [
        "armor",
        56
      ],
      "arena": [
        "",
        99
      ],
      "argon": [
        "organ",
        67
      ],
      "argot": [
        "armor",
        74
      ],
      "argue": [
        "arise",
        65
      ],
      "arise": [
        "",
        89
      ],
      "armed": [
        "tubed",
        77
      ],
      "armor": [
        "",
        88
      ],
      "aroma": [
        "armor",
        74
      ],
      "arose": [
        "arise",
        65
      ],
      "array": [
        "armor",
        74
      ],
      "arrow": [
        "armor",
        74
      ],
      "arson": [
        "organ",
        67
      ],
      "artsy": [
        "armor",
        74
      ],
      "ascot": [
        "hotly",
        75
      ],
      "ashed": [
        "petal-fades",
        35
      ],
      "ashen": [
        "sleep",
        72
      ],
      "aside": [
        "talus",
        72
      ],
      "asked": [
        "petal-fades-ashed",
        22
      ],
      "asker": [
        "tales",
        71
      ],
      "askew": [
        "petal-fades",
        38
      ],
      "aspen": [
        "sleep",
        72
      ],
      "aspic": [
        "hotly-basic",
        40
      ],
      "assay": [
        "toils-gassy",
        35
      ],
      "asset": [
        "petal",
        58
      ],
      "aster": [
        "tales",
        71
      ],
      "astir": [
        "tyros-sitar",
        46
      ],
      "atlas": [
        "toils",
        53
      ],
      "atoll": [
        "toils",
        53
      ],
      "atone": [
        "alone",
        61
      ],
      "atria": [
        "tyros",
        58
      ],
      "attic": [
        "hotly",
        75
      ],
      "audio": [
        "toils",
        54
      ],
      "audit": [
        "toils",
        53
      ],
      "auger": [
        "tales-audit",
        53
      ],
      "augur": [
        "tyros-rabid",
        33
      ],
      "aunty": [
        "natal-angst",
        46
      ],
      "aural": [
        "tyros-mural-rural",
        24
      ],
      "avail": [
        "spilt",
        56
      ],
      "avast": [
        "spilt-boast",
        42
      ],
      "avert": [
        "tales",
        66
      ],
      "avian": [
        "natal",
        73
      ],
      "avoid": [
        "toils-audio",
        38
      ],
      "await": [
        "spilt",
        73
      ],
      "awake": [
        "sloth-agave",
        39
      ],
      "award": [
        "midst-about",
        43
      ],
      "aware": [
        "aloft",
        85
      ],
      "awash": [
        "spilt",
        51
      ],
      "awful": [
        "toils-allay",
        28
      ],
      "awoke": [
        "talus-abide",
        42
      ],
      "axial": [
        "toils-alibi",
        40
      ],
      "axing": [
        "tings-aging-aping",
        41
      ],
      "axiom": [
        "toils",
        53
      ],
      "axion": [
        "natal-annoy",
        43
      ],
      "azure": [
        "lairs-adore",
        40
      ],
      "babka": [
        "toils-dumpy",
        33
      ],
      "bacon": [
        "panic",
        59
      ],
      "badge": [
        "talus-maybe",
        44
      ],
      "badly": [
        "toils-madly",
        34
      ],
      "bagel": [
        "petal",
        59
      ],
      "baggy": [
        "toils-dumpy",
        30
      ],
      "baked": [
        "petal-fades",
        41
      ],
      "baker": [
        "tales-pygmy-forks",
        41
      ],
      "baldy": [
        "toils-allay-balmy-balky",
        13
      ],
      "baled": [
        "petal-alley",
        47
      ],
      "baler": [
        "tales-paler",
        45
      ],
      "balky": [
        "toils-allay-balmy",
        23
      ],
      "balmy": [
        "toils-allay",
        28
      ],
      "balsa": [
        "toils-salad",
        30
      ],
      "banal": [
        "natal",
        73
      ],
      "bandy": [
        "natal-demos-handy",
        32
      ],
      "banjo": [
        "natal-demos",
        41
      ],
      "bared": [
        "tales-pygmy-forks-rarer",
        34
      ],
      "barer": [
        "tales-pygmy-forks-rarer",
        25
      ],
      "barge": [
        "lairs",
        76
      ],
      "baron": [
        "rayon",
        71
      ],
      "barre": [
        "lairs",
        60
      ],
      "basal": [
        "toils-salad",
        30
      ],
      "based": [
        "petal-fades-serve",
        29
      ],
      "basic": [
        "hotly",
        56
      ],
      "basil": [
        "toils",
        53
      ],
      "basin": [
        "natal-demos",
        47
      ],
      "basis": [
        "toils",
        53
      ],
      "baste": [
        "talus-whoop",
        50
      ],
      "batch": [
        "hotly-swamp",
        48
      ],
      "bated": [
        "petal-gated-shame-draft",
        38
      ],
      "bathe": [
        "talus",
        63
      ],
      "batik": [
        "toils-audit",
        36
      ],
      "baton": [
        "natal-satin",
        48
      ],
      "batty": [
        "toils-bumpy",
        34
      ],
      "bawdy": [
        "toils-dumpy",
        33
      ],
      "bayed": [
        "petal-fades-baked",
        29
      ],
      "bayou": [
        "toils",
        51
      ],
      "beach": [
        "leapt",
        72
      ],
      "beady": [
        "lefts-heady",
        44
      ],
      "beard": [
        "badly",
        80
      ],
      "beast": [
        "lefts",
        62
      ],
      "beaut": [
        "lefts",
        73
      ],
      "bebop": [
        "split-dopey",
        30
      ],
      "beech": [
        "pilot",
        57
      ],
      "beefy": [
        "split-dogma",
        34
      ],
      "befit": [
        "split-debit",
        41
      ],
      "befog": [
        "split-dogma",
        34
      ],
      "began": [
        "sleep",
        63
      ],
      "begat": [
        "petal",
        70
      ],
      "beget": [
        "split",
        50
      ],
      "begin": [
        "towel-deign",
        37
      ],
      "begot": [
        "split-beget",
        33
      ],
      "begun": [
        "towel-deign",
        37
      ],
      "beige": [
        "toils-guide",
        40
      ],
      "being": [
        "tipsy",
        53
      ],
      "belay": [
        "petal-delay",
        47
      ],
      "belch": [
        "pilot",
        71
      ],
      "belie": [
        "toils",
        57
      ],
      "belle": [
        "toils",
        58
      ],
      "belly": [
        "split",
        51
      ],
      "below": [
        "split-belly",
        34
      ],
      "bench": [
        "",
        85
      ],
      "bendy": [
        "towel-deign-needy",
        22
      ],
      "bento": [
        "towel",
        68
      ],
      "beret": [
        "betel",
        60
      ],
      "berry": [
        "betel",
        60
      ],
      "berth": [
        "betel",
        60
      ],
      "beryl": [
        "betel",
        60
      ],
      "beset": [
        "split-guest",
        37
      ],
      "besot": [
        "split-guest-beset",
        25
      ],
      "betel": [
        "split-hotel",
        32
      ],
      "bevel": [
        "split-dweeb-bezel",
        18
      ],
      "bezel": [
        "split-dweeb",
        31
      ],
      "bible": [
        "toils",
        61
      ],
      "bicep": [
        "pilot",
        71
      ],
      "biddy": [
        "sloth-dumpy-giddy",
        17
      ],
      "bided": [
        "split-edify-video",
        27
      ],
      "bidet": [
        "split-eight",
        40
      ],
      "bigot": [
        "sloth-doubt",
        29
      ],
      "biked": [
        "split-edify-video-bumpy",
        39
      ],
      "biker": [
        "betel-boxer-buyer",
        34
      ],
      "bilge": [
        "toils-belie",
        40
      ],
      "billy": [
        "sloth",
        39
      ],
      "binge": [
        "deist-hinge",
        40
      ],
      "bingo": [
        "pinot-lingo",
        47
      ],
      "biome": [
        "toils-diode",
        42
      ],
      "biped": [
        "split",
        54
      ],
      "bipod": [
        "sloth-gumbo",
        35
      ],
      "birch": [
        "soupy",
        71
      ],
      "birth": [
        "shout",
        52
      ],
      "bison": [
        "pinot",
        61
      ],
      "biter": [
        "betel",
        60
      ],
      "bitsy": [
        "sloth-midst-tipsy",
        18
      ],
      "bitty": [
        "sloth-batik",
        44
      ],
      "black": [
        "plush",
        59
      ],
      "blade": [
        "sloth-embed",
        51
      ],
      "blame": [
        "sloth-embed",
        51
      ],
      "bland": [
        "ghost",
        58
      ],
      "blank": [
        "ghost-bland",
        50
      ],
      "blare": [
        "aloft-glare",
        53
      ],
      "blase": [
        "sloth",
        75
      ],
      "blast": [
        "spilt",
        73
      ],
      "blaze": [
        "sloth-embed",
        51
      ],
      "bleak": [
        "petal",
        62
      ],
      "bleat": [
        "petal",
        70
      ],
      "bleed": [
        "split-dweeb",
        32
      ],
      "bleep": [
        "split-expel",
        39
      ],
      "blend": [
        "tipsy",
        73
      ],
      "bless": [
        "split-flesh",
        40
      ],
      "blimp": [
        "sloth-bluff",
        34
      ],
      "blind": [
        "gluts-blond",
        35
      ],
      "bling": [
        "gluts-fling",
        45
      ],
      "blink": [
        "gluts-blond",
        35
      ],
      "bliss": [
        "sloth",
        50
      ],
      "blitz": [
        "sloth",
        55
      ],
      "bloat": [
        "toils-float-gloat",
        28
      ],
      "block": [
        "spoil",
        56
      ],
      "bloke": [
        "toils-globe",
        36
      ],
      "blond": [
        "gluts",
        52
      ],
      "blood": [
        "sloth",
        48
      ],
      "bloom": [
        "sloth-blood",
        35
      ],
      "bloop": [
        "sloth-blood-bloom",
        23
      ],
      "blown": [
        "pinot-snowy",
        36
      ],
      "bluer": [
        "betel",
        60
      ],
      "bluff": [
        "sloth",
        47
      ],
      "blunt": [
        "gluts",
        66
      ],
      "blurb": [
        "shout-lurid",
        39
      ],
      "blurt": [
        "shout",
        60
      ],
      "blush": [
        "sloth-probe",
        44
      ],
      "board": [
        "midst-about",
        43
      ],
      "boast": [
        "spilt",
        59
      ],
      "bobby": [
        "sloth-gumbo",
        33
      ],
      "bocce": [
        "pious",
        71
      ],
      "boded": [
        "split-dogma-oxbow",
        27
      ],
      "boffo": [
        "sloth-gumbo",
        33
      ],
      "bogey": [
        "split-dogma",
        33
      ],
      "boggy": [
        "sloth-gumbo",
        33
      ],
      "bogie": [
        "toils-movie",
        39
      ],
      "bogus": [
        "sloth-modus",
        32
      ],
      "boing": [
        "gluts-doing",
        37
      ],
      "bolus": [
        "sloth-lousy",
        38
      ],
      "boned": [
        "towel-honey",
        41
      ],
      "boner": [
        "rites-below",
        42
      ],
      "boney": [
        "towel-honey-money",
        27
      ],
      "bongo": [
        "pinot",
        50
      ],
      "bonny": [
        "gluts-phony-downy",
        18
      ],
      "bonus": [
        "pinot-bongo",
        34
      ],
      "booby": [
        "sloth-gazed-kooky-poofy",
        17
      ],
      "booed": [
        "split-dogma-oxbow",
        27
      ],
      "boost": [
        "sloth",
        50
      ],
      "booth": [
        "sloth",
        55
      ],
      "booty": [
        "sloth",
        50
      ],
      "booze": [
        "toils-vogue",
        36
      ],
      "boozy": [
        "sloth-gazed",
        35
      ],
      "borax": [
        "tyros-moral",
        46
      ],
      "bored": [
        "betel-boxer",
        50
      ],
      "boric": [
        "soupy-torch",
        39
      ],
      "borne": [
        "",
        99
      ],
      "boron": [
        "boson",
        72
      ],
      "bosom": [
        "sloth-modus",
        32
      ],
      "boson": [
        "pinot-swoon",
        37
      ],
      "bossy": [
        "sloth-modus",
        32
      ],
      "botch": [
        "spoil-touch",
        38
      ],
      "bough": [
        "sloth-dough",
        38
      ],
      "boule": [
        "toils",
        55
      ],
      "bound": [
        "gluts-whomp",
        35
      ],
      "bowed": [
        "split-dogma-oxbow",
        27
      ],
      "bowel": [
        "split-dweeb",
        32
      ],
      "bower": [
        "betel-boxer",
        50
      ],
      "boxed": [
        "split-dogma-oxbow",
        27
      ],
      "boxer": [
        "betel",
        60
      ],
      "brace": [
        "trace-grace",
        51
      ],
      "braid": [
        "twigs-frail",
        48
      ],
      "brain": [
        "debit",
        71
      ],
      "brake": [
        "digit-brave",
        54
      ],
      "brand": [
        "gated",
        78
      ],
      "brash": [
        "twigs",
        75
      ],
      "brass": [
        "twigs",
        75
      ],
      "brava": [
        "twigs-drama",
        39
      ],
      "brave": [
        "digit",
        62
      ],
      "bravo": [
        "twigs-drama",
        39
      ],
      "brawl": [
        "twigs",
        62
      ],
      "brawn": [
        "debit",
        71
      ],
      "bread": [
        "tubed",
        77
      ],
      "break": [
        "tubed",
        62
      ],
      "bream": [
        "tubed-break",
        46
      ],
      "breed": [
        "defer-greed",
        43
      ],
      "briar": [
        "armor-friar",
        47
      ],
      "bribe": [
        "pivot-bride",
        46
      ],
      "brick": [
        "trick",
        56
      ],
      "bride": [
        "pivot",
        54
      ],
      "brief": [
        "defer-grief",
        44
      ],
      "brier": [
        "defer-truer",
        47
      ],
      "brine": [
        "prone-urine",
        46
      ],
      "bring": [
        "bigot",
        73
      ],
      "brink": [
        "bigot",
        57
      ],
      "briny": [
        "bigot-brink",
        40
      ],
      "brisk": [
        "pilot-frisk",
        36
      ],
      "broad": [
        "armor",
        74
      ],
      "broil": [
        "pilot",
        70
      ],
      "broke": [
        "pivot-beard",
        52
      ],
      "bronc": [
        "",
        99
      ],
      "brood": [
        "pilot-groom",
        41
      ],
      "brook": [
        "pilot-groom-brood",
        28
      ],
      "broom": [
        "pilot-groom",
        50
      ],
      "broth": [
        "pilot",
        62
      ],
      "brown": [
        "gibed",
        72
      ],
      "brunt": [
        "bigot",
        73
      ],
      "brush": [
        "pilot",
        59
      ],
      "brusk": [
        "pilot-brush",
        42
      ],
      "brute": [
        "pivot",
        75
      ],
      "buddy": [
        "sloth-dumpy-fudgy",
        16
      ],
      "budge": [
        "toils-fudge-judge",
        25
      ],
      "buggy": [
        "sloth-dumpy-fuzzy",
        13
      ],
      "bugle": [
        "toils-belle",
        41
      ],
      "build": [
        "sloth-billy",
        30
      ],
      "built": [
        "sloth-guilt",
        39
      ],
      "bulge": [
        "toils-dumpy",
        30
      ],
      "bulgy": [
        "sloth-billy-bulky",
        19
      ],
      "bulky": [
        "sloth-billy",
        32
      ],
      "bully": [
        "sloth-billy",
        30
      ],
      "bumpy": [
        "sloth-dumpy",
        29
      ],
      "bunch": [
        "posit-blame",
        46
      ],
      "bunny": [
        "gluts-funny",
        52
      ],
      "burka": [
        "tyros-mural",
        38
      ],
      "burly": [
        "shout-lurid",
        39
      ],
      "burnt": [
        "runny",
        67
      ],
      "burro": [
        "shout-furor",
        33
      ],
      "bursa": [
        "tyros-harsh",
        41
      ],
      "burst": [
        "shout",
        57
      ],
      "bused": [
        "split-guess-frame",
        31
      ],
      "bushy": [
        "sloth-might",
        31
      ],
      "busty": [
        "sloth-fudge-musty",
        26
      ],
      "butch": [
        "spoil-humid",
        41
      ],
      "butte": [
        "toils-etude",
        42
      ],
      "buxom": [
        "sloth-gumbo",
        33
      ],
      "buyer": [
        "betel-boxer",
        46
      ],
      "buzzy": [
        "sloth-dumpy-fuzzy",
        13
      ],
      "bylaw": [
        "toils-allay",
        28
      ],
      "byway": [
        "toils-dumpy-baggy",
        18
      ],
      "cabal": [
        "limbo",
        73
      ],
      "cabby": [
        "limbo",
        73
      ],
      "cabin": [
        "pilot",
        71
      ],
      "cable": [
        "adult",
        71
      ],
      "cacao": [
        "limbo",
        73
      ],
      "cache": [
        "adult",
        71
      ],
      "cacti": [
        "limbo",
        73
      ],
      "caddy": [
        "limbo-catch",
        41
      ],
      "cadet": [
        "salty",
        71
      ],
      "cadge": [
        "adult",
        71
      ],
      "cadre": [
        "carve",
        65
      ],
      "caged": [
        "salty-cameo-gawky",
        53
      ],
      "cagey": [
        "salty",
        71
      ],
      "cairn": [
        "",
        99
      ],
      "caked": [
        "salty-cameo-gawky",
        53
      ],
      "calve": [
        "adult",
        71
      ],
      "camel": [
        "salty",
        71
      ],
      "cameo": [
        "salty",
        64
      ],
      "campy": [
        "limbo",
        73
      ],
      "canal": [
        "pilot",
        71
      ],
      "candy": [
        "pilot",
        71
      ],
      "caned": [
        "clean",
        49
      ],
      "canny": [
        "",
        86
      ],
      "canoe": [
        "",
        99
      ],
      "canon": [
        "pilot",
        71
      ],
      "caped": [
        "salty-cameo-gawky",
        47
      ],
      "caper": [
        "tired",
        72
      ],
      "capon": [
        "pilot",
        71
      ],
      "capri": [
        "carol",
        75
      ],
      "caput": [
        "limbo-catch",
        41
      ],
      "carat": [
        "carol-carry",
        45
      ],
      "cared": [
        "tired",
        72
      ],
      "carer": [
        "tired",
        72
      ],
      "caret": [
        "tired",
        72
      ],
      "cargo": [
        "carol",
        75
      ],
      "carny": [
        "",
        99
      ],
      "carob": [
        "carol-carom",
        40
      ],
      "carol": [
        "",
        91
      ],
      "carom": [
        "carol",
        56
      ],
      "carry": [
        "carol",
        62
      ],
      "carte": [
        "carve",
        65
      ],
      "carve": [
        "",
        89
      ],
      "cased": [
        "salty",
        71
      ],
      "caste": [
        "adult",
        71
      ],
      "catch": [
        "limbo",
        58
      ],
      "cater": [
        "tired",
        72
      ],
      "catty": [
        "limbo-catch",
        41
      ],
      "caulk": [
        "limbo",
        73
      ],
      "cause": [
        "adult",
        71
      ],
      "caved": [
        "salty-cameo-gawky-caped",
        37
      ],
      "cavil": [
        "limbo",
        73
      ],
      "cawed": [
        "salty-cameo-gawky",
        53
      ],
      "cease": [
        "chase",
        72
      ],
      "cedar": [
        "tired",
        72
      ],
      "ceded": [
        "volts-cheek",
        44
      ],
      "celeb": [
        "volts",
        72
      ],
      "cello": [
        "volts",
        72
      ],
      "chafe": [
        "chase",
        72
      ],
      "chaff": [
        "plush",
        71
      ],
      "chain": [
        "",
        99
      ],
      "chair": [
        "dirty",
        72
      ],
      "chalk": [
        "plush",
        71
      ],
      "champ": [
        "plush",
        71
      ],
      "chant": [
        "clang",
        65
      ],
      "chaos": [
        "plush",
        71
      ],
      "chard": [
        "dirty",
        72
      ],
      "charm": [
        "dirty",
        72
      ],
      "chart": [
        "dirty",
        72
      ],
      "chary": [
        "dirty",
        72
      ],
      "chase": [
        "",
        91
      ],
      "chasm": [
        "plush",
        71
      ],
      "cheap": [
        "salty",
        71
      ],
      "cheat": [
        "salty",
        71
      ],
      "check": [
        "volts-cheek",
        44
      ],
      "cheek": [
        "volts",
        60
      ],
      "cheep": [
        "volts-cheek",
        44
      ],
      "cheer": [
        "would",
        59
      ],
      "chemo": [
        "volts",
        72
      ],
      "chess": [
        "volts",
        72
      ],
      "chest": [
        "volts",
        72
      ],
      "chewy": [
        "volts-cheek",
        44
      ],
      "chick": [
        "hokum",
        70
      ],
      "chide": [
        "solid",
        73
      ],
      "chief": [
        "volts-cheek",
        44
      ],
      "child": [
        "hokum-pedal",
        45
      ],
      "chile": [
        "solid",
        59
      ],
      "chili": [
        "hokum-pedal",
        45
      ],
      "chill": [
        "hokum-pedal",
        45
      ],
      "chime": [
        "solid",
        54
      ],
      "chimp": [
        "hokum",
        70
      ],
      "china": [
        "canny",
        61
      ],
      "chino": [
        "clunk",
        67
      ],
      "chirp": [
        "lorry",
        73
      ],
      "chive": [
        "solid-chime",
        38
      ],
      "chock": [
        "hokum",
        70
      ],
      "choir": [
        "lorry",
        73
      ],
      "choke": [
        "solid",
        73
      ],
      "chomp": [
        "hokum",
        70
      ],
      "chord": [
        "lorry",
        73
      ],
      "chore": [
        "curse",
        65
      ],
      "chose": [
        "solid",
        73
      ],
      "choux": [
        "hokum",
        70
      ],
      "chuck": [
        "hokum",
        70
      ],
      "chump": [
        "hokum",
        70
      ],
      "chunk": [
        "clunk",
        67
      ],
      "churl": [
        "lorry",
        73
      ],
      "churn": [
        "",
        99
      ],
      "chute": [
        "solid",
        73
      ],
      "cider": [
        "would",
        83
      ],
      "cigar": [
        "carol",
        75
      ],
      "cilia": [
        "limbo",
        73
      ],
      "cinch": [
        "conch",
        67
      ],
      "circa": [
        "carol",
        75
      ],
      "cited": [
        "volts",
        72
      ],
      "civet": [
        "volts",
        72
      ],
      "civic": [
        "hokum-civil",
        40
      ],
      "civil": [
        "hokum",
        56
      ],
      "clack": [
        "plush-claim",
        38
      ],
      "clade": [
        "chase-clave",
        36
      ],
      "claim": [
        "plush",
        55
      ],
      "clamp": [
        "plush",
        71
      ],
      "clang": [
        "",
        90
      ],
      "clank": [
        "clang",
        65
      ],
      "clash": [
        "plush",
        71
      ],
      "clasp": [
        "plush",
        71
      ],
      "class": [
        "plush",
        71
      ],
      "clave": [
        "chase",
        52
      ],
      "clean": [
        "",
        74
      ],
      "clear": [
        "tired",
        72
      ],
      "cleat": [
        "salty",
        71
      ],
      "cleft": [
        "volts",
        72
      ],
      "clerk": [
        "would",
        83
      ],
      "click": [
        "hokum",
        70
      ],
      "cliff": [
        "hokum-civil",
        40
      ],
      "climb": [
        "hokum",
        70
      ],
      "clime": [
        "solid-chile",
        42
      ],
      "cling": [
        "clunk",
        67
      ],
      "clink": [
        "clunk",
        67
      ],
      "cloak": [
        "limbo",
        73
      ],
      "clock": [
        "hokum",
        70
      ],
      "clomp": [
        "hokum",
        70
      ],
      "clone": [
        "",
        99
      ],
      "close": [
        "solid",
        73
      ],
      "cloth": [
        "hokum",
        70
      ],
      "cloud": [
        "hokum-clout",
        44
      ],
      "clout": [
        "hokum",
        61
      ],
      "clove": [
        "solid",
        73
      ],
      "clown": [
        "conch",
        67
      ],
      "cluck": [
        "hokum",
        70
      ],
      "clued": [
        "volts",
        72
      ],
      "clump": [
        "hokum",
        70
      ],
      "clung": [
        "clunk",
        67
      ],
      "clunk": [
        "",
        92
      ],
      "coach": [
        "plush",
        71
      ],
      "coast": [
        "plush",
        71
      ],
      "coati": [
        "plush",
        71
      ],
      "cobra": [
        "carol",
        75
      ],
      "cocky": [
        "hokum",
        70
      ],
      "cocoa": [
        "limbo",
        53
      ],
      "coded": [
        "volts-codex",
        48
      ],
      "coder": [
        "would",
        83
      ],
      "codex": [
        "volts",
        65
      ],
      "colic": [
        "hokum-coyly",
        46
      ],
      "colon": [
        "conch",
        67
      ],
      "color": [
        "lorry",
        73
      ],
      "combo": [
        "hokum-comic",
        48
      ],
      "comet": [
        "volts",
        72
      ],
      "comfy": [
        "hokum-comic-combo",
        36
      ],
      "comic": [
        "hokum",
        56
      ],
      "comma": [
        "limbo",
        73
      ],
      "conch": [
        "",
        92
      ],
      "condo": [
        "conch",
        67
      ],
      "coned": [
        "coven",
        49
      ],
      "conga": [
        "pilot",
        71
      ],
      "conic": [
        "conch",
        67
      ],
      "cooed": [
        "volts-codex-trope",
        48
      ],
      "copay": [
        "limbo-cocoa",
        36
      ],
      "coped": [
        "volts-codex-trope",
        48
      ],
      "copse": [
        "solid",
        73
      ],
      "coral": [
        "carol",
        75
      ],
      "cored": [
        "would",
        83
      ],
      "corer": [
        "would-cover",
        41
      ],
      "corgi": [
        "lorry-corps",
        40
      ],
      "corky": [
        "lorry",
        73
      ],
      "corny": [
        "",
        99
      ],
      "corps": [
        "lorry",
        56
      ],
      "couch": [
        "hokum-cough",
        45
      ],
      "cough": [
        "hokum",
        59
      ],
      "could": [
        "hokum",
        70
      ],
      "count": [
        "clunk",
        67
      ],
      "coupe": [
        "solid",
        73
      ],
      "court": [
        "lorry",
        73
      ],
      "couth": [
        "hokum-cough-couch",
        32
      ],
      "coven": [
        "",
        74
      ],
      "cover": [
        "would",
        58
      ],
      "covet": [
        "volts",
        72
      ],
      "covey": [
        "volts",
        72
      ],
      "cowed": [
        "volts-codex-trope",
        48
      ],
      "cower": [
        "would",
        83
      ],
      "coxed": [
        "volts-codex",
        48
      ],
      "coyly": [
        "hokum",
        62
      ],
      "crack": [
        "flays",
        60
      ],
      "craft": [
        "flays",
        78
      ],
      "cramp": [
        "flays-crack",
        43
      ],
      "crane": [
        "",
        99
      ],
      "crank": [
        "",
        99
      ],
      "crash": [
        "flays",
        78
      ],
      "crass": [
        "flays",
        78
      ],
      "crate": [
        "crave-craze",
        51
      ],
      "crave": [
        "",
        89
      ],
      "crawl": [
        "flays",
        78
      ],
      "craze": [
        "crave",
        68
      ],
      "crazy": [
        "flays",
        78
      ],
      "creak": [
        "cream",
        64
      ],
      "cream": [
        "",
        89
      ],
      "credo": [
        "plied",
        74
      ],
      "creed": [
        "plied",
        74
      ],
      "creek": [
        "plied",
        74
      ],
      "creep": [
        "plied",
        74
      ],
      "crema": [
        "cream",
        64
      ],
      "creme": [
        "",
        91
      ],
      "crepe": [
        "creme",
        66
      ],
      "crept": [
        "plied",
        74
      ],
      "cress": [
        "plied-crest",
        40
      ],
      "crest": [
        "plied",
        57
      ],
      "crick": [
        "stoop-crumb",
        43
      ],
      "cried": [
        "plied",
        74
      ],
      "crier": [
        "plied",
        74
      ],
      "crime": [
        "creme",
        66
      ],
      "crimp": [
        "stoop",
        57
      ],
      "crisp": [
        "stoop",
        78
      ],
      "croak": [
        "",
        99
      ],
      "crock": [
        "stoop-crowd",
        39
      ],
      "crone": [
        "",
        99
      ],
      "crony": [
        "",
        99
      ],
      "crook": [
        "stoop",
        78
      ],
      "croon": [
        "crown",
        61
      ],
      "cross": [
        "stoop",
        78
      ],
      "croup": [
        "stoop",
        78
      ],
      "crowd": [
        "stoop",
        56
      ],
      "crown": [
        "",
        86
      ],
      "crude": [
        "creme",
        66
      ],
      "cruel": [
        "plied",
        74
      ],
      "crumb": [
        "stoop",
        60
      ],
      "crump": [
        "stoop-crimp",
        41
      ],
      "crush": [
        "stoop",
        78
      ],
      "crust": [
        "stoop",
        78
      ],
      "crypt": [
        "stoop",
        78
      ],
      "cubby": [
        "hokum-cubic",
        34
      ],
      "cubed": [
        "volts-cheek",
        44
      ],
      "cubic": [
        "hokum",
        50
      ],
      "cubit": [
        "hokum-cubic",
        34
      ],
      "cuing": [
        "clunk",
        67
      ],
      "cumin": [
        "conch",
        67
      ],
      "cupid": [
        "hokum-cubic",
        34
      ],
      "cured": [
        "would",
        83
      ],
      "curer": [
        "would-cuter",
        45
      ],
      "curio": [
        "lorry",
        73
      ],
      "curly": [
        "lorry",
        73
      ],
      "curry": [
        "lorry",
        73
      ],
      "curse": [
        "",
        89
      ],
      "curve": [
        "curse",
        65
      ],
      "curvy": [
        "lorry",
        73
      ],
      "cushy": [
        "hokum",
        70
      ],
      "cuter": [
        "would",
        62
      ],
      "cutie": [
        "solid",
        73
      ],
      "cutup": [
        "hokum",
        70
      ],
      "cyber": [
        "would-cheer",
        43
      ],
      "cycle": [
        "solid",
        73
      ],
      "cynic": [
        "conch",
        67
      ],
      "dacha": [
        "hotly",
        58
      ],
      "daddy": [
        "toils-dumpy",
        35
      ],
      "daffy": [
        "toils-dumpy-daddy",
        22
      ],
      "daily": [
        "toils",
        55
      ],
      "dairy": [
        "tyros",
        59
      ],
      "daisy": [
        "toils",
        55
      ],
      "dally": [
        "toils-madly",
        34
      ],
      "dance": [
        "",
        85
      ],
      "dandy": [
        "natal-demos",
        47
      ],
      "dared": [
        "tales-pygmy-forks-rarer-bared",
        26
      ],
      "dated": [
        "petal-gated-shame-draft",
        38
      ],
      "dater": [
        "tales-hewed",
        47
      ],
      "datum": [
        "toils-bumpy",
        34
      ],
      "daunt": [
        "tings-hived",
        44
      ],
      "dazed": [
        "petal-fades-baked-weigh-maxed",
        29
      ],
      "dealt": [
        "lefts",
        73
      ],
      "death": [
        "lefts",
        57
      ],
      "debar": [
        "tales-rehab",
        46
      ],
      "debit": [
        "split",
        58
      ],
      "debug": [
        "split-dogma",
        34
      ],
      "debut": [
        "split-beget",
        33
      ],
      "decaf": [
        "fecal",
        67
      ],
      "decal": [
        "fecal",
        67
      ],
      "decay": [
        "fecal",
        67
      ],
      "decor": [
        "hirer",
        75
      ],
      "decoy": [
        "pilot",
        71
      ],
      "decry": [
        "hirer",
        55
      ],
      "defer": [
        "betel-fewer",
        42
      ],
      "defog": [
        "split-dogma",
        34
      ],
      "deify": [
        "split-edify",
        36
      ],
      "deign": [
        "towel",
        51
      ],
      "deist": [
        "split-heist",
        39
      ],
      "deity": [
        "split-thief",
        40
      ],
      "delay": [
        "petal",
        64
      ],
      "delta": [
        "petal",
        70
      ],
      "delve": [
        "toils-dumpy",
        30
      ],
      "demon": [
        "towel-venom",
        41
      ],
      "demur": [
        "betel-smirk-femur",
        26
      ],
      "denim": [
        "towel-deign",
        37
      ],
      "dense": [
        "deist",
        73
      ],
      "depot": [
        "split-tempt",
        40
      ],
      "depth": [
        "split-empty",
        37
      ],
      "derby": [
        "betel",
        60
      ],
      "deter": [
        "betel",
        62
      ],
      "detox": [
        "split-teeth",
        30
      ],
      "deuce": [
        "pious",
        48
      ],
      "devil": [
        "split",
        56
      ],
      "diary": [
        "midst",
        77
      ],
      "diced": [
        "pilot-dicey",
        47
      ],
      "dicer": [
        "hirer",
        75
      ],
      "dicey": [
        "pilot",
        64
      ],
      "digit": [
        "sloth-timid",
        34
      ],
      "diked": [
        "split-edify-video-bumpy-hiked",
        28
      ],
      "dilly": [
        "sloth-billy-filly-willy",
        14
      ],
      "dimly": [
        "sloth-billy",
        30
      ],
      "dined": [
        "towel-hived-denim",
        36
      ],
      "diner": [
        "rites-medal",
        47
      ],
      "dingo": [
        "pinot-lingo-bingo",
        35
      ],
      "dingy": [
        "pinot-desks",
        36
      ],
      "dinky": [
        "pinot-desks",
        36
      ],
      "diode": [
        "toils",
        59
      ],
      "dippy": [
        "sloth-dumpy",
        28
      ],
      "dirge": [
        "south-verge",
        38
      ],
      "dirty": [
        "shout",
        52
      ],
      "disco": [
        "spoil",
        63
      ],
      "dishy": [
        "sloth-might-fishy",
        23
      ],
      "ditch": [
        "spoil-which",
        35
      ],
      "ditsy": [
        "sloth-midst",
        37
      ],
      "ditto": [
        "sloth",
        54
      ],
      "ditty": [
        "sloth-batik-witty",
        24
      ],
      "ditzy": [
        "sloth-timid",
        34
      ],
      "divan": [
        "natal-human",
        42
      ],
      "dived": [
        "split-edify-video-hived",
        26
      ],
      "diver": [
        "betel-whips-river",
        39
      ],
      "divot": [
        "sloth-doubt",
        29
      ],
      "divvy": [
        "sloth-dumpy-dizzy",
        18
      ],
      "dizzy": [
        "sloth-dumpy",
        30
      ],
      "dodge": [
        "toils-vogue",
        36
      ],
      "dodgy": [
        "sloth-gumbo-foggy",
        20
      ],
      "doggo": [
        "sloth-gumbo",
        33
      ],
      "doggy": [
        "sloth-gumbo-foggy",
        20
      ],
      "dogma": [
        "toils-vodka",
        39
      ],
      "doily": [
        "sloth-dolly",
        30
      ],
      "doing": [
        "gluts",
        54
      ],
      "doled": [
        "split-belly-golem-holed",
        25
      ],
      "dolly": [
        "sloth",
        41
      ],
      "domed": [
        "split-dogma",
        34
      ],
      "donor": [
        "boson",
        53
      ],
      "donut": [
        "pinot",
        61
      ],
      "doozy": [
        "sloth-gazed",
        41
      ],
      "doped": [
        "split-dopey",
        30
      ],
      "doper": [
        "betel-whips-purer",
        28
      ],
      "dopey": [
        "split",
        47
      ],
      "dorky": [
        "shout-dowry",
        32
      ],
      "dosed": [
        "split-guess-mosey-hosed",
        27
      ],
      "doted": [
        "split-teeth-voted",
        21
      ],
      "dotty": [
        "sloth-ditto",
        38
      ],
      "doubt": [
        "sloth",
        45
      ],
      "dough": [
        "sloth",
        55
      ],
      "doula": [
        "toils",
        53
      ],
      "douse": [
        "toils-dumpy",
        33
      ],
      "dowdy": [
        "sloth-gumbo-widow",
        20
      ],
      "dowel": [
        "split-dweeb",
        32
      ],
      "downy": [
        "gluts-phony",
        30
      ],
      "dowry": [
        "shout",
        45
      ],
      "dowse": [
        "toils-dumpy",
        33
      ],
      "dozed": [
        "split-dogma",
        34
      ],
      "dozen": [
        "towel-honey",
        47
      ],
      "dozer": [
        "betel-whips-roofs-mover-joker",
        15
      ],
      "draft": [
        "twigs",
        75
      ],
      "drain": [
        "debit",
        71
      ],
      "drake": [
        "digit-drape",
        53
      ],
      "drama": [
        "twigs",
        56
      ],
      "drank": [
        "gated",
        78
      ],
      "drape": [
        "digit",
        70
      ],
      "drawl": [
        "twigs-brawl",
        46
      ],
      "drawn": [
        "debit",
        71
      ],
      "dread": [
        "tubed",
        77
      ],
      "dream": [
        "tubed",
        77
      ],
      "dreck": [
        "wreck",
        64
      ],
      "dress": [
        "defer",
        74
      ],
      "dried": [
        "defer",
        74
      ],
      "drier": [
        "defer-dryer",
        46
      ],
      "drift": [
        "pilot-grist",
        32
      ],
      "drill": [
        "pilot-fudge",
        43
      ],
      "drink": [
        "bigot",
        73
      ],
      "drive": [
        "pivot",
        75
      ],
      "droid": [
        "pilot",
        70
      ],
      "droit": [
        "pilot-orbit",
        48
      ],
      "droll": [
        "pilot",
        61
      ],
      "drone": [
        "prone",
        77
      ],
      "drool": [
        "pilot",
        70
      ],
      "droop": [
        "pilot",
        70
      ],
      "dross": [
        "pilot-gross",
        41
      ],
      "drove": [
        "pivot",
        68
      ],
      "drown": [
        "gibed",
        72
      ],
      "druid": [
        "pilot-frisk",
        36
      ],
      "drunk": [
        "bigot",
        73
      ],
      "dryer": [
        "defer",
        63
      ],
      "dryly": [
        "pilot-wryly",
        43
      ],
      "ducat": [
        "hotly-tacit",
        43
      ],
      "duchy": [
        "spoil-humid",
        36
      ],
      "ducky": [
        "spoil-humid",
        41
      ],
      "duked": [
        "split-dogma-dweeb",
        26
      ],
      "dully": [
        "sloth-billy-fully-gully",
        19
      ],
      "dummy": [
        "sloth-dumpy",
        28
      ],
      "dumpy": [
        "sloth",
        36
      ],
      "dunce": [
        "humps-ounce",
        49
      ],
      "duped": [
        "split-dopey",
        30
      ],
      "dusky": [
        "sloth",
        51
      ],
      "dusty": [
        "sloth-fudge",
        44
      ],
      "dutch": [
        "spoil-humid-duchy",
        23
      ],
      "duvet": [
        "split-beget",
        33
      ],
      "dwarf": [
        "midst-about",
        43
      ],
      "dweeb": [
        "split-dogma",
        38
      ],
      "dwell": [
        "split-dweeb",
        32
      ],
      "dwelt": [
        "split-fleet",
        38
      ],
      "dying": [
        "gluts-doing",
        37
      ],
      "eager": [
        "tales-pygmy",
        47
      ],
      "eagle": [
        "talus-badge",
        46
      ],
      "eared": [
        "tales-pygmy-forks-rarer-bared",
        26
      ],
      "early": [
        "tales",
        71
      ],
      "earth": [
        "tales",
        71
      ],
      "eased": [
        "petal-fades-serve",
        29
      ],
      "easel": [
        "petal-bagel",
        45
      ],
      "eaten": [
        "sleep",
        72
      ],
      "eater": [
        "tales-hewed",
        47
      ],
      "ebbed": [
        "split-dogma-weedy",
        26
      ],
      "ebony": [
        "tipsy",
        73
      ],
      "ebook": [
        "split-dogma",
        34
      ],
      "eclat": [
        "fecal",
        67
      ],
      "edema": [
        "petal-fades",
        38
      ],
      "edged": [
        "split-dogma",
        33
      ],
      "edger": [
        "betel-sheer-eider",
        30
      ],
      "edict": [
        "pilot-evict",
        40
      ],
      "edify": [
        "split",
        52
      ],
      "educe": [
        "pious-deuce",
        31
      ],
      "eerie": [
        "south-verge",
        38
      ],
      "egged": [
        "split-dogma-edged",
        20
      ],
      "egret": [
        "betel-steer",
        46
      ],
      "eider": [
        "betel-sheer",
        42
      ],
      "eight": [
        "split",
        56
      ],
      "eject": [
        "pilot",
        71
      ],
      "eking": [
        "tipsy-being",
        36
      ],
      "elate": [
        "sloth-plate",
        46
      ],
      "elbow": [
        "split-dweeb",
        32
      ],
      "elder": [
        "betel",
        60
      ],
      "elect": [
        "pilot",
        71
      ],
      "elegy": [
        "split-dweeb",
        32
      ],
      "elfin": [
        "towel",
        68
      ],
      "elide": [
        "toils-glide",
        43
      ],
      "elite": [
        "toils",
        61
      ],
      "elope": [
        "toils-globe",
        36
      ],
      "elude": [
        "toils-dumpy",
        30
      ],
      "email": [
        "lefts",
        73
      ],
      "embed": [
        "split-dogma",
        38
      ],
      "ember": [
        "betel",
        60
      ],
      "emcee": [
        "pious",
        71
      ],
      "emery": [
        "betel-every",
        45
      ],
      "emoji": [
        "split-edify",
        36
      ],
      "emote": [
        "toils-quote",
        42
      ],
      "empty": [
        "split",
        53
      ],
      "enact": [
        "",
        99
      ],
      "ended": [
        "towel-hived-unfed-kneed",
        29
      ],
      "endow": [
        "towel",
        68
      ],
      "enema": [
        "sleep",
        72
      ],
      "enemy": [
        "towel-deign",
        37
      ],
      "enjoy": [
        "towel-venom",
        41
      ],
      "ennui": [
        "towel-deign",
        37
      ],
      "ensue": [
        "deist",
        62
      ],
      "enter": [
        "rites",
        73
      ],
      "entry": [
        "rites",
        73
      ],
      "envoy": [
        "towel-venom",
        41
      ],
      "epoch": [
        "pilot",
        71
      ],
      "epoxy": [
        "split",
        54
      ],
      "equal": [
        "petal-ideal",
        43
      ],
      "equip": [
        "split",
        56
      ],
      "erase": [
        "digit-brave",
        49
      ],
      "erect": [
        "wreck",
        64
      ],
      "erode": [
        "pivot-beard",
        52
      ],
      "erred": [
        "defer-greed",
        41
      ],
      "error": [
        "defer",
        74
      ],
      "erupt": [
        "defer-press",
        37
      ],
      "essay": [
        "petal-ahead",
        43
      ],
      "ester": [
        "betel",
        60
      ],
      "ether": [
        "betel-steer",
        46
      ],
      "ethic": [
        "pilot",
        71
      ],
      "ethos": [
        "split-testy",
        38
      ],
      "ethyl": [
        "split-hotel",
        32
      ],
      "etude": [
        "toils",
        59
      ],
      "evade": [
        "sloth-agave",
        43
      ],
      "event": [
        "tipsy",
        73
      ],
      "evert": [
        "betel-exert",
        38
      ],
      "every": [
        "betel",
        61
      ],
      "evict": [
        "pilot",
        57
      ],
      "evoke": [
        "toils",
        61
      ],
      "exact": [
        "leapt",
        72
      ],
      "exalt": [
        "lefts",
        73
      ],
      "excel": [
        "pilot",
        55
      ],
      "exert": [
        "betel",
        55
      ],
      "exile": [
        "toils-while",
        46
      ],
      "exist": [
        "split-heist",
        39
      ],
      "expat": [
        "petal",
        70
      ],
      "expel": [
        "split",
        55
      ],
      "extol": [
        "split-hotel",
        32
      ],
      "extra": [
        "tales-avert",
        49
      ],
      "exude": [
        "toils-fudge",
        35
      ],
      "exult": [
        "split-fleet",
        38
      ],
      "exurb": [
        "betel",
        60
      ],
      "eying": [
        "tipsy",
        73
      ],
      "fable": [
        "talus-badge",
        46
      ],
      "faced": [
        "fecal-facet",
        44
      ],
      "facet": [
        "fecal",
        61
      ],
      "faded": [
        "petal-fades",
        38
      ],
      "fader": [
        "tales-pygmy-forks",
        39
      ],
      "faint": [
        "tings-paint",
        48
      ],
      "fairy": [
        "tyros-dairy",
        47
      ],
      "faith": [
        "toils-agita",
        37
      ],
      "faked": [
        "petal-fades-famed-kudzu",
        33
      ],
      "faker": [
        "tales-pygmy-forks",
        39
      ],
      "fakir": [
        "tyros-rabid",
        33
      ],
      "false": [
        "talus",
        66
      ],
      "famed": [
        "petal-fades",
        41
      ],
      "fancy": [
        "panic",
        74
      ],
      "farce": [
        "",
        99
      ],
      "fared": [
        "tales-pygmy-forks",
        39
      ],
      "fatal": [
        "toils-waltz",
        39
      ],
      "fated": [
        "petal-gated-shame-draft",
        38
      ],
      "fatty": [
        "toils-bumpy",
        34
      ],
      "fatwa": [
        "toils-bumpy",
        34
      ],
      "fault": [
        "toils",
        54
      ],
      "fauna": [
        "tings",
        79
      ],
      "favor": [
        "tyros-valor",
        42
      ],
      "faxed": [
        "petal-fades-famed-kudzu",
        33
      ],
      "fazed": [
        "petal-fades-famed-kudzu",
        33
      ],
      "feast": [
        "lefts",
        73
      ],
      "fecal": [
        "",
        91
      ],
      "feces": [
        "pilot-beech",
        41
      ],
      "feign": [
        "towel-deign",
        37
      ],
      "feint": [
        "tipsy",
        73
      ],
      "fella": [
        "petal",
        58
      ],
      "felon": [
        "towel-lemon",
        45
      ],
      "femme": [
        "toils-fudge",
        35
      ],
      "femur": [
        "betel-smirk",
        38
      ],
      "fence": [
        "humps-niece",
        45
      ],
      "feral": [
        "tales-regal",
        51
      ],
      "ferry": [
        "betel-smirk",
        37
      ],
      "fetal": [
        "petal-metal",
        43
      ],
      "fetch": [
        "pilot",
        71
      ],
      "feted": [
        "split-teeth-meted",
        18
      ],
      "fetid": [
        "split",
        56
      ],
      "fetus": [
        "split-testy",
        38
      ],
      "fever": [
        "betel-fewer",
        50
      ],
      "fewer": [
        "betel",
        57
      ],
      "fiber": [
        "betel-sober",
        53
      ],
      "ficus": [
        "spoil",
        63
      ],
      "field": [
        "split-windy",
        44
      ],
      "fiend": [
        "tipsy",
        73
      ],
      "fiery": [
        "betel",
        61
      ],
      "fifth": [
        "sloth",
        55
      ],
      "fifty": [
        "sloth-batik",
        44
      ],
      "fight": [
        "sloth-thump",
        29
      ],
      "filch": [
        "spoil-flick",
        37
      ],
      "filed": [
        "split-flown",
        43
      ],
      "filer": [
        "betel-folic",
        46
      ],
      "filet": [
        "split",
        56
      ],
      "filly": [
        "sloth-billy",
        29
      ],
      "filmy": [
        "sloth-billy-milky",
        20
      ],
      "filth": [
        "sloth",
        50
      ],
      "final": [
        "natal",
        65
      ],
      "finch": [
        "posit-winch",
        43
      ],
      "fined": [
        "towel-hived-denim-pined",
        24
      ],
      "finer": [
        "rites-medal",
        47
      ],
      "fired": [
        "betel-whips-river-mired",
        22
      ],
      "first": [
        "shout",
        60
      ],
      "firth": [
        "shout-birth-girth-mirth",
        26
      ],
      "fishy": [
        "sloth-might",
        35
      ],
      "fixed": [
        "split-edify",
        36
      ],
      "fixer": [
        "betel-whips-river-mixer",
        22
      ],
      "fizzy": [
        "sloth-dumpy",
        31
      ],
      "fjord": [
        "shout-glory",
        33
      ],
      "flack": [
        "plush-black",
        43
      ],
      "flail": [
        "spilt-avail-quail",
        36
      ],
      "flair": [
        "midst",
        77
      ],
      "flake": [
        "sloth-embed-glaze",
        32
      ],
      "flaky": [
        "spilt",
        56
      ],
      "flame": [
        "sloth-embed",
        51
      ],
      "flank": [
        "ghost-bland",
        47
      ],
      "flare": [
        "aloft",
        85
      ],
      "flash": [
        "spilt",
        56
      ],
      "flask": [
        "spilt-flash",
        40
      ],
      "fleck": [
        "pilot-excel",
        38
      ],
      "fleet": [
        "split",
        55
      ],
      "flesh": [
        "split",
        57
      ],
      "flick": [
        "spoil",
        54
      ],
      "flied": [
        "split-windy",
        43
      ],
      "flier": [
        "betel-folic",
        46
      ],
      "fling": [
        "gluts",
        61
      ],
      "flint": [
        "gluts",
        66
      ],
      "flirt": [
        "shout",
        60
      ],
      "float": [
        "toils",
        53
      ],
      "flock": [
        "spoil-block",
        39
      ],
      "flood": [
        "sloth-blood",
        43
      ],
      "floor": [
        "shout-glory",
        33
      ],
      "flora": [
        "tyros-amour",
        40
      ],
      "floss": [
        "sloth-gloss",
        38
      ],
      "flour": [
        "shout",
        60
      ],
      "flout": [
        "sloth",
        50
      ],
      "flown": [
        "pinot-snowy-blown",
        23
      ],
      "flowy": [
        "sloth-blood",
        42
      ],
      "fluff": [
        "sloth-bluff",
        34
      ],
      "fluid": [
        "sloth-bluff",
        33
      ],
      "fluke": [
        "toils-dumpy",
        30
      ],
      "fluky": [
        "sloth-bluff-fluid",
        21
      ],
      "flume": [
        "toils-dumpy",
        30
      ],
      "flung": [
        "gluts",
        66
      ],
      "flunk": [
        "gluts-plunk",
        46
      ],
      "flush": [
        "sloth-probe",
        44
      ],
      "flute": [
        "toils",
        59
      ],
      "flyby": [
        "sloth-bluff",
        34
      ],
      "flyer": [
        "betel-folic",
        46
      ],
      "foamy": [
        "spilt",
        56
      ],
      "focal": [
        "hotly-lover",
        52
      ],
      "focus": [
        "spoil",
        53
      ],
      "fogey": [
        "split-dogma-bogey",
        20
      ],
      "foggy": [
        "sloth-gumbo",
        32
      ],
      "foist": [
        "sloth-moist",
        40
      ],
      "folic": [
        "spoil-logic",
        42
      ],
      "folio": [
        "sloth-dolly-polio",
        18
      ],
      "folky": [
        "sloth-dolly",
        30
      ],
      "folly": [
        "sloth-dolly-fjord",
        27
      ],
      "foray": [
        "tyros",
        62
      ],
      "force": [
        "score",
        67
      ],
      "forge": [
        "south",
        62
      ],
      "forgo": [
        "shout-dowry",
        32
      ],
      "forte": [
        "south",
        63
      ],
      "forth": [
        "shout",
        53
      ],
      "forty": [
        "shout-motor",
        35
      ],
      "forum": [
        "shout",
        60
      ],
      "found": [
        "gluts-whomp-bound",
        23
      ],
      "fount": [
        "gluts-mount",
        47
      ],
      "foyer": [
        "betel-whips-roofs",
        31
      ],
      "frack": [
        "track",
        64
      ],
      "frail": [
        "twigs",
        65
      ],
      "frame": [
        "digit-brave-erase",
        37
      ],
      "franc": [
        "",
        99
      ],
      "frank": [
        "gated",
        60
      ],
      "fraud": [
        "twigs-drama",
        39
      ],
      "freak": [
        "tubed",
        57
      ],
      "freed": [
        "defer",
        74
      ],
      "freer": [
        "defer",
        74
      ],
      "fresh": [
        "defer",
        74
      ],
      "friar": [
        "armor",
        63
      ],
      "fried": [
        "defer",
        74
      ],
      "frill": [
        "pilot-fudge",
        43
      ],
      "frise": [
        "pivot-bride-grime",
        31
      ],
      "frisk": [
        "pilot",
        53
      ],
      "fritz": [
        "pilot",
        70
      ],
      "frizz": [
        "pilot-frisk",
        36
      ],
      "frock": [
        "trick",
        74
      ],
      "frond": [
        "bigot",
        73
      ],
      "front": [
        "bigot",
        73
      ],
      "frosh": [
        "pilot-gross",
        41
      ],
      "frost": [
        "pilot-trout",
        42
      ],
      "froth": [
        "pilot-broth",
        46
      ],
      "frown": [
        "gibed",
        72
      ],
      "froze": [
        "pivot-beard",
        52
      ],
      "fruit": [
        "pilot-grist",
        32
      ],
      "frump": [
        "pilot-grump",
        49
      ],
      "fryer": [
        "defer",
        74
      ],
      "fubar": [
        "tyros-rabid-umbra",
        14
      ],
      "fudge": [
        "toils",
        44
      ],
      "fudgy": [
        "sloth-dumpy",
        28
      ],
      "fugue": [
        "toils-fudge",
        35
      ],
      "fully": [
        "sloth-billy",
        30
      ],
      "fumed": [
        "split-dogma-embed",
        26
      ],
      "fungi": [
        "pinot",
        61
      ],
      "fungo": [
        "pinot-bongo",
        34
      ],
      "funky": [
        "pinot-fight",
        41
      ],
      "funny": [
        "gluts",
        62
      ],
      "furor": [
        "shout",
        50
      ],
      "furry": [
        "shout-lurid-murky",
        22
      ],
      "fused": [
        "split-guess-frame",
        31
      ],
      "fussy": [
        "sloth-dusky",
        38
      ],
      "fusty": [
        "sloth-fudge",
        44
      ],
      "futon": [
        "pinot",
        61
      ],
      "fuzzy": [
        "sloth-dumpy",
        26
      ],
      "gabby": [
        "toils-dumpy-baggy",
        18
      ],
      "gable": [
        "talus-badge",
        46
      ],
      "gaffe": [
        "talus-maybe-waive",
        29
      ],
      "gaily": [
        "toils-daily",
        39
      ],
      "gamed": [
        "petal-fades-baked-weigh",
        37
      ],
      "gamer": [
        "tales-pygmy",
        50
      ],
      "gamey": [
        "petal-fades",
        38
      ],
      "gamma": [
        "toils-dumpy",
        32
      ],
      "gamut": [
        "toils-bumpy",
        34
      ],
      "gaped": [
        "petal",
        59
      ],
      "gassy": [
        "toils",
        44
      ],
      "gated": [
        "petal",
        62
      ],
      "gator": [
        "tyros",
        65
      ],
      "gaudy": [
        "toils-dumpy",
        33
      ],
      "gauge": [
        "talus",
        63
      ],
      "gaunt": [
        "tings",
        79
      ],
      "gauze": [
        "talus-gauge",
        46
      ],
      "gauzy": [
        "toils-dumpy",
        33
      ],
      "gavel": [
        "petal-bagel",
        49
      ],
      "gawky": [
        "toils-dumpy-baggy",
        18
      ],
      "gayer": [
        "tales-pygmy",
        50
      ],
      "gayly": [
        "toils-madly",
        34
      ],
      "gazed": [
        "petal-fades-baked-weigh-gamed",
        29
      ],
      "gazer": [
        "tales-pygmy",
        50
      ],
      "gecko": [
        "pilot",
        71
      ],
      "geeky": [
        "split-dogma",
        34
      ],
      "geese": [
        "toils-suede",
        34
      ],
      "genie": [
        "deist",
        73
      ],
      "genre": [
        "nurse",
        67
      ],
      "geode": [
        "toils-evoke",
        44
      ],
      "getup": [
        "split-empty",
        37
      ],
      "ghost": [
        "sloth",
        50
      ],
      "ghoul": [
        "sloth",
        50
      ],
      "giant": [
        "ghost",
        78
      ],
      "gibed": [
        "split-edify-video-bumpy",
        36
      ],
      "giddy": [
        "sloth-dumpy",
        29
      ],
      "gimme": [
        "toils-pique",
        37
      ],
      "girly": [
        "shout-rigid",
        39
      ],
      "girth": [
        "shout-birth",
        45
      ],
      "given": [
        "towel-hived",
        41
      ],
      "giver": [
        "betel-whips-river-diver",
        29
      ],
      "gizmo": [
        "sloth-gumbo",
        33
      ],
      "glade": [
        "sloth-embed",
        51
      ],
      "glamp": [
        "spilt-plaza",
        43
      ],
      "gland": [
        "ghost",
        78
      ],
      "glare": [
        "aloft",
        69
      ],
      "glass": [
        "spilt-flash",
        40
      ],
      "glaze": [
        "sloth-embed",
        44
      ],
      "gleam": [
        "petal-bleak",
        45
      ],
      "glean": [
        "sleep",
        72
      ],
      "glide": [
        "toils",
        60
      ],
      "glint": [
        "gluts",
        66
      ],
      "glitz": [
        "sloth-blitz",
        38
      ],
      "gloam": [
        "toils-allow",
        32
      ],
      "gloat": [
        "toils-float",
        41
      ],
      "globe": [
        "toils",
        53
      ],
      "gloom": [
        "sloth-blood",
        41
      ],
      "gloop": [
        "sloth-blood-gloom",
        29
      ],
      "glory": [
        "shout",
        50
      ],
      "gloss": [
        "sloth",
        55
      ],
      "glove": [
        "toils-globe",
        36
      ],
      "glowy": [
        "sloth-blood-flowy",
        29
      ],
      "glued": [
        "split-dweeb-model",
        17
      ],
      "glute": [
        "toils-flute",
        42
      ],
      "glyph": [
        "sloth",
        50
      ],
      "gnarl": [
        "snarl",
        73
      ],
      "gnash": [
        "slain",
        78
      ],
      "gnome": [
        "deist-noble",
        37
      ],
      "godly": [
        "sloth-dolly",
        30
      ],
      "gofer": [
        "betel-whips-roofs-foyer",
        21
      ],
      "going": [
        "gluts",
        66
      ],
      "golem": [
        "split-belly",
        38
      ],
      "golly": [
        "sloth-dolly-fjord",
        26
      ],
      "gonad": [
        "natal-human",
        42
      ],
      "goner": [
        "rites-below",
        42
      ],
      "gonna": [
        "tings",
        79
      ],
      "gonzo": [
        "pinot-bongo",
        34
      ],
      "goody": [
        "sloth-gazed",
        41
      ],
      "gooey": [
        "split-dogma",
        34
      ],
      "goofy": [
        "sloth-gazed",
        43
      ],
      "goopy": [
        "sloth-gazed-goofy",
        31
      ],
      "goose": [
        "toils-dumpy",
        33
      ],
      "gored": [
        "betel-whips-roofs-mover",
        22
      ],
      "gorge": [
        "south-forge",
        45
      ],
      "gorse": [
        "south-worse",
        49
      ],
      "gotta": [
        "toils",
        53
      ],
      "gouge": [
        "toils-vogue",
        36
      ],
      "gourd": [
        "shout-furor",
        33
      ],
      "grace": [
        "trace",
        68
      ],
      "grade": [
        "digit",
        83
      ],
      "graft": [
        "twigs",
        75
      ],
      "grail": [
        "twigs",
        75
      ],
      "grain": [
        "debit",
        71
      ],
      "grand": [
        "gated",
        78
      ],
      "grant": [
        "gated",
        78
      ],
      "grape": [
        "digit",
        69
      ],
      "graph": [
        "twigs-gravy",
        41
      ],
      "grasp": [
        "twigs",
        75
      ],
      "grass": [
        "twigs",
        75
      ],
      "grate": [
        "digit",
        83
      ],
      "grave": [
        "digit-grape",
        58
      ],
      "gravy": [
        "twigs",
        58
      ],
      "graze": [
        "digit-grape-grave",
        46
      ],
      "great": [
        "tubed",
        77
      ],
      "greed": [
        "defer",
        57
      ],
      "green": [
        "",
        85
      ],
      "greet": [
        "defer",
        74
      ],
      "grief": [
        "defer",
        60
      ],
      "grift": [
        "pilot-grist",
        32
      ],
      "grill": [
        "pilot-fudge",
        43
      ],
      "grime": [
        "pivot-bride",
        43
      ],
      "grimy": [
        "pilot-frisk",
        36
      ],
      "grind": [
        "bigot",
        53
      ],
      "gripe": [
        "pivot",
        75
      ],
      "grist": [
        "pilot",
        49
      ],
      "groan": [
        "organ",
        67
      ],
      "groin": [
        "gibed",
        72
      ],
      "groom": [
        "pilot",
        53
      ],
      "grope": [
        "pivot",
        75
      ],
      "gross": [
        "pilot",
        57
      ],
      "group": [
        "pilot",
        70
      ],
      "grout": [
        "pilot-trout",
        42
      ],
      "grove": [
        "pivot-drove",
        51
      ],
      "growl": [
        "pilot-droll",
        44
      ],
      "grown": [
        "gibed",
        72
      ],
      "gruel": [
        "defer",
        74
      ],
      "gruff": [
        "pilot-brush",
        42
      ],
      "grump": [
        "pilot",
        65
      ],
      "grunt": [
        "bigot",
        73
      ],
      "guano": [
        "ghost",
        78
      ],
      "guard": [
        "midst-about",
        43
      ],
      "guava": [
        "spilt-foamy",
        40
      ],
      "guess": [
        "split",
        53
      ],
      "guest": [
        "split",
        55
      ],
      "guide": [
        "toils",
        57
      ],
      "guild": [
        "sloth-billy",
        30
      ],
      "guile": [
        "toils-while-exile",
        34
      ],
      "guilt": [
        "sloth",
        52
      ],
      "guise": [
        "toils-spike",
        35
      ],
      "gulag": [
        "toils-allay",
        28
      ],
      "gulch": [
        "spoil-mulch",
        41
      ],
      "gully": [
        "sloth-billy-fully",
        29
      ],
      "gumbo": [
        "sloth",
        43
      ],
      "gummy": [
        "sloth-dumpy",
        26
      ],
      "gunky": [
        "pinot-fight",
        41
      ],
      "guppy": [
        "sloth-dumpy-puppy",
        19
      ],
      "gushy": [
        "sloth-might",
        39
      ],
      "gussy": [
        "sloth-dusky-fussy",
        26
      ],
      "gusto": [
        "sloth",
        50
      ],
      "gusty": [
        "sloth-fudge",
        44
      ],
      "gutsy": [
        "sloth-midst",
        37
      ],
      "gutty": [
        "sloth-batik-putty",
        30
      ],
      "habit": [
        "toils-audit",
        36
      ],
      "hacky": [
        "hotly",
        75
      ],
      "haiku": [
        "toils",
        53
      ],
      "hairy": [
        "tyros-dairy-fairy",
        35
      ],
      "halal": [
        "toils-allay",
        28
      ],
      "halve": [
        "talus-valve",
        51
      ],
      "hammy": [
        "toils-dumpy",
        33
      ],
      "handy": [
        "natal-demos",
        44
      ],
      "hanky": [
        "natal-demos-janky",
        25
      ],
      "happy": [
        "toils-dumpy",
        36
      ],
      "hardy": [
        "tyros-parry",
        47
      ],
      "harem": [
        "tales-pygmy-maker",
        39
      ],
      "harpy": [
        "tyros-parry",
        47
      ],
      "harry": [
        "tyros-parry-marry",
        30
      ],
      "harsh": [
        "tyros",
        58
      ],
      "haste": [
        "talus-whoop",
        50
      ],
      "hasty": [
        "toils-pasta",
        36
      ],
      "hatch": [
        "hotly",
        75
      ],
      "hated": [
        "petal-gated-shame",
        48
      ],
      "hater": [
        "tales-hewed",
        47
      ],
      "haunt": [
        "tings-hived",
        44
      ],
      "haute": [
        "talus",
        72
      ],
      "haven": [
        "sleep-known",
        43
      ],
      "havoc": [
        "hotly",
        75
      ],
      "hazed": [
        "petal-fades-baked-weigh",
        39
      ],
      "hazel": [
        "petal-bagel-easel",
        33
      ],
      "heady": [
        "lefts",
        61
      ],
      "heard": [
        "badly",
        80
      ],
      "heart": [
        "badly",
        65
      ],
      "heath": [
        "lefts-death",
        48
      ],
      "heave": [
        "sloth",
        67
      ],
      "heavy": [
        "lefts-heady",
        44
      ],
      "hedge": [
        "toils-fudge",
        37
      ],
      "hefty": [
        "split-teeth",
        30
      ],
      "heist": [
        "split",
        56
      ],
      "helix": [
        "split",
        56
      ],
      "hello": [
        "split-belly",
        34
      ],
      "hence": [
        "humps",
        80
      ],
      "henna": [
        "agent",
        66
      ],
      "heron": [
        "rites-nerdy",
        45
      ],
      "hertz": [
        "betel-merit-terry",
        31
      ],
      "hewed": [
        "split-dogma-weedy",
        26
      ],
      "hexed": [
        "split-dogma-weedy",
        35
      ],
      "hider": [
        "betel-whips-hiker",
        37
      ],
      "hijab": [
        "toils-mafia",
        30
      ],
      "hiked": [
        "split-edify-video-bumpy",
        36
      ],
      "hiker": [
        "betel-whips",
        42
      ],
      "hilly": [
        "sloth",
        48
      ],
      "hinge": [
        "deist",
        56
      ],
      "hinky": [
        "pinot-desks-kinky",
        13
      ],
      "hippo": [
        "sloth-hobby",
        44
      ],
      "hippy": [
        "sloth-huffy",
        37
      ],
      "hired": [
        "betel-whips-hiker",
        30
      ],
      "hirer": [
        "betel-whips-hiker-hider",
        27
      ],
      "hissy": [
        "sloth-might",
        39
      ],
      "hitch": [
        "spoil-which",
        35
      ],
      "hived": [
        "split-edify-video",
        36
      ],
      "hoard": [
        "midst-about",
        43
      ],
      "hoary": [
        "midst",
        61
      ],
      "hobby": [
        "sloth",
        54
      ],
      "hocus": [
        "spoil-focus",
        36
      ],
      "hoist": [
        "sloth",
        50
      ],
      "hokey": [
        "split-dogma",
        32
      ],
      "hokum": [
        "sloth-hobby",
        44
      ],
      "holed": [
        "split-belly-golem",
        35
      ],
      "holey": [
        "split-belly",
        34
      ],
      "holly": [
        "sloth",
        50
      ],
      "homed": [
        "split-dogma-modem",
        26
      ],
      "homer": [
        "betel-whips",
        44
      ],
      "homey": [
        "split-dogma",
        34
      ],
      "honed": [
        "towel-honey",
        47
      ],
      "honey": [
        "towel",
        58
      ],
      "honor": [
        "boson-donor",
        36
      ],
      "hooch": [
        "spoil",
        58
      ],
      "hoody": [
        "sloth-hooky",
        37
      ],
      "hooey": [
        "split-dogma-hokey",
        20
      ],
      "hooky": [
        "sloth",
        54
      ],
      "hoped": [
        "split-dopey-moped",
        22
      ],
      "hoppy": [
        "sloth-hobby",
        42
      ],
      "horde": [
        "south",
        73
      ],
      "horny": [
        "runny",
        67
      ],
      "horse": [
        "south",
        73
      ],
      "hosed": [
        "split-guess-mosey",
        37
      ],
      "hotel": [
        "split",
        49
      ],
      "hotly": [
        "sloth",
        50
      ],
      "hound": [
        "gluts-whomp",
        39
      ],
      "house": [
        "toils-dumpy",
        33
      ],
      "hovel": [
        "split-dweeb-kugel",
        17
      ],
      "hover": [
        "betel-whips-homer",
        32
      ],
      "howdy": [
        "sloth-hobby-hoppy",
        29
      ],
      "hubby": [
        "sloth-huffy",
        37
      ],
      "huffy": [
        "sloth",
        53
      ],
      "hulky": [
        "sloth-hilly",
        32
      ],
      "human": [
        "natal",
        58
      ],
      "humid": [
        "sloth-huffy",
        37
      ],
      "humor": [
        "shout",
        53
      ],
      "humph": [
        "sloth",
        50
      ],
      "humus": [
        "sloth-might",
        39
      ],
      "hunch": [
        "posit-blame",
        46
      ],
      "hunky": [
        "pinot-fight",
        41
      ],
      "hurry": [
        "shout",
        60
      ],
      "husky": [
        "sloth-might",
        39
      ],
      "hussy": [
        "sloth-might-husky",
        27
      ],
      "hutch": [
        "spoil-humid",
        41
      ],
      "hydra": [
        "tyros",
        65
      ],
      "hydro": [
        "shout-morph",
        41
      ],
      "hyena": [
        "agent",
        66
      ],
      "hymen": [
        "towel-hived",
        41
      ],
      "hyped": [
        "split-dopey",
        30
      ],
      "hyper": [
        "betel-whips",
        43
      ],
      "icier": [
        "hirer",
        75
      ],
      "icily": [
        "spoil-flick",
        37
      ],
      "icing": [
        "",
        99
      ],
      "ideal": [
        "petal",
        59
      ],
      "idiom": [
        "sloth-gumbo",
        33
      ],
      "idiot": [
        "sloth-doubt",
        29
      ],
      "idled": [
        "split-flown",
        43
      ],
      "idler": [
        "betel-folic-miler",
        30
      ],
      "idyll": [
        "sloth-billy",
        30
      ],
      "igloo": [
        "sloth-dolly",
        30
      ],
      "iliac": [
        "hotly-lilac",
        46
      ],
      "image": [
        "sloth-agave",
        43
      ],
      "imbed": [
        "split-edify-video",
        27
      ],
      "imbue": [
        "toils-pique",
        38
      ],
      "impel": [
        "split-pixel",
        40
      ],
      "imply": [
        "sloth-billy",
        30
      ],
      "inane": [
        "plane",
        61
      ],
      "inapt": [
        "slain",
        78
      ],
      "inbox": [
        "pinot-union",
        38
      ],
      "incel": [
        "bench",
        60
      ],
      "incur": [
        "scorn",
        64
      ],
      "index": [
        "towel-hived",
        41
      ],
      "indie": [
        "deist",
        73
      ],
      "inept": [
        "towel",
        63
      ],
      "inert": [
        "rites",
        73
      ],
      "infer": [
        "rites-inner",
        45
      ],
      "ingot": [
        "pinot",
        61
      ],
      "inked": [
        "towel-hived",
        41
      ],
      "inlay": [
        "natal",
        73
      ],
      "inlet": [
        "towel",
        68
      ],
      "inner": [
        "rites",
        62
      ],
      "input": [
        "pinot",
        61
      ],
      "inset": [
        "towel-unmet",
        47
      ],
      "intel": [
        "towel",
        68
      ],
      "inter": [
        "rites",
        73
      ],
      "intro": [
        "boson",
        59
      ],
      "inure": [
        "nurse",
        67
      ],
      "ionic": [
        "posit",
        75
      ],
      "irate": [
        "digit",
        83
      ],
      "irked": [
        "defer-tried",
        38
      ],
      "irony": [
        "bigot",
        73
      ],
      "islet": [
        "split",
        56
      ],
      "issue": [
        "toils-siege",
        37
      ],
      "itchy": [
        "spoil-which",
        35
      ],
      "ivied": [
        "split-edify",
        36
      ],
      "ivory": [
        "shout-glory",
        33
      ],
      "jaded": [
        "petal-fades",
        41
      ],
      "jammy": [
        "toils-dumpy-hammy",
        20
      ],
      "janky": [
        "natal-demos",
        38
      ],
      "jaunt": [
        "tings-hived",
        44
      ],
      "jawed": [
        "petal-fades-baked-weigh",
        39
      ],
      "jazzy": [
        "toils-dumpy-baggy",
        18
      ],
      "jelly": [
        "split-belly",
        34
      ],
      "jerky": [
        "betel-smirk-perky",
        23
      ],
      "jetty": [
        "split-teeth",
        30
      ],
      "jewel": [
        "split-dweeb",
        32
      ],
      "jibed": [
        "split-edify-video-bumpy-gibed",
        28
      ],
      "jiffy": [
        "sloth-dumpy-fizzy",
        19
      ],
      "jimmy": [
        "sloth-dumpy",
        28
      ],
      "joint": [
        "gluts-point",
        39
      ],
      "joist": [
        "sloth-moist-foist",
        28
      ],
      "joked": [
        "split-dogma-oxbow-yoked",
        17
      ],
      "joker": [
        "betel-whips-roofs-mover",
        23
      ],
      "jokey": [
        "split-dogma-hokey",
        20
      ],
      "jolly": [
        "sloth-dolly-fjord",
        27
      ],
      "joule": [
        "toils-boule",
        38
      ],
      "joust": [
        "sloth-moist",
        44
      ],
      "jowly": [
        "sloth-dolly",
        30
      ],
      "judge": [
        "toils-fudge",
        31
      ],
      "judgy": [
        "sloth-dumpy-fudgy",
        16
      ],
      "juice": [
        "pious",
        71
      ],
      "juicy": [
        "spoil-which",
        34
      ],
      "juked": [
        "split-dogma-weedy",
        26
      ],
      "julep": [
        "split",
        54
      ],
      "jumbo": [
        "sloth-gumbo",
        33
      ],
      "jumpy": [
        "sloth-dumpy-bumpy",
        16
      ],
      "junky": [
        "pinot-fight",
        41
      ],
      "junta": [
        "natal-angst",
        46
      ],
      "junto": [
        "pinot-month",
        41
      ],
      "juror": [
        "shout-furor",
        33
      ],
      "kabob": [
        "toils-bayou",
        35
      ],
      "kappa": [
        "toils-dumpy",
        33
      ],
      "kaput": [
        "toils-bumpy",
        34
      ],
      "karat": [
        "tyros-atria",
        42
      ],
      "karma": [
        "tyros-mural",
        38
      ],
      "kayak": [
        "toils-dumpy",
        33
      ],
      "kazoo": [
        "toils-bayou",
        35
      ],
      "kebab": [
        "petal",
        70
      ],
      "kempt": [
        "split-tempt",
        40
      ],
      "keyed": [
        "split-dogma-weedy",
        26
      ],
      "khaki": [
        "spilt",
        67
      ],
      "kiddo": [
        "sloth-gumbo",
        33
      ],
      "kinda": [
        "natal-annoy",
        43
      ],
      "kinky": [
        "pinot-desks",
        25
      ],
      "kiosk": [
        "sloth-pious",
        38
      ],
      "kissy": [
        "sloth-dusky",
        43
      ],
      "kitty": [
        "sloth-batik",
        44
      ],
      "klutz": [
        "sloth-blitz",
        38
      ],
      "knack": [
        "snack",
        61
      ],
      "knave": [
        "snake",
        60
      ],
      "knead": [
        "sleep",
        72
      ],
      "kneed": [
        "towel-hived-unfed",
        39
      ],
      "kneel": [
        "towel",
        68
      ],
      "knell": [
        "towel",
        68
      ],
      "knelt": [
        "towel",
        68
      ],
      "knife": [
        "deist",
        73
      ],
      "knish": [
        "pinot-unify",
        35
      ],
      "knock": [
        "posit",
        75
      ],
      "knoll": [
        "pinot-snowy",
        37
      ],
      "known": [
        "pinot-snowy",
        37
      ],
      "koala": [
        "spilt",
        66
      ],
      "kooky": [
        "sloth-gazed",
        31
      ],
      "koran": [
        "rayon-adorn",
        47
      ],
      "krill": [
        "pilot-fudge",
        43
      ],
      "kudos": [
        "sloth-modus",
        32
      ],
      "kudzu": [
        "sloth-dumpy",
        28
      ],
      "kugel": [
        "split-dweeb",
        29
      ],
      "kvell": [
        "split-dweeb-quell",
        20
      ],
      "label": [
        "petal-bagel",
        49
      ],
      "labor": [
        "tyros-valor",
        42
      ],
      "laced": [
        "fecal-lacey",
        44
      ],
      "lacey": [
        "fecal",
        61
      ],
      "laden": [
        "sleep",
        62
      ],
      "ladle": [
        "talus-badge",
        46
      ],
      "lager": [
        "tales-layer",
        54
      ],
      "laity": [
        "toils",
        53
      ],
      "lamed": [
        "petal-alley-movie",
        47
      ],
      "lamer": [
        "tales-layer-lager",
        42
      ],
      "lance": [
        "dance",
        60
      ],
      "lanky": [
        "natal-manly",
        41
      ],
      "lapel": [
        "petal",
        70
      ],
      "lapse": [
        "talus",
        69
      ],
      "larch": [
        "scram",
        49
      ],
      "large": [
        "lairs",
        76
      ],
      "larva": [
        "tyros-mural",
        38
      ],
      "laser": [
        "tales",
        71
      ],
      "lasso": [
        "toils-salvo",
        39
      ],
      "latch": [
        "hotly",
        75
      ],
      "later": [
        "tales",
        71
      ],
      "latex": [
        "petal",
        70
      ],
      "lathe": [
        "talus-latte",
        54
      ],
      "latke": [
        "talus-latte-lathe",
        42
      ],
      "latte": [
        "talus",
        64
      ],
      "laugh": [
        "toils-allay",
        28
      ],
      "laved": [
        "petal-alley-movie",
        47
      ],
      "layer": [
        "tales",
        66
      ],
      "layup": [
        "toils-allay",
        28
      ],
      "lazed": [
        "petal-alley-movie",
        47
      ],
      "leach": [
        "leapt",
        72
      ],
      "leafy": [
        "lefts",
        73
      ],
      "leaky": [
        "lefts",
        73
      ],
      "leant": [
        "meant",
        50
      ],
      "leapt": [
        "lefts",
        73
      ],
      "learn": [
        "",
        86
      ],
      "lease": [
        "sloth",
        75
      ],
      "leash": [
        "lefts",
        73
      ],
      "least": [
        "lefts",
        73
      ],
      "leave": [
        "sloth",
        75
      ],
      "ledge": [
        "toils-dumpy",
        30
      ],
      "leech": [
        "pilot-excel",
        38
      ],
      "leery": [
        "betel",
        60
      ],
      "lefty": [
        "split-hotel",
        32
      ],
      "legal": [
        "petal-medal",
        43
      ],
      "leggy": [
        "split-dweeb",
        32
      ],
      "legit": [
        "split",
        56
      ],
      "lemma": [
        "petal-fella",
        42
      ],
      "lemon": [
        "towel",
        61
      ],
      "lemur": [
        "betel-reply",
        45
      ],
      "leper": [
        "betel-lever",
        45
      ],
      "letup": [
        "split",
        56
      ],
      "levee": [
        "toils-dumpy",
        30
      ],
      "level": [
        "split-dweeb",
        32
      ],
      "lever": [
        "betel",
        61
      ],
      "lexis": [
        "split",
        56
      ],
      "libel": [
        "split-windy",
        43
      ],
      "licit": [
        "spoil-lucid",
        42
      ],
      "liege": [
        "toils-belie",
        40
      ],
      "lifer": [
        "betel-folic",
        46
      ],
      "light": [
        "sloth",
        50
      ],
      "liked": [
        "split-windy-field",
        40
      ],
      "liken": [
        "towel-linen",
        50
      ],
      "lilac": [
        "hotly",
        62
      ],
      "limbo": [
        "sloth-dolly",
        30
      ],
      "limit": [
        "sloth-guilt",
        41
      ],
      "lined": [
        "towel-linen",
        53
      ],
      "linen": [
        "towel",
        59
      ],
      "liner": [
        "rites-medal",
        47
      ],
      "lingo": [
        "pinot",
        56
      ],
      "lipid": [
        "sloth-billy-vigil",
        14
      ],
      "lippy": [
        "sloth-billy",
        30
      ],
      "liter": [
        "betel",
        60
      ],
      "lithe": [
        "toils",
        61
      ],
      "litre": [
        "south-metre",
        42
      ],
      "lived": [
        "split-windy-field-liked",
        30
      ],
      "liven": [
        "towel-linen-liken",
        38
      ],
      "liver": [
        "betel-folic",
        39
      ],
      "livid": [
        "sloth-billy-vigil",
        14
      ],
      "llama": [
        "spilt-flaky",
        39
      ],
      "loamy": [
        "spilt-flaky",
        39
      ],
      "loath": [
        "spilt",
        73
      ],
      "lobby": [
        "sloth-dolly",
        30
      ],
      "lobed": [
        "split-dweeb",
        29
      ],
      "local": [
        "hotly-lover",
        52
      ],
      "locus": [
        "spoil",
        63
      ],
      "lodge": [
        "toils",
        60
      ],
      "loess": [
        "split-flesh",
        40
      ],
      "lofty": [
        "sloth",
        55
      ],
      "logic": [
        "spoil",
        58
      ],
      "login": [
        "pinot-noisy",
        40
      ],
      "logon": [
        "pinot-swoon",
        37
      ],
      "lolly": [
        "sloth-dolly-fjord-golly-molly",
        13
      ],
      "loner": [
        "rites-below",
        42
      ],
      "loony": [
        "gluts",
        66
      ],
      "loopy": [
        "sloth",
        55
      ],
      "loose": [
        "toils",
        56
      ],
      "loped": [
        "split-expel",
        39
      ],
      "lordy": [
        "shout-dowry",
        32
      ],
      "lorry": [
        "shout-dowry",
        32
      ],
      "loser": [
        "betel-folic",
        41
      ],
      "lotto": [
        "sloth-lofty",
        39
      ],
      "lotus": [
        "sloth",
        50
      ],
      "loupe": [
        "toils-lodge",
        44
      ],
      "louse": [
        "toils-loose",
        39
      ],
      "lousy": [
        "sloth",
        55
      ],
      "loved": [
        "split-dweeb-model",
        17
      ],
      "lover": [
        "betel-folic-loser-lower",
        27
      ],
      "lower": [
        "betel-folic-loser",
        37
      ],
      "lowly": [
        "sloth-dolly",
        30
      ],
      "loyal": [
        "toils",
        54
      ],
      "lubed": [
        "split-dweeb-lobed",
        16
      ],
      "lucid": [
        "spoil",
        59
      ],
      "lucky": [
        "spoil-mulch",
        41
      ],
      "lucre": [
        "score",
        67
      ],
      "luger": [
        "betel-folic",
        47
      ],
      "lumen": [
        "towel-linen",
        53
      ],
      "lumpy": [
        "sloth-billy",
        30
      ],
      "lunar": [
        "rayon",
        59
      ],
      "lunch": [
        "posit-blame",
        46
      ],
      "lunge": [
        "deist-noble",
        37
      ],
      "lupus": [
        "sloth",
        50
      ],
      "lurch": [
        "soupy",
        71
      ],
      "lured": [
        "betel-folic-luger",
        35
      ],
      "lurid": [
        "shout",
        48
      ],
      "lusty": [
        "sloth",
        50
      ],
      "luted": [
        "split-hotel",
        32
      ],
      "lying": [
        "gluts",
        66
      ],
      "lymph": [
        "sloth",
        50
      ],
      "lyric": [
        "soupy",
        71
      ],
      "macaw": [
        "hotly-basic",
        40
      ],
      "macho": [
        "hotly",
        60
      ],
      "macro": [
        "scram",
        70
      ],
      "madam": [
        "toils-dumpy",
        33
      ],
      "madly": [
        "toils",
        50
      ],
      "mafia": [
        "toils",
        47
      ],
      "magic": [
        "hotly-basic",
        40
      ],
      "magma": [
        "toils-dumpy",
        33
      ],
      "maize": [
        "talus-maybe",
        44
      ],
      "major": [
        "tyros-valor",
        39
      ],
      "maker": [
        "tales-pygmy",
        52
      ],
      "malic": [
        "hotly-lilac",
        46
      ],
      "malty": [
        "toils-waltz",
        39
      ],
      "mamba": [
        "toils-dumpy-gamma",
        19
      ],
      "mambo": [
        "toils-bayou",
        35
      ],
      "mamma": [
        "toils-dumpy-gamma",
        19
      ],
      "manga": [
        "natal-mania",
        45
      ],
      "mange": [
        "gloms",
        69
      ],
      "mango": [
        "natal-demos",
        47
      ],
      "mangy": [
        "natal-demos",
        47
      ],
      "mania": [
        "natal",
        62
      ],
      "manic": [
        "panic",
        74
      ],
      "manly": [
        "natal",
        58
      ],
      "manna": [
        "tings-nanny",
        54
      ],
      "manor": [
        "rayon",
        71
      ],
      "manse": [
        "gloms",
        69
      ],
      "maple": [
        "talus-badge",
        46
      ],
      "march": [
        "scram",
        70
      ],
      "marry": [
        "tyros-parry",
        43
      ],
      "marsh": [
        "tyros-harsh",
        41
      ],
      "mason": [
        "natal-demos",
        47
      ],
      "masse": [
        "talus",
        66
      ],
      "match": [
        "hotly-swamp",
        48
      ],
      "mated": [
        "petal-gated-shame",
        48
      ],
      "matey": [
        "petal-gated",
        45
      ],
      "matte": [
        "talus-bathe",
        47
      ],
      "matzo": [
        "toils-adopt",
        39
      ],
      "mauve": [
        "talus-gauge",
        46
      ],
      "maven": [
        "sleep-known-haven",
        31
      ],
      "maxed": [
        "petal-fades-baked-weigh",
        37
      ],
      "maxim": [
        "toils-mafia",
        30
      ],
      "maybe": [
        "talus",
        55
      ],
      "mayor": [
        "tyros",
        65
      ],
      "mealy": [
        "lefts",
        73
      ],
      "meant": [
        "",
        75
      ],
      "meaty": [
        "lefts-death",
        45
      ],
      "mecca": [
        "fecal",
        67
      ],
      "medal": [
        "petal",
        59
      ],
      "media": [
        "petal",
        63
      ],
      "medic": [
        "pilot",
        71
      ],
      "melee": [
        "toils-dumpy",
        30
      ],
      "melon": [
        "towel-lemon",
        45
      ],
      "mensa": [
        "sleep",
        72
      ],
      "merch": [
        "hirer-perch",
        44
      ],
      "mercy": [
        "hirer",
        75
      ],
      "merge": [
        "south-verge",
        38
      ],
      "merit": [
        "betel",
        58
      ],
      "merry": [
        "betel-smirk",
        43
      ],
      "meshy": [
        "split-guess-mosey",
        28
      ],
      "messy": [
        "split-guess",
        37
      ],
      "metal": [
        "petal",
        59
      ],
      "meted": [
        "split-teeth",
        30
      ],
      "meter": [
        "betel-deter",
        52
      ],
      "metre": [
        "south",
        59
      ],
      "metro": [
        "betel-retro",
        44
      ],
      "mewed": [
        "split-dogma-embed",
        26
      ],
      "mezzo": [
        "split-dogma",
        34
      ],
      "micro": [
        "soupy",
        71
      ],
      "midge": [
        "toils-pique-gimme",
        24
      ],
      "midst": [
        "sloth",
        51
      ],
      "might": [
        "sloth-thump",
        36
      ],
      "miked": [
        "split-edify-video-bumpy",
        36
      ],
      "miler": [
        "betel-folic",
        42
      ],
      "milky": [
        "sloth-billy",
        32
      ],
      "mimed": [
        "split-edify-video-bumpy",
        39
      ],
      "mimic": [
        "spoil",
        63
      ],
      "mince": [
        "humps",
        80
      ],
      "mined": [
        "towel-hived-denim",
        36
      ],
      "miner": [
        "rites-medal",
        47
      ],
      "minim": [
        "pinot-desks-vinyl",
        16
      ],
      "minor": [
        "boson",
        72
      ],
      "minty": [
        "pinot-ninth",
        42
      ],
      "minus": [
        "pinot-desks",
        36
      ],
      "mired": [
        "betel-whips-river",
        32
      ],
      "mirin": [
        "boson",
        72
      ],
      "mirth": [
        "shout-birth-girth",
        36
      ],
      "miser": [
        "betel-whips-riser",
        32
      ],
      "missy": [
        "sloth-dusky-wispy",
        27
      ],
      "misty": [
        "sloth-fudge",
        44
      ],
      "miter": [
        "betel-outer",
        37
      ],
      "mixed": [
        "split-edify-video-bumpy-miked",
        28
      ],
      "mixer": [
        "betel-whips-river",
        32
      ],
      "mixup": [
        "sloth-dumpy",
        28
      ],
      "mocha": [
        "hotly",
        75
      ],
      "mochi": [
        "spoil",
        63
      ],
      "modal": [
        "toils-loyal",
        37
      ],
      "model": [
        "split-dweeb",
        30
      ],
      "modem": [
        "split-dogma",
        38
      ],
      "modus": [
        "sloth",
        49
      ],
      "mogul": [
        "sloth-dolly",
        30
      ],
      "moist": [
        "sloth",
        55
      ],
      "molar": [
        "tyros-amour",
        40
      ],
      "moldy": [
        "sloth-dolly",
        30
      ],
      "molly": [
        "sloth-dolly-fjord-golly",
        22
      ],
      "momma": [
        "toils-vodka",
        39
      ],
      "mommy": [
        "sloth-gumbo",
        33
      ],
      "money": [
        "towel-honey",
        39
      ],
      "month": [
        "pinot",
        57
      ],
      "mooch": [
        "spoil-hooch",
        41
      ],
      "moody": [
        "sloth-gazed",
        39
      ],
      "mooed": [
        "split-dogma-modem-wrote",
        30
      ],
      "moony": [
        "gluts-phony",
        36
      ],
      "moose": [
        "toils-dumpy",
        33
      ],
      "moped": [
        "split-dopey",
        35
      ],
      "moper": [
        "betel-whips-purer-doper",
        18
      ],
      "mopey": [
        "split-dopey",
        30
      ],
      "moral": [
        "tyros",
        63
      ],
      "moray": [
        "tyros-foray",
        45
      ],
      "morel": [
        "betel",
        60
      ],
      "moron": [
        "boson",
        72
      ],
      "morph": [
        "shout",
        57
      ],
      "mosey": [
        "split-guess",
        40
      ],
      "mossy": [
        "sloth-modus",
        32
      ],
      "motel": [
        "split-hotel",
        32
      ],
      "motif": [
        "sloth-doubt",
        29
      ],
      "motor": [
        "shout",
        51
      ],
      "motto": [
        "sloth-ditto",
        38
      ],
      "mould": [
        "sloth-dolly-would",
        20
      ],
      "moult": [
        "sloth-pilot",
        32
      ],
      "mound": [
        "gluts-whomp",
        39
      ],
      "mount": [
        "gluts",
        64
      ],
      "mourn": [
        "boson",
        72
      ],
      "mouse": [
        "toils-dumpy",
        33
      ],
      "mousy": [
        "sloth-modus",
        32
      ],
      "mouth": [
        "sloth",
        54
      ],
      "moved": [
        "split-dogma-modem-wrote",
        30
      ],
      "mover": [
        "betel-whips-roofs",
        27
      ],
      "movie": [
        "toils",
        56
      ],
      "mowed": [
        "split-dogma-modem-wrote",
        30
      ],
      "mower": [
        "betel-whips",
        44
      ],
      "moxie": [
        "toils-movie",
        39
      ],
      "mucky": [
        "spoil-humid",
        41
      ],
      "mucus": [
        "spoil",
        63
      ],
      "muddy": [
        "sloth-dumpy",
        28
      ],
      "muggy": [
        "sloth-dumpy",
        28
      ],
      "mulch": [
        "spoil",
        57
      ],
      "mummy": [
        "sloth-dumpy-gummy",
        25
      ],
      "munch": [
        "posit-blame",
        46
      ],
      "mural": [
        "tyros",
        50
      ],
      "murky": [
        "shout-lurid",
        34
      ],
      "mused": [
        "split-guess-frame",
        31
      ],
      "mushy": [
        "sloth-might",
        39
      ],
      "music": [
        "spoil",
        63
      ],
      "musky": [
        "sloth-dusky",
        43
      ],
      "musty": [
        "sloth-fudge",
        39
      ],
      "muted": [
        "split-teeth-voted",
        21
      ],
      "myrrh": [
        "shout",
        60
      ],
      "nabob": [
        "natal-nappy",
        44
      ],
      "nacho": [
        "panic-bacon",
        43
      ],
      "nadir": [
        "rayon",
        71
      ],
      "naggy": [
        "natal-nappy",
        44
      ],
      "naive": [
        "gloms",
        69
      ],
      "naked": [
        "sleep-known",
        49
      ],
      "named": [
        "sleep-known",
        49
      ],
      "nanny": [
        "tings",
        70
      ],
      "nappy": [
        "natal",
        61
      ],
      "nasal": [
        "natal-naval",
        48
      ],
      "nasty": [
        "natal",
        73
      ],
      "natal": [
        "",
        79
      ],
      "natty": [
        "natal",
        73
      ],
      "naval": [
        "natal",
        65
      ],
      "navel": [
        "sleep-laden",
        46
      ],
      "needy": [
        "towel-deign",
        34
      ],
      "neigh": [
        "towel-deign",
        37
      ],
      "nerdy": [
        "rites",
        62
      ],
      "nerve": [
        "nurse",
        67
      ],
      "nervy": [
        "rites-nerdy",
        45
      ],
      "never": [
        "rites-below",
        42
      ],
      "newer": [
        "rites-below",
        42
      ],
      "newly": [
        "towel",
        68
      ],
      "newsy": [
        "towel",
        68
      ],
      "nexus": [
        "towel-deign",
        37
      ],
      "nicer": [
        "",
        85
      ],
      "niche": [
        "humps",
        80
      ],
      "niece": [
        "humps",
        61
      ],
      "nifty": [
        "pinot",
        61
      ],
      "night": [
        "pinot",
        61
      ],
      "nimby": [
        "pinot",
        61
      ],
      "ninja": [
        "natal",
        73
      ],
      "ninny": [
        "gluts-phony",
        36
      ],
      "ninth": [
        "pinot",
        59
      ],
      "nippy": [
        "pinot",
        61
      ],
      "nitro": [
        "boson-intro",
        42
      ],
      "nixed": [
        "towel-hived-denim",
        36
      ],
      "noble": [
        "deist",
        54
      ],
      "nobly": [
        "pinot-snowy",
        37
      ],
      "nodal": [
        "natal",
        73
      ],
      "noise": [
        "deist",
        73
      ],
      "noisy": [
        "pinot",
        57
      ],
      "nomad": [
        "natal",
        73
      ],
      "noose": [
        "deist",
        73
      ],
      "north": [
        "boson",
        72
      ],
      "nosed": [
        "towel-honey-dozen",
        35
      ],
      "nosey": [
        "towel-honey",
        47
      ],
      "notch": [
        "posit",
        75
      ],
      "noted": [
        "towel",
        68
      ],
      "novel": [
        "towel",
        68
      ],
      "nudge": [
        "deist",
        56
      ],
      "nuked": [
        "towel-hived-unfed",
        31
      ],
      "nurse": [
        "",
        92
      ],
      "nutso": [
        "pinot",
        61
      ],
      "nutty": [
        "pinot",
        61
      ],
      "nylon": [
        "pinot-swoon",
        37
      ],
      "nymph": [
        "pinot",
        61
      ],
      "oaken": [
        "sleep-known",
        49
      ],
      "oared": [
        "tales-pygmy-forks",
        39
      ],
      "oasis": [
        "toils",
        53
      ],
      "obese": [
        "toils-spoke",
        31
      ],
      "occur": [
        "soupy",
        71
      ],
      "ocean": [
        "",
        86
      ],
      "ocher": [
        "hirer",
        75
      ],
      "ochre": [
        "score",
        67
      ],
      "octal": [
        "hotly",
        75
      ],
      "octet": [
        "pilot",
        71
      ],
      "odder": [
        "betel-whips-roofs",
        30
      ],
      "oddly": [
        "sloth-dolly",
        30
      ],
      "offal": [
        "toils-allow",
        32
      ],
      "offed": [
        "split-dogma",
        34
      ],
      "offer": [
        "betel-whips-roofs",
        30
      ],
      "often": [
        "towel-onset",
        48
      ],
      "ogled": [
        "split-belly-golem",
        26
      ],
      "ogler": [
        "betel-folic",
        46
      ],
      "oiled": [
        "split-flown",
        43
      ],
      "oiler": [
        "betel-folic",
        46
      ],
      "okapi": [
        "spilt",
        73
      ],
      "olden": [
        "towel",
        68
      ],
      "older": [
        "betel-folic",
        46
      ],
      "oldie": [
        "toils",
        61
      ],
      "olive": [
        "toils",
        61
      ],
      "ombre": [
        "south",
        73
      ],
      "omega": [
        "petal-fades",
        38
      ],
      "onion": [
        "pinot-union",
        38
      ],
      "onset": [
        "towel",
        65
      ],
      "oomph": [
        "sloth-dough",
        38
      ],
      "oozed": [
        "split-dogma-oxbow",
        27
      ],
      "opera": [
        "tales-rehab",
        46
      ],
      "opine": [
        "whips",
        68
      ],
      "opium": [
        "sloth-gumbo",
        33
      ],
      "opted": [
        "split",
        56
      ],
      "optic": [
        "spoil",
        63
      ],
      "orate": [
        "digit",
        83
      ],
      "orbed": [
        "defer-tried",
        41
      ],
      "orbit": [
        "pilot",
        65
      ],
      "order": [
        "defer",
        74
      ],
      "organ": [
        "",
        92
      ],
      "other": [
        "betel-tiger",
        43
      ],
      "otter": [
        "betel-outer",
        45
      ],
      "ought": [
        "sloth",
        50
      ],
      "ouija": [
        "toils-axiom",
        37
      ],
      "ounce": [
        "humps",
        65
      ],
      "outdo": [
        "sloth-doubt",
        29
      ],
      "outed": [
        "split-teeth-voted",
        21
      ],
      "outer": [
        "betel",
        59
      ],
      "outgo": [
        "sloth-doubt",
        29
      ],
      "outre": [
        "south",
        73
      ],
      "ovary": [
        "midst-hoary",
        44
      ],
      "ovate": [
        "sloth",
        75
      ],
      "overt": [
        "betel-twerp",
        45
      ],
      "ovine": [
        "whips",
        68
      ],
      "ovoid": [
        "sloth-gazed",
        41
      ],
      "owing": [
        "gluts-doing",
        37
      ],
      "owned": [
        "towel",
        68
      ],
      "owner": [
        "rites-below",
        42
      ],
      "oxbow": [
        "sloth-gumbo-bipod",
        22
      ],
      "oxide": [
        "toils",
        61
      ],
      "ozone": [
        "whips",
        68
      ],
      "paced": [
        "fecal",
        67
      ],
      "pacer": [
        "recap",
        64
      ],
      "paddy": [
        "toils-dumpy",
        33
      ],
      "padre": [
        "lairs-barre",
        44
      ],
      "paean": [
        "sleep",
        72
      ],
      "pagan": [
        "natal",
        73
      ],
      "paged": [
        "petal-grave",
        48
      ],
      "pager": [
        "tales-pygmy",
        50
      ],
      "paint": [
        "tings",
        65
      ],
      "paled": [
        "petal",
        70
      ],
      "paler": [
        "tales",
        61
      ],
      "palsy": [
        "toils-salad",
        30
      ],
      "panda": [
        "natal-mania",
        45
      ],
      "panel": [
        "sleep",
        72
      ],
      "panic": [
        "",
        92
      ],
      "panko": [
        "natal-demos-banjo",
        28
      ],
      "panty": [
        "natal-tangy",
        47
      ],
      "papal": [
        "toils-allay",
        28
      ],
      "paper": [
        "tales-pygmy",
        48
      ],
      "parch": [
        "scram-larch",
        33
      ],
      "pared": [
        "tales-pygmy-paper",
        41
      ],
      "parer": [
        "tales-pygmy-paper-paver",
        29
      ],
      "parka": [
        "tyros-mural",
        38
      ],
      "parry": [
        "tyros",
        58
      ],
      "parse": [
        "lairs",
        76
      ],
      "party": [
        "tyros",
        61
      ],
      "passe": [
        "talus-masse",
        50
      ],
      "pasta": [
        "toils",
        53
      ],
      "paste": [
        "talus-whoop",
        50
      ],
      "pasty": [
        "toils-pasta",
        36
      ],
      "patch": [
        "hotly-swamp",
        48
      ],
      "patio": [
        "toils",
        53
      ],
      "patsy": [
        "toils-pasta",
        36
      ],
      "patty": [
        "toils-bumpy",
        34
      ],
      "pause": [
        "talus",
        72
      ],
      "paved": [
        "petal-grave",
        48
      ],
      "paver": [
        "tales-pygmy-paper",
        39
      ],
      "pawed": [
        "petal-grave",
        48
      ],
      "payee": [
        "talus-maybe",
        44
      ],
      "payer": [
        "tales-pygmy",
        50
      ],
      "peace": [
        "scale",
        61
      ],
      "peach": [
        "leapt",
        72
      ],
      "pearl": [
        "badly",
        80
      ],
      "peaty": [
        "lefts-death-meaty",
        33
      ],
      "pecan": [
        "ocean",
        61
      ],
      "pedal": [
        "petal",
        70
      ],
      "peeve": [
        "toils-fudge",
        35
      ],
      "penal": [
        "sleep",
        72
      ],
      "pence": [
        "humps",
        80
      ],
      "penne": [
        "whips",
        68
      ],
      "penny": [
        "tipsy",
        57
      ],
      "peony": [
        "tipsy-penny",
        40
      ],
      "peppy": [
        "split-dopey",
        30
      ],
      "perch": [
        "hirer",
        60
      ],
      "peril": [
        "betel",
        60
      ],
      "perky": [
        "betel-smirk",
        35
      ],
      "pesky": [
        "split",
        56
      ],
      "pesto": [
        "split",
        56
      ],
      "petal": [
        "",
        78
      ],
      "peter": [
        "betel-deter-meter",
        40
      ],
      "petit": [
        "split",
        56
      ],
      "petri": [
        "betel-retro",
        44
      ],
      "petty": [
        "split-empty",
        37
      ],
      "phage": [
        "sloth-heave",
        50
      ],
      "phase": [
        "sloth",
        75
      ],
      "phish": [
        "sloth",
        50
      ],
      "phone": [
        "whips",
        68
      ],
      "phony": [
        "gluts",
        49
      ],
      "photo": [
        "sloth",
        50
      ],
      "piano": [
        "ghost",
        78
      ],
      "picky": [
        "spoil-pitch",
        40
      ],
      "piece": [
        "pious",
        71
      ],
      "piety": [
        "split",
        56
      ],
      "piggy": [
        "sloth-dumpy",
        28
      ],
      "piked": [
        "split-biped",
        37
      ],
      "piker": [
        "betel-whips-piper",
        38
      ],
      "pilaf": [
        "toils-valid",
        38
      ],
      "piled": [
        "split",
        56
      ],
      "pilot": [
        "sloth",
        48
      ],
      "pinch": [
        "posit",
        75
      ],
      "pined": [
        "towel-hived-denim",
        33
      ],
      "piney": [
        "towel-hived",
        41
      ],
      "pinky": [
        "pinot-pinup",
        39
      ],
      "pinot": [
        "",
        69
      ],
      "pinto": [
        "pinot",
        61
      ],
      "pinup": [
        "pinot",
        56
      ],
      "pious": [
        "sloth",
        55
      ],
      "piped": [
        "split-biped-wiped",
        34
      ],
      "piper": [
        "betel-whips",
        44
      ],
      "pipet": [
        "split",
        56
      ],
      "pique": [
        "toils",
        49
      ],
      "piste": [
        "toils",
        61
      ],
      "pitch": [
        "spoil",
        57
      ],
      "pithy": [
        "sloth-thump",
        36
      ],
      "pivot": [
        "sloth-doubt",
        29
      ],
      "pixel": [
        "split",
        57
      ],
      "pixie": [
        "toils-pique",
        38
      ],
      "pizza": [
        "toils-mafia",
        30
      ],
      "place": [
        "scale",
        76
      ],
      "plaid": [
        "spilt",
        73
      ],
      "plain": [
        "slain",
        78
      ],
      "plait": [
        "spilt",
        73
      ],
      "plane": [
        "",
        86
      ],
      "plank": [
        "ghost-bland-flank",
        35
      ],
      "plant": [
        "ghost",
        66
      ],
      "plasm": [
        "spilt",
        73
      ],
      "plate": [
        "sloth",
        63
      ],
      "playa": [
        "spilt-plaza",
        43
      ],
      "plaza": [
        "spilt",
        59
      ],
      "plead": [
        "petal",
        70
      ],
      "pleat": [
        "petal",
        70
      ],
      "plebe": [
        "toils-dumpy",
        30
      ],
      "plied": [
        "split-pixel",
        40
      ],
      "plier": [
        "betel-folic-liver",
        27
      ],
      "plink": [
        "gluts-blond",
        35
      ],
      "plonk": [
        "gluts-blond",
        35
      ],
      "pluck": [
        "spoil",
        63
      ],
      "plumb": [
        "sloth-bluff",
        34
      ],
      "plume": [
        "toils-dumpy",
        30
      ],
      "plump": [
        "sloth-bluff",
        34
      ],
      "plunk": [
        "gluts",
        62
      ],
      "plush": [
        "sloth-probe",
        44
      ],
      "poach": [
        "plush",
        76
      ],
      "poesy": [
        "split-pesky",
        39
      ],
      "point": [
        "gluts",
        55
      ],
      "poise": [
        "toils",
        61
      ],
      "poked": [
        "split-dopey",
        30
      ],
      "poker": [
        "betel-whips-purer",
        32
      ],
      "pokey": [
        "split-dopey",
        30
      ],
      "polar": [
        "tyros-amour",
        40
      ],
      "poled": [
        "split-julep",
        37
      ],
      "polio": [
        "sloth-dolly",
        30
      ],
      "polis": [
        "sloth-lousy",
        38
      ],
      "polka": [
        "toils-loyal",
        37
      ],
      "polyp": [
        "sloth-dolly",
        30
      ],
      "pooch": [
        "spoil",
        63
      ],
      "poofy": [
        "sloth-gazed-kooky",
        27
      ],
      "poppy": [
        "sloth-gumbo-widow",
        20
      ],
      "popup": [
        "sloth-gumbo",
        33
      ],
      "porch": [
        "soupy",
        71
      ],
      "pored": [
        "betel-whips-purer",
        32
      ],
      "porky": [
        "shout-dowry",
        32
      ],
      "posed": [
        "split-pesky",
        39
      ],
      "poser": [
        "betel-whips-super",
        33
      ],
      "posit": [
        "sloth-moist",
        44
      ],
      "posse": [
        "toils-dumpy",
        33
      ],
      "potty": [
        "sloth-ditto",
        38
      ],
      "pouch": [
        "spoil",
        63
      ],
      "pound": [
        "gluts-whomp",
        39
      ],
      "pouty": [
        "sloth-ditto",
        38
      ],
      "power": [
        "betel-whips",
        43
      ],
      "prank": [
        "gated-frank",
        44
      ],
      "prawn": [
        "debit",
        71
      ],
      "preen": [
        "green",
        60
      ],
      "press": [
        "defer",
        54
      ],
      "price": [
        "truce",
        64
      ],
      "prick": [
        "trick-brick",
        40
      ],
      "pricy": [
        "trick",
        74
      ],
      "pride": [
        "pivot-armed",
        52
      ],
      "pried": [
        "defer-tried",
        38
      ],
      "prima": [
        "armor",
        74
      ],
      "prime": [
        "pivot-armed",
        52
      ],
      "primo": [
        "pilot",
        70
      ],
      "primp": [
        "pilot-prism",
        39
      ],
      "print": [
        "bigot",
        73
      ],
      "prion": [
        "gibed",
        72
      ],
      "prior": [
        "pilot",
        70
      ],
      "prism": [
        "pilot",
        56
      ],
      "priss": [
        "pilot-prism",
        39
      ],
      "privy": [
        "pilot-prism",
        39
      ],
      "prize": [
        "pivot-armed",
        52
      ],
      "probe": [
        "pivot-prose",
        50
      ],
      "prole": [
        "pivot-prose-probe",
        37
      ],
      "promo": [
        "pilot-proud-proxy",
        37
      ],
      "prone": [
        "",
        92
      ],
      "prong": [
        "bigot-wrong",
        44
      ],
      "proof": [
        "pilot",
        70
      ],
      "prose": [
        "pivot",
        66
      ],
      "proto": [
        "pilot",
        70
      ],
      "proud": [
        "pilot",
        58
      ],
      "prove": [
        "pivot",
        75
      ],
      "prowl": [
        "pilot",
        70
      ],
      "proxy": [
        "pilot-proud",
        50
      ],
      "prude": [
        "pivot",
        75
      ],
      "prune": [
        "prone",
        77
      ],
      "psalm": [
        "spilt",
        73
      ],
      "pshaw": [
        "toils-gassy-squad",
        18
      ],
      "psych": [
        "spoil",
        63
      ],
      "pubic": [
        "spoil",
        63
      ],
      "pudge": [
        "toils-fudge-judge-budge",
        15
      ],
      "pudgy": [
        "sloth-dumpy",
        28
      ],
      "puffy": [
        "sloth-dumpy",
        28
      ],
      "puked": [
        "split-dopey",
        30
      ],
      "pulpy": [
        "sloth-billy",
        30
      ],
      "pulse": [
        "toils",
        61
      ],
      "punch": [
        "posit",
        75
      ],
      "punky": [
        "pinot",
        61
      ],
      "punny": [
        "gluts-funny-bunny",
        40
      ],
      "pupae": [
        "talus",
        72
      ],
      "pupil": [
        "sloth-billy",
        30
      ],
      "puppy": [
        "sloth-dumpy",
        31
      ],
      "puree": [
        "south-purge",
        42
      ],
      "purer": [
        "betel-whips",
        43
      ],
      "purge": [
        "south",
        59
      ],
      "purse": [
        "south",
        73
      ],
      "pushy": [
        "sloth-might-bushy",
        18
      ],
      "putty": [
        "sloth-batik",
        42
      ],
      "pygmy": [
        "sloth-dumpy",
        28
      ],
      "pylon": [
        "pinot",
        61
      ],
      "quack": [
        "plush",
        76
      ],
      "quaff": [
        "spilt-foamy",
        40
      ],
      "quail": [
        "spilt-avail",
        48
      ],
      "quake": [
        "sloth-agave",
        43
      ],
      "qualm": [
        "spilt-koala",
        50
      ],
      "quant": [
        "ghost-plant",
        49
      ],
      "quark": [
        "midst-hoary",
        44
      ],
      "quart": [
        "midst-apart",
        48
      ],
      "quash": [
        "spilt-awash",
        34
      ],
      "quasi": [
        "spilt",
        73
      ],
      "queen": [
        "towel-hived",
        41
      ],
      "queer": [
        "betel-sheer",
        49
      ],
      "quell": [
        "split-dweeb",
        32
      ],
      "query": [
        "betel-fiery",
        45
      ],
      "queso": [
        "split-guess",
        37
      ],
      "quest": [
        "split-guest",
        44
      ],
      "queue": [
        "toils-fudge",
        35
      ],
      "quick": [
        "spoil-which-juicy",
        22
      ],
      "quiet": [
        "split-eight",
        40
      ],
      "quill": [
        "sloth-billy",
        30
      ],
      "quilt": [
        "sloth-guilt-built",
        27
      ],
      "quirk": [
        "shout-lurid",
        39
      ],
      "quite": [
        "toils-white",
        40
      ],
      "quota": [
        "toils-adopt",
        39
      ],
      "quote": [
        "toils",
        58
      ],
      "quoth": [
        "sloth-booth",
        39
      ],
      "quran": [
        "rayon",
        71
      ],
      "rabbi": [
        "tyros-rabid",
        33
      ],
      "rabid": [
        "tyros",
        47
      ],
      "raced": [
        "recap-racer",
        43
      ],
      "racer": [
        "recap",
        59
      ],
      "radar": [
        "tyros-rabid",
        33
      ],
      "radii": [
        "tyros-rabid",
        33
      ],
      "radio": [
        "tyros-amour",
        40
      ],
      "radon": [
        "rayon",
        71
      ],
      "raged": [
        "tales-pygmy-eager",
        43
      ],
      "rager": [
        "tales-pygmy-eager-wager",
        32
      ],
      "rainy": [
        "",
        99
      ],
      "raise": [
        "lairs",
        76
      ],
      "rajah": [
        "tyros-rabid",
        26
      ],
      "raked": [
        "tales-pygmy-forks-baker",
        31
      ],
      "rally": [
        "tyros-dairy",
        51
      ],
      "ralph": [
        "tyros-rabid-rajah",
        14
      ],
      "ramen": [
        "",
        92
      ],
      "ranch": [
        "",
        85
      ],
      "randy": [
        "rayon-rangy",
        38
      ],
      "range": [
        "",
        99
      ],
      "rangy": [
        "rayon",
        54
      ],
      "rapid": [
        "tyros-rabid",
        33
      ],
      "rarer": [
        "tales-pygmy-forks",
        34
      ],
      "raspy": [
        "tyros",
        65
      ],
      "rated": [
        "tales-hewed",
        47
      ],
      "rater": [
        "tales-hewed",
        47
      ],
      "ratio": [
        "tyros",
        59
      ],
      "ratty": [
        "tyros",
        65
      ],
      "raved": [
        "tales-pygmy-forks-waver",
        23
      ],
      "raven": [
        "ramen",
        67
      ],
      "raver": [
        "tales-pygmy-forks-waver",
        23
      ],
      "rayon": [
        "",
        89
      ],
      "razed": [
        "tales-pygmy-forks-waver",
        23
      ],
      "razor": [
        "tyros-valor-major",
        27
      ],
      "reach": [
        "react",
        61
      ],
      "react": [
        "",
        86
      ],
      "ready": [
        "badly",
        80
      ],
      "realm": [
        "badly",
        80
      ],
      "rearm": [
        "badly-heart",
        48
      ],
      "rebar": [
        "tales-rehab",
        46
      ],
      "rebel": [
        "betel",
        60
      ],
      "rebid": [
        "betel-derby",
        41
      ],
      "rebus": [
        "betel-derby",
        49
      ],
      "rebut": [
        "betel",
        60
      ],
      "rebuy": [
        "betel-derby",
        49
      ],
      "recap": [
        "",
        89
      ],
      "recon": [
        "nicer",
        60
      ],
      "recur": [
        "hirer",
        75
      ],
      "recut": [
        "hirer-decry",
        39
      ],
      "redid": [
        "betel-smirk",
        43
      ],
      "redub": [
        "betel-derby-rebid",
        29
      ],
      "redux": [
        "betel-smirk",
        35
      ],
      "reedy": [
        "betel",
        60
      ],
      "refer": [
        "betel-fewer-defer",
        30
      ],
      "refit": [
        "betel-merit",
        47
      ],
      "refry": [
        "betel-smirk-ferry",
        24
      ],
      "regal": [
        "tales",
        68
      ],
      "rehab": [
        "tales",
        58
      ],
      "reify": [
        "betel-smirk",
        43
      ],
      "reign": [
        "rites",
        73
      ],
      "reiki": [
        "betel-smirk",
        43
      ],
      "relax": [
        "tales-relay",
        50
      ],
      "relay": [
        "tales",
        67
      ],
      "relic": [
        "hirer",
        75
      ],
      "relit": [
        "betel",
        60
      ],
      "remap": [
        "tales-rehab-repay",
        30
      ],
      "remit": [
        "betel-merit",
        47
      ],
      "remix": [
        "betel-smirk",
        43
      ],
      "renal": [
        "ramen",
        67
      ],
      "renew": [
        "rites",
        73
      ],
      "repay": [
        "tales-rehab",
        42
      ],
      "repel": [
        "betel-revel",
        45
      ],
      "reply": [
        "betel",
        62
      ],
      "repot": [
        "betel-merit",
        47
      ],
      "reran": [
        "ramen",
        67
      ],
      "rerun": [
        "rites",
        73
      ],
      "resaw": [
        "tales-swamp",
        49
      ],
      "reset": [
        "betel",
        60
      ],
      "resin": [
        "rites",
        73
      ],
      "retag": [
        "tales-avert",
        49
      ],
      "retch": [
        "hirer",
        75
      ],
      "retie": [
        "south-metre",
        42
      ],
      "retro": [
        "betel",
        60
      ],
      "retry": [
        "betel-retro",
        44
      ],
      "reuse": [
        "south",
        73
      ],
      "revel": [
        "betel",
        61
      ],
      "revue": [
        "south-purge",
        42
      ],
      "rheum": [
        "betel-fiery",
        45
      ],
      "rhino": [
        "runny",
        67
      ],
      "rhyme": [
        "south-where",
        43
      ],
      "ricin": [
        "scorn",
        64
      ],
      "rider": [
        "betel-whips-river",
        36
      ],
      "ridge": [
        "south-verge",
        38
      ],
      "rifle": [
        "south-verge",
        38
      ],
      "right": [
        "shout",
        60
      ],
      "rigid": [
        "shout",
        56
      ],
      "rigor": [
        "shout-dowry-vigor",
        19
      ],
      "riled": [
        "betel-folic-miler",
        30
      ],
      "rinse": [
        "nurse",
        67
      ],
      "ripen": [
        "rites-riven",
        47
      ],
      "riper": [
        "betel-whips-piper-viper",
        29
      ],
      "risen": [
        "rites",
        73
      ],
      "riser": [
        "betel-whips",
        44
      ],
      "risky": [
        "shout",
        60
      ],
      "ritzy": [
        "shout-dirty",
        36
      ],
      "rival": [
        "tyros-rabid",
        33
      ],
      "riven": [
        "rites",
        64
      ],
      "river": [
        "betel-whips",
        40
      ],
      "rivet": [
        "betel-tiger",
        43
      ],
      "roach": [
        "scary",
        73
      ],
      "roast": [
        "midst",
        77
      ],
      "robed": [
        "betel-sober",
        57
      ],
      "robin": [
        "boson",
        72
      ],
      "robot": [
        "shout",
        60
      ],
      "rocky": [
        "soupy",
        71
      ],
      "rodeo": [
        "betel-whips-roofs",
        30
      ],
      "roger": [
        "betel-whips-roofs-rover",
        24
      ],
      "rogue": [
        "south",
        73
      ],
      "roman": [
        "rayon",
        71
      ],
      "roomy": [
        "shout-glory",
        33
      ],
      "roost": [
        "shout",
        60
      ],
      "roped": [
        "betel-whips-purer",
        32
      ],
      "roper": [
        "betel-whips-purer",
        32
      ],
      "rosin": [
        "boson",
        72
      ],
      "rotor": [
        "shout-motor",
        35
      ],
      "rouge": [
        "south",
        73
      ],
      "rough": [
        "shout-humor",
        37
      ],
      "round": [
        "runny",
        67
      ],
      "rouse": [
        "south",
        73
      ],
      "roust": [
        "shout",
        60
      ],
      "route": [
        "south",
        73
      ],
      "roved": [
        "betel-whips-roofs-rover",
        24
      ],
      "rover": [
        "betel-whips-roofs",
        34
      ],
      "rowdy": [
        "shout-dowry",
        32
      ],
      "rowed": [
        "betel-whips-mower",
        32
      ],
      "rower": [
        "betel-whips-mower",
        32
      ],
      "royal": [
        "tyros",
        65
      ],
      "ruble": [
        "south-purge",
        42
      ],
      "ruddy": [
        "shout-lurid",
        39
      ],
      "ruder": [
        "betel-whips-roofs",
        30
      ],
      "rugby": [
        "shout-lurid",
        39
      ],
      "ruing": [
        "runny",
        67
      ],
      "ruled": [
        "betel-folic-ruler",
        35
      ],
      "ruler": [
        "betel-folic",
        47
      ],
      "rumba": [
        "tyros-rabid",
        33
      ],
      "rummy": [
        "shout-lurid-rugby",
        27
      ],
      "rumor": [
        "shout-furor",
        33
      ],
      "runny": [
        "",
        92
      ],
      "runup": [
        "boson",
        72
      ],
      "rupee": [
        "south-purge",
        42
      ],
      "rural": [
        "tyros-mural",
        37
      ],
      "rusty": [
        "shout",
        60
      ],
      "saber": [
        "tales-safer",
        55
      ],
      "sable": [
        "talus-lapse",
        52
      ],
      "sabre": [
        "lairs",
        76
      ],
      "sadly": [
        "toils",
        56
      ],
      "safer": [
        "tales",
        66
      ],
      "saggy": [
        "toils-gassy",
        35
      ],
      "saint": [
        "tings",
        79
      ],
      "salad": [
        "toils",
        47
      ],
      "sally": [
        "toils-sadly",
        40
      ],
      "salon": [
        "natal-manly",
        41
      ],
      "salsa": [
        "toils-salad",
        30
      ],
      "salty": [
        "toils",
        56
      ],
      "salve": [
        "talus-false",
        50
      ],
      "salvo": [
        "toils",
        55
      ],
      "samba": [
        "toils-gassy",
        35
      ],
      "samey": [
        "petal-fades",
        38
      ],
      "sandy": [
        "natal-demos",
        47
      ],
      "saner": [
        "ramen",
        67
      ],
      "sappy": [
        "toils-gassy-savvy",
        24
      ],
      "sassy": [
        "toils-gassy",
        35
      ],
      "sated": [
        "petal-gated-shame",
        48
      ],
      "satin": [
        "natal",
        65
      ],
      "satyr": [
        "tyros",
        65
      ],
      "sauce": [
        "",
        86
      ],
      "saucy": [
        "hotly-wacky",
        46
      ],
      "sauna": [
        "tings",
        79
      ],
      "saute": [
        "talus",
        72
      ],
      "saved": [
        "petal-fades-serve",
        29
      ],
      "saver": [
        "tales-safer-saber",
        43
      ],
      "savor": [
        "tyros",
        65
      ],
      "savoy": [
        "toils",
        53
      ],
      "savvy": [
        "toils-gassy",
        36
      ],
      "sawed": [
        "petal-fades-serve",
        29
      ],
      "scald": [
        "plush-scaly",
        47
      ],
      "scale": [
        "",
        92
      ],
      "scalp": [
        "plush",
        76
      ],
      "scaly": [
        "plush",
        64
      ],
      "scamp": [
        "plush",
        76
      ],
      "scant": [
        "",
        99
      ],
      "scape": [
        "scale",
        76
      ],
      "scare": [
        "",
        99
      ],
      "scarf": [
        "scary",
        55
      ],
      "scarp": [
        "scary-scarf",
        38
      ],
      "scary": [
        "",
        89
      ],
      "scene": [
        "",
        85
      ],
      "scent": [
        "",
        99
      ],
      "schmo": [
        "spoil",
        63
      ],
      "schwa": [
        "hotly-dacha",
        42
      ],
      "scion": [
        "posit",
        75
      ],
      "scoff": [
        "spoil-scout",
        42
      ],
      "scold": [
        "spoil",
        63
      ],
      "scone": [
        "scene",
        60
      ],
      "scoop": [
        "spoil",
        63
      ],
      "scoot": [
        "spoil-scout",
        42
      ],
      "scope": [
        "pious",
        71
      ],
      "score": [
        "",
        91
      ],
      "scorn": [
        "",
        89
      ],
      "scour": [
        "soupy",
        71
      ],
      "scout": [
        "spoil",
        53
      ],
      "scowl": [
        "spoil",
        63
      ],
      "scram": [
        "",
        92
      ],
      "scrap": [
        "scram",
        70
      ],
      "scree": [
        "score",
        67
      ],
      "screw": [
        "hirer",
        75
      ],
      "scrim": [
        "soupy",
        71
      ],
      "scrip": [
        "soupy",
        71
      ],
      "scrod": [
        "soupy",
        71
      ],
      "scrub": [
        "soupy",
        54
      ],
      "scrum": [
        "soupy-scrub",
        37
      ],
      "scuba": [
        "hotly-basic",
        40
      ],
      "scuff": [
        "spoil-stuck",
        39
      ],
      "scull": [
        "spoil",
        63
      ],
      "seamy": [
        "lefts",
        73
      ],
      "sedan": [
        "sleep",
        72
      ],
      "seder": [
        "betel-fewer-sever",
        36
      ],
      "sedge": [
        "toils-suede",
        34
      ],
      "seedy": [
        "split",
        54
      ],
      "segue": [
        "toils-suede",
        34
      ],
      "seize": [
        "toils-spike",
        35
      ],
      "sense": [
        "deist",
        73
      ],
      "sepia": [
        "petal",
        70
      ],
      "serif": [
        "betel-smirk",
        43
      ],
      "serum": [
        "betel-smirk",
        43
      ],
      "serve": [
        "south-spree",
        43
      ],
      "setup": [
        "split",
        57
      ],
      "seven": [
        "towel-hived",
        41
      ],
      "sever": [
        "betel-fewer",
        49
      ],
      "sewed": [
        "split-seedy",
        37
      ],
      "sewer": [
        "betel-fewer",
        50
      ],
      "shack": [
        "plush",
        76
      ],
      "shade": [
        "sloth-vodka",
        57
      ],
      "shady": [
        "spilt",
        49
      ],
      "shaft": [
        "spilt",
        73
      ],
      "shake": [
        "sloth-vodka",
        57
      ],
      "shaky": [
        "spilt-shady",
        38
      ],
      "shale": [
        "sloth",
        75
      ],
      "shall": [
        "spilt",
        61
      ],
      "shalt": [
        "spilt",
        73
      ],
      "shame": [
        "sloth-vodka-shape",
        37
      ],
      "shank": [
        "ghost",
        78
      ],
      "shape": [
        "sloth-vodka",
        49
      ],
      "shard": [
        "midst",
        77
      ],
      "share": [
        "aloft",
        60
      ],
      "shark": [
        "midst-sharp",
        47
      ],
      "sharp": [
        "midst",
        64
      ],
      "shave": [
        "sloth-vodka",
        57
      ],
      "shawl": [
        "spilt-slash",
        47
      ],
      "sheaf": [
        "petal-ahead",
        43
      ],
      "shear": [
        "tales-swamp",
        49
      ],
      "sheen": [
        "towel-hived",
        41
      ],
      "sheep": [
        "split",
        57
      ],
      "sheer": [
        "betel",
        62
      ],
      "sheet": [
        "split",
        56
      ],
      "sheik": [
        "split",
        56
      ],
      "shelf": [
        "split-smell",
        43
      ],
      "shell": [
        "split-smell",
        41
      ],
      "shied": [
        "split",
        54
      ],
      "shift": [
        "sloth-sight",
        38
      ],
      "shill": [
        "sloth-shyly",
        38
      ],
      "shine": [
        "whips",
        68
      ],
      "shiny": [
        "gluts",
        63
      ],
      "shire": [
        "south",
        73
      ],
      "shirk": [
        "shout",
        60
      ],
      "shirt": [
        "shout",
        60
      ],
      "shiva": [
        "toils-daisy",
        38
      ],
      "shlep": [
        "split",
        56
      ],
      "shoal": [
        "toils-salvo",
        39
      ],
      "shock": [
        "spoil-scout",
        40
      ],
      "shoed": [
        "split-seedy",
        46
      ],
      "shone": [
        "whips",
        68
      ],
      "shook": [
        "sloth",
        55
      ],
      "shoot": [
        "sloth-shout",
        38
      ],
      "shore": [
        "south",
        73
      ],
      "shorn": [
        "boson-sworn",
        40
      ],
      "short": [
        "shout",
        60
      ],
      "shout": [
        "sloth",
        54
      ],
      "shove": [
        "toils-spoke",
        31
      ],
      "shown": [
        "pinot-snowy",
        37
      ],
      "showy": [
        "sloth-shook",
        38
      ],
      "shred": [
        "betel-whips",
        43
      ],
      "shrew": [
        "betel-whips",
        43
      ],
      "shrub": [
        "shout-shrug",
        38
      ],
      "shrug": [
        "shout",
        54
      ],
      "shuck": [
        "spoil-stuck",
        39
      ],
      "shunt": [
        "gluts-stunt",
        41
      ],
      "shush": [
        "sloth",
        56
      ],
      "shyly": [
        "sloth",
        55
      ],
      "sided": [
        "split-shied-sized",
        34
      ],
      "sidle": [
        "toils",
        61
      ],
      "siege": [
        "toils",
        54
      ],
      "sieve": [
        "toils-siege",
        37
      ],
      "sight": [
        "sloth",
        54
      ],
      "sigma": [
        "toils",
        53
      ],
      "silky": [
        "sloth-spill",
        33
      ],
      "silly": [
        "sloth-spill",
        33
      ],
      "silty": [
        "sloth",
        50
      ],
      "since": [
        "humps",
        80
      ],
      "sinew": [
        "towel-widen",
        48
      ],
      "singe": [
        "deist",
        73
      ],
      "sinus": [
        "pinot-desks",
        36
      ],
      "sired": [
        "betel-whips-riser",
        32
      ],
      "siren": [
        "rites",
        73
      ],
      "sissy": [
        "sloth-spiky",
        35
      ],
      "sitar": [
        "tyros",
        62
      ],
      "sited": [
        "split",
        56
      ],
      "situp": [
        "sloth-drift",
        40
      ],
      "sixth": [
        "sloth",
        53
      ],
      "sixty": [
        "sloth",
        50
      ],
      "sized": [
        "split-shied",
        46
      ],
      "skate": [
        "sloth-spate",
        56
      ],
      "skeet": [
        "split-sheet-sweet",
        36
      ],
      "skein": [
        "towel-deign",
        37
      ],
      "skied": [
        "split-shied",
        37
      ],
      "skier": [
        "betel-whips",
        43
      ],
      "skiff": [
        "sloth-spiky",
        35
      ],
      "skill": [
        "sloth-spill",
        32
      ],
      "skimp": [
        "sloth-spiky",
        35
      ],
      "skirt": [
        "shout",
        60
      ],
      "skulk": [
        "sloth-spill",
        33
      ],
      "skull": [
        "sloth-spill",
        33
      ],
      "skunk": [
        "gluts-spunk",
        42
      ],
      "slack": [
        "plush",
        76
      ],
      "slain": [
        "",
        90
      ],
      "slake": [
        "sloth",
        75
      ],
      "slang": [
        "ghost",
        61
      ],
      "slant": [
        "ghost",
        78
      ],
      "slash": [
        "spilt",
        64
      ],
      "slate": [
        "sloth",
        75
      ],
      "sleek": [
        "split-smell",
        43
      ],
      "sleep": [
        "split",
        56
      ],
      "sleet": [
        "split",
        58
      ],
      "slept": [
        "split",
        56
      ],
      "slice": [
        "pious",
        71
      ],
      "slick": [
        "spoil",
        63
      ],
      "slide": [
        "toils",
        57
      ],
      "slime": [
        "toils-slide",
        41
      ],
      "slimy": [
        "sloth-slump",
        38
      ],
      "sling": [
        "gluts",
        66
      ],
      "slink": [
        "gluts",
        66
      ],
      "sloop": [
        "sloth",
        50
      ],
      "slope": [
        "toils",
        61
      ],
      "slosh": [
        "sloth",
        50
      ],
      "sloth": [
        "",
        52
      ],
      "slump": [
        "sloth",
        55
      ],
      "slung": [
        "gluts",
        66
      ],
      "slunk": [
        "gluts",
        66
      ],
      "slurp": [
        "shout-surly",
        40
      ],
      "slush": [
        "sloth",
        50
      ],
      "slyly": [
        "sloth-slump",
        38
      ],
      "smack": [
        "plush-stack",
        38
      ],
      "small": [
        "spilt-shall",
        45
      ],
      "smarm": [
        "midst-swarm",
        52
      ],
      "smart": [
        "midst",
        77
      ],
      "smash": [
        "spilt-shady",
        33
      ],
      "smear": [
        "tales-swamp",
        49
      ],
      "smell": [
        "split",
        53
      ],
      "smelt": [
        "split-sleet",
        41
      ],
      "smile": [
        "toils",
        61
      ],
      "smirk": [
        "shout-swirl",
        36
      ],
      "smite": [
        "toils-suite-spite",
        35
      ],
      "smith": [
        "sloth-sixth",
        37
      ],
      "smock": [
        "spoil-scout-shock",
        27
      ],
      "smoke": [
        "toils-spoke",
        31
      ],
      "smoky": [
        "sloth-spoof",
        38
      ],
      "smote": [
        "toils-stoke",
        40
      ],
      "smush": [
        "sloth-shush",
        39
      ],
      "snack": [
        "",
        86
      ],
      "snafu": [
        "slain",
        56
      ],
      "snail": [
        "slain",
        78
      ],
      "snake": [
        "",
        85
      ],
      "snaky": [
        "slain-snafu",
        39
      ],
      "snare": [
        "",
        99
      ],
      "snarf": [
        "snarl-snark",
        41
      ],
      "snark": [
        "snarl",
        57
      ],
      "snarl": [
        "",
        86
      ],
      "sneak": [
        "sleep",
        72
      ],
      "sneer": [
        "rites",
        73
      ],
      "snide": [
        "deist",
        73
      ],
      "sniff": [
        "pinot-unify",
        35
      ],
      "snipe": [
        "deist",
        73
      ],
      "snoop": [
        "pinot-spoon",
        41
      ],
      "snoot": [
        "pinot",
        61
      ],
      "snore": [
        "nurse",
        67
      ],
      "snort": [
        "boson",
        72
      ],
      "snout": [
        "pinot",
        61
      ],
      "snowy": [
        "pinot",
        48
      ],
      "snuck": [
        "posit",
        63
      ],
      "snuff": [
        "pinot",
        61
      ],
      "soapy": [
        "spilt-swamp",
        48
      ],
      "sober": [
        "betel",
        62
      ],
      "softy": [
        "sloth",
        50
      ],
      "soggy": [
        "sloth-soupy",
        39
      ],
      "solar": [
        "tyros",
        65
      ],
      "soled": [
        "split",
        56
      ],
      "solid": [
        "sloth",
        50
      ],
      "solve": [
        "toils-loose",
        39
      ],
      "sonar": [
        "rayon",
        71
      ],
      "sonic": [
        "posit",
        75
      ],
      "sooth": [
        "sloth",
        50
      ],
      "sooty": [
        "sloth",
        50
      ],
      "soppy": [
        "sloth-soupy",
        39
      ],
      "sorry": [
        "shout",
        60
      ],
      "sound": [
        "gluts-spunk",
        42
      ],
      "soupy": [
        "sloth",
        55
      ],
      "south": [
        "sloth",
        50
      ],
      "sowed": [
        "split-seedy-shoed",
        34
      ],
      "sower": [
        "betel-whips",
        43
      ],
      "space": [
        "scale",
        76
      ],
      "spade": [
        "sloth-suave",
        49
      ],
      "spank": [
        "ghost-swank",
        43
      ],
      "spare": [
        "aloft-share",
        44
      ],
      "spark": [
        "midst-sharp",
        47
      ],
      "spasm": [
        "spilt",
        73
      ],
      "spate": [
        "sloth",
        66
      ],
      "spawn": [
        "slain",
        78
      ],
      "speak": [
        "petal",
        70
      ],
      "spear": [
        "tales-swamp",
        49
      ],
      "speck": [
        "pilot",
        71
      ],
      "speed": [
        "split",
        56
      ],
      "spell": [
        "split",
        56
      ],
      "spelt": [
        "split",
        56
      ],
      "spend": [
        "tipsy",
        73
      ],
      "spent": [
        "tipsy",
        73
      ],
      "sperm": [
        "betel-fiery",
        45
      ],
      "spice": [
        "pious",
        71
      ],
      "spicy": [
        "spoil",
        63
      ],
      "spied": [
        "split",
        56
      ],
      "spiel": [
        "split",
        56
      ],
      "spiff": [
        "sloth-spiky",
        35
      ],
      "spike": [
        "toils",
        51
      ],
      "spiky": [
        "sloth",
        47
      ],
      "spill": [
        "sloth",
        46
      ],
      "spilt": [
        "sloth-split",
        38
      ],
      "spine": [
        "whips",
        68
      ],
      "spiny": [
        "gluts-shiny",
        46
      ],
      "spire": [
        "south-spree",
        43
      ],
      "spite": [
        "toils-suite",
        47
      ],
      "splat": [
        "toils-salty",
        39
      ],
      "splay": [
        "toils-salad",
        30
      ],
      "split": [
        "sloth",
        55
      ],
      "spoil": [
        "sloth",
        55
      ],
      "spoke": [
        "toils",
        48
      ],
      "spoof": [
        "sloth",
        55
      ],
      "spook": [
        "sloth-spoof",
        38
      ],
      "spool": [
        "sloth-spoil",
        39
      ],
      "spoon": [
        "pinot",
        58
      ],
      "spore": [
        "south-swore",
        48
      ],
      "spork": [
        "shout-sword",
        41
      ],
      "sport": [
        "shout",
        60
      ],
      "spout": [
        "sloth-stoop",
        37
      ],
      "spray": [
        "tyros",
        65
      ],
      "spree": [
        "south",
        60
      ],
      "sprig": [
        "shout-swirl",
        36
      ],
      "spume": [
        "toils-suede",
        34
      ],
      "spunk": [
        "gluts",
        58
      ],
      "spurn": [
        "boson",
        72
      ],
      "spurt": [
        "shout",
        60
      ],
      "squab": [
        "toils-gassy-squad",
        18
      ],
      "squad": [
        "toils-gassy",
        30
      ],
      "squat": [
        "toils-pasta",
        36
      ],
      "squib": [
        "sloth-spiky-squid",
        21
      ],
      "squid": [
        "sloth-spiky",
        34
      ],
      "stack": [
        "plush",
        55
      ],
      "staff": [
        "spilt-swath",
        40
      ],
      "stage": [
        "sloth",
        66
      ],
      "staid": [
        "spilt",
        73
      ],
      "stain": [
        "slain",
        66
      ],
      "stair": [
        "midst",
        77
      ],
      "stake": [
        "sloth-stage",
        56
      ],
      "stale": [
        "sloth",
        75
      ],
      "stalk": [
        "spilt-stall",
        46
      ],
      "stall": [
        "spilt",
        63
      ],
      "stamp": [
        "spilt",
        68
      ],
      "stand": [
        "ghost",
        63
      ],
      "stank": [
        "ghost-stand",
        46
      ],
      "staph": [
        "spilt-stamp",
        52
      ],
      "stare": [
        "aloft",
        85
      ],
      "stark": [
        "midst",
        77
      ],
      "start": [
        "midst",
        77
      ],
      "stash": [
        "spilt-swath",
        40
      ],
      "state": [
        "sloth-spate-skate",
        43
      ],
      "stave": [
        "sloth-stage-stake",
        43
      ],
      "stead": [
        "petal-steak-steam",
        30
      ],
      "steak": [
        "petal",
        56
      ],
      "steal": [
        "petal",
        70
      ],
      "steam": [
        "petal-steak",
        42
      ],
      "steed": [
        "split",
        56
      ],
      "steel": [
        "split",
        56
      ],
      "steep": [
        "split-setup",
        41
      ],
      "steer": [
        "betel",
        62
      ],
      "stein": [
        "towel-inept",
        47
      ],
      "stele": [
        "toils-style",
        43
      ],
      "steno": [
        "tipsy-stent",
        43
      ],
      "stent": [
        "tipsy",
        60
      ],
      "stern": [
        "rites",
        73
      ],
      "stick": [
        "spoil",
        63
      ],
      "stiff": [
        "sloth-drift",
        40
      ],
      "stile": [
        "toils",
        61
      ],
      "still": [
        "sloth-split",
        38
      ],
      "stilt": [
        "sloth-split",
        38
      ],
      "sting": [
        "gluts",
        66
      ],
      "stink": [
        "gluts-stint",
        42
      ],
      "stint": [
        "gluts",
        58
      ],
      "stock": [
        "spoil-scout",
        42
      ],
      "stoic": [
        "spoil",
        63
      ],
      "stoke": [
        "toils",
        56
      ],
      "stole": [
        "toils",
        61
      ],
      "stomp": [
        "sloth-stoop",
        37
      ],
      "stone": [
        "whips",
        68
      ],
      "stony": [
        "gluts-stint",
        42
      ],
      "stood": [
        "sloth-stoop",
        37
      ],
      "stool": [
        "sloth",
        50
      ],
      "stoop": [
        "sloth",
        54
      ],
      "store": [
        "south",
        73
      ],
      "stork": [
        "shout-story-storm",
        34
      ],
      "storm": [
        "shout-story",
        47
      ],
      "story": [
        "shout",
        55
      ],
      "stout": [
        "sloth-stoop",
        37
      ],
      "stove": [
        "toils-stoke",
        40
      ],
      "strap": [
        "tyros-straw",
        41
      ],
      "straw": [
        "tyros",
        58
      ],
      "stray": [
        "tyros",
        65
      ],
      "strep": [
        "betel-tiger",
        39
      ],
      "strew": [
        "betel-tiger-strep",
        27
      ],
      "strip": [
        "shout",
        60
      ],
      "strum": [
        "shout",
        60
      ],
      "strut": [
        "shout",
        60
      ],
      "stuck": [
        "spoil",
        56
      ],
      "study": [
        "sloth-drift",
        40
      ],
      "stuff": [
        "sloth-drift",
        40
      ],
      "stump": [
        "sloth-drift",
        40
      ],
      "stung": [
        "gluts",
        66
      ],
      "stunk": [
        "gluts-stunt",
        41
      ],
      "stunt": [
        "gluts",
        58
      ],
      "style": [
        "toils",
        60
      ],
      "suave": [
        "sloth",
        66
      ],
      "sudsy": [
        "sloth-spiky",
        35
      ],
      "suede": [
        "toils",
        50
      ],
      "sugar": [
        "tyros",
        65
      ],
      "suing": [
        "gluts",
        60
      ],
      "suite": [
        "toils",
        56
      ],
      "sulky": [
        "sloth-spill",
        33
      ],
      "sully": [
        "sloth-spill",
        33
      ],
      "sumac": [
        "hotly-basic",
        40
      ],
      "sunny": [
        "gluts",
        66
      ],
      "sunup": [
        "pinot",
        61
      ],
      "super": [
        "betel-whips",
        46
      ],
      "surer": [
        "betel-whips",
        43
      ],
      "surge": [
        "south",
        73
      ],
      "surly": [
        "shout",
        57
      ],
      "sushi": [
        "sloth",
        50
      ],
      "swain": [
        "slain-stain",
        50
      ],
      "swale": [
        "sloth",
        75
      ],
      "swami": [
        "spilt",
        73
      ],
      "swamp": [
        "spilt",
        65
      ],
      "swang": [
        "ghost-slang",
        44
      ],
      "swank": [
        "ghost",
        59
      ],
      "swarm": [
        "midst",
        68
      ],
      "swash": [
        "spilt-shady-smash",
        20
      ],
      "swath": [
        "spilt",
        56
      ],
      "swear": [
        "tales-swamp",
        49
      ],
      "sweat": [
        "petal-steak",
        45
      ],
      "sweep": [
        "split-sheep",
        41
      ],
      "sweet": [
        "split-sheet",
        48
      ],
      "swell": [
        "split-smell-shell",
        28
      ],
      "swept": [
        "split",
        56
      ],
      "swift": [
        "sloth-drift",
        40
      ],
      "swill": [
        "sloth-spill-skill",
        20
      ],
      "swine": [
        "whips",
        68
      ],
      "swing": [
        "gluts",
        66
      ],
      "swipe": [
        "toils-spike",
        35
      ],
      "swirl": [
        "shout",
        52
      ],
      "swish": [
        "sloth-shush",
        39
      ],
      "swoon": [
        "pinot",
        53
      ],
      "swoop": [
        "sloth-spoof",
        38
      ],
      "sword": [
        "shout",
        58
      ],
      "swore": [
        "south",
        65
      ],
      "sworn": [
        "boson",
        57
      ],
      "swung": [
        "gluts",
        66
      ],
      "synch": [
        "posit-snuck",
        47
      ],
      "synod": [
        "pinot",
        61
      ],
      "synth": [
        "pinot",
        61
      ],
      "syrup": [
        "shout",
        60
      ],
      "tabby": [
        "toils-taffy",
        46
      ],
      "table": [
        "talus",
        72
      ],
      "taboo": [
        "toils",
        53
      ],
      "tacit": [
        "hotly",
        59
      ],
      "tacky": [
        "hotly",
        75
      ],
      "taffy": [
        "toils",
        54
      ],
      "taint": [
        "tings",
        79
      ],
      "taken": [
        "sleep-known",
        49
      ],
      "taker": [
        "tales-tempt",
        51
      ],
      "talky": [
        "toils",
        56
      ],
      "tally": [
        "toils",
        53
      ],
      "talon": [
        "natal",
        73
      ],
      "talus": [
        "toils",
        53
      ],
      "tamed": [
        "petal-asset",
        49
      ],
      "tamer": [
        "tales-tempt",
        51
      ],
      "tango": [
        "natal-tangy",
        47
      ],
      "tangy": [
        "natal",
        64
      ],
      "taped": [
        "petal-adept",
        47
      ],
      "taper": [
        "tales-tempt",
        51
      ],
      "tapir": [
        "tyros",
        65
      ],
      "tardy": [
        "tyros",
        61
      ],
      "tarot": [
        "tyros",
        65
      ],
      "tarry": [
        "tyros-tardy",
        44
      ],
      "tased": [
        "petal-asset",
        42
      ],
      "taser": [
        "tales",
        71
      ],
      "taste": [
        "talus",
        72
      ],
      "tasty": [
        "toils",
        53
      ],
      "tater": [
        "tales-tempt",
        51
      ],
      "tatty": [
        "toils-taffy-tabby",
        34
      ],
      "taunt": [
        "tings",
        67
      ],
      "taupe": [
        "talus",
        72
      ],
      "tawny": [
        "tings-taunt",
        51
      ],
      "taxed": [
        "petal-asset-tamed",
        37
      ],
      "teach": [
        "leapt",
        72
      ],
      "teary": [
        "badly-weary",
        42
      ],
      "tease": [
        "sloth",
        75
      ],
      "teddy": [
        "split-teeth",
        30
      ],
      "teeny": [
        "tipsy",
        73
      ],
      "teeth": [
        "split",
        47
      ],
      "telos": [
        "split",
        56
      ],
      "tempo": [
        "split-empty",
        37
      ],
      "tempt": [
        "split",
        57
      ],
      "tenet": [
        "towel",
        62
      ],
      "tenor": [
        "rites",
        73
      ],
      "tense": [
        "deist",
        73
      ],
      "tenth": [
        "towel",
        68
      ],
      "tepee": [
        "toils-theme",
        37
      ],
      "tepid": [
        "split",
        56
      ],
      "terra": [
        "tales",
        61
      ],
      "terry": [
        "betel-merit",
        44
      ],
      "terse": [
        "south",
        73
      ],
      "testy": [
        "split",
        55
      ],
      "tetra": [
        "tales-terra",
        45
      ],
      "thank": [
        "ghost",
        78
      ],
      "theft": [
        "split-beget",
        33
      ],
      "their": [
        "betel-twerp",
        45
      ],
      "theme": [
        "toils",
        54
      ],
      "there": [
        "south-three",
        43
      ],
      "these": [
        "toils",
        61
      ],
      "theta": [
        "petal-asset",
        42
      ],
      "thick": [
        "spoil-which",
        35
      ],
      "thief": [
        "split",
        56
      ],
      "thigh": [
        "sloth",
        50
      ],
      "thine": [
        "whips",
        68
      ],
      "thing": [
        "gluts-tying",
        41
      ],
      "think": [
        "gluts-point",
        39
      ],
      "third": [
        "shout",
        60
      ],
      "thong": [
        "gluts-tying",
        41
      ],
      "thorn": [
        "boson",
        72
      ],
      "those": [
        "toils",
        61
      ],
      "three": [
        "south",
        60
      ],
      "threw": [
        "betel-tiger",
        43
      ],
      "throb": [
        "shout-throw",
        38
      ],
      "throw": [
        "shout",
        55
      ],
      "thrum": [
        "shout",
        60
      ],
      "thumb": [
        "sloth-thump",
        36
      ],
      "thump": [
        "sloth",
        50
      ],
      "thyme": [
        "toils-theme",
        37
      ],
      "tiara": [
        "midst",
        77
      ],
      "tibia": [
        "toils",
        53
      ],
      "tidal": [
        "toils",
        53
      ],
      "tided": [
        "split-thief-timed",
        30
      ],
      "tiger": [
        "betel",
        56
      ],
      "tight": [
        "sloth-thump",
        36
      ],
      "tilde": [
        "toils",
        61
      ],
      "tiled": [
        "split",
        56
      ],
      "timed": [
        "split-thief",
        42
      ],
      "timer": [
        "betel-tiger",
        43
      ],
      "timid": [
        "sloth",
        50
      ],
      "tinge": [
        "deist",
        60
      ],
      "tinny": [
        "gluts-point",
        39
      ],
      "tipsy": [
        "sloth-midst",
        30
      ],
      "tired": [
        "betel-tiger",
        43
      ],
      "titan": [
        "natal",
        61
      ],
      "titer": [
        "betel-outer-miter",
        24
      ],
      "tithe": [
        "toils",
        61
      ],
      "title": [
        "toils",
        61
      ],
      "tizzy": [
        "sloth-timid",
        34
      ],
      "toady": [
        "spilt",
        73
      ],
      "toast": [
        "spilt-boast",
        42
      ],
      "today": [
        "toils",
        56
      ],
      "toddy": [
        "sloth-doubt",
        29
      ],
      "token": [
        "towel",
        58
      ],
      "tonal": [
        "natal",
        73
      ],
      "toned": [
        "towel-token-toney",
        31
      ],
      "toner": [
        "rites-tuner",
        49
      ],
      "toney": [
        "towel-token",
        43
      ],
      "tonga": [
        "natal-angst",
        46
      ],
      "tonic": [
        "posit",
        75
      ],
      "tooth": [
        "sloth-booth",
        39
      ],
      "topaz": [
        "toils-today",
        40
      ],
      "topic": [
        "spoil",
        63
      ],
      "torah": [
        "tyros",
        65
      ],
      "torch": [
        "soupy",
        56
      ],
      "torso": [
        "shout",
        60
      ],
      "torte": [
        "south-forte",
        47
      ],
      "torus": [
        "shout",
        60
      ],
      "total": [
        "toils",
        53
      ],
      "toted": [
        "split-teeth-totem",
        22
      ],
      "totem": [
        "split-teeth",
        35
      ],
      "touch": [
        "spoil",
        54
      ],
      "tough": [
        "sloth",
        50
      ],
      "towed": [
        "split-teeth-toyed",
        20
      ],
      "towel": [
        "split-hotel",
        32
      ],
      "tower": [
        "betel-tiger",
        43
      ],
      "toxic": [
        "spoil",
        63
      ],
      "toxin": [
        "pinot",
        61
      ],
      "toyed": [
        "split-teeth",
        33
      ],
      "trace": [
        "",
        89
      ],
      "track": [
        "",
        91
      ],
      "tract": [
        "track",
        76
      ],
      "trade": [
        "digit",
        83
      ],
      "trail": [
        "twigs",
        58
      ],
      "train": [
        "debit",
        71
      ],
      "trait": [
        "twigs-trail",
        41
      ],
      "tramp": [
        "twigs",
        75
      ],
      "trans": [
        "gated",
        78
      ],
      "trash": [
        "twigs",
        75
      ],
      "trawl": [
        "twigs",
        75
      ],
      "tread": [
        "tubed",
        77
      ],
      "treat": [
        "tubed",
        77
      ],
      "treed": [
        "defer-greed-breed",
        31
      ],
      "trend": [
        "",
        99
      ],
      "tress": [
        "defer-press",
        37
      ],
      "triad": [
        "armor-trial",
        40
      ],
      "trial": [
        "armor",
        56
      ],
      "tribe": [
        "pivot",
        59
      ],
      "trice": [
        "truce",
        64
      ],
      "trick": [
        "",
        92
      ],
      "tried": [
        "defer",
        55
      ],
      "trike": [
        "pivot-tribe-trite",
        33
      ],
      "trill": [
        "pilot",
        70
      ],
      "tripe": [
        "pivot",
        75
      ],
      "trite": [
        "pivot-tribe",
        46
      ],
      "troll": [
        "pilot",
        70
      ],
      "tromp": [
        "pilot",
        70
      ],
      "troop": [
        "pilot",
        70
      ],
      "trope": [
        "pivot",
        75
      ],
      "trout": [
        "pilot",
        58
      ],
      "trove": [
        "pivot",
        75
      ],
      "truce": [
        "",
        88
      ],
      "truck": [
        "trick",
        74
      ],
      "truer": [
        "defer",
        63
      ],
      "truly": [
        "pilot",
        70
      ],
      "trump": [
        "pilot",
        70
      ],
      "trunk": [
        "bigot",
        73
      ],
      "truss": [
        "pilot-truth",
        48
      ],
      "trust": [
        "pilot",
        63
      ],
      "truth": [
        "pilot",
        64
      ],
      "tryst": [
        "pilot-trust",
        47
      ],
      "tubal": [
        "toils-talky",
        39
      ],
      "tubby": [
        "sloth-timid",
        34
      ],
      "tubed": [
        "split-teeth-toyed",
        20
      ],
      "tuber": [
        "betel",
        60
      ],
      "tufty": [
        "sloth-batik",
        44
      ],
      "tulip": [
        "sloth-guilt",
        41
      ],
      "tulle": [
        "toils",
        61
      ],
      "tummy": [
        "sloth-timid",
        34
      ],
      "tumor": [
        "shout",
        52
      ],
      "tuned": [
        "towel-tenet",
        45
      ],
      "tuner": [
        "rites",
        66
      ],
      "tunic": [
        "posit",
        75
      ],
      "turbo": [
        "shout-tumor",
        36
      ],
      "tutor": [
        "shout-tumor",
        36
      ],
      "twain": [
        "slain-again",
        44
      ],
      "twang": [
        "ghost",
        78
      ],
      "tweak": [
        "petal-steak",
        45
      ],
      "tweed": [
        "split-teeth",
        30
      ],
      "tween": [
        "towel",
        68
      ],
      "tweet": [
        "split-beget",
        33
      ],
      "twerk": [
        "betel-twerp",
        45
      ],
      "twerp": [
        "betel",
        62
      ],
      "twice": [
        "pious",
        71
      ],
      "twill": [
        "sloth-guilt",
        41
      ],
      "twine": [
        "whips",
        68
      ],
      "twirl": [
        "shout-dirty",
        36
      ],
      "twist": [
        "sloth-midst",
        37
      ],
      "twixt": [
        "sloth-timid",
        34
      ],
      "tying": [
        "gluts",
        58
      ],
      "typed": [
        "split-empty",
        37
      ],
      "udder": [
        "betel-whips-roofs",
        30
      ],
      "ulcer": [
        "hirer",
        75
      ],
      "ulnar": [
        "rayon-lunar",
        42
      ],
      "ultra": [
        "tyros-altar",
        43
      ],
      "umami": [
        "spilt-khaki",
        51
      ],
      "umber": [
        "betel-sober-fiber",
        40
      ],
      "umbra": [
        "tyros-rabid",
        26
      ],
      "unarm": [
        "snarl",
        73
      ],
      "unbox": [
        "pinot-swoon",
        37
      ],
      "uncap": [
        "panic",
        74
      ],
      "uncle": [
        "humps",
        80
      ],
      "uncut": [
        "posit",
        75
      ],
      "under": [
        "rites-below",
        42
      ],
      "undid": [
        "pinot-unify",
        35
      ],
      "undue": [
        "deist-nudge",
        40
      ],
      "unfed": [
        "towel-hived",
        43
      ],
      "unfit": [
        "pinot",
        59
      ],
      "unhip": [
        "pinot",
        54
      ],
      "unify": [
        "pinot",
        51
      ],
      "union": [
        "pinot",
        55
      ],
      "unite": [
        "deist",
        73
      ],
      "unity": [
        "pinot-until",
        39
      ],
      "unjam": [
        "natal-human",
        42
      ],
      "unlit": [
        "pinot-unfit",
        42
      ],
      "unmet": [
        "towel",
        64
      ],
      "unpin": [
        "pinot-unhip",
        38
      ],
      "unsay": [
        "natal-human",
        42
      ],
      "unsee": [
        "deist-ensue",
        46
      ],
      "unset": [
        "towel-unmet",
        47
      ],
      "untag": [
        "natal-titan",
        44
      ],
      "untie": [
        "deist-tinge",
        43
      ],
      "until": [
        "pinot",
        55
      ],
      "unwed": [
        "towel",
        68
      ],
      "unzip": [
        "pinot-unhip",
        38
      ],
      "upend": [
        "tipsy",
        73
      ],
      "upped": [
        "split-epoxy",
        37
      ],
      "upper": [
        "betel-whips-purer",
        32
      ],
      "upset": [
        "split",
        56
      ],
      "urban": [
        "organ",
        67
      ],
      "urged": [
        "defer-tried-orbed",
        29
      ],
      "urine": [
        "prone",
        63
      ],
      "usage": [
        "sloth",
        67
      ],
      "usher": [
        "betel-whips",
        43
      ],
      "using": [
        "gluts-suing",
        44
      ],
      "usual": [
        "toils-salad",
        30
      ],
      "usurp": [
        "shout",
        55
      ],
      "usury": [
        "shout-usurp",
        39
      ],
      "utile": [
        "toils",
        61
      ],
      "utter": [
        "betel-outer",
        45
      ],
      "uvula": [
        "toils-madly",
        34
      ],
      "vague": [
        "talus",
        72
      ],
      "valet": [
        "petal",
        70
      ],
      "valid": [
        "toils",
        55
      ],
      "valor": [
        "tyros",
        53
      ],
      "value": [
        "talus",
        72
      ],
      "valve": [
        "talus",
        68
      ],
      "vampy": [
        "toils-dumpy",
        33
      ],
      "vaped": [
        "petal-gaped",
        43
      ],
      "vapid": [
        "toils-mafia",
        30
      ],
      "vapor": [
        "tyros-valor",
        42
      ],
      "vault": [
        "toils-fault",
        37
      ],
      "vaunt": [
        "tings-hived",
        44
      ],
      "vegan": [
        "sleep-began",
        46
      ],
      "veiny": [
        "tipsy",
        73
      ],
      "veldt": [
        "split",
        56
      ],
      "venal": [
        "sleep",
        72
      ],
      "venom": [
        "towel",
        58
      ],
      "venti": [
        "towel-inept",
        47
      ],
      "venue": [
        "deist",
        73
      ],
      "verge": [
        "south",
        55
      ],
      "verse": [
        "south",
        73
      ],
      "verso": [
        "betel-smirk",
        43
      ],
      "verve": [
        "south-verge",
        38
      ],
      "vexed": [
        "split-dogma-weedy-hexed",
        25
      ],
      "vicar": [
        "scram",
        70
      ],
      "video": [
        "split-edify",
        39
      ],
      "vigil": [
        "sloth-billy",
        27
      ],
      "vigor": [
        "shout-dowry",
        31
      ],
      "villa": [
        "toils",
        53
      ],
      "vined": [
        "towel-hived",
        41
      ],
      "vinyl": [
        "pinot-desks",
        29
      ],
      "viola": [
        "toils",
        54
      ],
      "viper": [
        "betel-whips-piper",
        38
      ],
      "viral": [
        "tyros-mural",
        38
      ],
      "virus": [
        "shout",
        60
      ],
      "visit": [
        "sloth-midst",
        37
      ],
      "visor": [
        "shout",
        60
      ],
      "vista": [
        "toils",
        53
      ],
      "vital": [
        "toils",
        53
      ],
      "vitro": [
        "shout-motor",
        35
      ],
      "vivid": [
        "sloth-dumpy",
        28
      ],
      "vixen": [
        "towel-hived",
        41
      ],
      "vocal": [
        "hotly-lover",
        52
      ],
      "vodka": [
        "toils",
        55
      ],
      "vogue": [
        "toils",
        53
      ],
      "voice": [
        "pious",
        71
      ],
      "voila": [
        "toils",
        53
      ],
      "voile": [
        "toils",
        61
      ],
      "vomit": [
        "sloth-doubt",
        29
      ],
      "voted": [
        "split-teeth",
        34
      ],
      "voter": [
        "betel-outer",
        45
      ],
      "vouch": [
        "spoil-touch",
        38
      ],
      "vowed": [
        "split-dogma-oxbow",
        26
      ],
      "vowel": [
        "split-dweeb",
        32
      ],
      "vroom": [
        "pilot-groom-broom",
        38
      ],
      "vying": [
        "gluts-doing",
        37
      ],
      "wacko": [
        "hotly",
        75
      ],
      "wacky": [
        "hotly",
        63
      ],
      "waded": [
        "petal-fades-jaded",
        29
      ],
      "wader": [
        "tales-pygmy-forks-waver",
        23
      ],
      "wafer": [
        "tales-pygmy-forks",
        39
      ],
      "waged": [
        "petal-fades-baked-weigh",
        39
      ],
      "wager": [
        "tales-pygmy-eager",
        42
      ],
      "wagon": [
        "natal-demos",
        47
      ],
      "waist": [
        "toils",
        53
      ],
      "waive": [
        "talus-maybe",
        41
      ],
      "waked": [
        "petal-fades-baked",
        29
      ],
      "waken": [
        "sleep-known",
        49
      ],
      "waltz": [
        "toils",
        55
      ],
      "waned": [
        "sleep-known",
        49
      ],
      "wanly": [
        "natal-manly",
        41
      ],
      "warty": [
        "tyros-party",
        45
      ],
      "waste": [
        "talus-whoop",
        50
      ],
      "watch": [
        "hotly-swamp",
        48
      ],
      "water": [
        "tales-hewed",
        47
      ],
      "waved": [
        "petal-fades-baked-weigh",
        37
      ],
      "waver": [
        "tales-pygmy-forks",
        33
      ],
      "waxed": [
        "petal-fades-baked-weigh-waved",
        29
      ],
      "waxen": [
        "sleep-known",
        49
      ],
      "weary": [
        "badly",
        58
      ],
      "weave": [
        "sloth-agave",
        43
      ],
      "wedge": [
        "toils-fudge-hedge",
        24
      ],
      "weedy": [
        "split-dogma",
        38
      ],
      "weepy": [
        "split-dopey",
        30
      ],
      "weigh": [
        "split-edify",
        36
      ],
      "weird": [
        "betel-smirk",
        43
      ],
      "whack": [
        "plush",
        76
      ],
      "whale": [
        "sloth",
        75
      ],
      "wharf": [
        "midst-hoary",
        44
      ],
      "wheat": [
        "petal-steak",
        45
      ],
      "wheel": [
        "split-dweeb",
        32
      ],
      "whelk": [
        "split-dweeb",
        32
      ],
      "whelp": [
        "split-expel",
        39
      ],
      "where": [
        "south",
        60
      ],
      "which": [
        "spoil",
        48
      ],
      "whiff": [
        "sloth-huffy",
        37
      ],
      "while": [
        "toils",
        54
      ],
      "whine": [
        "whips",
        68
      ],
      "whiny": [
        "gluts-phony",
        36
      ],
      "whirl": [
        "shout",
        58
      ],
      "whirr": [
        "shout-whirl",
        41
      ],
      "whisk": [
        "sloth-might",
        39
      ],
      "whist": [
        "sloth",
        50
      ],
      "white": [
        "toils",
        57
      ],
      "whizz": [
        "sloth-huffy",
        37
      ],
      "whole": [
        "toils",
        61
      ],
      "whomp": [
        "sloth-hooky",
        37
      ],
      "whoop": [
        "sloth-hooky",
        37
      ],
      "whorl": [
        "shout",
        60
      ],
      "whose": [
        "toils-spoke",
        31
      ],
      "widen": [
        "towel",
        65
      ],
      "wider": [
        "betel-whips",
        44
      ],
      "widow": [
        "sloth-gumbo",
        32
      ],
      "width": [
        "sloth-fifth",
        38
      ],
      "wield": [
        "split-windy",
        43
      ],
      "wight": [
        "sloth-thump-fight",
        17
      ],
      "wiled": [
        "split-flown",
        43
      ],
      "willy": [
        "sloth-billy-filly",
        24
      ],
      "wimpy": [
        "sloth-dumpy",
        28
      ],
      "wince": [
        "humps-niece",
        45
      ],
      "winch": [
        "posit",
        60
      ],
      "windy": [
        "pinot-desks",
        36
      ],
      "wined": [
        "towel-widen",
        48
      ],
      "winey": [
        "towel-widen",
        48
      ],
      "wiped": [
        "split-biped",
        46
      ],
      "wiper": [
        "betel-whips",
        43
      ],
      "wired": [
        "betel-whips-wider",
        32
      ],
      "wiser": [
        "betel-whips",
        43
      ],
      "wispy": [
        "sloth-dusky",
        39
      ],
      "witch": [
        "spoil-which",
        35
      ],
      "witty": [
        "sloth-batik",
        36
      ],
      "woken": [
        "towel-women-woven",
        40
      ],
      "woman": [
        "natal-human",
        42
      ],
      "women": [
        "towel",
        62
      ],
      "wonky": [
        "pinot-bongo",
        34
      ],
      "woody": [
        "sloth-gazed-moody",
        27
      ],
      "wooed": [
        "split-dogma-oxbow",
        27
      ],
      "wooer": [
        "betel-whips",
        43
      ],
      "wooly": [
        "sloth-loopy",
        39
      ],
      "woozy": [
        "sloth-gazed-boozy",
        22
      ],
      "wordy": [
        "shout-dowry",
        32
      ],
      "world": [
        "shout-dowry",
        32
      ],
      "wormy": [
        "shout-dowry",
        32
      ],
      "worry": [
        "shout-dowry",
        32
      ],
      "worse": [
        "south",
        66
      ],
      "worst": [
        "shout",
        60
      ],
      "worth": [
        "shout-forth",
        37
      ],
      "would": [
        "sloth-dolly",
        32
      ],
      "wound": [
        "gluts-whomp",
        39
      ],
      "woven": [
        "towel-women",
        52
      ],
      "wowed": [
        "split-dogma-oxbow-vowed",
        17
      ],
      "wrack": [
        "track-frack",
        47
      ],
      "wrath": [
        "twigs",
        75
      ],
      "wreak": [
        "tubed-freak",
        40
      ],
      "wreck": [
        "",
        89
      ],
      "wrest": [
        "defer-press",
        37
      ],
      "wring": [
        "bigot-grind",
        37
      ],
      "wrist": [
        "pilot-grist",
        32
      ],
      "write": [
        "pivot-tribe",
        50
      ],
      "wrong": [
        "bigot",
        61
      ],
      "wrote": [
        "pivot",
        75
      ],
      "wrung": [
        "bigot",
        73
      ],
      "wryly": [
        "pilot",
        60
      ],
      "wurst": [
        "shout-burst",
        41
      ],
      "xenon": [
        "towel-venom",
        41
      ],
      "xerox": [
        "betel-smirk-redux",
        23
      ],
      "yacht": [
        "hotly",
        75
      ],
      "yahoo": [
        "toils-bayou",
        35
      ],
      "yappy": [
        "toils-dumpy-happy",
        24
      ],
      "yearn": [
        "learn",
        61
      ],
      "yeast": [
        "lefts-beast",
        46
      ],
      "yield": [
        "split-windy",
        43
      ],
      "yodel": [
        "split-dweeb-model",
        17
      ],
      "yoked": [
        "split-dogma-oxbow",
        26
      ],
      "yokel": [
        "split-dweeb-kugel",
        17
      ],
      "young": [
        "gluts",
        66
      ],
      "youth": [
        "sloth-mouth",
        38
      ],
      "yucca": [
        "hotly",
        75
      ],
      "yucky": [
        "spoil-humid",
        41
      ],
      "yummy": [
        "sloth-dumpy-gummy-mummy",
        16
      ],
      "zebra": [
        "tales-rehab",
        46
      ],
      "zesty": [
        "split-testy",
        38
      ],
      "zilch": [
        "spoil-flick",
        37
      ],
      "zippy": [
        "sloth-dumpy",
        28
      ],
      "zonal": [
        "natal-final",
        48
      ],
      "zoned": [
        "towel-honey-boned",
        29
      ]
    }
  },
  "hard-simple": {
    "starting_word": "plate",
    "unsolved": [
      "bated",
      "bowed",
      "boxed",
      "busty",
      "caved",
      "cawed",
      "corer",
      "coxed",
      "dared",
      "dated",
      "doped",
      "eared",
      "eased",
      "fated",
      "faxed",
      "fazed",
      "fixed",
      "giver",
      "hatch",
      "hazed",
      "hider",
      "hound",
      "lazed",
      "lolly",
      "molly",
      "parer",
      "razed",
      "roger",
      "rover",
      "rower",
      "saved",
      "sower",
      "vaunt",
      "vowed",
      "waved",
      "waxed",
      "willy",
      "wired"
    ],
    "guesses": {
      "aback": [
        "shark-knack",
        54
      ],
      "abase": [
        "share-cease",
        55
      ],
      "abash": [
        "shark-awash",
        56
      ],
      "abate": [
        "grate-skate",
        44
      ],
      "abbey": [
        "amber",
        68
      ],
      "abbot": [
        "taint-abort",
        42
      ],
      "abhor": [
        "manor-ardor",
        40
      ],
      "abide": [
        "raise",
        71
      ],
      "abled": [
        "regal-laden-ailed",
        41
      ],
      "abode": [
        "raise-adobe",
        48
      ],
      "aboil": [
        "solar-viola",
        49
      ],
      "abort": [
        "taint",
        56
      ],
      "about": [
        "taint-abort",
        42
      ],
      "above": [
        "raise-adobe",
        48
      ],
      "abuse": [
        "raise",
        70
      ],
      "abuzz": [
        "manor-squab",
        29
      ],
      "abyss": [
        "manor-squab",
        29
      ],
      "ached": [
        "amber-ashen",
        46
      ],
      "achoo": [
        "manor-cocoa",
        41
      ],
      "acing": [
        "manor-aging",
        37
      ],
      "acorn": [
        "manor-adorn",
        39
      ],
      "acrid": [
        "manor-circa",
        38
      ],
      "acted": [
        "tread-gated",
        50
      ],
      "actor": [
        "taint-stray",
        46
      ],
      "acute": [
        "taste",
        81
      ],
      "adage": [
        "share-agave",
        61
      ],
      "adapt": [
        "apart",
        75
      ],
      "added": [
        "amber-ashen-adieu",
        35
      ],
      "adder": [
        "amber-anger",
        47
      ],
      "addle": [
        "angle-aisle-amble",
        45
      ],
      "adept": [
        "",
        90
      ],
      "adieu": [
        "amber-ashen",
        47
      ],
      "adios": [
        "manor-cocoa",
        41
      ],
      "admin": [
        "manor-human",
        41
      ],
      "admit": [
        "taint-audit",
        48
      ],
      "adobe": [
        "raise",
        65
      ],
      "adobo": [
        "manor-audio",
        37
      ],
      "adopt": [
        "kaput",
        67
      ],
      "adore": [
        "raise-argue",
        44
      ],
      "adorn": [
        "manor",
        56
      ],
      "adult": [
        "natal",
        78
      ],
      "aegis": [
        "amber-ahead",
        49
      ],
      "aerie": [
        "raise",
        76
      ],
      "affix": [
        "manor-squab",
        29
      ],
      "afire": [
        "raise",
        76
      ],
      "afoot": [
        "taint-abort",
        42
      ],
      "afore": [
        "raise-argue-adore",
        32
      ],
      "afoul": [
        "solar-viola",
        49
      ],
      "after": [
        "tread-earth",
        50
      ],
      "again": [
        "shark-guava",
        40
      ],
      "agape": [
        "spare",
        83
      ],
      "agate": [
        "grate",
        86
      ],
      "agave": [
        "share",
        68
      ],
      "agent": [
        "tread",
        74
      ],
      "agile": [
        "angle",
        79
      ],
      "aging": [
        "manor",
        50
      ],
      "agita": [
        "tarts-quota",
        41
      ],
      "aglow": [
        "solar",
        70
      ],
      "agony": [
        "manor",
        61
      ],
      "agora": [
        "manor-broad",
        34
      ],
      "agree": [
        "raise-argue",
        55
      ],
      "ahead": [
        "amber",
        66
      ],
      "ahold": [
        "solar-viola",
        49
      ],
      "aided": [
        "amber-ashen-adieu",
        35
      ],
      "aider": [
        "amber-anger-adder",
        34
      ],
      "ailed": [
        "regal-laden",
        53
      ],
      "aimed": [
        "amber",
        68
      ],
      "aioli": [
        "solar-viola",
        49
      ],
      "aired": [
        "amber",
        64
      ],
      "aisle": [
        "angle",
        70
      ],
      "alarm": [
        "clans-flair",
        41
      ],
      "album": [
        "aloha-align",
        47
      ],
      "alder": [
        "clean-alley",
        50
      ],
      "alert": [
        "cleat",
        67
      ],
      "algae": [
        "alike-alone",
        48
      ],
      "alias": [
        "aloha-allay",
        53
      ],
      "alibi": [
        "aloha-align",
        47
      ],
      "alien": [
        "clean",
        79
      ],
      "align": [
        "aloha",
        63
      ],
      "alike": [
        "",
        91
      ],
      "alive": [
        "alike",
        79
      ],
      "allay": [
        "aloha",
        70
      ],
      "alley": [
        "clean",
        67
      ],
      "allot": [
        "float",
        74
      ],
      "allow": [
        "aloha",
        75
      ],
      "alloy": [
        "aloha-allow",
        58
      ],
      "aloft": [
        "float",
        74
      ],
      "aloha": [
        "",
        91
      ],
      "alone": [
        "alike",
        65
      ],
      "along": [
        "aloha-aloud",
        54
      ],
      "aloof": [
        "aloha-aloud-along",
        41
      ],
      "aloud": [
        "aloha",
        63
      ],
      "alpha": [
        "",
        99
      ],
      "altar": [
        "float",
        74
      ],
      "alter": [
        "cleat",
        67
      ],
      "amaro": [
        "shark-award",
        45
      ],
      "amass": [
        "shark",
        67
      ],
      "amaze": [
        "share-agave-awake",
        41
      ],
      "amber": [
        "",
        72
      ],
      "ambit": [
        "taint-audit",
        48
      ],
      "amble": [
        "angle-aisle",
        57
      ],
      "amend": [
        "amber",
        68
      ],
      "amigo": [
        "manor-dogma",
        42
      ],
      "amino": [
        "manor-among",
        47
      ],
      "amiss": [
        "manor",
        57
      ],
      "amity": [
        "tarts-quota",
        41
      ],
      "among": [
        "manor",
        56
      ],
      "amour": [
        "manor",
        58
      ],
      "amped": [
        "caper-aspen",
        47
      ],
      "ample": [
        "maple",
        66
      ],
      "amply": [
        "apply",
        66
      ],
      "amuck": [
        "manor-amiss",
        41
      ],
      "amuse": [
        "raise-abuse",
        53
      ],
      "ancho": [
        "manor-agony",
        44
      ],
      "angel": [
        "regal",
        69
      ],
      "anger": [
        "amber",
        59
      ],
      "angle": [
        "",
        87
      ],
      "angry": [
        "manor-urban",
        43
      ],
      "angst": [
        "taint",
        71
      ],
      "anime": [
        "raise-abide",
        55
      ],
      "anise": [
        "raise",
        76
      ],
      "ankle": [
        "angle",
        69
      ],
      "annal": [
        "solar-canal",
        44
      ],
      "annex": [
        "amber-ashen",
        46
      ],
      "annoy": [
        "manor",
        58
      ],
      "annul": [
        "solar-daily-awful",
        30
      ],
      "anode": [
        "raise-adobe",
        48
      ],
      "anole": [
        "angle-ankle",
        52
      ],
      "antic": [
        "taint",
        71
      ],
      "antsy": [
        "taint",
        60
      ],
      "anvil": [
        "solar-daily",
        43
      ],
      "aorta": [
        "tarts",
        79
      ],
      "apace": [
        "spare",
        83
      ],
      "apart": [
        "",
        92
      ],
      "aphid": [
        "carps-aping",
        46
      ],
      "aping": [
        "carps",
        62
      ],
      "apnea": [
        "caper",
        70
      ],
      "apple": [
        "maple",
        66
      ],
      "apply": [
        "",
        91
      ],
      "apron": [
        "carps",
        74
      ],
      "aptly": [
        "",
        86
      ],
      "arbor": [
        "manor-ardor",
        40
      ],
      "arced": [
        "amber-aired",
        48
      ],
      "ardor": [
        "manor",
        57
      ],
      "arena": [
        "amber",
        68
      ],
      "argon": [
        "manor-arson",
        44
      ],
      "argot": [
        "taint-abort",
        42
      ],
      "argue": [
        "raise",
        67
      ],
      "arise": [
        "raise",
        76
      ],
      "armed": [
        "amber",
        68
      ],
      "armor": [
        "manor",
        58
      ],
      "aroma": [
        "manor",
        58
      ],
      "arose": [
        "raise",
        76
      ],
      "array": [
        "manor-circa",
        38
      ],
      "arrow": [
        "manor",
        58
      ],
      "arson": [
        "manor",
        61
      ],
      "artsy": [
        "taint-stray",
        46
      ],
      "ascot": [
        "taint-abort",
        42
      ],
      "ashed": [
        "amber-ashen",
        46
      ],
      "ashen": [
        "amber",
        63
      ],
      "aside": [
        "raise",
        76
      ],
      "asked": [
        "amber-ashen-askew",
        35
      ],
      "asker": [
        "amber-anger-adder",
        34
      ],
      "askew": [
        "amber-ashen",
        47
      ],
      "aspen": [
        "caper",
        63
      ],
      "aspic": [
        "carps",
        74
      ],
      "assay": [
        "manor-squab",
        29
      ],
      "asset": [
        "tread-eaten",
        54
      ],
      "aster": [
        "tread-earth-after",
        38
      ],
      "astir": [
        "taint-sitar",
        49
      ],
      "atlas": [
        "natal",
        78
      ],
      "atoll": [
        "natal",
        78
      ],
      "atone": [
        "bathe",
        61
      ],
      "atria": [
        "taint-sitar",
        49
      ],
      "attic": [
        "taint",
        71
      ],
      "audio": [
        "manor",
        53
      ],
      "audit": [
        "taint",
        65
      ],
      "auger": [
        "amber-anger",
        49
      ],
      "augur": [
        "manor-cigar",
        38
      ],
      "aunty": [
        "tarts-quota",
        41
      ],
      "aural": [
        "solar-mural-rural",
        36
      ],
      "avail": [
        "crawl-shall",
        47
      ],
      "avast": [
        "scant-roast",
        55
      ],
      "avert": [
        "tread",
        74
      ],
      "avian": [
        "manor-aging",
        38
      ],
      "avoid": [
        "manor-audio",
        37
      ],
      "await": [
        "scant-draft",
        40
      ],
      "awake": [
        "share-agave",
        53
      ],
      "award": [
        "shark",
        54
      ],
      "aware": [
        "share",
        78
      ],
      "awash": [
        "shark",
        62
      ],
      "awful": [
        "solar-daily",
        43
      ],
      "awoke": [
        "raise-adobe",
        48
      ],
      "axial": [
        "solar-canal",
        44
      ],
      "axing": [
        "manor-aging-acing",
        25
      ],
      "axiom": [
        "manor",
        58
      ],
      "axion": [
        "manor",
        58
      ],
      "azure": [
        "raise-argue",
        55
      ],
      "babka": [
        "manor-daubs-baggy",
        28
      ],
      "bacon": [
        "manor",
        58
      ],
      "badge": [
        "raise-cadge",
        53
      ],
      "badly": [
        "solar-daily",
        39
      ],
      "bagel": [
        "regal-angel",
        52
      ],
      "baggy": [
        "manor-daubs",
        40
      ],
      "baked": [
        "amber",
        62
      ],
      "baker": [
        "amber",
        59
      ],
      "baldy": [
        "solar-balmy-balky",
        28
      ],
      "baled": [
        "regal-laden",
        52
      ],
      "baler": [
        "regal-laser",
        50
      ],
      "balky": [
        "solar-balmy",
        40
      ],
      "balmy": [
        "solar",
        55
      ],
      "balsa": [
        "solar",
        70
      ],
      "banal": [
        "solar-canal",
        44
      ],
      "bandy": [
        "manor-dance-sandy-handy",
        24
      ],
      "banjo": [
        "manor",
        58
      ],
      "bared": [
        "amber",
        68
      ],
      "barer": [
        "amber-baker",
        43
      ],
      "barge": [
        "raise-cadre",
        45
      ],
      "baron": [
        "manor-rayon",
        40
      ],
      "barre": [
        "raise-cadre",
        45
      ],
      "basal": [
        "solar-nasal",
        50
      ],
      "based": [
        "amber-baked",
        53
      ],
      "basic": [
        "manor-daubs",
        37
      ],
      "basil": [
        "solar",
        70
      ],
      "basin": [
        "manor",
        54
      ],
      "basis": [
        "manor-daubs",
        37
      ],
      "baste": [
        "taste-waste-caste-haste",
        40
      ],
      "batch": [
        "taint-maths",
        43
      ],
      "bated": [
        "tread-gated-sated-hated-mated",
        45
      ],
      "bathe": [
        "",
        86
      ],
      "batik": [
        "taint-ratio",
        50
      ],
      "baton": [
        "taint",
        71
      ],
      "batty": [
        "tarts-fatty-natty-catty",
        41
      ],
      "bawdy": [
        "manor-daubs",
        37
      ],
      "bayed": [
        "amber-baked-based",
        40
      ],
      "bayou": [
        "manor-yahoo",
        39
      ],
      "beach": [
        "heard",
        72
      ],
      "beady": [
        "heard",
        72
      ],
      "beard": [
        "heard",
        72
      ],
      "beast": [
        "teary",
        64
      ],
      "beaut": [
        "teary-beast",
        47
      ],
      "bebop": [
        "speed-equip",
        45
      ],
      "beech": [
        "diner-becks",
        35
      ],
      "beefy": [
        "diner-becks",
        27
      ],
      "befit": [
        "reset-debit",
        38
      ],
      "befog": [
        "diner-becks-beefy",
        15
      ],
      "began": [
        "amber",
        68
      ],
      "begat": [
        "tread",
        74
      ],
      "beget": [
        "reset-tenet",
        50
      ],
      "begin": [
        "diner-eking",
        37
      ],
      "begot": [
        "reset-debit",
        38
      ],
      "begun": [
        "diner-envoy",
        38
      ],
      "beige": [
        "snore-guide",
        37
      ],
      "being": [
        "diner-eking",
        37
      ],
      "belay": [
        "regal-delay",
        55
      ],
      "belch": [
        "lever-cello",
        49
      ],
      "belie": [
        "bugle",
        75
      ],
      "belle": [
        "bugle",
        65
      ],
      "belly": [
        "lever-cello",
        48
      ],
      "below": [
        "lever-cello-felon",
        31
      ],
      "bench": [
        "diner-venom",
        39
      ],
      "bendy": [
        "diner",
        54
      ],
      "bento": [
        "tenth",
        63
      ],
      "beret": [
        "reset",
        68
      ],
      "berry": [
        "diner-mercy-ferry",
        19
      ],
      "berth": [
        "tenth",
        79
      ],
      "beryl": [
        "lever-relic",
        46
      ],
      "beset": [
        "reset",
        68
      ],
      "besot": [
        "reset",
        68
      ],
      "betel": [
        "islet-hotel",
        42
      ],
      "bevel": [
        "lever",
        72
      ],
      "bezel": [
        "lever-jewel",
        51
      ],
      "bible": [
        "bugle-belle",
        48
      ],
      "bicep": [
        "speed-ripen",
        49
      ],
      "biddy": [
        "corns-fudgy",
        26
      ],
      "bided": [
        "diner-video-sided",
        33
      ],
      "bidet": [
        "reset-civet",
        36
      ],
      "bigot": [
        "roust-idiot",
        38
      ],
      "biked": [
        "diner-video-miked-hiked",
        40
      ],
      "biker": [
        "diner-riser-fiber",
        36
      ],
      "bilge": [
        "bugle",
        75
      ],
      "billy": [
        "could-skill-hilly-filly",
        32
      ],
      "binge": [
        "snore-niche",
        41
      ],
      "bingo": [
        "corns-union",
        33
      ],
      "biome": [
        "snore-evoke-booze",
        36
      ],
      "biped": [
        "speed-moped",
        49
      ],
      "bipod": [
        "croup-oomph",
        42
      ],
      "birch": [
        "corns",
        50
      ],
      "birth": [
        "softy",
        66
      ],
      "bison": [
        "corns-snowy",
        35
      ],
      "biter": [
        "reset-outer-miter",
        25
      ],
      "bitsy": [
        "roust-ditsy",
        38
      ],
      "bitty": [
        "softy-ditty-witty-kitty",
        29
      ],
      "black": [
        "clans",
        70
      ],
      "blade": [
        "blare",
        77
      ],
      "blame": [
        "blare-blade",
        66
      ],
      "bland": [
        "clans",
        63
      ],
      "blank": [
        "clans-bland",
        47
      ],
      "blare": [
        "",
        90
      ],
      "blase": [
        "blare-blade-blame-blaze",
        48
      ],
      "blast": [
        "",
        86
      ],
      "blaze": [
        "blare-blade-blame",
        58
      ],
      "bleak": [
        "clean",
        59
      ],
      "bleat": [
        "cleat",
        67
      ],
      "bleed": [
        "",
        89
      ],
      "bleep": [
        "sleep",
        61
      ],
      "blend": [
        "bleed",
        76
      ],
      "bless": [
        "bleed",
        76
      ],
      "blimp": [
        "slump",
        57
      ],
      "blind": [
        "flunk-cling",
        48
      ],
      "bling": [
        "flunk-cling-sling",
        32
      ],
      "blink": [
        "flunk",
        66
      ],
      "bliss": [
        "flunk-gloms",
        43
      ],
      "blitz": [
        "",
        92
      ],
      "bloat": [
        "float-gloat",
        43
      ],
      "block": [
        "flunk-clock",
        47
      ],
      "bloke": [
        "clove-globe",
        55
      ],
      "blond": [
        "flunk-cling",
        48
      ],
      "blood": [
        "flunk-gloms",
        43
      ],
      "bloom": [
        "flunk-gloms",
        43
      ],
      "bloop": [
        "slump",
        57
      ],
      "blown": [
        "flunk-clown",
        51
      ],
      "bluer": [
        "bleed",
        76
      ],
      "bluff": [
        "flunk",
        74
      ],
      "blunt": [
        "flirt-clout",
        44
      ],
      "blurb": [
        "flunk-blush",
        50
      ],
      "blurt": [
        "flirt",
        74
      ],
      "blush": [
        "flunk",
        66
      ],
      "board": [
        "shark-award",
        40
      ],
      "boast": [
        "scant-roast",
        52
      ],
      "bobby": [
        "corns-goody-hobby",
        20
      ],
      "bocce": [
        "snore-vogue-moxie",
        27
      ],
      "boded": [
        "diner-modem-codex",
        27
      ],
      "boffo": [
        "corns-goody",
        35
      ],
      "bogey": [
        "diner-cheek",
        37
      ],
      "boggy": [
        "corns-goody-foggy",
        26
      ],
      "bogie": [
        "snore-vogue",
        42
      ],
      "bogus": [
        "corns",
        54
      ],
      "boing": [
        "corns-downy-going",
        25
      ],
      "bolus": [
        "could-mogul",
        45
      ],
      "boned": [
        "diner-coned-honed",
        41
      ],
      "boner": [
        "diner-owner-goner",
        29
      ],
      "boney": [
        "diner-honey-money",
        29
      ],
      "bongo": [
        "corns-gonzo",
        38
      ],
      "bonny": [
        "corns-downy-moony",
        24
      ],
      "bonus": [
        "corns",
        50
      ],
      "booby": [
        "corns-goody-boozy",
        23
      ],
      "booed": [
        "diner-modem-wooed-cooed",
        34
      ],
      "boost": [
        "roust-moist",
        43
      ],
      "booth": [
        "softy-motto",
        53
      ],
      "booty": [
        "softy-dotty",
        50
      ],
      "booze": [
        "snore-evoke",
        48
      ],
      "boozy": [
        "corns-goody",
        30
      ],
      "borax": [
        "manor-broad",
        34
      ],
      "bored": [
        "diner-breed",
        41
      ],
      "boric": [
        "corns",
        50
      ],
      "borne": [
        "snore",
        64
      ],
      "boron": [
        "corns-moron",
        39
      ],
      "bosom": [
        "corns",
        52
      ],
      "boson": [
        "corns-noisy",
        39
      ],
      "bossy": [
        "corns-bosom",
        35
      ],
      "botch": [
        "roust-notch",
        27
      ],
      "bough": [
        "corns-goody",
        35
      ],
      "boule": [
        "bugle",
        75
      ],
      "bound": [
        "corns-downy-mound",
        35
      ],
      "bowed": [
        "diner-modem-wooed-sowed-cowed",
        33
      ],
      "bowel": [
        "lever-yodel",
        48
      ],
      "bower": [
        "diner-fever",
        35
      ],
      "boxed": [
        "diner-modem-wooed-yoked-hosed",
        26
      ],
      "boxer": [
        "diner-fever-bower",
        31
      ],
      "brace": [
        "share-crave-grace",
        43
      ],
      "braid": [
        "shark-brand",
        43
      ],
      "brain": [
        "shark-brand",
        41
      ],
      "brake": [
        "share-crave-grade-frame",
        29
      ],
      "brand": [
        "shark",
        51
      ],
      "brash": [
        "shark-crash",
        48
      ],
      "brass": [
        "shark-grass",
        55
      ],
      "brava": [
        "shark-brand-bravo",
        31
      ],
      "brave": [
        "share-crave-grave",
        43
      ],
      "bravo": [
        "shark-brand",
        43
      ],
      "brawl": [
        "crawl",
        71
      ],
      "brawn": [
        "shark-brand-brain",
        29
      ],
      "bread": [
        "amber",
        65
      ],
      "break": [
        "amber-bread",
        48
      ],
      "bream": [
        "amber",
        68
      ],
      "breed": [
        "diner",
        51
      ],
      "briar": [
        "manor-cigar-friar",
        24
      ],
      "bribe": [
        "snore-verge-crude",
        27
      ],
      "brick": [
        "corns",
        50
      ],
      "bride": [
        "snore-verge-crude",
        27
      ],
      "brief": [
        "diner-grief",
        39
      ],
      "brier": [
        "diner-crier",
        37
      ],
      "brine": [
        "snore-urine",
        47
      ],
      "bring": [
        "corns",
        44
      ],
      "brink": [
        "corns-bring",
        31
      ],
      "briny": [
        "corns-bring-brink",
        18
      ],
      "brisk": [
        "corns",
        48
      ],
      "broad": [
        "manor",
        51
      ],
      "broil": [
        "could-lingo",
        38
      ],
      "broke": [
        "snore-drove",
        46
      ],
      "bronc": [
        "corns",
        50
      ],
      "brood": [
        "corns-vroom",
        36
      ],
      "brook": [
        "corns-vroom-brood",
        23
      ],
      "broom": [
        "corns-vroom-groom",
        19
      ],
      "broth": [
        "softy",
        68
      ],
      "brown": [
        "corns-drown-grown",
        39
      ],
      "brunt": [
        "roust",
        55
      ],
      "brush": [
        "corns-brisk",
        36
      ],
      "brusk": [
        "corns-brisk",
        36
      ],
      "brute": [
        "route",
        82
      ],
      "buddy": [
        "corns-fudgy-muddy",
        15
      ],
      "budge": [
        "snore-guide-judge",
        31
      ],
      "buggy": [
        "corns-fudgy",
        27
      ],
      "bugle": [
        "",
        84
      ],
      "build": [
        "could",
        61
      ],
      "built": [
        "guilt",
        59
      ],
      "bulge": [
        "bugle",
        75
      ],
      "bulgy": [
        "could-bulky",
        50
      ],
      "bulky": [
        "could",
        60
      ],
      "bully": [
        "could-bulls",
        46
      ],
      "bumpy": [
        "croup",
        56
      ],
      "bunch": [
        "corns",
        52
      ],
      "bunny": [
        "corns-dying-funny",
        25
      ],
      "burka": [
        "manor-circa-bursa",
        23
      ],
      "burly": [
        "could-bulls",
        46
      ],
      "burnt": [
        "roust",
        60
      ],
      "burro": [
        "corns-furor",
        39
      ],
      "bursa": [
        "manor-circa",
        36
      ],
      "burst": [
        "roust",
        61
      ],
      "bused": [
        "diner-modem-edges",
        40
      ],
      "bushy": [
        "corns-smush",
        26
      ],
      "busty": [
        "softy-rusty-dusty-musty-gusty",
        39
      ],
      "butch": [
        "roust",
        46
      ],
      "butte": [
        "route-suite",
        44
      ],
      "buxom": [
        "corns-gizmo",
        29
      ],
      "buyer": [
        "diner-fever-bower",
        31
      ],
      "buzzy": [
        "corns-fudgy-mummy",
        23
      ],
      "bylaw": [
        "solar-lilac-gulag",
        36
      ],
      "byway": [
        "manor-squab",
        29
      ],
      "cabal": [
        "solar-canal",
        44
      ],
      "cabby": [
        "manor-daubs",
        38
      ],
      "cabin": [
        "manor-basin",
        42
      ],
      "cable": [
        "angle",
        67
      ],
      "cacao": [
        "manor",
        57
      ],
      "cache": [
        "raise-cadge",
        46
      ],
      "cacti": [
        "tarts-faith",
        53
      ],
      "caddy": [
        "manor-daubs",
        37
      ],
      "cadet": [
        "tread",
        74
      ],
      "cadge": [
        "raise",
        58
      ],
      "cadre": [
        "raise",
        62
      ],
      "caged": [
        "amber-naked-jaded",
        48
      ],
      "cagey": [
        "amber-naked",
        49
      ],
      "cairn": [
        "manor-rainy",
        42
      ],
      "caked": [
        "amber-naked",
        40
      ],
      "calve": [
        "angle-value-salve-halve",
        34
      ],
      "camel": [
        "regal-email",
        53
      ],
      "cameo": [
        "amber-gamed",
        39
      ],
      "campy": [
        "carps",
        74
      ],
      "canal": [
        "solar",
        60
      ],
      "candy": [
        "manor-dance",
        42
      ],
      "caned": [
        "amber-naked",
        38
      ],
      "canny": [
        "manor-dance",
        42
      ],
      "canoe": [
        "raise-cadge-cache",
        34
      ],
      "canon": [
        "manor",
        58
      ],
      "caped": [
        "caper",
        70
      ],
      "caper": [
        "",
        91
      ],
      "capon": [
        "carps",
        74
      ],
      "capri": [
        "carps",
        74
      ],
      "caput": [
        "kaput",
        67
      ],
      "carat": [
        "taint",
        65
      ],
      "cared": [
        "amber-raven",
        56
      ],
      "carer": [
        "amber-rager",
        48
      ],
      "caret": [
        "tread-earth",
        53
      ],
      "cargo": [
        "manor-radio",
        43
      ],
      "carny": [
        "manor-rainy",
        42
      ],
      "carob": [
        "manor",
        58
      ],
      "carol": [
        "solar",
        70
      ],
      "carom": [
        "manor",
        58
      ],
      "carry": [
        "manor-hardy",
        31
      ],
      "carte": [
        "taste-haute",
        54
      ],
      "carve": [
        "raise-cadre",
        45
      ],
      "cased": [
        "amber-naked-jaded-caged",
        49
      ],
      "caste": [
        "taste-waste",
        57
      ],
      "catch": [
        "taint-maths-batch-watch",
        38
      ],
      "cater": [
        "tread-earth",
        45
      ],
      "catty": [
        "tarts-fatty-natty",
        51
      ],
      "caulk": [
        "solar-daily",
        43
      ],
      "cause": [
        "raise-masse",
        53
      ],
      "caved": [
        "amber-naked-jaded-caged-cased",
        40
      ],
      "cavil": [
        "solar-daily",
        43
      ],
      "cawed": [
        "amber-naked-jaded-caged-cased",
        40
      ],
      "cease": [
        "share",
        72
      ],
      "cedar": [
        "amber-swear",
        48
      ],
      "ceded": [
        "diner-modem",
        36
      ],
      "celeb": [
        "lever-jewel",
        51
      ],
      "cello": [
        "lever",
        57
      ],
      "chafe": [
        "share",
        78
      ],
      "chaff": [
        "shark-chain",
        51
      ],
      "chain": [
        "shark",
        68
      ],
      "chair": [
        "shark",
        70
      ],
      "chalk": [
        "crawl",
        84
      ],
      "champ": [
        "cramp",
        73
      ],
      "chant": [
        "scant",
        78
      ],
      "chaos": [
        "shark",
        65
      ],
      "chard": [
        "shark-charm",
        48
      ],
      "charm": [
        "shark",
        61
      ],
      "chart": [
        "scant",
        66
      ],
      "chary": [
        "shark-charm-chard",
        36
      ],
      "chase": [
        "share",
        78
      ],
      "chasm": [
        "shark-chaos",
        48
      ],
      "cheap": [
        "caper",
        70
      ],
      "cheat": [
        "tread",
        63
      ],
      "check": [
        "diner-becks",
        35
      ],
      "cheek": [
        "diner",
        46
      ],
      "cheep": [
        "speed-creep",
        48
      ],
      "cheer": [
        "diner-fever-sheer",
        29
      ],
      "chemo": [
        "diner-becks-chewy",
        18
      ],
      "chess": [
        "diner-becks",
        35
      ],
      "chest": [
        "reset-guest",
        43
      ],
      "chewy": [
        "diner-becks",
        30
      ],
      "chick": [
        "corns-civic",
        35
      ],
      "chide": [
        "snore-guide",
        37
      ],
      "chief": [
        "diner",
        54
      ],
      "child": [
        "could",
        64
      ],
      "chile": [
        "bugle-while",
        52
      ],
      "chili": [
        "could-chill",
        43
      ],
      "chill": [
        "could",
        60
      ],
      "chime": [
        "snore-guide",
        36
      ],
      "chimp": [
        "croup",
        70
      ],
      "china": [
        "manor-aging",
        38
      ],
      "chino": [
        "corns",
        50
      ],
      "chirp": [
        "croup",
        70
      ],
      "chive": [
        "snore-guide-chime",
        24
      ],
      "chock": [
        "corns",
        55
      ],
      "choir": [
        "corns-chord",
        42
      ],
      "choke": [
        "snore-evoke",
        51
      ],
      "chomp": [
        "croup",
        70
      ],
      "chord": [
        "corns",
        52
      ],
      "chore": [
        "snore",
        64
      ],
      "chose": [
        "snore",
        62
      ],
      "choux": [
        "corns-chock",
        38
      ],
      "chuck": [
        "corns-civic",
        35
      ],
      "chump": [
        "croup",
        70
      ],
      "chunk": [
        "corns",
        56
      ],
      "churl": [
        "could",
        64
      ],
      "churn": [
        "corns",
        50
      ],
      "chute": [
        "route",
        82
      ],
      "cider": [
        "diner-wider-rider",
        41
      ],
      "cigar": [
        "manor",
        50
      ],
      "cilia": [
        "solar-balmy-villa",
        27
      ],
      "cinch": [
        "corns-cumin",
        38
      ],
      "circa": [
        "manor",
        52
      ],
      "cited": [
        "reset-token",
        39
      ],
      "civet": [
        "reset",
        52
      ],
      "civic": [
        "corns",
        52
      ],
      "civil": [
        "could",
        64
      ],
      "clack": [
        "clans-claim",
        56
      ],
      "clade": [
        "blare-flake-glaze-clave",
        30
      ],
      "claim": [
        "clans",
        72
      ],
      "clamp": [
        "",
        86
      ],
      "clang": [
        "clans",
        67
      ],
      "clank": [
        "clans-clang",
        51
      ],
      "clash": [
        "clans",
        80
      ],
      "clasp": [
        "clamp",
        61
      ],
      "class": [
        "clans",
        80
      ],
      "clave": [
        "blare-flake-glaze",
        40
      ],
      "clean": [
        "",
        92
      ],
      "clear": [
        "clean",
        79
      ],
      "cleat": [
        "",
        91
      ],
      "cleft": [
        "fleet",
        66
      ],
      "clerk": [
        "bleed",
        63
      ],
      "click": [
        "flunk-clock",
        47
      ],
      "cliff": [
        "flunk",
        74
      ],
      "climb": [
        "flunk-gloms",
        43
      ],
      "clime": [
        "clove",
        81
      ],
      "cling": [
        "flunk",
        58
      ],
      "clink": [
        "flunk-blink-slink",
        43
      ],
      "cloak": [
        "aloha",
        72
      ],
      "clock": [
        "flunk",
        64
      ],
      "clomp": [
        "slump-blimp",
        41
      ],
      "clone": [
        "clove-close",
        51
      ],
      "close": [
        "clove",
        68
      ],
      "cloth": [
        "blitz",
        63
      ],
      "cloud": [
        "flunk",
        74
      ],
      "clout": [
        "flirt",
        60
      ],
      "clove": [
        "",
        90
      ],
      "clown": [
        "flunk",
        68
      ],
      "cluck": [
        "flunk",
        74
      ],
      "clued": [
        "bleed",
        58
      ],
      "clump": [
        "slump",
        75
      ],
      "clung": [
        "flunk",
        70
      ],
      "clunk": [
        "flunk-slunk",
        54
      ],
      "coach": [
        "shark",
        70
      ],
      "coast": [
        "scant",
        78
      ],
      "coati": [
        "wrath",
        62
      ],
      "cobra": [
        "manor-broad",
        34
      ],
      "cocky": [
        "corns-comic-couch",
        24
      ],
      "cocoa": [
        "manor",
        58
      ],
      "coded": [
        "diner-modem-codex",
        27
      ],
      "coder": [
        "diner-order",
        41
      ],
      "codex": [
        "diner-modem",
        40
      ],
      "colic": [
        "could-color",
        43
      ],
      "colon": [
        "could-color",
        43
      ],
      "color": [
        "could",
        60
      ],
      "combo": [
        "corns-comic",
        45
      ],
      "comet": [
        "reset-civet",
        36
      ],
      "comfy": [
        "corns-comic-combo",
        32
      ],
      "comic": [
        "corns",
        49
      ],
      "comma": [
        "manor-dogma",
        42
      ],
      "conch": [
        "corns-condo",
        40
      ],
      "condo": [
        "corns",
        53
      ],
      "coned": [
        "diner",
        52
      ],
      "conga": [
        "manor-gonna",
        41
      ],
      "conic": [
        "corns-condo-conch",
        28
      ],
      "cooed": [
        "diner-modem-wooed",
        44
      ],
      "copay": [
        "carps",
        74
      ],
      "coped": [
        "speed-moped-roped",
        49
      ],
      "copse": [
        "spire",
        77
      ],
      "coral": [
        "solar",
        66
      ],
      "cored": [
        "diner-breed-shred",
        41
      ],
      "corer": [
        "diner-fever-bower-homer-joker",
        16
      ],
      "corgi": [
        "corns",
        49
      ],
      "corky": [
        "corns-corgi",
        32
      ],
      "corny": [
        "corns",
        50
      ],
      "corps": [
        "croup",
        70
      ],
      "couch": [
        "corns-comic",
        37
      ],
      "cough": [
        "corns-comic",
        43
      ],
      "could": [
        "",
        68
      ],
      "count": [
        "roust",
        53
      ],
      "coupe": [
        "spire",
        77
      ],
      "court": [
        "roust",
        60
      ],
      "couth": [
        "softy-motto-north",
        31
      ],
      "coven": [
        "diner-seven-woven",
        31
      ],
      "cover": [
        "diner-fever",
        41
      ],
      "covet": [
        "reset-civet",
        36
      ],
      "covey": [
        "diner-cheek",
        39
      ],
      "cowed": [
        "diner-modem-wooed-sowed",
        41
      ],
      "cower": [
        "diner-fever-bower-mower",
        27
      ],
      "coxed": [
        "diner-modem-wooed-yoked-hosed",
        26
      ],
      "coyly": [
        "could",
        64
      ],
      "crack": [
        "shark-frack",
        43
      ],
      "craft": [
        "scant-chart",
        49
      ],
      "cramp": [
        "",
        91
      ],
      "crane": [
        "share-crave",
        55
      ],
      "crank": [
        "shark-frack",
        48
      ],
      "crash": [
        "shark",
        65
      ],
      "crass": [
        "shark-grass-brass",
        42
      ],
      "crate": [
        "grate-irate",
        62
      ],
      "crave": [
        "share",
        59
      ],
      "crawl": [
        "",
        88
      ],
      "craze": [
        "share-crave-crane",
        43
      ],
      "crazy": [
        "shark-brand",
        36
      ],
      "creak": [
        "amber-wreak-freak",
        33
      ],
      "cream": [
        "amber",
        65
      ],
      "credo": [
        "diner",
        53
      ],
      "creed": [
        "diner-breed-greed-freed",
        28
      ],
      "creek": [
        "diner-screw",
        39
      ],
      "creep": [
        "speed",
        65
      ],
      "crema": [
        "amber-cream",
        48
      ],
      "creme": [
        "snore-verge",
        38
      ],
      "crepe": [
        "spire",
        60
      ],
      "crept": [
        "",
        90
      ],
      "cress": [
        "diner-mercy",
        35
      ],
      "crest": [
        "reset",
        64
      ],
      "crick": [
        "corns-crumb",
        38
      ],
      "cried": [
        "diner",
        56
      ],
      "crier": [
        "diner",
        53
      ],
      "crime": [
        "snore-verge-crude",
        27
      ],
      "crimp": [
        "croup-crisp",
        44
      ],
      "crisp": [
        "croup",
        61
      ],
      "croak": [
        "manor-broad",
        34
      ],
      "crock": [
        "corns-chord-crook",
        27
      ],
      "crone": [
        "snore-drone",
        48
      ],
      "crony": [
        "corns",
        50
      ],
      "crook": [
        "corns-chord",
        40
      ],
      "croon": [
        "corns-crown",
        38
      ],
      "cross": [
        "corns",
        50
      ],
      "croup": [
        "",
        78
      ],
      "crowd": [
        "corns-chord",
        42
      ],
      "crown": [
        "corns",
        55
      ],
      "crude": [
        "snore-verge",
        39
      ],
      "cruel": [
        "lever",
        67
      ],
      "crumb": [
        "corns",
        55
      ],
      "crump": [
        "croup",
        70
      ],
      "crush": [
        "corns",
        50
      ],
      "crust": [
        "roust",
        58
      ],
      "crypt": [
        "tromp",
        66
      ],
      "cubby": [
        "corns-civic",
        35
      ],
      "cubed": [
        "diner-modem-edges",
        40
      ],
      "cubic": [
        "corns-civic",
        35
      ],
      "cubit": [
        "roust-unfit",
        40
      ],
      "cuing": [
        "corns-chunk",
        39
      ],
      "cumin": [
        "corns",
        55
      ],
      "cupid": [
        "croup",
        70
      ],
      "cured": [
        "diner-breed-shred-cored",
        31
      ],
      "curer": [
        "diner-fever-bower-usher",
        22
      ],
      "curio": [
        "corns",
        50
      ],
      "curly": [
        "could",
        64
      ],
      "curry": [
        "corns",
        54
      ],
      "curse": [
        "snore",
        62
      ],
      "curve": [
        "snore-verge",
        38
      ],
      "curvy": [
        "corns-curry",
        37
      ],
      "cushy": [
        "corns",
        50
      ],
      "cuter": [
        "reset-outer",
        43
      ],
      "cutie": [
        "terse-untie",
        51
      ],
      "cutup": [
        "tromp",
        45
      ],
      "cyber": [
        "diner-fever-bower",
        35
      ],
      "cycle": [
        "bugle-while",
        52
      ],
      "cynic": [
        "corns-cumin",
        38
      ],
      "dacha": [
        "manor-daubs-daddy",
        26
      ],
      "daddy": [
        "manor-daubs",
        38
      ],
      "daffy": [
        "manor-daubs-daddy",
        26
      ],
      "daily": [
        "solar",
        52
      ],
      "dairy": [
        "manor-hardy",
        31
      ],
      "daisy": [
        "manor-daubs",
        37
      ],
      "dally": [
        "solar-balmy",
        46
      ],
      "dance": [
        "raise-cadge",
        53
      ],
      "dandy": [
        "manor-dance",
        42
      ],
      "dared": [
        "amber-raven-cared-oared-fared",
        41
      ],
      "dated": [
        "tread-gated-sated-hated-mated",
        45
      ],
      "dater": [
        "tread",
        74
      ],
      "datum": [
        "taint-maths",
        48
      ],
      "daunt": [
        "taint-haunt-gaunt-jaunt",
        40
      ],
      "dazed": [
        "amber-naked-jaded",
        37
      ],
      "dealt": [
        "least",
        64
      ],
      "death": [
        "",
        90
      ],
      "debar": [
        "amber-rebar",
        43
      ],
      "debit": [
        "reset",
        55
      ],
      "debug": [
        "diner-decoy",
        38
      ],
      "debut": [
        "reset-debit",
        38
      ],
      "decaf": [
        "amber-sedan-decay",
        25
      ],
      "decal": [
        "regal",
        65
      ],
      "decay": [
        "amber-sedan",
        38
      ],
      "decor": [
        "diner",
        58
      ],
      "decoy": [
        "diner",
        54
      ],
      "decry": [
        "diner",
        52
      ],
      "defer": [
        "diner-dryer",
        41
      ],
      "defog": [
        "diner-decoy",
        38
      ],
      "deify": [
        "diner",
        54
      ],
      "deign": [
        "diner",
        54
      ],
      "deist": [
        "reset-heist",
        43
      ],
      "deity": [
        "tenth",
        57
      ],
      "delay": [
        "regal",
        71
      ],
      "delta": [
        "",
        99
      ],
      "delve": [
        "bugle-solve",
        50
      ],
      "demon": [
        "diner",
        54
      ],
      "demur": [
        "diner-decor",
        41
      ],
      "denim": [
        "diner",
        54
      ],
      "dense": [
        "snore",
        64
      ],
      "depot": [
        "crept-upset",
        49
      ],
      "depth": [
        "",
        86
      ],
      "derby": [
        "diner-decry",
        35
      ],
      "deter": [
        "reset",
        64
      ],
      "detox": [
        "reset-fetch",
        42
      ],
      "deuce": [
        "snore-guide",
        34
      ],
      "devil": [
        "lever",
        72
      ],
      "diary": [
        "shark-award",
        45
      ],
      "diced": [
        "diner-dicey",
        36
      ],
      "dicer": [
        "diner-diver",
        34
      ],
      "dicey": [
        "diner",
        53
      ],
      "digit": [
        "roust-theft",
        41
      ],
      "diked": [
        "diner-dicey",
        46
      ],
      "dilly": [
        "could-drill",
        43
      ],
      "dimly": [
        "could-drill",
        43
      ],
      "dined": [
        "diner",
        54
      ],
      "diner": [
        "",
        57
      ],
      "dingo": [
        "corns-union-bingo",
        21
      ],
      "dingy": [
        "corns",
        42
      ],
      "dinky": [
        "corns-dingy",
        32
      ],
      "diode": [
        "snore-evoke-booze",
        36
      ],
      "dippy": [
        "croup-nymph-zippy",
        29
      ],
      "dirge": [
        "snore-verge",
        38
      ],
      "dirty": [
        "softy-ditty",
        47
      ],
      "disco": [
        "corns-shock",
        37
      ],
      "dishy": [
        "corns-smush-fishy",
        14
      ],
      "ditch": [
        "roust",
        43
      ],
      "ditsy": [
        "roust",
        54
      ],
      "ditto": [
        "softy-broth",
        53
      ],
      "ditty": [
        "softy",
        55
      ],
      "ditzy": [
        "roust-ditch",
        34
      ],
      "divan": [
        "manor-aging",
        38
      ],
      "dived": [
        "diner-dicey-diked",
        33
      ],
      "diver": [
        "diner",
        51
      ],
      "divot": [
        "roust-idiot",
        38
      ],
      "divvy": [
        "corns-fudgy-dizzy",
        18
      ],
      "dizzy": [
        "corns-fudgy",
        30
      ],
      "dodge": [
        "snore-vogue",
        42
      ],
      "dodgy": [
        "corns-goody",
        36
      ],
      "doggo": [
        "corns-goody",
        35
      ],
      "doggy": [
        "corns-goody-dodgy",
        24
      ],
      "dogma": [
        "manor",
        59
      ],
      "doily": [
        "could-dolly",
        43
      ],
      "doing": [
        "corns-downy",
        37
      ],
      "doled": [
        "lever-yodel-soled-holed",
        30
      ],
      "dolly": [
        "could",
        60
      ],
      "domed": [
        "diner",
        56
      ],
      "donor": [
        "corns",
        54
      ],
      "donut": [
        "roust",
        60
      ],
      "doozy": [
        "corns-goody",
        35
      ],
      "doped": [
        "speed-moped-roped-coped-hoped",
        37
      ],
      "doper": [
        "speed-dopey",
        53
      ],
      "dopey": [
        "speed",
        70
      ],
      "dorky": [
        "corns-wormy",
        39
      ],
      "dosed": [
        "diner-domed",
        43
      ],
      "doted": [
        "reset-token-voted",
        26
      ],
      "dotty": [
        "softy",
        67
      ],
      "doubt": [
        "roust-count",
        44
      ],
      "dough": [
        "corns-goody",
        35
      ],
      "doula": [
        "solar-voila",
        50
      ],
      "douse": [
        "snore-house-mouse",
        36
      ],
      "dowdy": [
        "corns-goody",
        40
      ],
      "dowel": [
        "lever-yodel",
        48
      ],
      "downy": [
        "corns",
        43
      ],
      "dowry": [
        "corns-rowdy",
        35
      ],
      "dowse": [
        "snore-house",
        52
      ],
      "dozed": [
        "diner-domed-dosed",
        30
      ],
      "dozen": [
        "diner",
        54
      ],
      "dozer": [
        "diner-dryer-defer",
        29
      ],
      "draft": [
        "scant",
        57
      ],
      "drain": [
        "shark-brand",
        36
      ],
      "drake": [
        "share-crave-grade",
        40
      ],
      "drama": [
        "shark-brand",
        43
      ],
      "drank": [
        "shark-frack",
        48
      ],
      "drape": [
        "spare-grape",
        49
      ],
      "drawl": [
        "crawl-brawl",
        55
      ],
      "drawn": [
        "shark-brand-drain",
        24
      ],
      "dread": [
        "amber-wreak",
        48
      ],
      "dream": [
        "amber-cream",
        48
      ],
      "dreck": [
        "diner-decry",
        35
      ],
      "dress": [
        "diner-decry",
        35
      ],
      "dried": [
        "diner",
        54
      ],
      "drier": [
        "diner",
        54
      ],
      "drift": [
        "roust",
        61
      ],
      "drill": [
        "could",
        60
      ],
      "drink": [
        "corns-bring",
        31
      ],
      "drive": [
        "snore-verge",
        38
      ],
      "droid": [
        "corns-vroom",
        33
      ],
      "droit": [
        "roust-orbit",
        40
      ],
      "droll": [
        "could-oddly",
        44
      ],
      "drone": [
        "snore",
        65
      ],
      "drool": [
        "could",
        64
      ],
      "droop": [
        "croup",
        70
      ],
      "dross": [
        "corns-gross",
        39
      ],
      "drove": [
        "snore",
        60
      ],
      "drown": [
        "corns",
        50
      ],
      "druid": [
        "corns-grimy",
        32
      ],
      "drunk": [
        "corns-bring",
        31
      ],
      "dryer": [
        "diner",
        54
      ],
      "dryly": [
        "could-drill",
        43
      ],
      "ducat": [
        "taint-abort-squat",
        21
      ],
      "duchy": [
        "corns-mucky",
        34
      ],
      "ducky": [
        "corns-mucky-yucky",
        20
      ],
      "duked": [
        "diner-domed",
        40
      ],
      "dully": [
        "could",
        64
      ],
      "dummy": [
        "corns-fudgy",
        26
      ],
      "dumpy": [
        "croup-bumpy-jumpy",
        31
      ],
      "dunce": [
        "snore-niche-fence",
        27
      ],
      "duped": [
        "speed-moped-biped-hyped",
        34
      ],
      "dusky": [
        "corns-smush",
        28
      ],
      "dusty": [
        "softy-rusty",
        56
      ],
      "dutch": [
        "roust-butch-hutch",
        21
      ],
      "duvet": [
        "reset-civet",
        36
      ],
      "dwarf": [
        "shark-award",
        45
      ],
      "dweeb": [
        "diner-domed",
        40
      ],
      "dwell": [
        "lever-swell",
        47
      ],
      "dwelt": [
        "islet-knelt",
        47
      ],
      "dying": [
        "corns",
        50
      ],
      "eager": [
        "amber-rager",
        50
      ],
      "eagle": [
        "angle",
        79
      ],
      "eared": [
        "amber-raven-cared-oared-fared",
        41
      ],
      "early": [
        "regal-laser",
        50
      ],
      "earth": [
        "",
        75
      ],
      "eased": [
        "amber-naked-jaded-caged-sawed",
        41
      ],
      "easel": [
        "regal-email",
        53
      ],
      "eaten": [
        "tread",
        71
      ],
      "eater": [
        "tread-earth",
        53
      ],
      "ebbed": [
        "diner-modem-edges",
        40
      ],
      "ebony": [
        "diner-envoy",
        40
      ],
      "ebook": [
        "diner-becks",
        35
      ],
      "eclat": [
        "metal",
        75
      ],
      "edema": [
        "amber-media",
        51
      ],
      "edged": [
        "diner-modem-edges",
        40
      ],
      "edger": [
        "diner-order",
        41
      ],
      "edict": [
        "reset-evict",
        42
      ],
      "edify": [
        "diner-medic",
        41
      ],
      "educe": [
        "snore-guide-deuce",
        22
      ],
      "eerie": [
        "snore-verge",
        38
      ],
      "egged": [
        "diner-modem-edges",
        40
      ],
      "egret": [
        "reset-greet",
        50
      ],
      "eider": [
        "diner-wider-rider-cider",
        34
      ],
      "eight": [
        "reset-evict",
        42
      ],
      "eject": [
        "reset-event",
        49
      ],
      "eking": [
        "diner",
        50
      ],
      "elate": [
        "slate",
        50
      ],
      "elbow": [
        "bleed",
        76
      ],
      "elder": [
        "bleed",
        76
      ],
      "elect": [
        "fleet",
        66
      ],
      "elegy": [
        "bleed",
        76
      ],
      "elfin": [
        "bleed",
        76
      ],
      "elide": [
        "clove-slide-glide",
        35
      ],
      "elite": [
        "flute",
        63
      ],
      "elope": [
        "slope",
        61
      ],
      "elude": [
        "clove-slide",
        58
      ],
      "email": [
        "leafy",
        76
      ],
      "embed": [
        "diner-modem",
        40
      ],
      "ember": [
        "diner-fever-sheer",
        29
      ],
      "emcee": [
        "snore-guide",
        36
      ],
      "emery": [
        "diner-mercy",
        35
      ],
      "emoji": [
        "diner-weigh",
        39
      ],
      "emote": [
        "route",
        72
      ],
      "empty": [
        "depth",
        61
      ],
      "enact": [
        "teary",
        69
      ],
      "ended": [
        "diner-unwed-kneed",
        30
      ],
      "endow": [
        "diner-needy",
        41
      ],
      "enema": [
        "amber-media",
        51
      ],
      "enemy": [
        "diner-envoy",
        40
      ],
      "enjoy": [
        "diner-envoy",
        40
      ],
      "ennui": [
        "diner",
        54
      ],
      "ensue": [
        "snore",
        65
      ],
      "enter": [
        "reset",
        62
      ],
      "entry": [
        "reset",
        61
      ],
      "envoy": [
        "diner",
        52
      ],
      "epoch": [
        "speed",
        68
      ],
      "epoxy": [
        "speed-epoch",
        52
      ],
      "equal": [
        "regal-ideal",
        49
      ],
      "equip": [
        "speed",
        61
      ],
      "erase": [
        "share",
        78
      ],
      "erect": [
        "reset-exert",
        45
      ],
      "erode": [
        "snore-drove",
        50
      ],
      "erred": [
        "diner-breed",
        41
      ],
      "error": [
        "diner",
        55
      ],
      "erupt": [
        "crept",
        79
      ],
      "essay": [
        "amber-sedan",
        41
      ],
      "ester": [
        "reset-steer",
        44
      ],
      "ether": [
        "reset-enter",
        46
      ],
      "ethic": [
        "reset",
        68
      ],
      "ethos": [
        "reset",
        62
      ],
      "ethyl": [
        "islet-extol",
        48
      ],
      "etude": [
        "terse",
        75
      ],
      "evade": [
        "share-agave",
        61
      ],
      "event": [
        "reset",
        66
      ],
      "evert": [
        "reset-exert",
        45
      ],
      "every": [
        "diner-mercy-query",
        21
      ],
      "evict": [
        "reset",
        58
      ],
      "evoke": [
        "snore",
        59
      ],
      "exact": [
        "teary-enact",
        52
      ],
      "exalt": [
        "least",
        64
      ],
      "excel": [
        "lever-wheel",
        51
      ],
      "exert": [
        "reset",
        62
      ],
      "exile": [
        "bugle-while-smile",
        41
      ],
      "exist": [
        "reset-guest",
        43
      ],
      "expat": [
        "adept",
        65
      ],
      "expel": [
        "",
        91
      ],
      "extol": [
        "islet",
        65
      ],
      "extra": [
        "tread-earth",
        53
      ],
      "exude": [
        "snore-guide",
        37
      ],
      "exult": [
        "islet-knelt",
        47
      ],
      "exurb": [
        "diner-mercy-fresh",
        24
      ],
      "eying": [
        "diner-eking",
        37
      ],
      "fable": [
        "angle-cable",
        53
      ],
      "faced": [
        "amber-naked-jaded-caged",
        46
      ],
      "facet": [
        "tread-eaten",
        54
      ],
      "faded": [
        "amber-naked-jaded",
        44
      ],
      "fader": [
        "amber-rager-safer-faker",
        23
      ],
      "faint": [
        "taint-saint",
        48
      ],
      "fairy": [
        "manor-hardy",
        31
      ],
      "faith": [
        "tarts",
        69
      ],
      "faked": [
        "amber-naked-caked",
        37
      ],
      "faker": [
        "amber-rager-safer",
        33
      ],
      "fakir": [
        "manor-radar",
        38
      ],
      "false": [
        "angle-value",
        52
      ],
      "famed": [
        "amber-gamed",
        51
      ],
      "fancy": [
        "manor-dance",
        42
      ],
      "farce": [
        "raise-cadre",
        45
      ],
      "fared": [
        "amber-raven-cared-oared",
        49
      ],
      "fatal": [
        "natal",
        78
      ],
      "fated": [
        "tread-gated-sated-hated-mated",
        45
      ],
      "fatty": [
        "tarts",
        65
      ],
      "fatwa": [
        "taint-maths",
        47
      ],
      "fault": [
        "natal",
        61
      ],
      "fauna": [
        "manor-basin",
        35
      ],
      "favor": [
        "manor-savor",
        40
      ],
      "faxed": [
        "amber-naked-jaded-caged-sawed",
        36
      ],
      "fazed": [
        "amber-naked-jaded-caged-sawed",
        36
      ],
      "feast": [
        "teary-beast",
        47
      ],
      "fecal": [
        "regal-decal",
        48
      ],
      "feces": [
        "diner-cheek",
        39
      ],
      "feign": [
        "diner-eking",
        34
      ],
      "feint": [
        "reset-debit",
        38
      ],
      "fella": [
        "regal",
        66
      ],
      "felon": [
        "lever-cello",
        44
      ],
      "femme": [
        "snore-guide-emcee",
        24
      ],
      "femur": [
        "diner-error",
        39
      ],
      "fence": [
        "snore-niche",
        40
      ],
      "feral": [
        "regal",
        79
      ],
      "ferry": [
        "diner-mercy",
        31
      ],
      "fetal": [
        "metal",
        75
      ],
      "fetch": [
        "reset",
        58
      ],
      "feted": [
        "reset-meted",
        47
      ],
      "fetid": [
        "reset-fetch",
        42
      ],
      "fetus": [
        "reset",
        68
      ],
      "fever": [
        "diner",
        40
      ],
      "fewer": [
        "diner-fever",
        37
      ],
      "fiber": [
        "diner-riser",
        43
      ],
      "ficus": [
        "corns-mucus",
        38
      ],
      "field": [
        "lever-swell-yield",
        26
      ],
      "fiend": [
        "diner",
        54
      ],
      "fiery": [
        "diner",
        54
      ],
      "fifth": [
        "softy",
        74
      ],
      "fifty": [
        "softy-nifty",
        50
      ],
      "fight": [
        "roust-theft",
        41
      ],
      "filch": [
        "could-zilch",
        45
      ],
      "filed": [
        "lever-yodel",
        43
      ],
      "filer": [
        "lever-miler",
        49
      ],
      "filet": [
        "islet",
        75
      ],
      "filly": [
        "could-skill-hilly",
        35
      ],
      "filmy": [
        "could-silky",
        35
      ],
      "filth": [
        "lofty",
        67
      ],
      "final": [
        "solar-canal",
        44
      ],
      "finch": [
        "corns-bunch-winch",
        27
      ],
      "fined": [
        "diner-mined",
        47
      ],
      "finer": [
        "diner-miner",
        39
      ],
      "fired": [
        "diner-sired-hired-mired",
        42
      ],
      "first": [
        "roust-wrist",
        36
      ],
      "firth": [
        "softy-fritz",
        49
      ],
      "fishy": [
        "corns-smush",
        27
      ],
      "fixed": [
        "diner-video-miked-gibed-sized",
        30
      ],
      "fixer": [
        "diner-riser-fiber",
        36
      ],
      "fizzy": [
        "corns-fudgy",
        26
      ],
      "fjord": [
        "corns-vroom",
        33
      ],
      "flack": [
        "clans-black",
        53
      ],
      "flail": [
        "clans-flair",
        41
      ],
      "flair": [
        "clans",
        58
      ],
      "flake": [
        "blare",
        66
      ],
      "flaky": [
        "clans-flair",
        41
      ],
      "flame": [
        "blare-flake",
        58
      ],
      "flank": [
        "clans-bland",
        47
      ],
      "flare": [
        "blare-glare",
        65
      ],
      "flash": [
        "clans",
        67
      ],
      "flask": [
        "clans-flash",
        50
      ],
      "fleck": [
        "bleed-clerk",
        47
      ],
      "fleet": [
        "",
        91
      ],
      "flesh": [
        "bleed-clerk",
        47
      ],
      "flick": [
        "flunk-flock",
        51
      ],
      "flied": [
        "bleed-clued",
        41
      ],
      "flier": [
        "bleed",
        58
      ],
      "fling": [
        "flunk",
        74
      ],
      "flint": [
        "flirt",
        74
      ],
      "flirt": [
        "",
        92
      ],
      "float": [
        "",
        92
      ],
      "flock": [
        "flunk",
        68
      ],
      "flood": [
        "flunk-floor",
        51
      ],
      "floor": [
        "flunk",
        61
      ],
      "flora": [
        "aloha",
        87
      ],
      "floss": [
        "flunk-floor",
        47
      ],
      "flour": [
        "flunk",
        74
      ],
      "flout": [
        "flirt",
        74
      ],
      "flown": [
        "flunk",
        74
      ],
      "flowy": [
        "flunk-floor-floss",
        34
      ],
      "fluff": [
        "flunk-fluid-flush",
        43
      ],
      "fluid": [
        "flunk",
        66
      ],
      "fluke": [
        "clove-slide",
        54
      ],
      "fluky": [
        "flunk",
        74
      ],
      "flume": [
        "clove-slide-fluke",
        42
      ],
      "flung": [
        "flunk",
        74
      ],
      "flunk": [
        "",
        79
      ],
      "flush": [
        "flunk-fluid",
        56
      ],
      "flute": [
        "",
        88
      ],
      "flyby": [
        "flunk-floor",
        51
      ],
      "flyer": [
        "bleed-flier",
        41
      ],
      "foamy": [
        "shark-guava",
        40
      ],
      "focal": [
        "solar-local",
        51
      ],
      "focus": [
        "corns",
        49
      ],
      "fogey": [
        "diner-cheek-bogey",
        25
      ],
      "foggy": [
        "corns-goody",
        38
      ],
      "foist": [
        "roust-moist-hoist",
        38
      ],
      "folic": [
        "could-logic",
        45
      ],
      "folio": [
        "could-lobby",
        49
      ],
      "folky": [
        "could-lobby",
        49
      ],
      "folly": [
        "could-jolly",
        40
      ],
      "foray": [
        "manor-broad",
        34
      ],
      "force": [
        "snore-forge",
        39
      ],
      "forge": [
        "snore",
        55
      ],
      "forgo": [
        "corns-wormy",
        39
      ],
      "forte": [
        "route",
        66
      ],
      "forth": [
        "softy",
        74
      ],
      "forty": [
        "softy",
        74
      ],
      "forum": [
        "corns-wormy",
        39
      ],
      "found": [
        "corns-downy-mound-bound",
        33
      ],
      "fount": [
        "roust-count-mount",
        30
      ],
      "foyer": [
        "diner-fever",
        42
      ],
      "frack": [
        "shark",
        59
      ],
      "frail": [
        "crawl",
        68
      ],
      "frame": [
        "share-crave-grade",
        39
      ],
      "franc": [
        "shark-brand",
        43
      ],
      "frank": [
        "shark-frack",
        48
      ],
      "fraud": [
        "shark-brand",
        43
      ],
      "freak": [
        "amber-wreak",
        45
      ],
      "freed": [
        "diner-breed-greed",
        38
      ],
      "freer": [
        "diner-fever",
        37
      ],
      "fresh": [
        "diner-mercy",
        36
      ],
      "friar": [
        "manor-cigar",
        37
      ],
      "fried": [
        "diner-cried",
        39
      ],
      "frill": [
        "could-skill-grill",
        29
      ],
      "frise": [
        "snore-curse",
        45
      ],
      "frisk": [
        "corns-brisk",
        36
      ],
      "fritz": [
        "softy",
        66
      ],
      "frizz": [
        "corns-grimy",
        32
      ],
      "frock": [
        "corns-occur",
        38
      ],
      "frond": [
        "corns-irony-wrong",
        31
      ],
      "front": [
        "roust-orbit",
        40
      ],
      "frosh": [
        "corns-sword",
        36
      ],
      "frost": [
        "roust",
        60
      ],
      "froth": [
        "softy",
        74
      ],
      "frown": [
        "corns-drown-grown-brown",
        29
      ],
      "froze": [
        "snore-drove-broke",
        34
      ],
      "fruit": [
        "roust-brunt",
        39
      ],
      "frump": [
        "croup-grump",
        48
      ],
      "fryer": [
        "diner-fever-foyer",
        29
      ],
      "fubar": [
        "manor-cigar",
        38
      ],
      "fudge": [
        "snore-guide-judge-budge",
        21
      ],
      "fudgy": [
        "corns",
        36
      ],
      "fugue": [
        "snore-guide",
        37
      ],
      "fully": [
        "could-bulls",
        40
      ],
      "fumed": [
        "diner-modem-embed",
        27
      ],
      "fungi": [
        "corns-dingy",
        32
      ],
      "fungo": [
        "corns-union",
        35
      ],
      "funky": [
        "corns-dingy",
        32
      ],
      "funny": [
        "corns-dying",
        37
      ],
      "furor": [
        "corns",
        55
      ],
      "furry": [
        "corns-hurry",
        37
      ],
      "fused": [
        "diner-modem-edges-bused",
        30
      ],
      "fussy": [
        "corns-smush",
        31
      ],
      "fusty": [
        "softy",
        74
      ],
      "futon": [
        "roust-outdo",
        39
      ],
      "fuzzy": [
        "corns-fudgy",
        26
      ],
      "gabby": [
        "manor-daubs-cabby",
        26
      ],
      "gable": [
        "angle",
        79
      ],
      "gaffe": [
        "raise-cadge-vague",
        31
      ],
      "gaily": [
        "solar-daily",
        43
      ],
      "gamed": [
        "amber",
        63
      ],
      "gamer": [
        "amber-maker",
        49
      ],
      "gamey": [
        "amber-gamed",
        51
      ],
      "gamma": [
        "manor-hammy",
        39
      ],
      "gamut": [
        "taint-carat",
        48
      ],
      "gaped": [
        "caper",
        54
      ],
      "gassy": [
        "manor-daubs",
        36
      ],
      "gated": [
        "tread",
        66
      ],
      "gator": [
        "taint-maths-fatwa",
        35
      ],
      "gaudy": [
        "manor-daubs",
        37
      ],
      "gauge": [
        "raise-cadge",
        54
      ],
      "gaunt": [
        "taint-haunt",
        53
      ],
      "gauze": [
        "raise-cadge-vague",
        31
      ],
      "gauzy": [
        "manor-daubs",
        37
      ],
      "gavel": [
        "regal",
        79
      ],
      "gawky": [
        "manor-daubs-wacky",
        20
      ],
      "gayer": [
        "amber-rager",
        52
      ],
      "gayly": [
        "solar-daily-manly",
        23
      ],
      "gazed": [
        "amber-naked-jaded-caged",
        46
      ],
      "gazer": [
        "amber-rager-gayer",
        40
      ],
      "gecko": [
        "diner-becks",
        35
      ],
      "geeky": [
        "diner-becks",
        35
      ],
      "geese": [
        "snore-guise",
        47
      ],
      "genie": [
        "snore-niche",
        41
      ],
      "genre": [
        "snore",
        64
      ],
      "geode": [
        "snore-evoke",
        51
      ],
      "getup": [
        "crept-setup",
        42
      ],
      "ghost": [
        "roust",
        60
      ],
      "ghoul": [
        "could",
        64
      ],
      "giant": [
        "scant-grant",
        49
      ],
      "gibed": [
        "diner-video-miked",
        44
      ],
      "giddy": [
        "corns-fudgy",
        26
      ],
      "gimme": [
        "snore-guide",
        37
      ],
      "girly": [
        "could-skill",
        39
      ],
      "girth": [
        "softy-birth",
        57
      ],
      "given": [
        "diner",
        58
      ],
      "giver": [
        "diner-riser-fiber-mixer-hiker",
        27
      ],
      "gizmo": [
        "corns",
        46
      ],
      "glade": [
        "blare-flake-glaze",
        45
      ],
      "glamp": [
        "clamp",
        61
      ],
      "gland": [
        "clans-bland",
        47
      ],
      "glare": [
        "blare",
        81
      ],
      "glass": [
        "clans",
        80
      ],
      "glaze": [
        "blare-flake",
        53
      ],
      "gleam": [
        "clean-bleak",
        42
      ],
      "glean": [
        "clean",
        79
      ],
      "glide": [
        "clove-slide",
        48
      ],
      "glint": [
        "flirt",
        74
      ],
      "glitz": [
        "blitz",
        77
      ],
      "gloam": [
        "aloha-cloak",
        56
      ],
      "gloat": [
        "float",
        60
      ],
      "globe": [
        "clove",
        72
      ],
      "gloom": [
        "flunk-gloms",
        43
      ],
      "gloop": [
        "slump-bloop",
        40
      ],
      "glory": [
        "flunk-gloms",
        38
      ],
      "gloss": [
        "flunk-gloms",
        43
      ],
      "glove": [
        "clove",
        81
      ],
      "glowy": [
        "flunk-gloms-glory",
        25
      ],
      "glued": [
        "bleed-clued",
        41
      ],
      "glute": [
        "flute",
        63
      ],
      "glyph": [
        "slump",
        75
      ],
      "gnarl": [
        "crawl-snarl",
        53
      ],
      "gnash": [
        "shark-awash-quash",
        40
      ],
      "gnome": [
        "snore",
        64
      ],
      "godly": [
        "could-dolly",
        43
      ],
      "gofer": [
        "diner-fever-offer",
        31
      ],
      "going": [
        "corns-downy",
        38
      ],
      "golem": [
        "lever-yodel",
        48
      ],
      "golly": [
        "could-jolly-folly-holly",
        36
      ],
      "gonad": [
        "manor-gonna",
        41
      ],
      "goner": [
        "diner-owner",
        41
      ],
      "gonna": [
        "manor",
        58
      ],
      "gonzo": [
        "corns",
        55
      ],
      "goody": [
        "corns",
        40
      ],
      "gooey": [
        "diner-cheek-bogey",
        25
      ],
      "goofy": [
        "corns-goody",
        35
      ],
      "goopy": [
        "croup-spoon",
        52
      ],
      "goose": [
        "snore-chose",
        49
      ],
      "gored": [
        "diner-breed-shred-cored",
        31
      ],
      "gorge": [
        "snore-forge",
        39
      ],
      "gorse": [
        "snore-horse-worse",
        37
      ],
      "gotta": [
        "tarts",
        79
      ],
      "gouge": [
        "snore-vogue",
        42
      ],
      "gourd": [
        "corns-rowdy",
        35
      ],
      "grace": [
        "share-crave",
        55
      ],
      "grade": [
        "share-crave",
        47
      ],
      "graft": [
        "scant-draft",
        40
      ],
      "grail": [
        "crawl-frail",
        51
      ],
      "grain": [
        "shark-brand",
        43
      ],
      "grand": [
        "shark-brand",
        43
      ],
      "grant": [
        "scant",
        66
      ],
      "grape": [
        "spare",
        66
      ],
      "graph": [
        "cramp",
        73
      ],
      "grasp": [
        "cramp",
        73
      ],
      "grass": [
        "shark",
        65
      ],
      "grate": [
        "",
        92
      ],
      "grave": [
        "share-crave",
        55
      ],
      "gravy": [
        "shark-brand-crazy",
        24
      ],
      "graze": [
        "share-crave-grade",
        40
      ],
      "great": [
        "tread",
        74
      ],
      "greed": [
        "diner-breed",
        41
      ],
      "green": [
        "diner",
        54
      ],
      "greet": [
        "reset",
        67
      ],
      "grief": [
        "diner",
        56
      ],
      "grift": [
        "roust-drift",
        44
      ],
      "grill": [
        "could-skill",
        41
      ],
      "grime": [
        "snore-verge",
        38
      ],
      "grimy": [
        "corns",
        45
      ],
      "grind": [
        "corns-bring",
        31
      ],
      "gripe": [
        "spire",
        77
      ],
      "grist": [
        "roust-wrist",
        36
      ],
      "groan": [
        "manor-adorn",
        39
      ],
      "groin": [
        "corns-drown",
        43
      ],
      "groom": [
        "corns-vroom",
        32
      ],
      "grope": [
        "spire-crepe",
        43
      ],
      "gross": [
        "corns",
        55
      ],
      "group": [
        "croup",
        70
      ],
      "grout": [
        "roust-trout",
        44
      ],
      "grove": [
        "snore-drove",
        50
      ],
      "growl": [
        "could-lingo",
        38
      ],
      "grown": [
        "corns-drown",
        43
      ],
      "gruel": [
        "lever-cruel",
        51
      ],
      "gruff": [
        "corns-grimy",
        32
      ],
      "grump": [
        "croup",
        64
      ],
      "grunt": [
        "roust-brunt",
        39
      ],
      "guano": [
        "shark-guava",
        40
      ],
      "guard": [
        "shark-award-board",
        28
      ],
      "guava": [
        "shark",
        57
      ],
      "guess": [
        "diner-becks",
        35
      ],
      "guest": [
        "reset",
        54
      ],
      "guide": [
        "snore",
        46
      ],
      "guild": [
        "could-build",
        45
      ],
      "guile": [
        "bugle",
        75
      ],
      "guilt": [
        "",
        88
      ],
      "guise": [
        "snore",
        64
      ],
      "gulag": [
        "solar-lilac",
        49
      ],
      "gulch": [
        "could-lunch-mulch",
        32
      ],
      "gully": [
        "could-bulls-fully",
        28
      ],
      "gumbo": [
        "corns-gizmo",
        29
      ],
      "gummy": [
        "corns-fudgy",
        26
      ],
      "gunky": [
        "corns-dingy",
        32
      ],
      "guppy": [
        "croup-bumpy",
        50
      ],
      "gushy": [
        "corns-smush-bushy",
        14
      ],
      "gussy": [
        "corns-smush-fussy",
        19
      ],
      "gusto": [
        "softy",
        74
      ],
      "gusty": [
        "softy-rusty-dusty-musty",
        47
      ],
      "gutsy": [
        "roust",
        60
      ],
      "gutty": [
        "softy-ditty-nutty",
        34
      ],
      "habit": [
        "taint",
        71
      ],
      "hacky": [
        "manor-daubs-wacky",
        20
      ],
      "haiku": [
        "manor-daubs",
        37
      ],
      "hairy": [
        "manor-hardy",
        31
      ],
      "halal": [
        "solar-lilac",
        53
      ],
      "halve": [
        "angle-value-salve",
        44
      ],
      "hammy": [
        "manor",
        56
      ],
      "handy": [
        "manor-dance-sandy",
        34
      ],
      "hanky": [
        "manor-dance-janky",
        32
      ],
      "happy": [
        "carps",
        57
      ],
      "hardy": [
        "manor",
        46
      ],
      "harem": [
        "amber-ramen",
        48
      ],
      "harpy": [
        "carps",
        74
      ],
      "harry": [
        "manor-hardy",
        31
      ],
      "harsh": [
        "manor-hardy",
        31
      ],
      "haste": [
        "taste-waste-caste",
        50
      ],
      "hasty": [
        "tarts-nasty",
        50
      ],
      "hatch": [
        "taint-maths-batch-watch-catch",
        30
      ],
      "hated": [
        "tread-gated-sated",
        56
      ],
      "hater": [
        "tread-earth",
        53
      ],
      "haunt": [
        "taint",
        60
      ],
      "haute": [
        "taste",
        71
      ],
      "haven": [
        "amber-naked",
        41
      ],
      "havoc": [
        "manor-yahoo",
        42
      ],
      "hazed": [
        "amber-naked-jaded-caged-sawed",
        36
      ],
      "hazel": [
        "regal-email-label-navel",
        33
      ],
      "heady": [
        "heard",
        72
      ],
      "heard": [
        "",
        91
      ],
      "heart": [
        "teary",
        80
      ],
      "heath": [
        "death",
        65
      ],
      "heave": [
        "share",
        78
      ],
      "heavy": [
        "heard",
        72
      ],
      "hedge": [
        "snore-guide",
        34
      ],
      "hefty": [
        "tenth",
        68
      ],
      "heist": [
        "reset",
        60
      ],
      "helix": [
        "lever-cello",
        49
      ],
      "hello": [
        "lever-cello",
        49
      ],
      "hence": [
        "snore-niche",
        41
      ],
      "henna": [
        "amber-sedan",
        41
      ],
      "heron": [
        "diner-rerun",
        35
      ],
      "hertz": [
        "tenth-hefty",
        51
      ],
      "hewed": [
        "diner-modem-edges-hexed",
        26
      ],
      "hexed": [
        "diner-modem-edges",
        36
      ],
      "hider": [
        "diner-wider-rider-cider-eider",
        26
      ],
      "hijab": [
        "manor-squab",
        29
      ],
      "hiked": [
        "diner-video-miked",
        50
      ],
      "hiker": [
        "diner-riser-fiber-mixer",
        35
      ],
      "hilly": [
        "could-skill",
        36
      ],
      "hinge": [
        "snore-niche",
        41
      ],
      "hinky": [
        "corns-dingy-kinky",
        16
      ],
      "hippo": [
        "croup-oomph",
        42
      ],
      "hippy": [
        "croup-nymph",
        42
      ],
      "hired": [
        "diner-sired",
        49
      ],
      "hirer": [
        "diner-riser",
        45
      ],
      "hissy": [
        "corns-smush",
        28
      ],
      "hitch": [
        "roust-ditch-witch",
        18
      ],
      "hived": [
        "diner-video",
        36
      ],
      "hoard": [
        "shark",
        66
      ],
      "hoary": [
        "shark-hoard",
        50
      ],
      "hobby": [
        "corns-goody",
        33
      ],
      "hocus": [
        "corns-focus",
        32
      ],
      "hoist": [
        "roust-moist",
        42
      ],
      "hokey": [
        "diner-cheek",
        39
      ],
      "hokum": [
        "corns-goody",
        35
      ],
      "holed": [
        "lever-yodel-soled",
        39
      ],
      "holey": [
        "lever-yodel",
        48
      ],
      "holly": [
        "could-jolly-folly",
        39
      ],
      "homed": [
        "diner-modem",
        36
      ],
      "homer": [
        "diner-fever-bower",
        29
      ],
      "homey": [
        "diner-cheek",
        41
      ],
      "honed": [
        "diner-coned",
        45
      ],
      "honey": [
        "diner",
        55
      ],
      "honor": [
        "corns-donor",
        46
      ],
      "hooch": [
        "corns",
        54
      ],
      "hoody": [
        "corns-goody-moody-woody",
        17
      ],
      "hooey": [
        "diner-cheek-homey",
        29
      ],
      "hooky": [
        "corns-goody-boozy-kooky",
        16
      ],
      "hoped": [
        "speed-moped-roped-coped",
        45
      ],
      "hoppy": [
        "croup-oomph",
        42
      ],
      "horde": [
        "snore-forge",
        39
      ],
      "horny": [
        "corns",
        50
      ],
      "horse": [
        "snore",
        63
      ],
      "hosed": [
        "diner-modem-wooed-yoked",
        34
      ],
      "hotel": [
        "islet",
        59
      ],
      "hotly": [
        "guilt",
        62
      ],
      "hound": [
        "corns-downy-mound-bound-found",
        25
      ],
      "house": [
        "snore",
        60
      ],
      "hovel": [
        "lever-novel",
        52
      ],
      "hover": [
        "diner-fever-cover",
        39
      ],
      "howdy": [
        "corns-goody-dowdy",
        27
      ],
      "hubby": [
        "corns-fudgy-mummy-buzzy",
        13
      ],
      "huffy": [
        "corns-fudgy",
        26
      ],
      "hulky": [
        "could-bulky-sulky",
        31
      ],
      "human": [
        "manor",
        58
      ],
      "humid": [
        "corns-fudgy",
        26
      ],
      "humor": [
        "corns-vroom",
        28
      ],
      "humph": [
        "croup-bumpy",
        50
      ],
      "humus": [
        "corns",
        50
      ],
      "hunch": [
        "corns-bunch",
        49
      ],
      "hunky": [
        "corns-dingy-funky",
        30
      ],
      "hurry": [
        "corns",
        54
      ],
      "husky": [
        "corns-smush-bushy",
        14
      ],
      "hussy": [
        "corns-smush",
        28
      ],
      "hutch": [
        "roust-butch",
        33
      ],
      "hydra": [
        "manor-circa",
        38
      ],
      "hydro": [
        "corns-vroom",
        33
      ],
      "hyena": [
        "amber-sedan",
        41
      ],
      "hymen": [
        "diner-seven-women",
        26
      ],
      "hyped": [
        "speed-moped-biped",
        44
      ],
      "hyper": [
        "speed-ripen",
        42
      ],
      "icier": [
        "diner-crier",
        37
      ],
      "icily": [
        "could",
        64
      ],
      "icing": [
        "corns",
        50
      ],
      "ideal": [
        "regal",
        65
      ],
      "idiom": [
        "corns-gizmo",
        29
      ],
      "idiot": [
        "roust",
        55
      ],
      "idled": [
        "lever-yodel-filed",
        31
      ],
      "idler": [
        "lever-miler",
        59
      ],
      "idyll": [
        "could-drill",
        43
      ],
      "igloo": [
        "could-lingo",
        38
      ],
      "iliac": [
        "aloha-ulnar",
        54
      ],
      "image": [
        "share-agave",
        61
      ],
      "imbed": [
        "diner-shied",
        40
      ],
      "imbue": [
        "snore-guide",
        37
      ],
      "impel": [
        "expel",
        69
      ],
      "imply": [
        "",
        91
      ],
      "inane": [
        "share-agave-quake",
        36
      ],
      "inapt": [
        "apart",
        75
      ],
      "inbox": [
        "corns-union",
        35
      ],
      "incel": [
        "lever-yodel-kugel",
        31
      ],
      "incur": [
        "corns",
        55
      ],
      "index": [
        "diner",
        53
      ],
      "indie": [
        "snore-knife",
        47
      ],
      "inept": [
        "crept-swept",
        44
      ],
      "inert": [
        "reset-overt",
        48
      ],
      "infer": [
        "diner",
        54
      ],
      "ingot": [
        "roust-idiot",
        38
      ],
      "inked": [
        "diner-index",
        36
      ],
      "inlay": [
        "solar-lilac",
        53
      ],
      "inlet": [
        "islet",
        75
      ],
      "inner": [
        "diner",
        54
      ],
      "input": [
        "tromp",
        66
      ],
      "inset": [
        "reset-onset",
        46
      ],
      "intel": [
        "islet",
        75
      ],
      "inter": [
        "reset-outer-miter",
        27
      ],
      "intro": [
        "roust-vitro",
        34
      ],
      "inure": [
        "snore",
        64
      ],
      "ionic": [
        "corns",
        50
      ],
      "irate": [
        "grate",
        76
      ],
      "irked": [
        "diner-cried",
        39
      ],
      "irony": [
        "corns",
        54
      ],
      "islet": [
        "",
        88
      ],
      "issue": [
        "snore-guise",
        47
      ],
      "itchy": [
        "roust-ditch",
        34
      ],
      "ivied": [
        "diner-shied",
        40
      ],
      "ivory": [
        "corns-vroom",
        33
      ],
      "jaded": [
        "amber-naked",
        49
      ],
      "jammy": [
        "manor-hammy",
        39
      ],
      "janky": [
        "manor-dance",
        44
      ],
      "jaunt": [
        "taint-haunt-gaunt",
        47
      ],
      "jawed": [
        "amber-naked-jaded",
        37
      ],
      "jazzy": [
        "manor-daubs-wacky",
        20
      ],
      "jelly": [
        "lever-cello-belly",
        35
      ],
      "jerky": [
        "diner-mercy-ferry",
        19
      ],
      "jetty": [
        "tenth",
        79
      ],
      "jewel": [
        "lever",
        67
      ],
      "jibed": [
        "diner-video-miked-gibed",
        39
      ],
      "jiffy": [
        "corns-fudgy",
        26
      ],
      "jimmy": [
        "corns-fudgy",
        26
      ],
      "joint": [
        "roust",
        60
      ],
      "joist": [
        "roust-moist-hoist-foist",
        28
      ],
      "joked": [
        "diner-modem-wooed-yoked",
        33
      ],
      "joker": [
        "diner-fever-bower-homer",
        24
      ],
      "jokey": [
        "diner-cheek",
        39
      ],
      "jolly": [
        "could",
        49
      ],
      "joule": [
        "bugle-uncle",
        45
      ],
      "joust": [
        "roust",
        60
      ],
      "jowly": [
        "could-jolly",
        44
      ],
      "judge": [
        "snore-guide",
        33
      ],
      "judgy": [
        "corns-fudgy",
        26
      ],
      "juice": [
        "snore-guide",
        37
      ],
      "juicy": [
        "corns-mucky",
        34
      ],
      "juked": [
        "diner-modem-edges-cubed",
        30
      ],
      "julep": [
        "expel",
        48
      ],
      "jumbo": [
        "corns-gizmo",
        29
      ],
      "jumpy": [
        "croup-bumpy",
        43
      ],
      "junky": [
        "corns-dingy-funky-hunky",
        20
      ],
      "junta": [
        "tarts-quota",
        41
      ],
      "junto": [
        "softy-broth-ditto",
        40
      ],
      "juror": [
        "corns-furor",
        39
      ],
      "kabob": [
        "manor-yahoo",
        42
      ],
      "kappa": [
        "carps-happy",
        48
      ],
      "kaput": [
        "",
        92
      ],
      "karat": [
        "taint-carat",
        48
      ],
      "karma": [
        "manor",
        58
      ],
      "kayak": [
        "manor-daubs-wacky",
        20
      ],
      "kazoo": [
        "manor-yahoo",
        42
      ],
      "kebab": [
        "amber",
        68
      ],
      "kempt": [
        "crept-tempt",
        51
      ],
      "keyed": [
        "diner-modem-edges-hexed",
        26
      ],
      "khaki": [
        "shark",
        70
      ],
      "kiddo": [
        "corns-gizmo",
        29
      ],
      "kinda": [
        "manor",
        60
      ],
      "kinky": [
        "corns-dingy",
        29
      ],
      "kiosk": [
        "corns-smoky",
        37
      ],
      "kissy": [
        "corns-smush",
        28
      ],
      "kitty": [
        "softy-ditty-witty",
        39
      ],
      "klutz": [
        "blitz",
        77
      ],
      "knack": [
        "shark",
        65
      ],
      "knave": [
        "share-agave-weave",
        45
      ],
      "knead": [
        "amber-sedan",
        41
      ],
      "kneed": [
        "diner-unwed",
        42
      ],
      "kneel": [
        "lever-wheel",
        51
      ],
      "knell": [
        "lever-swell-quell",
        33
      ],
      "knelt": [
        "islet",
        63
      ],
      "knife": [
        "snore",
        64
      ],
      "knish": [
        "corns-sniff",
        38
      ],
      "knock": [
        "corns",
        50
      ],
      "knoll": [
        "could",
        64
      ],
      "known": [
        "corns-union",
        35
      ],
      "koala": [
        "crawl-loamy",
        49
      ],
      "kooky": [
        "corns-goody-boozy",
        26
      ],
      "koran": [
        "manor-adorn-organ",
        29
      ],
      "krill": [
        "could-skill",
        39
      ],
      "kudos": [
        "corns",
        50
      ],
      "kudzu": [
        "corns-fudgy",
        26
      ],
      "kugel": [
        "lever-yodel",
        43
      ],
      "kvell": [
        "lever",
        72
      ],
      "label": [
        "regal-email",
        48
      ],
      "labor": [
        "solar",
        70
      ],
      "laced": [
        "regal-laden",
        56
      ],
      "lacey": [
        "regal-laden",
        52
      ],
      "laden": [
        "regal",
        69
      ],
      "ladle": [
        "angle-cable",
        59
      ],
      "lager": [
        "regal",
        79
      ],
      "laity": [
        "salty",
        66
      ],
      "lamed": [
        "regal-laden-laced",
        52
      ],
      "lamer": [
        "regal-laser-layer",
        33
      ],
      "lance": [
        "angle",
        79
      ],
      "lanky": [
        "solar-daily",
        43
      ],
      "lapel": [
        "",
        99
      ],
      "lapse": [
        "maple",
        66
      ],
      "larch": [
        "solar-larva",
        50
      ],
      "large": [
        "angle",
        79
      ],
      "larva": [
        "solar",
        66
      ],
      "laser": [
        "regal",
        60
      ],
      "lasso": [
        "solar",
        70
      ],
      "latch": [
        "natal",
        78
      ],
      "later": [
        "metal",
        60
      ],
      "latex": [
        "metal-later",
        44
      ],
      "lathe": [
        "",
        90
      ],
      "latke": [
        "lathe",
        65
      ],
      "latte": [
        "",
        99
      ],
      "laugh": [
        "solar-daily",
        43
      ],
      "laved": [
        "regal-laden-laced-lamed",
        47
      ],
      "layer": [
        "regal-laser",
        46
      ],
      "layup": [
        "apply",
        66
      ],
      "lazed": [
        "regal-laden-laced-lamed-laved",
        39
      ],
      "leach": [
        "leafy-leash",
        47
      ],
      "leafy": [
        "",
        92
      ],
      "leaky": [
        "leafy",
        76
      ],
      "leant": [
        "least",
        64
      ],
      "leapt": [
        "",
        99
      ],
      "learn": [
        "leafy-leash",
        47
      ],
      "lease": [
        "scale",
        75
      ],
      "leash": [
        "leafy",
        64
      ],
      "least": [
        "",
        89
      ],
      "leave": [
        "scale",
        75
      ],
      "ledge": [
        "bugle-lodge",
        51
      ],
      "leech": [
        "lever",
        72
      ],
      "leery": [
        "lever",
        72
      ],
      "lefty": [
        "",
        99
      ],
      "legal": [
        "regal",
        79
      ],
      "leggy": [
        "lever-lemon",
        51
      ],
      "legit": [
        "islet",
        75
      ],
      "lemma": [
        "regal-fella",
        50
      ],
      "lemon": [
        "lever",
        67
      ],
      "lemur": [
        "lever",
        72
      ],
      "leper": [
        "expel",
        69
      ],
      "letup": [
        "",
        86
      ],
      "levee": [
        "bugle-solve",
        50
      ],
      "level": [
        "lever",
        72
      ],
      "lever": [
        "",
        76
      ],
      "lexis": [
        "lever-lemon-leggy",
        38
      ],
      "libel": [
        "lever-linen",
        49
      ],
      "licit": [
        "guilt-limit",
        49
      ],
      "liege": [
        "bugle-lodge",
        51
      ],
      "lifer": [
        "lever-loner",
        56
      ],
      "light": [
        "guilt",
        75
      ],
      "liked": [
        "lever-linen-libel",
        36
      ],
      "liken": [
        "lever-linen",
        48
      ],
      "lilac": [
        "solar",
        63
      ],
      "limbo": [
        "could-lingo",
        38
      ],
      "limit": [
        "guilt",
        65
      ],
      "lined": [
        "lever-linen",
        48
      ],
      "linen": [
        "lever",
        65
      ],
      "liner": [
        "lever-loner",
        58
      ],
      "lingo": [
        "could",
        55
      ],
      "lipid": [
        "imply",
        66
      ],
      "lippy": [
        "imply",
        66
      ],
      "liter": [
        "islet",
        75
      ],
      "lithe": [
        "title",
        64
      ],
      "litre": [
        "title-lithe",
        48
      ],
      "lived": [
        "lever-liven",
        48
      ],
      "liven": [
        "lever",
        65
      ],
      "liver": [
        "lever-lover",
        52
      ],
      "livid": [
        "could",
        64
      ],
      "llama": [
        "clans-flair",
        41
      ],
      "loamy": [
        "crawl",
        66
      ],
      "loath": [
        "",
        99
      ],
      "lobby": [
        "could",
        58
      ],
      "lobed": [
        "lever-linen",
        47
      ],
      "local": [
        "solar",
        58
      ],
      "locus": [
        "could",
        64
      ],
      "lodge": [
        "bugle",
        67
      ],
      "loess": [
        "lever",
        72
      ],
      "lofty": [
        "",
        91
      ],
      "logic": [
        "could",
        61
      ],
      "login": [
        "could-lobby",
        43
      ],
      "logon": [
        "could-lobby-login",
        31
      ],
      "lolly": [
        "could-jolly-folly-holly-golly",
        28
      ],
      "loner": [
        "lever",
        64
      ],
      "loony": [
        "could-lobby",
        42
      ],
      "loopy": [
        "imply",
        66
      ],
      "loose": [
        "bugle-solve",
        50
      ],
      "loped": [
        "expel",
        69
      ],
      "lordy": [
        "could-moldy",
        40
      ],
      "lorry": [
        "could-lobby-loony",
        30
      ],
      "loser": [
        "lever-loner",
        48
      ],
      "lotto": [
        "lofty",
        67
      ],
      "lotus": [
        "guilt",
        75
      ],
      "loupe": [
        "",
        99
      ],
      "louse": [
        "bugle",
        75
      ],
      "lousy": [
        "could",
        64
      ],
      "loved": [
        "lever-liven",
        48
      ],
      "lover": [
        "lever",
        69
      ],
      "lower": [
        "lever-loner-loser",
        35
      ],
      "lowly": [
        "could-jolly",
        44
      ],
      "loyal": [
        "solar-local",
        52
      ],
      "lubed": [
        "lever-linen-lobed",
        34
      ],
      "lucid": [
        "could",
        64
      ],
      "lucky": [
        "could-lunch",
        48
      ],
      "lucre": [
        "bugle",
        75
      ],
      "luger": [
        "lever-loner-lifer",
        43
      ],
      "lumen": [
        "lever-linen",
        48
      ],
      "lumpy": [
        "imply",
        66
      ],
      "lunar": [
        "solar",
        70
      ],
      "lunch": [
        "could",
        59
      ],
      "lunge": [
        "bugle",
        75
      ],
      "lupus": [
        "imply",
        66
      ],
      "lurch": [
        "could-lunch",
        48
      ],
      "lured": [
        "lever",
        72
      ],
      "lurid": [
        "could",
        64
      ],
      "lusty": [
        "lofty",
        67
      ],
      "luted": [
        "islet-hotel",
        42
      ],
      "lying": [
        "could-silky",
        35
      ],
      "lymph": [
        "imply",
        66
      ],
      "lyric": [
        "could-zilch",
        45
      ],
      "macaw": [
        "manor-magma",
        32
      ],
      "macho": [
        "manor",
        61
      ],
      "macro": [
        "manor",
        58
      ],
      "madam": [
        "manor-magma",
        32
      ],
      "madly": [
        "solar-daily-badly",
        27
      ],
      "mafia": [
        "manor-magma",
        32
      ],
      "magic": [
        "manor-magma",
        32
      ],
      "magma": [
        "manor",
        49
      ],
      "maize": [
        "raise-naive",
        53
      ],
      "major": [
        "manor-mayor",
        43
      ],
      "maker": [
        "amber",
        66
      ],
      "malic": [
        "solar-balmy",
        46
      ],
      "malty": [
        "salty",
        66
      ],
      "mamba": [
        "manor-magma",
        32
      ],
      "mambo": [
        "manor-macho",
        44
      ],
      "mamma": [
        "manor-magma",
        32
      ],
      "manga": [
        "manor-mania",
        41
      ],
      "mange": [
        "raise-cadge-gauge",
        41
      ],
      "mango": [
        "manor",
        58
      ],
      "mangy": [
        "manor-mania",
        43
      ],
      "mania": [
        "manor",
        53
      ],
      "manic": [
        "manor-mania",
        43
      ],
      "manly": [
        "solar-daily",
        35
      ],
      "manna": [
        "manor-mania-manga",
        29
      ],
      "manor": [
        "",
        61
      ],
      "manse": [
        "raise-masse",
        53
      ],
      "maple": [
        "",
        91
      ],
      "march": [
        "manor",
        57
      ],
      "marry": [
        "manor-march",
        40
      ],
      "marsh": [
        "manor-march",
        40
      ],
      "mason": [
        "manor",
        58
      ],
      "masse": [
        "raise",
        70
      ],
      "match": [
        "taint-maths",
        48
      ],
      "mated": [
        "tread-gated-sated-hated",
        53
      ],
      "matey": [
        "tread-eaten",
        54
      ],
      "matte": [
        "taste",
        81
      ],
      "matzo": [
        "taint-maths",
        48
      ],
      "mauve": [
        "raise-cadge-maybe",
        38
      ],
      "maven": [
        "amber-gamed",
        51
      ],
      "maxed": [
        "amber-gamed",
        51
      ],
      "maxim": [
        "manor-magma",
        32
      ],
      "maybe": [
        "raise-cadge",
        51
      ],
      "mayor": [
        "manor",
        60
      ],
      "mealy": [
        "leafy",
        76
      ],
      "meant": [
        "teary-beast",
        47
      ],
      "meaty": [
        "death",
        65
      ],
      "mecca": [
        "amber-media",
        41
      ],
      "medal": [
        "regal-decal",
        48
      ],
      "media": [
        "amber",
        63
      ],
      "medic": [
        "diner",
        58
      ],
      "melee": [
        "bugle-solve",
        50
      ],
      "melon": [
        "lever-cello-felon",
        31
      ],
      "mensa": [
        "amber-media-mecca",
        29
      ],
      "merch": [
        "diner-mercy",
        35
      ],
      "mercy": [
        "diner",
        43
      ],
      "merge": [
        "snore-verge",
        38
      ],
      "merit": [
        "reset",
        68
      ],
      "merry": [
        "diner-mercy",
        35
      ],
      "meshy": [
        "diner-becks-messy",
        17
      ],
      "messy": [
        "diner-becks",
        29
      ],
      "metal": [
        "",
        92
      ],
      "meted": [
        "reset",
        64
      ],
      "meter": [
        "reset-deter",
        47
      ],
      "metre": [
        "terse",
        69
      ],
      "metro": [
        "reset-tenor",
        44
      ],
      "mewed": [
        "diner-modem-mused",
        25
      ],
      "mezzo": [
        "diner-becks",
        35
      ],
      "micro": [
        "corns-occur",
        38
      ],
      "midge": [
        "snore-guide",
        37
      ],
      "midst": [
        "roust-twist",
        40
      ],
      "might": [
        "roust-theft-night",
        30
      ],
      "miked": [
        "diner-video",
        51
      ],
      "miler": [
        "lever",
        65
      ],
      "milky": [
        "could-silky",
        35
      ],
      "mimed": [
        "diner-video-miked-mixed",
        40
      ],
      "mimic": [
        "corns-mucky",
        34
      ],
      "mince": [
        "snore-niche-wince",
        24
      ],
      "mined": [
        "diner",
        52
      ],
      "miner": [
        "diner",
        56
      ],
      "minim": [
        "corns-dingy",
        32
      ],
      "minor": [
        "corns-drown",
        43
      ],
      "minty": [
        "softy-ditty",
        47
      ],
      "minus": [
        "corns",
        55
      ],
      "mired": [
        "diner-sired-hired",
        45
      ],
      "mirin": [
        "corns",
        50
      ],
      "mirth": [
        "softy-birth-girth",
        45
      ],
      "miser": [
        "diner-riser-wiser",
        36
      ],
      "missy": [
        "corns-smush",
        28
      ],
      "misty": [
        "softy-rusty",
        60
      ],
      "miter": [
        "reset-outer",
        35
      ],
      "mixed": [
        "diner-video-miked",
        50
      ],
      "mixer": [
        "diner-riser-fiber",
        37
      ],
      "mixup": [
        "croup-sunup",
        46
      ],
      "mocha": [
        "manor",
        60
      ],
      "mochi": [
        "corns-hooch",
        38
      ],
      "modal": [
        "solar-local",
        43
      ],
      "model": [
        "lever-yodel",
        48
      ],
      "modem": [
        "diner",
        53
      ],
      "modus": [
        "corns-bogus",
        37
      ],
      "mogul": [
        "could",
        61
      ],
      "moist": [
        "roust",
        50
      ],
      "molar": [
        "solar",
        70
      ],
      "moldy": [
        "could",
        56
      ],
      "molly": [
        "could-jolly-folly-holly-golly",
        28
      ],
      "momma": [
        "manor-mocha",
        44
      ],
      "mommy": [
        "corns-goody-hobby",
        20
      ],
      "money": [
        "diner-honey",
        41
      ],
      "month": [
        "softy-motto",
        51
      ],
      "mooch": [
        "corns-hooch",
        38
      ],
      "moody": [
        "corns-goody",
        34
      ],
      "mooed": [
        "diner-modem-mowed-moved",
        27
      ],
      "moony": [
        "corns-downy",
        36
      ],
      "moose": [
        "snore-chose-goose",
        37
      ],
      "moped": [
        "speed",
        65
      ],
      "moper": [
        "speed-ripen-hyper",
        30
      ],
      "mopey": [
        "speed-ripen",
        49
      ],
      "moral": [
        "solar-coral",
        50
      ],
      "moray": [
        "manor",
        58
      ],
      "morel": [
        "lever-cruel",
        51
      ],
      "moron": [
        "corns",
        55
      ],
      "morph": [
        "croup",
        70
      ],
      "mosey": [
        "diner-cheek-bogey",
        25
      ],
      "mossy": [
        "corns-bosom",
        35
      ],
      "motel": [
        "islet-hotel",
        42
      ],
      "motif": [
        "roust-notch",
        27
      ],
      "motor": [
        "roust-torch",
        41
      ],
      "motto": [
        "softy",
        60
      ],
      "mould": [
        "could-would",
        45
      ],
      "moult": [
        "guilt",
        75
      ],
      "mound": [
        "corns-downy",
        35
      ],
      "mount": [
        "roust-count",
        42
      ],
      "mourn": [
        "corns-donor",
        43
      ],
      "mouse": [
        "snore-house",
        48
      ],
      "mousy": [
        "corns-bosom",
        35
      ],
      "mouth": [
        "softy-motto-month",
        39
      ],
      "moved": [
        "diner-modem-mowed",
        37
      ],
      "mover": [
        "diner-fever-cover-hover",
        37
      ],
      "movie": [
        "snore-vogue",
        42
      ],
      "mowed": [
        "diner-modem",
        40
      ],
      "mower": [
        "diner-fever-bower",
        27
      ],
      "moxie": [
        "snore-vogue",
        39
      ],
      "mucky": [
        "corns",
        47
      ],
      "mucus": [
        "corns",
        54
      ],
      "muddy": [
        "corns-fudgy",
        27
      ],
      "muggy": [
        "corns-fudgy-buggy",
        15
      ],
      "mulch": [
        "could-lunch",
        45
      ],
      "mummy": [
        "corns-fudgy",
        26
      ],
      "munch": [
        "corns-bunch-hunch",
        37
      ],
      "mural": [
        "solar",
        63
      ],
      "murky": [
        "corns-hurry",
        37
      ],
      "mused": [
        "diner-modem",
        38
      ],
      "mushy": [
        "corns-smush",
        28
      ],
      "music": [
        "corns-shuck",
        38
      ],
      "musky": [
        "corns-smush",
        28
      ],
      "musty": [
        "softy-rusty-dusty",
        51
      ],
      "muted": [
        "reset-token-cited",
        26
      ],
      "myrrh": [
        "corns-hurry",
        37
      ],
      "nabob": [
        "manor-bacon",
        41
      ],
      "nacho": [
        "manor",
        58
      ],
      "nadir": [
        "manor",
        58
      ],
      "naggy": [
        "manor-basin-fauna",
        22
      ],
      "naive": [
        "raise",
        70
      ],
      "naked": [
        "amber",
        57
      ],
      "named": [
        "amber-gamed-famed",
        39
      ],
      "nanny": [
        "manor-dance-janky",
        32
      ],
      "nappy": [
        "carps-happy",
        46
      ],
      "nasal": [
        "solar",
        66
      ],
      "nasty": [
        "tarts",
        66
      ],
      "natal": [
        "",
        89
      ],
      "natty": [
        "tarts-fatty",
        57
      ],
      "naval": [
        "solar-canal",
        44
      ],
      "navel": [
        "regal-email-label",
        43
      ],
      "needy": [
        "diner",
        57
      ],
      "neigh": [
        "diner-eking-feign",
        21
      ],
      "nerdy": [
        "diner",
        54
      ],
      "nerve": [
        "snore-urine",
        47
      ],
      "nervy": [
        "diner-rerun",
        35
      ],
      "never": [
        "diner-newer",
        39
      ],
      "newer": [
        "diner",
        55
      ],
      "newly": [
        "lever-cello",
        49
      ],
      "newsy": [
        "diner-envoy",
        40
      ],
      "nexus": [
        "diner-envoy-begun",
        26
      ],
      "nicer": [
        "diner",
        54
      ],
      "niche": [
        "snore",
        53
      ],
      "niece": [
        "snore-niche",
        41
      ],
      "nifty": [
        "softy",
        67
      ],
      "night": [
        "roust-theft",
        37
      ],
      "nimby": [
        "corns-dingy",
        32
      ],
      "ninja": [
        "manor-kinda",
        44
      ],
      "ninny": [
        "corns-dying",
        39
      ],
      "ninth": [
        "softy-birth",
        49
      ],
      "nippy": [
        "croup-nymph",
        42
      ],
      "nitro": [
        "roust-vitro",
        34
      ],
      "nixed": [
        "diner-widen",
        36
      ],
      "noble": [
        "bugle",
        75
      ],
      "nobly": [
        "could-jolly",
        46
      ],
      "nodal": [
        "solar-local-modal",
        31
      ],
      "noise": [
        "snore",
        64
      ],
      "noisy": [
        "corns",
        55
      ],
      "nomad": [
        "manor-among-woman",
        32
      ],
      "noose": [
        "snore",
        64
      ],
      "north": [
        "softy-motto",
        44
      ],
      "nosed": [
        "diner-unwed",
        39
      ],
      "nosey": [
        "diner-seven",
        42
      ],
      "notch": [
        "roust",
        44
      ],
      "noted": [
        "reset-token",
        39
      ],
      "novel": [
        "lever",
        69
      ],
      "nudge": [
        "snore-niche",
        41
      ],
      "nuked": [
        "diner-unwed",
        39
      ],
      "nurse": [
        "snore",
        64
      ],
      "nutso": [
        "roust",
        60
      ],
      "nutty": [
        "softy-ditty",
        46
      ],
      "nylon": [
        "could-lingo",
        38
      ],
      "nymph": [
        "croup",
        54
      ],
      "oaken": [
        "amber-naked",
        47
      ],
      "oared": [
        "amber-raven-cared",
        52
      ],
      "oasis": [
        "manor-cacao",
        40
      ],
      "obese": [
        "snore-house",
        52
      ],
      "occur": [
        "corns",
        55
      ],
      "ocean": [
        "amber-sedan",
        41
      ],
      "ocher": [
        "diner-fever-bower",
        31
      ],
      "ochre": [
        "snore-ombre",
        47
      ],
      "octal": [
        "natal-total",
        52
      ],
      "octet": [
        "reset-civet",
        36
      ],
      "odder": [
        "diner-order",
        41
      ],
      "oddly": [
        "could",
        61
      ],
      "offal": [
        "solar",
        70
      ],
      "offed": [
        "diner-modem-shoed",
        25
      ],
      "offer": [
        "diner-fever",
        43
      ],
      "often": [
        "reset-token",
        39
      ],
      "ogled": [
        "lever-yodel-oiled",
        29
      ],
      "ogler": [
        "lever-miler-ruler",
        39
      ],
      "oiled": [
        "lever-yodel",
        41
      ],
      "oiler": [
        "lever-miler-filer",
        36
      ],
      "okapi": [
        "cramp-spawn",
        45
      ],
      "olden": [
        "bleed-older",
        49
      ],
      "older": [
        "bleed",
        65
      ],
      "oldie": [
        "clove",
        81
      ],
      "olive": [
        "clove",
        81
      ],
      "ombre": [
        "snore",
        64
      ],
      "omega": [
        "amber",
        68
      ],
      "onion": [
        "corns-union",
        35
      ],
      "onset": [
        "reset",
        61
      ],
      "oomph": [
        "croup",
        59
      ],
      "oozed": [
        "diner-modem-wooed",
        40
      ],
      "opera": [
        "caper",
        55
      ],
      "opine": [
        "spire",
        77
      ],
      "opium": [
        "croup",
        70
      ],
      "opted": [
        "crept-setup",
        42
      ],
      "optic": [
        "tromp",
        66
      ],
      "orate": [
        "grate-irate-crate",
        49
      ],
      "orbed": [
        "diner-breed",
        41
      ],
      "orbit": [
        "roust",
        56
      ],
      "order": [
        "diner",
        52
      ],
      "organ": [
        "manor-adorn",
        42
      ],
      "other": [
        "reset-outer",
        43
      ],
      "otter": [
        "reset-outer",
        43
      ],
      "ought": [
        "roust",
        60
      ],
      "ouija": [
        "manor-audio",
        37
      ],
      "ounce": [
        "snore",
        64
      ],
      "outdo": [
        "roust",
        56
      ],
      "outed": [
        "reset-token",
        39
      ],
      "outer": [
        "reset",
        49
      ],
      "outgo": [
        "roust-outdo",
        39
      ],
      "outre": [
        "terse",
        75
      ],
      "ovary": [
        "shark-award",
        39
      ],
      "ovate": [
        "grate-skate-abate",
        32
      ],
      "overt": [
        "reset",
        65
      ],
      "ovine": [
        "snore-ounce",
        47
      ],
      "ovoid": [
        "corns-gizmo",
        29
      ],
      "owing": [
        "corns",
        50
      ],
      "owned": [
        "diner-coned",
        46
      ],
      "owner": [
        "diner",
        55
      ],
      "oxbow": [
        "corns-gizmo",
        29
      ],
      "oxide": [
        "snore-vogue",
        42
      ],
      "ozone": [
        "snore",
        64
      ],
      "paced": [
        "paper",
        77
      ],
      "pacer": [
        "paper-pager-payer",
        52
      ],
      "paddy": [
        "parka-panic",
        41
      ],
      "padre": [
        "parse",
        77
      ],
      "paean": [
        "paper",
        80
      ],
      "pagan": [
        "parka",
        75
      ],
      "paged": [
        "paper-paced",
        66
      ],
      "pager": [
        "paper",
        68
      ],
      "paint": [
        "",
        91
      ],
      "paled": [
        "pedal",
        66
      ],
      "paler": [
        "pedal",
        66
      ],
      "palsy": [
        "polar",
        67
      ],
      "panda": [
        "parka",
        75
      ],
      "panel": [
        "pedal",
        66
      ],
      "panic": [
        "parka",
        58
      ],
      "panko": [
        "parka",
        75
      ],
      "panty": [
        "party-patty-pasty",
        45
      ],
      "papal": [
        "polar",
        67
      ],
      "paper": [
        "",
        91
      ],
      "parch": [
        "parka-parry",
        39
      ],
      "pared": [
        "paper",
        80
      ],
      "parer": [
        "paper-pager-payer-pacer-paver",
        35
      ],
      "parka": [
        "",
        92
      ],
      "parry": [
        "parka",
        56
      ],
      "parse": [
        "",
        92
      ],
      "party": [
        "",
        92
      ],
      "passe": [
        "parse-pause",
        46
      ],
      "pasta": [
        "party",
        81
      ],
      "paste": [
        "",
        99
      ],
      "pasty": [
        "party-patty",
        57
      ],
      "patch": [
        "paint",
        64
      ],
      "patio": [
        "paint",
        78
      ],
      "patsy": [
        "paint-patch",
        48
      ],
      "patty": [
        "party",
        68
      ],
      "pause": [
        "parse",
        63
      ],
      "paved": [
        "paper-paced-paged-pawed",
        48
      ],
      "paver": [
        "paper-pager-payer-pacer",
        43
      ],
      "pawed": [
        "paper-paced-paged",
        58
      ],
      "payee": [
        "parse",
        77
      ],
      "payer": [
        "paper-pager",
        58
      ],
      "peace": [
        "phase",
        63
      ],
      "peach": [
        "",
        99
      ],
      "pearl": [
        "",
        99
      ],
      "peaty": [
        "",
        99
      ],
      "pecan": [
        "paper",
        80
      ],
      "pedal": [
        "",
        91
      ],
      "peeve": [
        "prone-piece",
        56
      ],
      "penal": [
        "pedal",
        66
      ],
      "pence": [
        "prone",
        81
      ],
      "penne": [
        "prone",
        81
      ],
      "penny": [
        "poker",
        58
      ],
      "peony": [
        "poker",
        78
      ],
      "peppy": [
        "poker-penny",
        41
      ],
      "perch": [
        "poker",
        54
      ],
      "peril": [
        "",
        86
      ],
      "perky": [
        "poker",
        78
      ],
      "pesky": [
        "poker",
        78
      ],
      "pesto": [
        "petty",
        65
      ],
      "petal": [
        "",
        99
      ],
      "peter": [
        "petri",
        65
      ],
      "petit": [
        "petri",
        65
      ],
      "petri": [
        "",
        90
      ],
      "petty": [
        "",
        90
      ],
      "phage": [
        "phase",
        63
      ],
      "phase": [
        "",
        88
      ],
      "phish": [
        "phony",
        76
      ],
      "phone": [
        "prone",
        81
      ],
      "phony": [
        "",
        82
      ],
      "photo": [
        "",
        92
      ],
      "piano": [
        "",
        91
      ],
      "picky": [
        "phony-piggy",
        48
      ],
      "piece": [
        "prone",
        64
      ],
      "piety": [
        "petty",
        65
      ],
      "piggy": [
        "phony",
        57
      ],
      "piked": [
        "poker",
        54
      ],
      "piker": [
        "poker",
        78
      ],
      "pilaf": [
        "polar",
        67
      ],
      "piled": [
        "peril",
        61
      ],
      "pilot": [
        "",
        99
      ],
      "pinch": [
        "phony",
        64
      ],
      "pined": [
        "poker-piney",
        52
      ],
      "piney": [
        "poker",
        69
      ],
      "pinky": [
        "phony-punky",
        49
      ],
      "pinot": [
        "point",
        74
      ],
      "pinto": [
        "photo",
        76
      ],
      "pinup": [
        "phony",
        76
      ],
      "pious": [
        "phony-proof",
        43
      ],
      "piped": [
        "poker-piney",
        52
      ],
      "piper": [
        "poker-purer",
        45
      ],
      "pipet": [
        "petri",
        65
      ],
      "pique": [
        "prone-piece",
        51
      ],
      "piste": [
        "",
        99
      ],
      "pitch": [
        "point",
        60
      ],
      "pithy": [
        "point-pitch",
        43
      ],
      "pivot": [
        "point",
        74
      ],
      "pixel": [
        "peril",
        61
      ],
      "pixie": [
        "prone-piece-pique",
        39
      ],
      "pizza": [
        "parka",
        75
      ],
      "place": [
        "plane",
        61
      ],
      "plaid": [
        "plain",
        76
      ],
      "plain": [
        "",
        92
      ],
      "plait": [
        "plant",
        60
      ],
      "plane": [
        "",
        86
      ],
      "plank": [
        "plain",
        76
      ],
      "plant": [
        "",
        85
      ],
      "plasm": [
        "plain-plaza",
        45
      ],
      "plate": [
        "",
        99
      ],
      "playa": [
        "plain-plaza",
        45
      ],
      "plaza": [
        "plain",
        61
      ],
      "plead": [
        "",
        99
      ],
      "pleat": [
        "",
        99
      ],
      "plebe": [
        "plume",
        60
      ],
      "plied": [
        "plier",
        50
      ],
      "plier": [
        "",
        75
      ],
      "plink": [
        "plump-plonk",
        58
      ],
      "plonk": [
        "plump",
        74
      ],
      "pluck": [
        "plump",
        66
      ],
      "plumb": [
        "plump",
        85
      ],
      "plume": [
        "",
        85
      ],
      "plump": [
        "",
        92
      ],
      "plunk": [
        "plump-pluck",
        49
      ],
      "plush": [
        "plump-pluck",
        49
      ],
      "poach": [
        "piano",
        66
      ],
      "poesy": [
        "poker",
        78
      ],
      "point": [
        "",
        92
      ],
      "poise": [
        "prone",
        74
      ],
      "poked": [
        "poker-pokey",
        52
      ],
      "poker": [
        "",
        89
      ],
      "pokey": [
        "poker",
        69
      ],
      "polar": [
        "",
        92
      ],
      "poled": [
        "peril",
        61
      ],
      "polio": [
        "",
        92
      ],
      "polis": [
        "polio",
        67
      ],
      "polka": [
        "polar",
        67
      ],
      "polyp": [
        "polio",
        67
      ],
      "pooch": [
        "phony",
        76
      ],
      "poofy": [
        "phony-proxy",
        54
      ],
      "poppy": [
        "phony",
        69
      ],
      "popup": [
        "phony-prior",
        48
      ],
      "porch": [
        "phony",
        68
      ],
      "pored": [
        "poker",
        78
      ],
      "porky": [
        "phony-poppy",
        52
      ],
      "posed": [
        "poker",
        78
      ],
      "poser": [
        "poker-power",
        52
      ],
      "posit": [
        "point",
        74
      ],
      "posse": [
        "prone-poise",
        57
      ],
      "potty": [
        "photo",
        62
      ],
      "pouch": [
        "phony-porch",
        51
      ],
      "pound": [
        "phony",
        76
      ],
      "pouty": [
        "photo-potty",
        45
      ],
      "power": [
        "poker",
        69
      ],
      "prank": [
        "piano",
        66
      ],
      "prawn": [
        "piano",
        66
      ],
      "preen": [
        "poker-pried",
        49
      ],
      "press": [
        "poker-perch",
        37
      ],
      "price": [
        "prone",
        59
      ],
      "prick": [
        "phony-prism",
        46
      ],
      "pricy": [
        "phony-piggy-privy",
        34
      ],
      "pride": [
        "prone-price",
        50
      ],
      "pried": [
        "poker",
        65
      ],
      "prima": [
        "parka",
        75
      ],
      "prime": [
        "prone-price-pride",
        45
      ],
      "primo": [
        "phony-prior",
        48
      ],
      "primp": [
        "phony-prism",
        46
      ],
      "print": [
        "point",
        74
      ],
      "prion": [
        "phony",
        76
      ],
      "prior": [
        "phony",
        64
      ],
      "prism": [
        "phony",
        62
      ],
      "priss": [
        "phony-prism",
        46
      ],
      "privy": [
        "phony-piggy",
        47
      ],
      "prize": [
        "prone-price-pride-prime",
        35
      ],
      "probe": [
        "prone-prose",
        59
      ],
      "prole": [
        "pulse",
        50
      ],
      "promo": [
        "phony-proof",
        43
      ],
      "prone": [
        "",
        86
      ],
      "prong": [
        "phony",
        76
      ],
      "proof": [
        "phony",
        60
      ],
      "prose": [
        "prone",
        71
      ],
      "proto": [
        "photo",
        76
      ],
      "proud": [
        "phony-proof",
        43
      ],
      "prove": [
        "prone-prose-probe",
        47
      ],
      "prowl": [
        "polio",
        67
      ],
      "proxy": [
        "phony",
        71
      ],
      "prude": [
        "prone-price",
        52
      ],
      "prune": [
        "prone",
        81
      ],
      "psalm": [
        "",
        99
      ],
      "pshaw": [
        "parka",
        75
      ],
      "psych": [
        "phony",
        76
      ],
      "pubic": [
        "phony-prism",
        46
      ],
      "pudge": [
        "prone-piece",
        56
      ],
      "pudgy": [
        "phony-piggy",
        48
      ],
      "puffy": [
        "phony-piggy-puppy",
        29
      ],
      "puked": [
        "poker-piked",
        37
      ],
      "pulpy": [
        "polio",
        67
      ],
      "pulse": [
        "",
        75
      ],
      "punch": [
        "phony-pinch",
        48
      ],
      "punky": [
        "phony",
        66
      ],
      "punny": [
        "phony",
        76
      ],
      "pupae": [
        "parse",
        77
      ],
      "pupil": [
        "polio",
        67
      ],
      "puppy": [
        "phony-piggy",
        41
      ],
      "puree": [
        "prone-purse-purge",
        47
      ],
      "purer": [
        "poker",
        62
      ],
      "purge": [
        "prone-purse",
        59
      ],
      "purse": [
        "prone",
        71
      ],
      "pushy": [
        "phony",
        76
      ],
      "putty": [
        "photo",
        76
      ],
      "pygmy": [
        "phony-piggy",
        48
      ],
      "pylon": [
        "polio",
        67
      ],
      "quack": [
        "shark-knack-aback",
        42
      ],
      "quaff": [
        "shark-guava",
        40
      ],
      "quail": [
        "crawl-shall-avail",
        34
      ],
      "quake": [
        "share-agave",
        48
      ],
      "qualm": [
        "crawl-loamy",
        49
      ],
      "quant": [
        "scant-grant",
        49
      ],
      "quark": [
        "shark",
        70
      ],
      "quart": [
        "scant-draft",
        40
      ],
      "quash": [
        "shark-awash",
        52
      ],
      "quasi": [
        "shark-amass",
        51
      ],
      "queen": [
        "diner-seven",
        42
      ],
      "queer": [
        "diner-fever-sheer",
        29
      ],
      "quell": [
        "lever-swell",
        46
      ],
      "query": [
        "diner-mercy",
        34
      ],
      "queso": [
        "diner-becks",
        35
      ],
      "quest": [
        "reset-guest",
        43
      ],
      "queue": [
        "snore-guide",
        37
      ],
      "quick": [
        "corns-mucky",
        34
      ],
      "quiet": [
        "reset-civet",
        36
      ],
      "quill": [
        "could-bulls",
        46
      ],
      "quilt": [
        "guilt-built",
        42
      ],
      "quirk": [
        "corns-grimy",
        30
      ],
      "quite": [
        "route-suite",
        44
      ],
      "quota": [
        "tarts",
        58
      ],
      "quote": [
        "route",
        82
      ],
      "quoth": [
        "softy-broth",
        59
      ],
      "quran": [
        "manor-urban",
        43
      ],
      "rabbi": [
        "manor-hardy",
        31
      ],
      "rabid": [
        "manor-hardy",
        25
      ],
      "raced": [
        "amber-raven",
        56
      ],
      "racer": [
        "amber-rager-rarer",
        42
      ],
      "radar": [
        "manor",
        54
      ],
      "radii": [
        "manor-hardy-rabid",
        13
      ],
      "radio": [
        "manor",
        60
      ],
      "radon": [
        "manor-rayon",
        40
      ],
      "raged": [
        "amber-raven-raced",
        51
      ],
      "rager": [
        "amber",
        50
      ],
      "rainy": [
        "manor",
        58
      ],
      "raise": [
        "",
        81
      ],
      "rajah": [
        "manor-hardy",
        31
      ],
      "raked": [
        "amber-raven-raced-raged",
        47
      ],
      "rally": [
        "solar",
        70
      ],
      "ralph": [
        "apply",
        66
      ],
      "ramen": [
        "amber",
        64
      ],
      "ranch": [
        "manor-rangy",
        40
      ],
      "randy": [
        "manor-rangy",
        40
      ],
      "range": [
        "raise",
        76
      ],
      "rangy": [
        "manor",
        57
      ],
      "rapid": [
        "carps",
        59
      ],
      "rarer": [
        "amber-rager",
        47
      ],
      "raspy": [
        "carps",
        74
      ],
      "rated": [
        "tread",
        74
      ],
      "rater": [
        "tread-earth-cater-water",
        29
      ],
      "ratio": [
        "taint",
        67
      ],
      "ratty": [
        "tarts",
        79
      ],
      "raved": [
        "amber-raven",
        45
      ],
      "raven": [
        "amber",
        62
      ],
      "raver": [
        "amber-rager-rarer-racer",
        32
      ],
      "rayon": [
        "manor",
        57
      ],
      "razed": [
        "amber-raven-raced-raged-raked",
        39
      ],
      "razor": [
        "manor-savor",
        40
      ],
      "reach": [
        "heard",
        72
      ],
      "react": [
        "teary",
        80
      ],
      "ready": [
        "heard",
        72
      ],
      "realm": [
        "leafy",
        76
      ],
      "rearm": [
        "heard-weary",
        44
      ],
      "rebar": [
        "amber",
        59
      ],
      "rebel": [
        "lever",
        72
      ],
      "rebid": [
        "diner-redid",
        39
      ],
      "rebus": [
        "diner-mercy",
        35
      ],
      "rebut": [
        "reset",
        58
      ],
      "rebuy": [
        "diner-mercy",
        37
      ],
      "recap": [
        "caper",
        70
      ],
      "recon": [
        "diner-rerun",
        35
      ],
      "recur": [
        "diner-error",
        39
      ],
      "recut": [
        "reset-rebut",
        49
      ],
      "redid": [
        "diner",
        55
      ],
      "redub": [
        "diner-credo-redux",
        23
      ],
      "redux": [
        "diner-credo",
        36
      ],
      "reedy": [
        "diner-credo",
        42
      ],
      "refer": [
        "diner-fever",
        37
      ],
      "refit": [
        "reset-rebut-remit",
        34
      ],
      "refry": [
        "diner-mercy-rebuy",
        25
      ],
      "regal": [
        "",
        84
      ],
      "rehab": [
        "amber-bread",
        48
      ],
      "reify": [
        "diner-reiki",
        36
      ],
      "reign": [
        "diner",
        57
      ],
      "reiki": [
        "diner",
        53
      ],
      "relax": [
        "regal-relay",
        49
      ],
      "relay": [
        "regal",
        65
      ],
      "relic": [
        "lever",
        62
      ],
      "relit": [
        "islet",
        75
      ],
      "remap": [
        "caper-opera",
        39
      ],
      "remit": [
        "reset-rebut",
        47
      ],
      "remix": [
        "diner-reiki",
        36
      ],
      "renal": [
        "regal",
        79
      ],
      "renew": [
        "diner",
        54
      ],
      "repay": [
        "caper",
        70
      ],
      "repel": [
        "expel",
        69
      ],
      "reply": [
        "expel",
        69
      ],
      "repot": [
        "crept",
        79
      ],
      "reran": [
        "amber-wreak",
        48
      ],
      "rerun": [
        "diner",
        52
      ],
      "resaw": [
        "amber-wreak",
        48
      ],
      "reset": [
        "",
        70
      ],
      "resin": [
        "diner-reign",
        40
      ],
      "retag": [
        "tread",
        74
      ],
      "retch": [
        "reset-retro",
        45
      ],
      "retie": [
        "terse-metre",
        52
      ],
      "retro": [
        "reset",
        62
      ],
      "retry": [
        "reset-retro",
        45
      ],
      "reuse": [
        "snore-curse",
        45
      ],
      "revel": [
        "lever",
        72
      ],
      "revue": [
        "snore-verge",
        38
      ],
      "rheum": [
        "diner-mercy",
        35
      ],
      "rhino": [
        "corns-irony",
        45
      ],
      "rhyme": [
        "snore-verge-crude",
        27
      ],
      "ricin": [
        "corns-incur",
        38
      ],
      "rider": [
        "diner-wider",
        47
      ],
      "ridge": [
        "snore-verge",
        38
      ],
      "rifle": [
        "bugle-while",
        50
      ],
      "right": [
        "roust",
        60
      ],
      "rigid": [
        "corns-grimy",
        32
      ],
      "rigor": [
        "corns-vroom",
        33
      ],
      "riled": [
        "lever-cruel",
        51
      ],
      "rinse": [
        "snore-nurse",
        48
      ],
      "ripen": [
        "speed",
        59
      ],
      "riper": [
        "speed-ripen",
        49
      ],
      "risen": [
        "diner-siren",
        39
      ],
      "riser": [
        "diner",
        48
      ],
      "risky": [
        "corns-brisk",
        36
      ],
      "ritzy": [
        "roust",
        60
      ],
      "rival": [
        "solar-mural",
        53
      ],
      "riven": [
        "diner-siren",
        39
      ],
      "river": [
        "diner-riser",
        45
      ],
      "rivet": [
        "reset",
        68
      ],
      "roach": [
        "shark",
        70
      ],
      "roast": [
        "scant",
        61
      ],
      "robed": [
        "diner-breed",
        41
      ],
      "robin": [
        "corns-donor-mourn",
        31
      ],
      "robot": [
        "roust",
        60
      ],
      "rocky": [
        "corns",
        50
      ],
      "rodeo": [
        "diner-breed",
        41
      ],
      "roger": [
        "diner-fever-bower-homer-joker",
        16
      ],
      "rogue": [
        "snore-forge",
        39
      ],
      "roman": [
        "manor",
        58
      ],
      "roomy": [
        "corns-rowdy",
        35
      ],
      "roost": [
        "roust",
        60
      ],
      "roped": [
        "speed-moped",
        53
      ],
      "roper": [
        "speed-ripen",
        49
      ],
      "rosin": [
        "corns",
        50
      ],
      "rotor": [
        "roust",
        60
      ],
      "rouge": [
        "snore-forge",
        39
      ],
      "rough": [
        "corns-rowdy",
        35
      ],
      "round": [
        "corns",
        50
      ],
      "rouse": [
        "snore-horse",
        54
      ],
      "roust": [
        "",
        64
      ],
      "route": [
        "",
        90
      ],
      "roved": [
        "diner-breed-shred-rowed",
        30
      ],
      "rover": [
        "diner-fever-cover-hover-mover",
        29
      ],
      "rowdy": [
        "corns",
        52
      ],
      "rowed": [
        "diner-breed-shred",
        40
      ],
      "rower": [
        "diner-fever-bower-mower-cower",
        19
      ],
      "royal": [
        "solar-coral",
        50
      ],
      "ruble": [
        "bugle",
        75
      ],
      "ruddy": [
        "corns-grimy",
        32
      ],
      "ruder": [
        "diner-order",
        41
      ],
      "rugby": [
        "corns-grimy",
        32
      ],
      "ruing": [
        "corns-bring",
        31
      ],
      "ruled": [
        "lever-cruel",
        51
      ],
      "ruler": [
        "lever-miler",
        51
      ],
      "rumba": [
        "manor",
        59
      ],
      "rummy": [
        "corns-grimy",
        32
      ],
      "rumor": [
        "corns-vroom-humor",
        15
      ],
      "runny": [
        "corns-bring",
        31
      ],
      "runup": [
        "croup-syrup",
        47
      ],
      "rupee": [
        "spire-crepe",
        43
      ],
      "rural": [
        "solar-mural",
        49
      ],
      "rusty": [
        "softy",
        66
      ],
      "saber": [
        "amber",
        68
      ],
      "sable": [
        "angle-cable-fable",
        41
      ],
      "sabre": [
        "raise",
        76
      ],
      "sadly": [
        "solar",
        70
      ],
      "safer": [
        "amber-rager",
        41
      ],
      "saggy": [
        "manor-daubs-gassy",
        24
      ],
      "saint": [
        "taint",
        65
      ],
      "salad": [
        "solar",
        70
      ],
      "sally": [
        "solar-salsa",
        51
      ],
      "salon": [
        "solar",
        66
      ],
      "salsa": [
        "solar",
        68
      ],
      "salty": [
        "",
        91
      ],
      "salve": [
        "angle-value",
        49
      ],
      "salvo": [
        "solar-salon",
        49
      ],
      "samba": [
        "manor-hammy",
        39
      ],
      "samey": [
        "amber-gamed-cameo",
        26
      ],
      "sandy": [
        "manor-dance",
        37
      ],
      "saner": [
        "amber-rager-safer-saver",
        23
      ],
      "sappy": [
        "carps",
        74
      ],
      "sassy": [
        "manor-daubs-gassy",
        24
      ],
      "sated": [
        "tread-gated",
        60
      ],
      "satin": [
        "taint",
        71
      ],
      "satyr": [
        "taint-maths",
        48
      ],
      "sauce": [
        "raise",
        76
      ],
      "saucy": [
        "manor-daubs",
        37
      ],
      "sauna": [
        "manor-basin",
        42
      ],
      "saute": [
        "taste",
        81
      ],
      "saved": [
        "amber-naked-jaded-caged-sawed",
        41
      ],
      "saver": [
        "amber-rager-safer",
        33
      ],
      "savor": [
        "manor",
        57
      ],
      "savoy": [
        "manor-yahoo-bayou",
        27
      ],
      "savvy": [
        "manor-daubs-gassy",
        24
      ],
      "sawed": [
        "amber-naked-jaded-caged",
        44
      ],
      "scald": [
        "crawl-scaly",
        58
      ],
      "scale": [
        "",
        92
      ],
      "scalp": [
        "",
        99
      ],
      "scaly": [
        "crawl",
        75
      ],
      "scamp": [
        "cramp",
        73
      ],
      "scant": [
        "",
        83
      ],
      "scape": [
        "spare-shape",
        56
      ],
      "scare": [
        "share",
        74
      ],
      "scarf": [
        "shark",
        59
      ],
      "scarp": [
        "cramp",
        73
      ],
      "scary": [
        "shark-scarf",
        51
      ],
      "scene": [
        "snore-shine",
        46
      ],
      "scent": [
        "reset-guest",
        40
      ],
      "schmo": [
        "corns-shock",
        37
      ],
      "schwa": [
        "manor-squab-shiva",
        11
      ],
      "scion": [
        "corns",
        50
      ],
      "scoff": [
        "corns-shock",
        37
      ],
      "scold": [
        "could",
        64
      ],
      "scone": [
        "snore-shone",
        48
      ],
      "scoop": [
        "croup",
        70
      ],
      "scoot": [
        "roust-shoot",
        47
      ],
      "scope": [
        "spire",
        77
      ],
      "score": [
        "snore",
        64
      ],
      "scorn": [
        "corns",
        50
      ],
      "scour": [
        "corns",
        50
      ],
      "scout": [
        "roust",
        53
      ],
      "scowl": [
        "could",
        64
      ],
      "scram": [
        "manor-rumba",
        42
      ],
      "scrap": [
        "carps",
        74
      ],
      "scree": [
        "snore-serve",
        49
      ],
      "screw": [
        "diner",
        55
      ],
      "scrim": [
        "corns-scrub",
        38
      ],
      "scrip": [
        "croup",
        70
      ],
      "scrod": [
        "corns",
        50
      ],
      "scrub": [
        "corns",
        55
      ],
      "scrum": [
        "corns-scrub",
        38
      ],
      "scuba": [
        "manor-squab",
        29
      ],
      "scuff": [
        "corns-shuck",
        38
      ],
      "scull": [
        "could",
        64
      ],
      "seamy": [
        "heard",
        72
      ],
      "sedan": [
        "amber",
        54
      ],
      "seder": [
        "diner-order",
        39
      ],
      "sedge": [
        "snore-siege",
        41
      ],
      "seedy": [
        "diner",
        57
      ],
      "segue": [
        "snore-siege",
        41
      ],
      "seize": [
        "snore-siege",
        41
      ],
      "sense": [
        "snore-shine",
        46
      ],
      "sepia": [
        "caper",
        70
      ],
      "serif": [
        "diner-reiki",
        36
      ],
      "serum": [
        "diner-mercy",
        35
      ],
      "serve": [
        "snore",
        65
      ],
      "setup": [
        "crept",
        58
      ],
      "seven": [
        "diner",
        49
      ],
      "sever": [
        "diner-fever",
        37
      ],
      "sewed": [
        "diner-modem-edges",
        40
      ],
      "sewer": [
        "diner-fever",
        37
      ],
      "shack": [
        "shark",
        66
      ],
      "shade": [
        "share",
        71
      ],
      "shady": [
        "shark",
        70
      ],
      "shaft": [
        "scant-smart",
        49
      ],
      "shake": [
        "share-shade-shame",
        54
      ],
      "shaky": [
        "shark",
        70
      ],
      "shale": [
        "scale",
        60
      ],
      "shall": [
        "crawl",
        61
      ],
      "shalt": [
        "stall",
        77
      ],
      "shame": [
        "share-shade",
        62
      ],
      "shank": [
        "shark-shack",
        50
      ],
      "shape": [
        "spare",
        72
      ],
      "shard": [
        "shark",
        70
      ],
      "share": [
        "",
        82
      ],
      "shark": [
        "",
        74
      ],
      "sharp": [
        "cramp",
        73
      ],
      "shave": [
        "share-shade-shame-shake",
        44
      ],
      "shawl": [
        "crawl",
        84
      ],
      "sheaf": [
        "amber-sedan",
        41
      ],
      "shear": [
        "amber-swear",
        48
      ],
      "sheen": [
        "diner-seven",
        42
      ],
      "sheep": [
        "speed",
        59
      ],
      "sheer": [
        "diner-fever",
        41
      ],
      "sheet": [
        "reset",
        61
      ],
      "sheik": [
        "diner-weigh",
        39
      ],
      "shelf": [
        "lever-swell",
        47
      ],
      "shell": [
        "lever-swell",
        39
      ],
      "shied": [
        "diner",
        57
      ],
      "shift": [
        "roust",
        49
      ],
      "shill": [
        "could-skill",
        38
      ],
      "shine": [
        "snore",
        57
      ],
      "shiny": [
        "corns-suing",
        32
      ],
      "shire": [
        "snore",
        64
      ],
      "shirk": [
        "corns-brisk-smirk",
        23
      ],
      "shirt": [
        "roust",
        58
      ],
      "shiva": [
        "manor-squab",
        23
      ],
      "shlep": [
        "expel-julep",
        32
      ],
      "shoal": [
        "solar",
        70
      ],
      "shock": [
        "corns",
        53
      ],
      "shoed": [
        "diner-modem",
        38
      ],
      "shone": [
        "snore",
        64
      ],
      "shook": [
        "corns-smoky",
        37
      ],
      "shoot": [
        "roust",
        57
      ],
      "shore": [
        "snore-score",
        54
      ],
      "shorn": [
        "corns-sworn",
        37
      ],
      "short": [
        "roust",
        60
      ],
      "shout": [
        "roust-scout",
        48
      ],
      "shove": [
        "snore-smoke",
        47
      ],
      "shown": [
        "corns-snowy",
        35
      ],
      "showy": [
        "corns-smoky",
        37
      ],
      "shred": [
        "diner-breed",
        43
      ],
      "shrew": [
        "diner-screw",
        39
      ],
      "shrub": [
        "corns-shrug",
        38
      ],
      "shrug": [
        "corns",
        54
      ],
      "shuck": [
        "corns",
        55
      ],
      "shunt": [
        "roust-stunt",
        44
      ],
      "shush": [
        "corns-smush",
        28
      ],
      "shyly": [
        "could-skill",
        39
      ],
      "sided": [
        "diner-video",
        46
      ],
      "sidle": [
        "bugle-while-rifle",
        38
      ],
      "siege": [
        "snore",
        57
      ],
      "sieve": [
        "snore-siege",
        41
      ],
      "sight": [
        "roust-shift",
        32
      ],
      "sigma": [
        "manor-amiss",
        41
      ],
      "silky": [
        "could",
        52
      ],
      "silly": [
        "could-skill",
        39
      ],
      "silty": [
        "lofty",
        67
      ],
      "since": [
        "snore-shine",
        42
      ],
      "sinew": [
        "diner",
        58
      ],
      "singe": [
        "snore-shine-since",
        30
      ],
      "sinus": [
        "corns-minus",
        38
      ],
      "sired": [
        "diner",
        52
      ],
      "siren": [
        "diner",
        55
      ],
      "sissy": [
        "corns-smush",
        28
      ],
      "sitar": [
        "taint",
        65
      ],
      "sited": [
        "reset",
        68
      ],
      "situp": [
        "tromp-cutup",
        29
      ],
      "sixth": [
        "softy",
        66
      ],
      "sixty": [
        "softy",
        74
      ],
      "sized": [
        "diner-video-miked-gibed",
        38
      ],
      "skate": [
        "grate",
        65
      ],
      "skeet": [
        "reset-sheet-sweet",
        39
      ],
      "skein": [
        "diner-eking",
        37
      ],
      "skied": [
        "diner-shied",
        40
      ],
      "skier": [
        "diner-crier",
        37
      ],
      "skiff": [
        "corns-smush",
        28
      ],
      "skill": [
        "could",
        47
      ],
      "skimp": [
        "croup",
        70
      ],
      "skirt": [
        "roust-shirt",
        41
      ],
      "skulk": [
        "could-skull",
        45
      ],
      "skull": [
        "could",
        62
      ],
      "skunk": [
        "corns-suing",
        32
      ],
      "slack": [
        "clans",
        80
      ],
      "slain": [
        "clans",
        80
      ],
      "slake": [
        "blare-flake",
        58
      ],
      "slang": [
        "clans",
        80
      ],
      "slant": [
        "blast",
        61
      ],
      "slash": [
        "clans-flash",
        50
      ],
      "slate": [
        "",
        75
      ],
      "sleek": [
        "bleed",
        76
      ],
      "sleep": [
        "",
        86
      ],
      "sleet": [
        "fleet",
        66
      ],
      "slept": [
        "",
        99
      ],
      "slice": [
        "clove",
        81
      ],
      "slick": [
        "flunk-clock",
        47
      ],
      "slide": [
        "clove",
        65
      ],
      "slime": [
        "clove-slide",
        58
      ],
      "slimy": [
        "flunk-gloms",
        43
      ],
      "sling": [
        "flunk-cling",
        45
      ],
      "slink": [
        "flunk-blink",
        56
      ],
      "sloop": [
        "slump",
        75
      ],
      "slope": [
        "",
        86
      ],
      "slosh": [
        "flunk-gloms",
        43
      ],
      "sloth": [
        "blitz-cloth",
        46
      ],
      "slump": [
        "",
        91
      ],
      "slung": [
        "flunk-clung",
        53
      ],
      "slunk": [
        "flunk",
        71
      ],
      "slurp": [
        "slump",
        75
      ],
      "slush": [
        "flunk-blush",
        50
      ],
      "slyly": [
        "flunk-gloms",
        43
      ],
      "smack": [
        "shark-snack",
        48
      ],
      "small": [
        "crawl-shall",
        51
      ],
      "smarm": [
        "shark-scarf-swarm",
        34
      ],
      "smart": [
        "scant",
        66
      ],
      "smash": [
        "shark",
        61
      ],
      "smear": [
        "amber",
        68
      ],
      "smell": [
        "lever-swell-shell",
        26
      ],
      "smelt": [
        "islet",
        75
      ],
      "smile": [
        "bugle-while",
        46
      ],
      "smirk": [
        "corns-brisk",
        35
      ],
      "smite": [
        "route-white",
        53
      ],
      "smith": [
        "softy-sixth",
        50
      ],
      "smock": [
        "corns-shock",
        37
      ],
      "smoke": [
        "snore",
        64
      ],
      "smoky": [
        "corns",
        54
      ],
      "smote": [
        "route-emote",
        56
      ],
      "smush": [
        "corns",
        38
      ],
      "snack": [
        "shark",
        65
      ],
      "snafu": [
        "shark",
        61
      ],
      "snail": [
        "crawl-shall",
        51
      ],
      "snake": [
        "share",
        72
      ],
      "snaky": [
        "shark",
        70
      ],
      "snare": [
        "share-scare",
        57
      ],
      "snarf": [
        "shark-scarf",
        51
      ],
      "snark": [
        "shark",
        70
      ],
      "snarl": [
        "crawl",
        70
      ],
      "sneak": [
        "amber-sedan",
        41
      ],
      "sneer": [
        "diner-newer",
        39
      ],
      "snide": [
        "snore",
        64
      ],
      "sniff": [
        "corns",
        54
      ],
      "snipe": [
        "spire-swipe",
        48
      ],
      "snoop": [
        "croup-swoop",
        46
      ],
      "snoot": [
        "roust-shoot-scoot",
        34
      ],
      "snore": [
        "",
        66
      ],
      "snort": [
        "roust-short",
        43
      ],
      "snout": [
        "roust-scout-shout-stout",
        33
      ],
      "snowy": [
        "corns",
        52
      ],
      "snuck": [
        "corns",
        55
      ],
      "snuff": [
        "corns-sniff",
        38
      ],
      "soapy": [
        "cramp-spawn",
        45
      ],
      "sober": [
        "diner-fever-bower",
        31
      ],
      "softy": [
        "",
        80
      ],
      "soggy": [
        "corns-bosom",
        35
      ],
      "solar": [
        "",
        75
      ],
      "soled": [
        "lever-yodel",
        43
      ],
      "solid": [
        "could",
        64
      ],
      "solve": [
        "bugle",
        66
      ],
      "sonar": [
        "manor",
        58
      ],
      "sonic": [
        "corns",
        50
      ],
      "sooth": [
        "softy-south",
        50
      ],
      "sooty": [
        "softy",
        74
      ],
      "soppy": [
        "croup-oomph",
        42
      ],
      "sorry": [
        "corns",
        50
      ],
      "sound": [
        "corns",
        50
      ],
      "soupy": [
        "croup",
        70
      ],
      "south": [
        "softy",
        67
      ],
      "sowed": [
        "diner-modem-wooed",
        43
      ],
      "sower": [
        "diner-fever-bower-mower-cower",
        19
      ],
      "space": [
        "spare",
        58
      ],
      "spade": [
        "spare-space",
        42
      ],
      "spank": [
        "cramp-spawn",
        45
      ],
      "spare": [
        "",
        91
      ],
      "spark": [
        "cramp",
        73
      ],
      "spasm": [
        "cramp",
        73
      ],
      "spate": [
        "",
        99
      ],
      "spawn": [
        "cramp",
        62
      ],
      "speak": [
        "caper",
        70
      ],
      "spear": [
        "caper",
        70
      ],
      "speck": [
        "speed-sperm",
        47
      ],
      "speed": [
        "",
        85
      ],
      "spell": [
        "expel",
        69
      ],
      "spelt": [
        "letup",
        61
      ],
      "spend": [
        "speed",
        78
      ],
      "spent": [
        "crept",
        79
      ],
      "sperm": [
        "speed",
        64
      ],
      "spice": [
        "spire-spine",
        51
      ],
      "spicy": [
        "croup",
        70
      ],
      "spied": [
        "speed",
        78
      ],
      "spiel": [
        "expel",
        69
      ],
      "spiff": [
        "croup-nymph",
        42
      ],
      "spike": [
        "spire-spine-spice",
        39
      ],
      "spiky": [
        "croup-nymph",
        42
      ],
      "spill": [
        "imply",
        66
      ],
      "spilt": [
        "split",
        64
      ],
      "spine": [
        "spire",
        60
      ],
      "spiny": [
        "croup-nymph",
        42
      ],
      "spire": [
        "",
        88
      ],
      "spite": [
        "",
        99
      ],
      "splat": [
        "aptly",
        61
      ],
      "splay": [
        "apply",
        66
      ],
      "split": [
        "",
        89
      ],
      "spoil": [
        "imply",
        66
      ],
      "spoke": [
        "spire",
        66
      ],
      "spoof": [
        "croup-spoon",
        49
      ],
      "spook": [
        "croup-spoon-spoof",
        36
      ],
      "spool": [
        "imply",
        66
      ],
      "spoon": [
        "croup",
        61
      ],
      "spore": [
        "spire",
        77
      ],
      "spork": [
        "croup",
        70
      ],
      "sport": [
        "tromp",
        66
      ],
      "spout": [
        "tromp",
        66
      ],
      "spray": [
        "carps",
        74
      ],
      "spree": [
        "spire",
        77
      ],
      "sprig": [
        "croup",
        70
      ],
      "spume": [
        "spire-spoke",
        50
      ],
      "spunk": [
        "croup-bumpy",
        45
      ],
      "spurn": [
        "croup",
        70
      ],
      "spurt": [
        "tromp",
        66
      ],
      "squab": [
        "manor",
        45
      ],
      "squad": [
        "manor-squab",
        29
      ],
      "squat": [
        "taint-abort",
        34
      ],
      "squib": [
        "corns-smush-squid",
        16
      ],
      "squid": [
        "corns-smush",
        29
      ],
      "stack": [
        "scant",
        78
      ],
      "staff": [
        "scant-stair-stash",
        32
      ],
      "stage": [
        "trace",
        65
      ],
      "staid": [
        "scant-stair",
        47
      ],
      "stain": [
        "scant",
        78
      ],
      "stair": [
        "scant",
        57
      ],
      "stake": [
        "trace-stage",
        55
      ],
      "stale": [
        "",
        99
      ],
      "stalk": [
        "stall",
        77
      ],
      "stall": [
        "",
        92
      ],
      "stamp": [
        "apart",
        61
      ],
      "stand": [
        "scant",
        69
      ],
      "stank": [
        "scant-stand",
        53
      ],
      "staph": [
        "apart-stamp",
        44
      ],
      "stare": [
        "trace",
        78
      ],
      "stark": [
        "scant-stair",
        47
      ],
      "start": [
        "scant-smart",
        49
      ],
      "stash": [
        "scant-stair",
        44
      ],
      "state": [
        "grate-skate",
        53
      ],
      "stave": [
        "trace-stage-stake",
        43
      ],
      "stead": [
        "tread",
        74
      ],
      "steak": [
        "tread-cheat-steam",
        36
      ],
      "steal": [
        "metal",
        75
      ],
      "steam": [
        "tread-cheat",
        49
      ],
      "steed": [
        "reset",
        68
      ],
      "steel": [
        "islet",
        75
      ],
      "steep": [
        "crept",
        79
      ],
      "steer": [
        "reset",
        60
      ],
      "stein": [
        "reset-ethos",
        46
      ],
      "stele": [
        "title-stole-style",
        42
      ],
      "steno": [
        "reset-ethos",
        46
      ],
      "stent": [
        "reset-guest-scent",
        28
      ],
      "stern": [
        "reset",
        61
      ],
      "stick": [
        "roust-stink",
        36
      ],
      "stiff": [
        "roust-stink",
        36
      ],
      "stile": [
        "title",
        66
      ],
      "still": [
        "guilt-trill",
        40
      ],
      "stilt": [
        "guilt",
        75
      ],
      "sting": [
        "roust-stink",
        36
      ],
      "stink": [
        "roust",
        53
      ],
      "stint": [
        "roust-shift",
        32
      ],
      "stock": [
        "roust-stoic",
        44
      ],
      "stoic": [
        "roust",
        53
      ],
      "stoke": [
        "terse-stone",
        57
      ],
      "stole": [
        "title",
        65
      ],
      "stomp": [
        "tromp",
        66
      ],
      "stone": [
        "terse",
        67
      ],
      "stony": [
        "roust-stoic-stood",
        30
      ],
      "stood": [
        "roust-stoic",
        42
      ],
      "stool": [
        "guilt",
        75
      ],
      "stoop": [
        "tromp",
        66
      ],
      "store": [
        "terse",
        75
      ],
      "stork": [
        "roust-story-storm",
        35
      ],
      "storm": [
        "roust-story",
        47
      ],
      "story": [
        "roust",
        55
      ],
      "stout": [
        "roust-scout-shout",
        43
      ],
      "stove": [
        "terse-stone-stoke",
        44
      ],
      "strap": [
        "kaput",
        67
      ],
      "straw": [
        "taint-stray",
        46
      ],
      "stray": [
        "taint",
        63
      ],
      "strep": [
        "crept",
        79
      ],
      "strew": [
        "reset",
        68
      ],
      "strip": [
        "tromp",
        66
      ],
      "strum": [
        "roust",
        60
      ],
      "strut": [
        "roust",
        60
      ],
      "stuck": [
        "roust-stunk",
        39
      ],
      "study": [
        "roust-stunk",
        38
      ],
      "stuff": [
        "roust-stunk-study",
        26
      ],
      "stump": [
        "tromp",
        66
      ],
      "stung": [
        "roust-stunk",
        39
      ],
      "stunk": [
        "roust",
        49
      ],
      "stunt": [
        "roust",
        60
      ],
      "style": [
        "title-stole",
        54
      ],
      "suave": [
        "share-snake",
        55
      ],
      "sudsy": [
        "corns-smush",
        28
      ],
      "suede": [
        "snore-siege",
        41
      ],
      "sugar": [
        "manor-cigar",
        38
      ],
      "suing": [
        "corns",
        48
      ],
      "suite": [
        "route",
        60
      ],
      "sulky": [
        "could-bulky",
        43
      ],
      "sully": [
        "could-bulls",
        46
      ],
      "sumac": [
        "manor-amiss",
        41
      ],
      "sunny": [
        "corns-suing",
        32
      ],
      "sunup": [
        "croup",
        63
      ],
      "super": [
        "speed",
        78
      ],
      "surer": [
        "diner-fever-bower-usher",
        22
      ],
      "surge": [
        "snore-serve",
        49
      ],
      "surly": [
        "could-bulls",
        46
      ],
      "sushi": [
        "corns-smush",
        28
      ],
      "swain": [
        "shark-snafu",
        42
      ],
      "swale": [
        "scale-shale",
        43
      ],
      "swami": [
        "shark-snafu",
        50
      ],
      "swamp": [
        "cramp",
        73
      ],
      "swang": [
        "shark-snafu-swain",
        29
      ],
      "swank": [
        "shark-snack",
        48
      ],
      "swarm": [
        "shark-scarf",
        47
      ],
      "swash": [
        "shark-smash",
        45
      ],
      "swath": [
        "wrath",
        62
      ],
      "swear": [
        "amber",
        65
      ],
      "sweat": [
        "tread-cheat",
        53
      ],
      "sweep": [
        "speed-sheep",
        42
      ],
      "sweet": [
        "reset-sheet",
        51
      ],
      "swell": [
        "lever",
        52
      ],
      "swept": [
        "crept",
        61
      ],
      "swift": [
        "roust-shift",
        32
      ],
      "swill": [
        "could-skill-shill",
        26
      ],
      "swine": [
        "snore-shine",
        46
      ],
      "swing": [
        "corns-suing",
        32
      ],
      "swipe": [
        "spire",
        64
      ],
      "swirl": [
        "could-silky",
        35
      ],
      "swish": [
        "corns-smush",
        28
      ],
      "swoon": [
        "corns-snowy",
        35
      ],
      "swoop": [
        "croup",
        63
      ],
      "sword": [
        "corns",
        53
      ],
      "swore": [
        "snore-score-shore",
        42
      ],
      "sworn": [
        "corns",
        54
      ],
      "swung": [
        "corns-suing",
        32
      ],
      "synch": [
        "corns-snuck",
        38
      ],
      "synod": [
        "corns-snowy",
        35
      ],
      "synth": [
        "softy",
        74
      ],
      "syrup": [
        "croup",
        64
      ],
      "tabby": [
        "taint-tardy-tacky-taffy",
        34
      ],
      "table": [
        "lathe",
        65
      ],
      "taboo": [
        "taint-tardy",
        51
      ],
      "tacit": [
        "taint",
        71
      ],
      "tacky": [
        "taint-tardy",
        48
      ],
      "taffy": [
        "taint-tardy-tacky",
        44
      ],
      "taint": [
        "",
        77
      ],
      "taken": [
        "tread",
        74
      ],
      "taker": [
        "tread",
        68
      ],
      "talky": [
        "natal-fault",
        44
      ],
      "tally": [
        "natal-fault",
        44
      ],
      "talon": [
        "natal",
        78
      ],
      "talus": [
        "natal-fault",
        44
      ],
      "tamed": [
        "tread-tased",
        60
      ],
      "tamer": [
        "tread-taker",
        55
      ],
      "tango": [
        "taint-tangy",
        49
      ],
      "tangy": [
        "taint",
        66
      ],
      "taped": [
        "adept",
        65
      ],
      "taper": [
        "adept",
        65
      ],
      "tapir": [
        "kaput",
        67
      ],
      "tardy": [
        "taint",
        59
      ],
      "tarot": [
        "taint",
        71
      ],
      "tarry": [
        "taint-tardy",
        51
      ],
      "tased": [
        "tread",
        72
      ],
      "taser": [
        "tread-taker-tamer-tater",
        38
      ],
      "taste": [
        "",
        91
      ],
      "tasty": [
        "tarts",
        79
      ],
      "tater": [
        "tread-taker-tamer",
        48
      ],
      "tatty": [
        "tarts",
        79
      ],
      "taunt": [
        "taint",
        71
      ],
      "taupe": [
        "",
        99
      ],
      "tawny": [
        "taint",
        71
      ],
      "taxed": [
        "tread-tased-tamed",
        48
      ],
      "teach": [
        "teary",
        80
      ],
      "teary": [
        "",
        91
      ],
      "tease": [
        "trace",
        78
      ],
      "teddy": [
        "reset-fetch",
        42
      ],
      "teeny": [
        "reset",
        68
      ],
      "teeth": [
        "tenth",
        79
      ],
      "telos": [
        "islet",
        75
      ],
      "tempo": [
        "crept",
        79
      ],
      "tempt": [
        "crept",
        67
      ],
      "tenet": [
        "reset",
        66
      ],
      "tenor": [
        "reset",
        61
      ],
      "tense": [
        "terse",
        75
      ],
      "tenth": [
        "",
        91
      ],
      "tepee": [
        "trope",
        65
      ],
      "tepid": [
        "crept-setup",
        42
      ],
      "terra": [
        "tread-taker",
        58
      ],
      "terry": [
        "reset-tenor",
        44
      ],
      "terse": [
        "",
        85
      ],
      "testy": [
        "tenth",
        79
      ],
      "tetra": [
        "tread-taker-terra",
        45
      ],
      "thank": [
        "scant",
        68
      ],
      "theft": [
        "reset-evict",
        42
      ],
      "their": [
        "reset-entry",
        44
      ],
      "theme": [
        "terse",
        75
      ],
      "there": [
        "terse",
        75
      ],
      "these": [
        "terse",
        75
      ],
      "theta": [
        "earth",
        50
      ],
      "thick": [
        "roust-ditch",
        34
      ],
      "thief": [
        "reset-token",
        42
      ],
      "thigh": [
        "roust-ditch",
        34
      ],
      "thine": [
        "terse-twine",
        42
      ],
      "thing": [
        "roust-ditch",
        31
      ],
      "think": [
        "roust-ditch-thing",
        18
      ],
      "third": [
        "roust",
        58
      ],
      "thong": [
        "roust",
        60
      ],
      "thorn": [
        "roust-vitro",
        34
      ],
      "those": [
        "terse",
        75
      ],
      "three": [
        "terse",
        75
      ],
      "threw": [
        "reset-outer-tried",
        27
      ],
      "throb": [
        "roust-vitro-throw",
        21
      ],
      "throw": [
        "roust-vitro",
        34
      ],
      "thrum": [
        "roust",
        60
      ],
      "thumb": [
        "roust",
        60
      ],
      "thump": [
        "tromp",
        66
      ],
      "thyme": [
        "terse-twine",
        42
      ],
      "tiara": [
        "scant",
        72
      ],
      "tibia": [
        "taint",
        71
      ],
      "tidal": [
        "natal-trial",
        49
      ],
      "tided": [
        "reset-token-thief-timed",
        28
      ],
      "tiger": [
        "reset-outer",
        40
      ],
      "tight": [
        "roust-theft",
        41
      ],
      "tilde": [
        "title",
        81
      ],
      "tiled": [
        "islet",
        75
      ],
      "timed": [
        "reset-token-thief",
        38
      ],
      "timer": [
        "reset-outer-tiger",
        28
      ],
      "timid": [
        "roust-ditch",
        34
      ],
      "tinge": [
        "terse-twine",
        42
      ],
      "tinny": [
        "roust-ditch",
        36
      ],
      "tipsy": [
        "tromp",
        66
      ],
      "tired": [
        "reset-outer-tried",
        27
      ],
      "titan": [
        "taint",
        71
      ],
      "titer": [
        "reset-outer-miter-biter",
        15
      ],
      "tithe": [
        "terse-twine",
        42
      ],
      "title": [
        "",
        91
      ],
      "tizzy": [
        "roust-ditch-tinny",
        24
      ],
      "toady": [
        "scant-tiara",
        55
      ],
      "toast": [
        "scant-roast-boast",
        39
      ],
      "today": [
        "taint",
        60
      ],
      "toddy": [
        "roust-notch",
        27
      ],
      "token": [
        "reset",
        56
      ],
      "tonal": [
        "natal",
        78
      ],
      "toned": [
        "reset-token-toney",
        20
      ],
      "toner": [
        "reset-outer-tower",
        33
      ],
      "toney": [
        "reset-token",
        33
      ],
      "tonga": [
        "taint",
        71
      ],
      "tonic": [
        "roust-notch",
        27
      ],
      "tooth": [
        "softy-motto",
        53
      ],
      "topaz": [
        "kaput",
        67
      ],
      "topic": [
        "tromp",
        66
      ],
      "torah": [
        "taint-today",
        43
      ],
      "torch": [
        "roust",
        58
      ],
      "torso": [
        "roust",
        60
      ],
      "torte": [
        "route-forte",
        50
      ],
      "torus": [
        "roust",
        60
      ],
      "total": [
        "natal",
        68
      ],
      "toted": [
        "reset-token-totem",
        29
      ],
      "totem": [
        "reset-token",
        42
      ],
      "touch": [
        "roust",
        58
      ],
      "tough": [
        "roust-touch",
        41
      ],
      "towed": [
        "reset-token-totem-toyed",
        28
      ],
      "towel": [
        "islet-hotel",
        42
      ],
      "tower": [
        "reset-outer",
        45
      ],
      "toxic": [
        "roust-notch",
        27
      ],
      "toxin": [
        "roust-notch",
        27
      ],
      "toyed": [
        "reset-token-totem",
        38
      ],
      "trace": [
        "",
        92
      ],
      "track": [
        "scant",
        78
      ],
      "tract": [
        "scant-chart",
        49
      ],
      "trade": [
        "trace",
        78
      ],
      "trail": [
        "stall",
        62
      ],
      "train": [
        "scant",
        72
      ],
      "trait": [
        "scant-draft",
        40
      ],
      "tramp": [
        "apart",
        75
      ],
      "trans": [
        "scant",
        78
      ],
      "trash": [
        "scant",
        78
      ],
      "trawl": [
        "stall-trail",
        46
      ],
      "tread": [
        "",
        84
      ],
      "treat": [
        "tread",
        74
      ],
      "treed": [
        "reset-enter",
        46
      ],
      "trend": [
        "reset-entry",
        44
      ],
      "tress": [
        "reset-stern",
        44
      ],
      "triad": [
        "taint",
        71
      ],
      "trial": [
        "natal",
        66
      ],
      "tribe": [
        "terse-trice",
        49
      ],
      "trice": [
        "terse",
        66
      ],
      "trick": [
        "roust-third",
        41
      ],
      "tried": [
        "reset-outer",
        39
      ],
      "trike": [
        "terse-trice-tribe",
        36
      ],
      "trill": [
        "guilt",
        57
      ],
      "tripe": [
        "trope",
        65
      ],
      "trite": [
        "route-write",
        46
      ],
      "troll": [
        "guilt-hotly",
        46
      ],
      "tromp": [
        "",
        90
      ],
      "troop": [
        "tromp",
        66
      ],
      "trope": [
        "",
        90
      ],
      "trout": [
        "roust",
        61
      ],
      "trove": [
        "terse-trice",
        56
      ],
      "truce": [
        "terse-trice",
        56
      ],
      "truck": [
        "roust-trunk",
        41
      ],
      "truer": [
        "reset-outer",
        43
      ],
      "truly": [
        "guilt",
        75
      ],
      "trump": [
        "tromp",
        66
      ],
      "trunk": [
        "roust",
        58
      ],
      "truss": [
        "roust",
        60
      ],
      "trust": [
        "roust-crust",
        41
      ],
      "truth": [
        "softy-birth",
        60
      ],
      "tryst": [
        "roust-wrist",
        36
      ],
      "tubal": [
        "natal-trial",
        49
      ],
      "tubby": [
        "roust-butch",
        34
      ],
      "tubed": [
        "reset-token-thief",
        29
      ],
      "tuber": [
        "reset-outer-tuner",
        30
      ],
      "tufty": [
        "softy-nifty",
        50
      ],
      "tulip": [
        "split",
        64
      ],
      "tulle": [
        "title",
        81
      ],
      "tummy": [
        "roust-butch",
        34
      ],
      "tumor": [
        "roust",
        55
      ],
      "tuned": [
        "reset-token",
        39
      ],
      "tuner": [
        "reset-outer",
        43
      ],
      "tunic": [
        "roust-butch",
        34
      ],
      "turbo": [
        "roust-tumor",
        39
      ],
      "tutor": [
        "roust-tumor",
        39
      ],
      "twain": [
        "scant-train",
        55
      ],
      "twang": [
        "scant-thank",
        51
      ],
      "tweak": [
        "tread",
        74
      ],
      "tweed": [
        "reset",
        65
      ],
      "tween": [
        "reset-tweed",
        48
      ],
      "tweet": [
        "reset",
        68
      ],
      "twerk": [
        "reset-entry",
        44
      ],
      "twerp": [
        "crept",
        79
      ],
      "twice": [
        "terse-twine",
        42
      ],
      "twill": [
        "guilt-trill",
        40
      ],
      "twine": [
        "terse",
        59
      ],
      "twirl": [
        "guilt",
        75
      ],
      "twist": [
        "roust",
        57
      ],
      "twixt": [
        "roust-theft",
        41
      ],
      "tying": [
        "roust-ditch",
        34
      ],
      "typed": [
        "crept-setup",
        42
      ],
      "udder": [
        "diner-order-seder",
        27
      ],
      "ulcer": [
        "bleed-flier",
        41
      ],
      "ulnar": [
        "aloha",
        70
      ],
      "ultra": [
        "float",
        74
      ],
      "umami": [
        "shark-guava",
        40
      ],
      "umber": [
        "diner-fever-bower-cyber",
        25
      ],
      "umbra": [
        "manor-rumba",
        42
      ],
      "unarm": [
        "shark-award-ovary",
        27
      ],
      "unbox": [
        "corns-union",
        35
      ],
      "uncap": [
        "carps",
        74
      ],
      "uncle": [
        "bugle",
        61
      ],
      "uncut": [
        "roust-unfit",
        40
      ],
      "under": [
        "diner",
        54
      ],
      "undid": [
        "corns-dingy",
        32
      ],
      "undue": [
        "snore-knife",
        47
      ],
      "unfed": [
        "diner-unwed",
        39
      ],
      "unfit": [
        "roust",
        56
      ],
      "unhip": [
        "croup",
        62
      ],
      "unify": [
        "corns-dingy",
        32
      ],
      "union": [
        "corns",
        47
      ],
      "unite": [
        "route-suite",
        44
      ],
      "unity": [
        "softy-ditty",
        47
      ],
      "unjam": [
        "manor-human",
        41
      ],
      "unlit": [
        "guilt",
        75
      ],
      "unmet": [
        "reset-civet",
        36
      ],
      "unpin": [
        "croup-bumpy-spunk",
        33
      ],
      "unsay": [
        "manor-aging",
        38
      ],
      "unsee": [
        "snore-ensue",
        48
      ],
      "unset": [
        "reset-onset-inset",
        34
      ],
      "untag": [
        "taint-antsy",
        43
      ],
      "untie": [
        "terse",
        68
      ],
      "until": [
        "guilt",
        75
      ],
      "unwed": [
        "diner",
        56
      ],
      "unzip": [
        "croup-unhip",
        45
      ],
      "upend": [
        "speed",
        78
      ],
      "upped": [
        "speed",
        78
      ],
      "upper": [
        "speed",
        78
      ],
      "upset": [
        "crept",
        65
      ],
      "urban": [
        "manor",
        59
      ],
      "urged": [
        "diner-breed",
        41
      ],
      "urine": [
        "snore",
        64
      ],
      "usage": [
        "share-cease",
        55
      ],
      "usher": [
        "diner-fever-bower",
        32
      ],
      "using": [
        "corns-suing",
        32
      ],
      "usual": [
        "solar-nasal",
        50
      ],
      "usurp": [
        "croup",
        70
      ],
      "usury": [
        "corns-brisk",
        36
      ],
      "utile": [
        "title-stile",
        50
      ],
      "utter": [
        "reset-outer",
        43
      ],
      "uvula": [
        "solar-daily",
        43
      ],
      "vague": [
        "raise-cadge",
        43
      ],
      "valet": [
        "metal",
        75
      ],
      "valid": [
        "solar-balmy",
        46
      ],
      "valor": [
        "solar",
        70
      ],
      "value": [
        "angle",
        61
      ],
      "valve": [
        "angle-value",
        52
      ],
      "vampy": [
        "carps-happy",
        48
      ],
      "vaped": [
        "caper-gaped",
        37
      ],
      "vapid": [
        "carps",
        74
      ],
      "vapor": [
        "carps-rapid",
        42
      ],
      "vault": [
        "natal-fault",
        44
      ],
      "vaunt": [
        "taint-haunt-gaunt-jaunt-daunt",
        32
      ],
      "vegan": [
        "amber-sedan",
        41
      ],
      "veiny": [
        "diner-eking",
        37
      ],
      "veldt": [
        "islet",
        75
      ],
      "venal": [
        "regal-decal",
        48
      ],
      "venom": [
        "diner",
        55
      ],
      "venti": [
        "tenth-bento",
        46
      ],
      "venue": [
        "snore-niche",
        41
      ],
      "verge": [
        "snore",
        50
      ],
      "verse": [
        "snore-curse",
        45
      ],
      "verso": [
        "diner-mercy",
        33
      ],
      "verve": [
        "snore-verge",
        38
      ],
      "vexed": [
        "diner-modem-edges-hexed",
        26
      ],
      "vicar": [
        "manor-cigar",
        38
      ],
      "video": [
        "diner",
        53
      ],
      "vigil": [
        "could-silky",
        35
      ],
      "vigor": [
        "corns-vroom",
        33
      ],
      "villa": [
        "solar-balmy",
        40
      ],
      "vined": [
        "diner-mined-fined-wined",
        33
      ],
      "vinyl": [
        "could-silky",
        35
      ],
      "viola": [
        "solar",
        66
      ],
      "viper": [
        "speed-ripen-wiper",
        31
      ],
      "viral": [
        "solar-mural",
        53
      ],
      "virus": [
        "corns",
        50
      ],
      "visit": [
        "roust-shift",
        32
      ],
      "visor": [
        "corns-sword",
        36
      ],
      "vista": [
        "tarts",
        79
      ],
      "vital": [
        "natal-total",
        52
      ],
      "vitro": [
        "roust",
        45
      ],
      "vivid": [
        "corns-fudgy",
        26
      ],
      "vixen": [
        "diner-given",
        41
      ],
      "vocal": [
        "solar-local-focal",
        39
      ],
      "vodka": [
        "manor-audio",
        37
      ],
      "vogue": [
        "snore",
        54
      ],
      "voice": [
        "snore-vogue",
        42
      ],
      "voila": [
        "solar",
        67
      ],
      "voile": [
        "bugle-while-smile-exile",
        31
      ],
      "vomit": [
        "roust-joint",
        43
      ],
      "voted": [
        "reset-token",
        39
      ],
      "voter": [
        "reset-outer",
        43
      ],
      "vouch": [
        "corns-hooch",
        38
      ],
      "vowed": [
        "diner-modem-wooed-sowed-cowed",
        33
      ],
      "vowel": [
        "lever",
        72
      ],
      "vroom": [
        "corns",
        41
      ],
      "vying": [
        "corns-dying",
        39
      ],
      "wacko": [
        "manor-cacao",
        40
      ],
      "wacky": [
        "manor-daubs",
        32
      ],
      "waded": [
        "amber-naked-jaded-faded",
        34
      ],
      "wader": [
        "amber-rager-safer-waver",
        26
      ],
      "wafer": [
        "amber-rager-safer",
        37
      ],
      "waged": [
        "amber-naked-jaded-caged",
        46
      ],
      "wager": [
        "amber-rager-eager",
        37
      ],
      "wagon": [
        "manor-bacon",
        41
      ],
      "waist": [
        "taint",
        71
      ],
      "waive": [
        "raise-naive",
        53
      ],
      "waked": [
        "amber-naked-caked-faked",
        27
      ],
      "waken": [
        "amber-naked-oaken",
        35
      ],
      "waltz": [
        "salty",
        66
      ],
      "waned": [
        "amber-naked-caned",
        26
      ],
      "wanly": [
        "solar-daily-manly",
        23
      ],
      "warty": [
        "tarts",
        79
      ],
      "waste": [
        "taste",
        65
      ],
      "watch": [
        "taint-maths-batch",
        41
      ],
      "water": [
        "tread-earth-cater",
        39
      ],
      "waved": [
        "amber-naked-jaded-caged-sawed",
        31
      ],
      "waver": [
        "amber-rager-safer",
        36
      ],
      "waxed": [
        "amber-naked-jaded-caged-sawed",
        31
      ],
      "waxen": [
        "amber-naked-haven",
        29
      ],
      "weary": [
        "heard",
        60
      ],
      "weave": [
        "share-agave",
        57
      ],
      "wedge": [
        "snore-guide-hedge",
        22
      ],
      "weedy": [
        "diner-seedy",
        41
      ],
      "weepy": [
        "speed",
        78
      ],
      "weigh": [
        "diner",
        55
      ],
      "weird": [
        "diner-redid",
        39
      ],
      "whack": [
        "shark",
        70
      ],
      "whale": [
        "scale",
        75
      ],
      "wharf": [
        "shark-charm",
        52
      ],
      "wheat": [
        "tread-cheat",
        53
      ],
      "wheel": [
        "lever",
        68
      ],
      "whelk": [
        "lever-swell-wield",
        36
      ],
      "whelp": [
        "expel",
        69
      ],
      "where": [
        "snore",
        64
      ],
      "which": [
        "corns-mucky",
        34
      ],
      "whiff": [
        "corns-fudgy",
        26
      ],
      "while": [
        "bugle",
        60
      ],
      "whine": [
        "snore-niche",
        41
      ],
      "whiny": [
        "corns-dying",
        39
      ],
      "whirl": [
        "could-silky",
        35
      ],
      "whirr": [
        "corns-grimy-quirk",
        18
      ],
      "whisk": [
        "corns-smush",
        28
      ],
      "whist": [
        "roust-twist",
        40
      ],
      "white": [
        "route",
        70
      ],
      "whizz": [
        "corns-fudgy",
        26
      ],
      "whole": [
        "bugle-while",
        52
      ],
      "whomp": [
        "croup-swoop",
        46
      ],
      "whoop": [
        "croup-swoop",
        46
      ],
      "whorl": [
        "could-lingo",
        38
      ],
      "whose": [
        "snore-chose",
        54
      ],
      "widen": [
        "diner",
        53
      ],
      "wider": [
        "diner",
        53
      ],
      "widow": [
        "corns-gizmo",
        29
      ],
      "width": [
        "softy-birth-ninth",
        37
      ],
      "wield": [
        "lever-swell",
        49
      ],
      "wight": [
        "roust-theft-night-might",
        20
      ],
      "wiled": [
        "lever-yodel-filed",
        31
      ],
      "willy": [
        "could-skill-hilly-filly-billy",
        24
      ],
      "wimpy": [
        "croup-nymph",
        42
      ],
      "wince": [
        "snore-niche",
        36
      ],
      "winch": [
        "corns-bunch",
        40
      ],
      "windy": [
        "corns-dingy",
        32
      ],
      "wined": [
        "diner-mined-fined",
        43
      ],
      "winey": [
        "diner-sinew",
        41
      ],
      "wiped": [
        "speed-moped-biped",
        37
      ],
      "wiper": [
        "speed-ripen",
        43
      ],
      "wired": [
        "diner-sired-hired-mired-fired",
        34
      ],
      "wiser": [
        "diner-riser",
        48
      ],
      "wispy": [
        "croup-nymph-zippy",
        29
      ],
      "witch": [
        "roust-ditch",
        31
      ],
      "witty": [
        "softy-ditty",
        42
      ],
      "woken": [
        "diner-seven-women",
        26
      ],
      "woman": [
        "manor-among",
        45
      ],
      "women": [
        "diner-seven",
        38
      ],
      "wonky": [
        "corns-gonzo",
        38
      ],
      "woody": [
        "corns-goody-moody",
        27
      ],
      "wooed": [
        "diner-modem",
        43
      ],
      "wooer": [
        "diner-fever-bower",
        31
      ],
      "wooly": [
        "could-jolly-nobly",
        33
      ],
      "woozy": [
        "corns-goody-boozy",
        23
      ],
      "wordy": [
        "corns-wormy-worry",
        25
      ],
      "world": [
        "could",
        64
      ],
      "wormy": [
        "corns",
        50
      ],
      "worry": [
        "corns-wormy",
        37
      ],
      "worse": [
        "snore-horse",
        50
      ],
      "worst": [
        "roust",
        60
      ],
      "worth": [
        "softy-motto-north",
        31
      ],
      "would": [
        "could",
        62
      ],
      "wound": [
        "corns-downy",
        37
      ],
      "woven": [
        "diner-seven",
        44
      ],
      "wowed": [
        "diner-modem-wooed",
        40
      ],
      "wrack": [
        "shark-frack-crack",
        31
      ],
      "wrath": [
        "",
        86
      ],
      "wreak": [
        "amber",
        58
      ],
      "wreck": [
        "diner-mercy",
        35
      ],
      "wrest": [
        "reset-crest",
        47
      ],
      "wring": [
        "corns-bring",
        31
      ],
      "wrist": [
        "roust",
        53
      ],
      "write": [
        "route",
        62
      ],
      "wrong": [
        "corns-irony",
        43
      ],
      "wrote": [
        "route",
        82
      ],
      "wrung": [
        "corns-bring",
        31
      ],
      "wryly": [
        "could-skill",
        39
      ],
      "wurst": [
        "roust-burst",
        45
      ],
      "xenon": [
        "diner-venom",
        39
      ],
      "xerox": [
        "diner-mercy-verso",
        20
      ],
      "yacht": [
        "taint-carat",
        48
      ],
      "yahoo": [
        "manor",
        52
      ],
      "yappy": [
        "carps-happy-nappy",
        34
      ],
      "yearn": [
        "heard-weary",
        44
      ],
      "yeast": [
        "teary",
        80
      ],
      "yield": [
        "lever-swell",
        39
      ],
      "yodel": [
        "lever",
        61
      ],
      "yoked": [
        "diner-modem-wooed",
        37
      ],
      "yokel": [
        "lever-yodel",
        48
      ],
      "young": [
        "corns-downy",
        37
      ],
      "youth": [
        "softy",
        74
      ],
      "yucca": [
        "manor-squab",
        29
      ],
      "yucky": [
        "corns-mucky",
        33
      ],
      "yummy": [
        "corns-fudgy-mummy",
        20
      ],
      "zebra": [
        "amber",
        68
      ],
      "zesty": [
        "tenth-deity",
        40
      ],
      "zilch": [
        "could",
        61
      ],
      "zippy": [
        "croup-nymph",
        41
      ],
      "zonal": [
        "solar-local-modal",
        31
      ],
      "zoned": [
        "diner-coned-honed-boned",
        31
      ]
    }
  }
}
