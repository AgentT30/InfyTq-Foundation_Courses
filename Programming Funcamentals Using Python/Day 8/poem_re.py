import re

poem = '''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''


print(len(re.findall("v", poem)))

print()
print(re.sub(r'\n', ' ', poem)[1:])

print()
print(re.sub(r'(c)(h|o)', r'C\2', poem))

print()
print(re.sub(r'(hi|ai)(...)', r'\1*\*', poem))
