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
        """@""": """$""",
        """spin(""": """adjust-hue(""",
    }

    result = replace_all(content, lines)

    new = file(base_output, 'w')
    new.write(result)
    new.close()

def generate_mixins_scss():
    base_file = './less/mixins.less'
    base_output = './sass/_mixins.scss'

    old = file(base_file, 'r')
    content = old.read()
    old.close()

    lines = {
        # """ """: """ """,
        """@""": """$""",
        """.clearfix()""": """@mixin clearfix()""",
        """.border_radius""": """@mixin border_radius""",
        """.opacity(""": """@mixin opacity(""",
        """.box_shadow(""": """@mixin box_shadow(""",
        """.inset_box_shadow(""": """@mixin inset_box_shadow(""",
        """.text_shadow(""": """@mixin text_shadow(""",
        """.text_shadow(""": """@mixin text_shadow(""",
        """.vertical_gradient(""": """@mixin vertical_gradient(""",
        """.transition(""": """@mixin transition(""",
        """.scale(""": """@mixin scale(""",
        """.borderbox ()""": """@mixin borderbox()""",
        """.darkorlighttextshadow (""": """@mixin darkorlighttextshadow(""",

        # fix @mixins
        """$mixin""": """@mixin""",
        """{ @mixin text_shadow(""": """{ @include text_shadow(""",
        """filter:~\"alpha(opacity=$opacity * 100)\";""": """filter: alpha(opacity=( $opacity * 100 ) );""",
        """ when """: """ { @if """,
        """$opacity) ); }""": """$opacity) ); } }""",
    }

    result = replace_all(content, lines)

    new = file(base_output, 'w')
    new.write(result)
    new.close()

generate_woocommerce_base_scss()
generate_mixins_scss()

print 'Compiled!'
