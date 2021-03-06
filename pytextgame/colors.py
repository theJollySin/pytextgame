# -- coding: utf-8 --
'''color definitions and functions'''


def color_int2tuple(val):
    '''convert a 9-digit integer into a RGB color tuple'''
    r = val >> 16
    g = (val - (r << 16)) >> 8
    b = val - (r << 16) - (g << 8)

    return (r, g, b)


def color_tuple2int(tup):
    '''convert an RGB color tuple into an integer'''
    return (tup[0] << 16) + (tup[1] << 8) + tup[2]


def color_lighten_int(num, percent=25):
    '''Lighten a color (integer) by a certain percentage'''
    fraction = percent / 100.0
    r, g, b = color_int2tuple(num)
    r += int((255 - r) * fraction)
    g += int((255 - g) * fraction)
    b += int((255 - b) * fraction)

    return color_tuple2int((r, g, b))


def color_lighten_tuple(tup, percent=25):
    '''Lighten a color (RGB tuple) by a certain percentage'''
    fraction = percent / 100.0
    r, g, b = tup
    r += int((255 - r) * fraction)
    g += int((255 - g) * fraction)
    b += int((255 - b) * fraction)

    return (r, g, b)


def color_darken_int(num, percent=25):
    '''Darken a color (integer) by a certain percentage'''
    fraction = percent / 100.0
    r, g, b = color_int2tuple(num)
    r -= int(r * fraction)
    g -= int(g * fraction)
    b -= int(b * fraction)

    return color_tuple2int((r, g, b))


def color_darken_tuple(tup, percent=25):
    '''Darken a color (RGB tuple) by a certain percentage'''
    fraction = percent / 100.0
    r, g, b = tup
    r -= int(r * fraction)
    g -= int(g * fraction)
    b -= int(b * fraction)

    return (r, g, b)


BLACK   = 0
BLUE    = 255
BRICK   = 10249759
BROWN   = 10824234
GOLD    = 16766720
GRAY    = 8421504
GREEN   = 32768
GREY    = 8421504
MAGENTA = 16711935
PINK    = 16761035
PURPLE  = 8388736
RED     = 16711680
TEAL    = 32896
WHITE   = 16777215
YELLOW  = 16776960


