st = input('Enter string: ').lower()
chars = {}
import string
for ch in string.ascii_lowercase:
    chars[ch] = st.count(ch)
    if chars[ch] != 0:
        print(ch, chars[ch], sep=': ')