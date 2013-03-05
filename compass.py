#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def generate_woocommerce_base_scss():
    base_file = './less/woocommerce-base.less'
    base_output = './sass/_woocommerce-base.scss'

    old = file(base_file, 'r')
    content = old.read()
    old.close()

    lines = {
        # """ """: """ """,
        """@primary""": """$primary""",
        """@secondary""": """$secondary""",
        """@highlight""": """$highlight""",
        """@contentbg""": """$contentbg""",
        """@subtext""": """$subtext""",
        """spin(""": """adjust-hue(""",
    }

    result = replace_all(content, lines)

    new = file(base_output, 'w')
    new.write(result)
    new.close()


generate_woocommerce_base_scss()

print 'Compiled!'
