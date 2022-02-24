import re


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    org_text_code = re.findall(r"<code[^>]*>(.+?\n*.+?)</code>", org_text, re.MULTILINE | re.DOTALL)
    org_text_pre = re.findall(r"<pre[^>]*>(.+?\n*.+?)</pre>", org_text, re.MULTILINE | re.DOTALL)
    trans_text_code = re.findall(r"<code[^>]*>(.+?\n*.+?)</code>", trans_text, re.MULTILINE | re.DOTALL)
    trans_text_pre = re.findall(r"<pre[^>]*>(.+?\n*.+?)</pre>", trans_text, re.MULTILINE | re.DOTALL)

    if org_text_code:
        for i, word in enumerate(org_text_code):
            trans_text = trans_text.replace(trans_text_code[i], word)

    if org_text_pre:
        for i, word in enumerate(org_text_pre):
            trans_text = trans_text.replace(trans_text_pre[i], word)

    return trans_text
