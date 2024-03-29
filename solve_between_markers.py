import re


def between_markers(text: str, begin: str, end: str) -> str:
    re_obj = re.compile(r'[>\[][a-zA-Z ]*[<\]]')
    result = re_obj.search(text)
    return result.group(0).strip('><[]')


print(between_markers("[an apple]","[","]"))

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')