COLORS = {'ALICE_BLUE': 15792383,
          'ANTIQUE_WHITE': 16444375,
          'AQUA': 65535,
          'AQUAMARINE': 8388564,
          'AZURE': 15794175,
          'BANANA': 14929751,
          'BEIGE': 16119260,
          'BISQUE': 16770244,
          'BLACK': 0,
          'BLANCHED_ALMOND': 16772045,
          'BLUE': 255,
          'BLUE_VIOLET': 9055202,
          'BRICK': 10249759,
          'BROWN': 10824234,
          'BURLYWOOD': 14596231,
          'BURNT_SIENNA': 9057807,
          'BURNT_UMBER': 9057060,
          'CADET_BLUE': 6266528,
          'CADMIUM_ORANGE': 16736515,
          'CADMIUM_YELLOW': 16750866,
          'CARROT': 15569185,
          'CHARTREUSE': 8388352,
          'CHOCOLATE': 13789470,
          'COBALT': 4020651,
          'COBALT_GREEN': 4034880,
          'COLD_GREY': 8424071,
          'CORAL': 16744272,
          'CORNFLOWER_BLUE': 6591981,
          'CORNSILK': 16775388,
          'CRIMSON': 14423100,
          'CYAN': 65535,
          'DARK_GOLDENROD': 12092939,
          'DARK_GRAY': 11119017,
          'DARK_GREEN': 25600,
          'DARK_KHAKI': 12433259,
          'DARK_OLIVE_GREEN': 5597999,
          'DARK_ORANGE': 16747520,
          'DARK_ORCHID': 10040012,
          'DARK_RED': 9109504,
          'DARK_SALMON': 15308410,
          'DARK_SEAGREEN': 9419919,
          'DARK_SLATE_BLUE': 4734347,
          'DARK_SLATE_GRAY': 3100495,
          'DARK_TURQUOISE': 52945,
          'DARK_VIOLET': 9699539,
          'DEEP_PINK': 16716947,
          'DEEP_SKY_BLUE': 49151,
          'DIM_GRAY': 6908265,
          'DODGER_BLUE': 2003199,
          'EGGSHELL': 16574153,
          'EMERALD_GREEN': 51543,
          'FIREBRICK': 11674146,
          'FLORAL_WHITE': 16775920,
          'FOREST_GREEN': 2263842,
          'FUCHSIA': 16711935,
          'GAINSBORO': 14474460,
          'GHOST_WHITE': 16316671,
          'GOLD': 16766720,
          'GOLDENROD': 14329120,
          'GRAY': 8421504,
          'GREY': 8421504,
          'GREEN': 32768,
          'GREEN_YELLOW': 11403055,
          'HONEYDEW': 15794160,
          'HOT_PINK': 16738740,
          'INDIAN_RED': 13458524,
          'INDIGO': 4915330,
          'IVORY': 16777200,
          'IVORY_BLACK': 2696225,
          'KHAKI': 15787660,
          'LAVENDER': 15132410,
          'LAVENDER_BLUSH': 16773365,
          'LAWN_GREEN': 8190976,
          'LEMON_CHIFFON': 16775885,
          'LIGHT_BLUE': 11393254,
          'LIGHT_CORAL': 15761536,
          'LIGHT_CYAN': 14745599,
          'LIGHT_GOLDENROD': 16448210,
          'LIGHT_GREEN': 9498256,
          'LIGHT_GREY': 13882323,
          'LIGHT_PINK': 16758465,
          'LIGHT_SALMON': 16752762,
          'LIGHT_SEAGREEN': 2142890,
          'LIGHT_SKYBLUE': 8900346,
          'LIGHT_SLATEBLUE': 8679679,
          'LIGHT_SLATEGRAY': 7833753,
          'LIGHT_STEELBLUE': 11584734,
          'LIGHT_YELLOW': 16777184,
          'LIME': 65280,
          'LIME_GREEN': 3329330,
          'LINEN': 16445670,
          'MAGENTA': 16711935,
          'MANGANESE_BLUE': 239774,
          'MAROON': 9116770,
          'MEDIUM_AQUAMARINE': 6737322,
          'MEDIUM_ORCHID': 12211667,
          'MEDIUM_PURPLE': 9662683,
          'MEDIUM_SEAGREEN': 3978097,
          'MEDIUM_SLATE_BLUE': 8087790,
          'MEDIUM_SPRING_GREEN': 64154,
          'MEDIUM_TURQUOISE': 4772300,
          'MEDIUM_VIOLETRED': 13047173,
          'MELON': 14919785,
          'MIDNIGHT_BLUE': 1644912,
          'MINT': 12451017,
          'MINT_CREAM': 16121850,
          'MISTY_ROSE': 16770273,
          'MOCCASIN': 16770229,
          'NAVAJO_WHITE': 16768685,
          'NAVY': 128,
          'OLD_LACE': 16643558,
          'OLIVE': 8421376,
          'OLIVE_DRAB': 7048739,
          'ORANGE': 16744448,
          'ORANGE_RED': 16729344,
          'ORCHID': 14315734,
          'PALE_GOLDENROD': 15657130,
          'PALE_GREEN': 10025880,
          'PALE_TURQUOISE': 11464430,
          'PALE_VIOLET_RED': 14381203,
          'PAPAYA_WHIP': 16773077,
          'PEACHPUFF': 16767673,
          'PEACOCK': 3383753,
          'PINK': 16761035,
          'PLUM': 14524637,
          'POWDER_BLUE': 11591910,
          'PURPLE': 8388736,
          'RASPBERRY': 8857175,
          'RAW_SIENNA': 13066516,
          'RED': 16711680,
          'ROSY_BROWN': 12357519,
          'ROYAL_BLUE': 4286945,
          'SADDLE_BROWN': 9127187,
          'SALMON': 16416882,
          'SANDY_BROWN': 16032864,
          'SAP_GREEN': 3178516,
          'SEAGREEN': 3050327,
          'SEASHELL': 16774638,
          'SEPIA': 6170130,
          'SIENNA': 10506797,
          'SILVER': 12632256,
          'SKY_BLUE': 8900331,
          'SLATE_BLUE': 6970061,
          'SLATE_GRAY': 7372944,
          'SNOW': 16775930,
          'SPRING_GREEN': 65407,
          'STEEL_BLUE': 4620980,
          'TAN': 13808780,
          'TEAL': 32896,
          'THISTLE': 14204888,
          'TOMATO': 16737095,
          'TURQUOISE': 4251856,
          'TURQUOISE_BLUE': 51084,
          'VIOLET': 15631086,
          'VIOLET_RED': 13639824,
          'WARM_GREY': 8421481,
          'WHEAT': 16113331,
          'WHITE': 16777215,
          'WHITE_SMOKE': 16119285,
          'YELLOW': 16776960,
          'YELLOW_GREEN': 10145074}
