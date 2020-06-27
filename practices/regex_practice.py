import re

text_to_search = '''
abcdef
tesabc
'''


def find(input):
    pattern = re.compile(r'{0}'.format(input))
    matches = pattern.finditer(text_to_search)
    for m in matches:
        print(m.group())


find('abc')
