import streamlit as st
import re

def to_unicode_bold(text: str) -> str:
    result = []
    for c in text:
        if 'A' <= c <= 'Z':
            result.append(chr(ord(c) + 0x1D400 - ord('A')))
        elif 'a' <= c <= 'z':
            result.append(chr(ord(c) + 0x1D41A - ord('a')))
        elif '0' <= c <= '9':
            result.append(chr(ord(c) + 0x1D7CE - ord('0')))
        else:
            result.append(c)
    return ''.join(result)

def boldify_linkedin(text: str) -> str:
    pattern = r"\*\*(.+?)\*\*"
    def replacer(match):
        return to_unicode_bold(match.group(1))
    return re.sub(pattern, replacer, text)

st.title("LinkedIn Bold Text Converter")

input_text = st.text_area("Enter your text with **bold** parts:")

if input_text:
    converted = boldify_linkedin(input_text)
    st.markdown("### Converted Text:")
    st.code(converted, language=None)
    st.markdown("You can copy this output and paste it into LinkedIn. The bold parts will appear bold via Unicode fonts!")
