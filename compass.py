#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def generate_sass_file(base_file, base_output, items):
    old = file(base_file, 'r')
    content = old.read()
    old.close()

    result = replace_all(content, items)

    new = file(base_output, 'w')
    new.write(result)
    new.close()

# _woocommerce-base.scss
base_items = {
    """@""": """$""",
    """spin(""": """adjust-hue(""",
}
generate_sass_file('./less/woocommerce-base.less', './sass/_woocommerce-base.scss', base_items)

# _mixins.scss
mixins_items = {

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

    # fixed replaces
    """$mixin""": """@mixin""",
    """filter:~\"alpha(opacity=$opacity * 100)\";""": """filter: alpha(opacity=( $opacity * 100 ) );""",
    """.nobr { white-space: nowrap; }""": """.nobr { white-space: nowrap; }

@mixin darkorlighttextshadow( $a, $opacity: 0.8 ) {
    @if lightness( $a ) >= 65% {
        @include text_shadow( 0, -1px, 0, rgba(0, 0, 0, $opacity) );
    } @else {
        @include text_shadow( 0, 1px, 0, rgba(255, 255, 255, $opacity) );
    }
}""",
}
generate_sass_file('./less/mixins.less', './sass/_mixins.scss', mixins_items)

# Replace last lines
generate_sass_file_old = open('./sass/_mixins.scss')
generate_sass_file_lines = generate_sass_file_old.readlines()
generate_sass_file_old.close()

generate_sass_file_new = open('./sass/_mixins.scss','w')
generate_sass_file_new.writelines([item for item in generate_sass_file_lines[:-2]])
generate_sass_file_new.close()

# woocommerce.scss
woocommerce_items = {
    """@""": """$""",
    """.border_radius""": """@include border_radius""",
    """.vertical_gradient(""": """@include vertical_gradient(""",
    """.clearfix();""": """@include clearfix();""",
    """.clearfix;""": """@include clearfix();""",
    """.border_radius""": """@include border_radius""",
    """.opacity(""": """@include opacity(""",
    """.box_shadow(""": """@include box_shadow(""",
    """.inset_box_shadow(""": """@include inset_box_shadow(""",
    """.text_shadow(""": """@include text_shadow(""",
    """.text_shadow(""": """@include text_shadow(""",
    """.transition(""": """@include transition(""",
    """.scale(""": """@include scale(""",
    """.borderbox ();""": """@include borderbox();""",
    """.darkorlighttextshadow (""": """@include darkorlighttextshadow(""",
    """.darkorlighttextshadow(""": """@include darkorlighttextshadow(""",

    # fixed replaces
    """$import""": """@import""",
    """$include""": """@include""",
    """$media""": """@media""",
    """$2x""": """@2x""",
    """$font-face""": """@font-face""",
}

generate_sass_file('./less/woocommerce.less', './sass/woocommerce.scss', woocommerce_items)

print 'Compiled!'
