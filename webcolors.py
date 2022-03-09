"""
Utility functions for working with the color names and color value
formats defined by the HTML and CSS specifications for use in
documents on the Web.

See documentation (in docs/ directory of source distribution) for
details of the supported formats, conventions and conversions.

"""

import re
import string
from typing import NamedTuple, Tuple, Union


__version__ = "1.11.1"


def _reversedict(d: dict) -> dict:
    """
    Internal helper for generating reverse mappings; given a
    dictionary, returns a new dictionary with keys and values swapped.

    """
    return {value: key for key, value in d.items()}


HEX_COLOR_RE = re.compile(r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$")

HTML4 = "html4"
CSS2 = "css2"
CSS21 = "css21"
CSS3 = "css3"

SUPPORTED_SPECIFICATIONS = (HTML4, CSS2, CSS21, CSS3)

SPECIFICATION_ERROR_TEMPLATE = "{{spec}} is not a supported specification for color name lookups; \
supported specifications are: {supported}.".format(
    supported=",".join(SUPPORTED_SPECIFICATIONS)
)

IntegerRGB = NamedTuple("IntegerRGB", [("red", int), ("green", int), ("blue", int)])
PercentRGB = NamedTuple("PercentRGB", [("red", str), ("green", str), ("blue", str)])
HTML5SimpleColor = NamedTuple(
    "HTML5SimpleColor", [("red", int), ("green", int), ("blue", int)]
)

IntTuple = Union[IntegerRGB, HTML5SimpleColor, Tuple[int, int, int]]
PercentTuple = Union[PercentRGB, Tuple[str, str, str]]


# Mappings of color names to normalized hexadecimal color values.
#################################################################

# The HTML 4 named colors.
#
# The canonical source for these color definitions is the HTML 4
# specification:
#
# http://www.w3.org/TR/html401/types.html#h-6.5
#
# The file tests/definitions.py in the source distribution of this
# module downloads a copy of the HTML 4 standard and parses out the
# color names to ensure the values below are correct.
HTML4_NAMES_TO_HEX = {
    "aqua": "#00ffff",
    "black": "#000000",
    "blue": "#0000ff",
    "fuchsia": "#ff00ff",
    "green": "#008000",
    "gray": "#808080",
    "lime": "#00ff00",
    "maroon": "#800000",
    "navy": "#000080",
    "olive": "#808000",
    "purple": "#800080",
    "red": "#ff0000",
    "silver": "#c0c0c0",
    "teal": "#008080",
    "white": "#ffffff",
    "yellow": "#ffff00",
}

# CSS 2 used the same list as HTML 4.
CSS2_NAMES_TO_HEX = HTML4_NAMES_TO_HEX

# CSS 2.1 added orange.
CSS21_NAMES_TO_HEX = {"orange": "#ffa500", **HTML4_NAMES_TO_HEX}

# The CSS 3/SVG named colors.
#
# The canonical source for these color definitions is the SVG
# specification's color list (which was adopted as CSS 3's color
# definition):
#
# http://www.w3.org/TR/SVG11/types.html#ColorKeywords
#
# CSS 3 also provides definitions of these colors:
#
# http://www.w3.org/TR/css3-color/#svg-color
#
# SVG provides the definitions as RGB triplets. CSS 3 provides them
# both as RGB triplets and as hexadecimal. Since hex values are more
# common in real-world HTML and CSS, the mapping below is to hex
# values instead. The file tests/definitions.py in the source
# distribution of this module downloads a copy of the CSS 3 color
# module and parses out the color names to ensure the values below are
# correct.
CSS3_NAMES_TO_HEX = {
"أليس الأزرق": "#f0f8ff",
    "أبيض عتيق": "#faebd7",
    "أكوا": "#00ffff",
    "زبرجد": "#7fffd4",
    "أزور": "#f0ffff",
    "بيج": "#f5f5dc",
    "حساء دسم": "#ffe4c4",
    "أسود": "#000000",
    "لوز مقشر": "#ffebcd",
    "أزرق": "#0000ff",
    "البنفسجي الأزرق": "#8a2be2",
    "بني": "#a52a2a",
    "بيرلي وود": "#deb887",
    "cadet blue": "#5f9ea0",
    "الرسم البياني": "#7fff00",
    "شوكولاتة": "#d2691e",
    "كورال": "#ff7f50",
    "ردة الذرة الزرقاء": "#6495ed",
    "حرير الذرة": "#fff8dc",
    "قرمزي": "#dc143c",
    "سماوي": "#00ffff",
    "أزرق غامق": "#00008b",
    "سماوي غامق": "#008b8b",
    "ذهبي غامق": "#b8860b",
    "رمادي غامق": "#a9a9a9",
    "رمادي غامق": "#a9a9a9",
    "أخضر غامق": "#006400",
    "كاكي غامق": "#bdb76b",
    "أرجواني غامق": "#8b008b",
    "زيتون أخضر غامق": "#556b2f",
    "برتقالي غامق": "#ff8c00",
    "دارك أوركيد": "#9932cc",
    "أحمر غامق": "#8b0000",
    "سمك السلمون الداكن": "#e9967a",
    "أخضر البحر الداكن": "#8fbc8f",
    "ازرق غامق": "#483d8b",
    "الرمادي الداكن": "#2f4f4f",
    "الرمادي الداكن": "#2f4f4f",
    "الفيروز الداكن": "#00ced1",
    "بنفسجي غامق": "#9400d3",
    "وردي عميق": "#ff1493",
    "ديب سكاي بلو": "#00bfff",
    "رمادي خافت": "#696969",
    "رمادي خافت": "#696969",
    "المراوغ الأزرق": "#1e90ff",
    "طوب النار": "#b22222",
    "أبيض زهري": "#fffaf0",
    "الغابة الخضراء": "#228b22" ,
    "فوشيا": "#ff00ff",
    "ريكسبورو": "#dcdcdc",
    "شبح الأبيض": "#f8f8ff",
    "ذهبي": "#ffd700",
    "ذهبي": "#daa520",
    "الرمادي": "#808080",
    "الرمادي": "#808080",
    "أخضر": "#008000",
    "أصفر أخضر": "#adff2f",
    "ندى العسل": "#f0fff0",
    "وردي ساخن": "#ff69b4",
    "الأحمر الهندي": "#cd5c5c",
    "نيلي": "#4b0082",
    "عاج": "#fffff0",
    "كاكي": "#f0e68c",
    "الخزامى": "#e6e6fa",
    "لافندر بلاش": "#fff0f5",
    "لون أخضر": "#7cfc00",
    "ليمون": "#fffacd",
    "أزرق فاتح": "#add8e6",
    "مرجاني فاتح": "#f08080",
    "سماوي فاتح": "#e0ffff",
    "أصفر ذهبي فاتح": "#fafad2",
    "رمادي فاتح": "#d3d3d3",
    "رمادي فاتح": "#d3d3d3",
    "أخضر فاتح": "#90ee90",
    "وردي فاتح": "#ffb6c1",
    "سمك السلمون الخفيف": "#ffa07a",
    "أخضر بحري فاتح": "#20b2aa" ,
    "أزرق فاتح": "#87cefa" ,
    "رمادي أردوازي فاتح": "#778899",
    "رمادي أردوازي فاتح": "#778899",
    "أزرق فاتح": "#b0c4de",
    "أصفر فاتح": "#ffffe0",
    "الجير": "#00ff00",
    "أخضر ليموني": "#32cd32",
    "كتان": "#faf0e6",
    "أرجواني": "#ff00ff",
    "زبرجد متوسط": "#66cdaa",
    "أزرق متوسط": "#0000cd",
    "الأوركيد المتوسطة": "#ba55d3",
    "أرجواني متوسط": "#9370db",
    "أخضر البحر المتوسط": "#3cb371" ,
    "أزرق أردوازي متوسط": "#7b68ee",
    "أخضر ربيعي متوسط": "#00fa9a" ,
    "تركواز متوسط": "#48d1cc",
    "أحمر بنفسجي متوسط": "#c71585",
    "منتصف الليل الأزرق": "#191970",
    "كريم النعناع": "#f5fffa",
    "وردة ضبابية": "#ffe4e1",
    "موكاسين": "#ffe4b5",
    "أبيض": "#ffdead",
    "البحرية": "#000080",
    "الدانتيل القديم": "#fdf5e6",
    "زيتوني": "#808000",
    "زيتون باهت": "#6b8e23",
    "برتقالي": "#ffa500",
    "أحمر برتقالي": "#ff4500",
    "الأوركيد": "#da70d6",
    "ذهبي شاحب": "#eee8aa",
    "أخضر باهت": "#98fb98",
    "الفيروز الباهت": "#afeeee",
    "بنفسجي باهت": "#db7093",
    "باباياويب": "#ffefd5",
    "خوخ": "#ffdab9",
    "بيرو": "#cd853f",
    "وردي": "#ffc0cb",
    "البرقوق": "#dda0dd",
    "مسحوق أزرق": "#b0e0e6",
    "أرجواني": "#800080",
    "أحمر": "#ff0000",
    "وردية اللون": "#bc8f8f",
    "رويال بلو": "#4169e1",
    "سرج بني": "#8b4513",
    "سمك السلمون": "#fa8072",
    "ساندي براون": "#f4a460",
    "البحر الأخضر": "#2e8b57",
    "قذيفة البحر": "#fff5ee",
    "سيينا": "#a0522d",
    "فضي": "#c0c0c0",
    "السماء الزرقاء": "#87ceeb" ,
    "أزرق أردوازي": "#6a5acd",
    "رمادي أردوازي": "#708090",
    "رمادي أردوازي": "#708090",
    "الثلج": "#fffafa",
    "الربيع الأخضر": "#00ff7f",
    "أزرق صلب": "#4682b4",
    "بني": "#d2b48c",
    "البط البري": "#008080",
    "شوك": "#d8bfd8",
    "طماطم": "#ff6347",
    "تركواز": "#40e0d0",
    "البنفسجي": "#ee82ee",
    "قمح": "#f5deb3",
    "أبيض": "#ffffff",
    "دخان أبيض": "#f5f5f5",
    "أصفر": "#ffff00",
    "أصفر أخضر": "#9acd32",
}


# Mappings of normalized hexadecimal color values to color names.
#################################################################

HTML4_HEX_TO_NAMES = _reversedict(HTML4_NAMES_TO_HEX)

CSS2_HEX_TO_NAMES = HTML4_HEX_TO_NAMES

CSS21_HEX_TO_NAMES = _reversedict(CSS21_NAMES_TO_HEX)

CSS3_HEX_TO_NAMES = _reversedict(CSS3_NAMES_TO_HEX)

# CSS3 defines both 'gray' and 'grey', as well as defining either
# variant for other related colors like 'darkgray'/'darkgrey'. For a
# 'forward' lookup from name to hex, this is straightforward, but a
# 'reverse' lookup from hex to name requires picking one spelling.
#
# The way in which _reversedict() generates the reverse mappings will
# pick a spelling based on the ordering of dictionary keys, which
# varies according to the version and implementation of Python in use,
# and in some Python versions is explicitly not to be relied on for
# consistency. So here we manually pick a single spelling that will
# consistently be returned. Since 'gray' was the only spelling
# supported in HTML 4, CSS1, and CSS2, 'gray' and its varients are
# chosen.
CSS3_HEX_TO_NAMES["#a9a9a9"] = "darkgray"
CSS3_HEX_TO_NAMES["#2f4f4f"] = "darkslategray"
CSS3_HEX_TO_NAMES["#696969"] = "dimgray"
CSS3_HEX_TO_NAMES["#808080"] = "gray"
CSS3_HEX_TO_NAMES["#d3d3d3"] = "lightgray"
CSS3_HEX_TO_NAMES["#778899"] = "lightslategray"
CSS3_HEX_TO_NAMES["#708090"] = "slategray"


# Normalization functions.
#################################################################


def normalize_hex(hex_value: str) -> str:
    """
    Normalize a hexadecimal color value to 6 digits, lowercase.

    """
    match = HEX_COLOR_RE.match(hex_value)
    if match is None:
        raise ValueError(
            "'{}' is not a valid hexadecimal color value.".format(hex_value)
        )
    hex_digits = match.group(1)
    if len(hex_digits) == 3:
        hex_digits = "".join(2 * s for s in hex_digits)
    return "#{}".format(hex_digits.lower())


def _normalize_integer_rgb(value: int) -> int:
    """
    Internal normalization function for clipping integer values into
    the permitted range (0-255, inclusive).

    """
    return 0 if value < 0 else 255 if value > 255 else value


def normalize_integer_triplet(rgb_triplet: IntTuple) -> IntegerRGB:
    """
    Normalize an integer ``rgb()`` triplet so that all values are
    within the range 0-255 inclusive.

    """
    return IntegerRGB._make(_normalize_integer_rgb(value) for value in rgb_triplet)


def _normalize_percent_rgb(value: str) -> str:
    """
    Internal normalization function for clipping percent values into
    the permitted range (0%-100%, inclusive).

    """
    value = value.split("%")[0]
    percent = float(value) if "." in value else int(value)

    return "0%" if percent < 0 else "100%" if percent > 100 else "{}%".format(percent)


def normalize_percent_triplet(rgb_triplet: PercentTuple) -> PercentRGB:
    """
    Normalize a percentage ``rgb()`` triplet so that all values are
    within the range 0%-100% inclusive.

    """
    return PercentRGB._make(_normalize_percent_rgb(value) for value in rgb_triplet)


# Conversions from color names to various formats.
#################################################################


def name_to_hex(name: str, spec: str = CSS3) -> str:
    """
    Convert a color name to a normalized hexadecimal color value.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    When no color of that name exists in the given specification,
    ``ValueError`` is raised.

    """
    if spec not in SUPPORTED_SPECIFICATIONS:
        raise ValueError(SPECIFICATION_ERROR_TEMPLATE.format(spec=spec))
    normalized = name.lower()
    hex_value = {
        CSS2: CSS2_NAMES_TO_HEX,
        CSS21: CSS21_NAMES_TO_HEX,
        CSS3: CSS3_NAMES_TO_HEX,
        HTML4: HTML4_NAMES_TO_HEX,
    }[spec].get(normalized)
    if hex_value is None:
        raise ValueError(
            "'{name}' is not defined as a named color in {spec}".format(
                name=name, spec=spec
            )
        )
    return hex_value


def name_to_rgb(name: str, spec: str = CSS3) -> IntegerRGB:
    """
    Convert a color name to a 3-tuple of integers suitable for use in
    an ``rgb()`` triplet specifying that color.

    """
    return hex_to_rgb(name_to_hex(name, spec=spec))


def name_to_rgb_percent(name: str, spec: str = CSS3) -> PercentRGB:
    """
    Convert a color name to a 3-tuple of percentages suitable for use
    in an ``rgb()`` triplet specifying that color.

    """
    return rgb_to_rgb_percent(name_to_rgb(name, spec=spec))


# Conversions from hexadecimal color values to various formats.
#################################################################


def hex_to_name(hex_value: str, spec: str = CSS3) -> str:
    """
    Convert a hexadecimal color value to its corresponding normalized
    color name, if any such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    When no color name for the value is found in the given
    specification, ``ValueError`` is raised.

    """
    if spec not in SUPPORTED_SPECIFICATIONS:
        raise ValueError(SPECIFICATION_ERROR_TEMPLATE.format(spec=spec))
    normalized = normalize_hex(hex_value)
    name = {
        CSS2: CSS2_HEX_TO_NAMES,
        CSS21: CSS21_HEX_TO_NAMES,
        CSS3: CSS3_HEX_TO_NAMES,
        HTML4: HTML4_HEX_TO_NAMES,
    }[spec].get(normalized)
    if name is None:
        raise ValueError("'{}' has no defined color name in {}".format(hex_value, spec))
    return name


def hex_to_rgb(hex_value: str) -> IntegerRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of integers
    suitable for use in an ``rgb()`` triplet specifying that color.

    """
    int_value = int(normalize_hex(hex_value)[1:], 16)
    return IntegerRGB(int_value >> 16, int_value >> 8 & 0xFF, int_value & 0xFF)


def hex_to_rgb_percent(hex_value: str) -> PercentRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of percentages
    suitable for use in an ``rgb()`` triplet representing that color.

    """
    return rgb_to_rgb_percent(hex_to_rgb(hex_value))


# Conversions from  integer rgb() triplets to various formats.
#################################################################


def rgb_to_name(rgb_triplet: IntTuple, spec: str = CSS3) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    If there is no matching name, ``ValueError`` is raised.

    """
    return hex_to_name(rgb_to_hex(normalize_integer_triplet(rgb_triplet)), spec=spec)


def rgb_to_hex(rgb_triplet: IntTuple) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal value for that color.

    """
    return "#{:02x}{:02x}{:02x}".format(*normalize_integer_triplet(rgb_triplet))


def rgb_to_rgb_percent(rgb_triplet: IntTuple) -> PercentRGB:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of percentages suitable for use in
    representing that color.

    This function makes some trade-offs in terms of the accuracy of
    the final representation; for some common integer values,
    special-case logic is used to ensure a precise result (e.g.,
    integer 128 will always convert to '50%', integer 32 will always
    convert to '12.5%'), but for all other values a standard Python
    ``float`` is used and rounded to two decimal places, which may
    result in a loss of precision for some values.

    """
    # In order to maintain precision for common values,
    # special-case them.
    specials = {
        255: "100%",
        128: "50%",
        64: "25%",
        32: "12.5%",
        16: "6.25%",
        0: "0%",
    }
    return PercentRGB._make(
        specials.get(d, "{:.02f}%".format(d / 255.0 * 100))
        for d in normalize_integer_triplet(rgb_triplet)
    )


# Conversions from percentage rgb() triplets to various formats.
#################################################################


def rgb_percent_to_name(rgb_percent_triplet: PercentTuple, spec: str = CSS3) -> str:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    If there is no matching name, ``ValueError`` is raised.

    """
    return rgb_to_name(
        rgb_percent_to_rgb(normalize_percent_triplet(rgb_percent_triplet)), spec=spec
    )


def rgb_percent_to_hex(rgb_percent_triplet: PercentTuple) -> str:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal color value for that
    color.

    """
    return rgb_to_hex(
        rgb_percent_to_rgb(normalize_percent_triplet(rgb_percent_triplet))
    )


def _percent_to_integer(percent: str) -> int:
    """
    Internal helper for converting a percentage value to an integer
    between 0 and 255 inclusive.

    """
    return int(round(float(percent.split("%")[0]) / 100 * 255))


def rgb_percent_to_rgb(rgb_percent_triplet: PercentTuple) -> IntegerRGB:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of integers suitable for use in
    representing that color.

    Some precision may be lost in this conversion. See the note
    regarding precision for ``rgb_to_rgb_percent()`` for details.

    """
    return IntegerRGB._make(
        map(_percent_to_integer, normalize_percent_triplet(rgb_percent_triplet))
    )


# HTML5 color algorithms.
#################################################################

# These functions are written in a way that may seem strange to
# developers familiar with Python, because they do not use the most
# efficient or idiomatic way of accomplishing their tasks. This is
# because, for compliance, these functions are written as literal
# translations into Python of the algorithms in HTML5.
#
# For ease of understanding, the relevant steps of the algorithm from
# the standard are included as comments interspersed in the
# implementation.


def html5_parse_simple_color(input: str) -> HTML5SimpleColor:
    """
    Apply the simple color parsing algorithm from section 2.4.6 of
    HTML5.

    """
    # 1. Let input be the string being parsed.
    #
    # 2. If input is not exactly seven characters long, then return an
    #    error.
    if not isinstance(input, str) or len(input) != 7:
        raise ValueError(
            "An HTML5 simple color must be a Unicode string "
            "exactly seven characters long."
        )

    # 3. If the first character in input is not a U+0023 NUMBER SIGN
    #    character (#), then return an error.
    if not input.startswith("#"):
        raise ValueError(
            "An HTML5 simple color must begin with the " "character '#' (U+0023)."
        )

    # 4. If the last six characters of input are not all ASCII hex
    #    digits, then return an error.
    if not all(c in string.hexdigits for c in input[1:]):
        raise ValueError(
            "An HTML5 simple color must contain exactly six ASCII hex digits."
        )

    # 5. Let result be a simple color.
    #
    # 6. Interpret the second and third characters as a hexadecimal
    #    number and let the result be the red component of result.
    #
    # 7. Interpret the fourth and fifth characters as a hexadecimal
    #    number and let the result be the green component of result.
    #
    # 8. Interpret the sixth and seventh characters as a hexadecimal
    #    number and let the result be the blue component of result.
    #
    # 9. Return result.
    return HTML5SimpleColor(
        int(input[1:3], 16), int(input[3:5], 16), int(input[5:7], 16)
    )


def html5_serialize_simple_color(simple_color: IntTuple) -> str:
    """
    Apply the serialization algorithm for a simple color from section
    2.4.6 of HTML5.

    """
    red, green, blue = simple_color

    # 1. Let result be a string consisting of a single "#" (U+0023)
    #    character.
    result = "#"

    # 2. Convert the red, green, and blue components in turn to
    #    two-digit hexadecimal numbers using lowercase ASCII hex
    #    digits, zero-padding if necessary, and append these numbers
    #    to result, in the order red, green, blue.
    format_string = "{:02x}"
    result += format_string.format(red)
    result += format_string.format(green)
    result += format_string.format(blue)

    # 3. Return result, which will be a valid lowercase simple color.
    return result


def html5_parse_legacy_color(input: str) -> HTML5SimpleColor:
    """
    Apply the legacy color parsing algorithm from section 2.4.6 of
    HTML5.

    """
    # 1. Let input be the string being parsed.
    if not isinstance(input, str):
        raise ValueError(
            "HTML5 legacy color parsing requires a Unicode string as input."
        )

    # 2. If input is the empty string, then return an error.
    if input == "":
        raise ValueError("HTML5 legacy color parsing forbids empty string as a value.")

    # 3. Strip leading and trailing whitespace from input.
    input = input.strip()

    # 4. If input is an ASCII case-insensitive match for the string
    #    "transparent", then return an error.
    if input.lower() == "transparent":
        raise ValueError(
            u'HTML5 legacy color parsing forbids "transparent" as a value.'
        )

    # 5. If input is an ASCII case-insensitive match for one of the
    #    keywords listed in the SVG color keywords section of the CSS3
    #    Color specification, then return the simple color
    #    corresponding to that keyword.
    keyword_hex = CSS3_NAMES_TO_HEX.get(input.lower())
    if keyword_hex is not None:
        return html5_parse_simple_color(keyword_hex)

    # 6. If input is four characters long, and the first character in
    #    input is a "#" (U+0023) character, and the last three
    #    characters of input are all ASCII hex digits, then run these
    #    substeps:
    if (
        len(input) == 4
        and input.startswith("#")
        and all(c in string.hexdigits for c in input[1:])
    ):
        # 1. Let result be a simple color.
        #
        # 2. Interpret the second character of input as a hexadecimal
        #    digit; let the red component of result be the resulting
        #    number multiplied by 17.
        #
        # 3. Interpret the third character of input as a hexadecimal
        #    digit; let the green component of result be the resulting
        #    number multiplied by 17.
        #
        # 4. Interpret the fourth character of input as a hexadecimal
        #    digit; let the blue component of result be the resulting
        #    number multiplied by 17.
        result = HTML5SimpleColor(
            int(input[1], 16) * 17, int(input[2], 16) * 17, int(input[3], 16) * 17
        )

        # 5. Return result.
        return result

    # 7. Replace any characters in input that have a Unicode code
    #    point greater than U+FFFF (i.e. any characters that are not
    #    in the basic multilingual plane) with the two-character
    #    string "00".
    input = "".join("00" if ord(c) > 0xFFFF else c for c in input)

    # 8. If input is longer than 128 characters, truncate input,
    #    leaving only the first 128 characters.
    if len(input) > 128:
        input = input[:128]

    # 9. If the first character in input is a "#" (U+0023) character,
    #    remove it.
    if input.startswith("#"):
        input = input[1:]

    # 10. Replace any character in input that is not an ASCII hex
    #     digit with the character "0" (U+0030).
    input = "".join(c if c in string.hexdigits else "0" for c in input)

    # 11. While input's length is zero or not a multiple of three,
    #     append a "0" (U+0030) character to input.
    while (len(input) == 0) or (len(input) % 3 != 0):
        input += "0"

    # 12. Split input into three strings of equal length, to obtain
    #     three components. Let length be the length of those
    #     components (one third the length of input).
    length = int(len(input) / 3)
    red = input[:length]
    green = input[length : length * 2]
    blue = input[length * 2 :]

    # 13. If length is greater than 8, then remove the leading
    #     length-8 characters in each component, and let length be 8.
    if length > 8:
        red, green, blue = (red[length - 8 :], green[length - 8 :], blue[length - 8 :])
        length = 8

    # 14. While length is greater than two and the first character in
    #     each component is a "0" (U+0030) character, remove that
    #     character and reduce length by one.
    while (length > 2) and (red[0] == "0" and green[0] == "0" and blue[0] == "0"):
        red, green, blue = (red[1:], green[1:], blue[1:])
        length -= 1

    # 15. If length is still greater than two, truncate each
    #     component, leaving only the first two characters in each.
    if length > 2:
        red, green, blue = (red[:2], green[:2], blue[:2])

    # 16. Let result be a simple color.
    #
    # 17. Interpret the first component as a hexadecimal number; let
    #     the red component of result be the resulting number.
    #
    # 18. Interpret the second component as a hexadecimal number; let
    #     the green component of result be the resulting number.
    #
    # 19. Interpret the third component as a hexadecimal number; let
    #     the blue component of result be the resulting number.
    #
    # 20. Return result.
    return HTML5SimpleColor(int(red, 16), int(green, 16), int(blue, 16))
