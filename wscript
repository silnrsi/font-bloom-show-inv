#!/usr/bin/pythons
# encoding: utf-8
# this is a smith configuration file

APPNAME = 'BloomShowInv'
DESC_SHORT = "Bloom Show Invisibles Font"
DEBPKG = 'fonts-sil-bloom-show-inv'

getufoinfo('source/BloomShowInv-Regular.ufo')

fontfamily=APPNAME

designspace('source/' + fontfamily + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi"),
)
