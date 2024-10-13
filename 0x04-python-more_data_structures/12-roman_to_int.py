def roman_to_int(roman_s):
    """Converts a Roman numeral to an integer."""
    if not isinstance(roman_s, str) or roman_s is None:
        return 0
    roman_v = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
            }
    result = 0
    for i in range(len(roman_s)):
        if i > 0 and roman_v[roman_s[i]] > roman_v[roman_s[i - 1]]:
            result += roman_v[roman_s[i]] - 2 * roman_v[roman_s[i - 1]]
        else:
            result += roman_v[roman_s[i]]
    return result
