#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
import re
import math

import pklib.pok
from pklib.pok import SIDX
from pklib.pok import PType
from pklib.pok import Pokemon
from pklib.pok import MCat

def init_poks():
    global epoks
    global mpoks
    pklib.pok.PokBstat.init()

    epoks = [    
    #    Pokemon('ヨクバリス', PType.NONE,      82,  120, 95, 95, 55, 75, 20,  'ほおぶくろ',   0,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('ブラッキー', PType.DARK,   PType.NONE,    PType.NONE,      84,   95, 65,110, 60,130, 65,  'シンクロ',     20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('ウツボット', PType.GRASS,  PType.POISON,  PType.NONE,      80,   80,105, 65,100, 70, 70,  'ようりょくそ', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('バサギリ',   PType.BUG,    PType.ROCK,    PType.NONE,      80,   70,135, 95, 45, 70, 85,  'きれあじ', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),

        Pokemon('フシギバナ', '#NPC', PType.NONE, 99, 'しんりょく',   31, 0, 0, 252, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('ジュカイン', '#NPC', PType.NONE, 99, 'しんりょく',   31, 0, 0, 252, 0, 0, 4, 'がんばりや', 'なし'),
        Pokemon('ブリガロン', '#NPC', PType.NONE, 99, 'しんりょく',   31, 0, 0, 252, 0, 0, 4, 'がんばりや', 'なし')

    ]

    mpoks = [
        Pokemon('オーダイル', '#AD', PType.NONE, 100, 'げきりゅう',     31, 4, 252,  0, 0, 252, 0,   'いじっぱり', 'かいがらのすず'),
        Pokemon('メガオーダイル', '#AD', PType.NONE, 100, 'げきりゅう', 31, 4, 252, 0, 0, 252, 0,   'いじっぱり', 'オーダイルナイト'),
        Pokemon('メガオーダイル', '#CD', PType.NONE, 100, 'げきりゅう', 31, 4, 0,0, 252, 252, 0,   'ひかえめ', 'オーダイルナイト')

     ]


    print('---------------------- epoks ----------------------')
    for x in epoks:
        x.print_stat()

    print('---------------------- mpoks ----------------------')
    for x in mpoks:
        x.print_stat()



def try_move_each(mpok, mname, mcat, mtyp, mpower, scale):

    for x in epoks:
        (d, f) = mpok.damage_to(x, mname, mcat, mtyp, mpower, scale, 1)
        print ('    %s damage = %u (x%.3f), %u %% of HP' % (x.getName(), d, f, int(d*100/x.get_stat(SIDX.H))))

def try_move(mpok, mname, mcat, mtyp, mpower, scale):
    print('%sの%s:' % (mpok.getName(), mname))   
    try_move_each(mpok, mname, mcat, mtyp, mpower, scale)

def damage_to_enemy():
    for i in range(3):
        try_move(mpoks[i], 'こおりのキバ', MCat.PHYSICAL, PType.ICE, 65, 1)
        try_move(mpoks[i], 'つららばり', MCat.PHYSICAL, PType.ICE, 125, 1)
        try_move(mpoks[i], 'れいとうビーム', MCat.SPECIAL, PType.ICE, 90, 1)
        try_move(mpoks[i], 'ふぶき', MCat.SPECIAL, PType.ICE, 110, 1)
        try_move(mpoks[i], 'アクアジェット', MCat.PHYSICAL, PType.WATER, 30, 1)

    

#    try_move(mpoks[0], 'ばくおんぱ', MCat.SPECIAL, PType.NORMAL, 140, 1)
#    try_move(mpoks[0], 'フレアソング', MCat.SPECIAL, PType.FIRE, 80, 1)
#    try_move(mpoks[0], 'ドレインキッス', MCat.SPECIAL, PType.FAIRY, 50, 1)
#    try_move(mpoks[1], 'ムーンフォース', MCat.SPECIAL, PType.FAIRY, 95, 1)
#    try_move(mpoks[1], 'サイコショック', MCat.SPECIAL, PType.PSYCHIC, 80, 1)
#    try_move(mpoks[1], '背水の陣アシストパワー', MCat.SPECIAL, PType.PSYCHIC, 120, 1.5)
#    try_move(mpoks[1], 'マジカルフレイム', MCat.SPECIAL, PType.FIRE, 75, 1)
#    try_move(mpoks[1], 'シャドーボール', MCat.SPECIAL, PType.GHOST, 80, 1)
#    try_move(mpoks[1], '10まんボルト', MCat.SPECIAL, PType.ELECTRIC, 90, 1)
#    try_move(mpoks[1], 'はどうだん', MCat.SPECIAL, PType.FIGHTING, 80, 1)
#    try_move(mpoks[2], 'ムーンフォース', MCat.SPECIAL, PType.FAIRY, 95, 1)
#    try_move(mpoks[2], '10まんボルト',  MCat.SPECIAL, PType.ELECTRIC, 90, 1)
#    try_move(mpoks[2], 'サイコショック', MCat.SPECIAL, PType.PSYCHIC, 80, 1)
#    try_move(mpoks[4], 'フレアソング', MCat.SPECIAL, PType.FIRE, 80, 1)
#    try_move(mpoks[4], 'だいちのちから', MCat.SPECIAL, PType.GROUND, 90, 1)
#    try_move(mpoks[5], 'しんそく', MCat.PHYSICAL, PType.NORMAL, 80, 1)
#    try_move(mpoks[5], 'ドラゴンクロー', MCat.PHYSICAL, PType.DRAGON, 80, 1)
#    try_move(mpoks[5], 'つばめがえし', MCat.PHYSICAL, PType.FLYING, 60, 1)


def try_emove_each(epok, mname, mcat, mtyp, mpower, scale):
    print('%sの%s:' % (epok.getName(), mname))   
    for x in mpoks:
        (d, f) = epok.damage_to(x, mname, mcat, mtyp, mpower, scale, 0)
        print ('    %s rdamage = %u (x%.3f), %u %% of HP' % (x.getName(), d, f, int(d*100/x.get_stat(SIDX.H))))

def damage_from_enemy():
    print ("**************敵からの攻撃 ***************")

    print ('-----フシギバナ-----')
    try_emove_each(epoks[0], 'ハードプラント', MCat.SPECIAL, PType.GRASS, 150, 1)
    try_emove_each(epoks[0], 'ギガドレイン', MCat.SPECIAL, PType.GRASS, 75, 1)
    try_emove_each(epoks[0], 'ソーラービーム', MCat.SPECIAL, PType.GRASS, 120, 1)
    # こうごうせい

    
    print ('-----ジュカイン-----')
    try_emove_each(epoks[1], 'ハードプラント', MCat.SPECIAL, PType.GRASS, 150, 1)
    try_emove_each(epoks[1], 'リーフストーム', MCat.SPECIAL, PType.GRASS, 130, 1)
    try_emove_each(epoks[1], 'リーフブレード', MCat.PHYSICAL, PType.GRASS, 90, 1)
    try_emove_each(epoks[1], 'タネマシンガン', MCat.PHYSICAL, PType.GRASS, 75, 1)

    print ('-----ブリガロン-----')
    try_emove_each(epoks[2], 'ハードプラント', MCat.SPECIAL, PType.GRASS, 150, 1)
    try_emove_each(epoks[2], 'ウッドハンマー', MCat.PHYSICAL, PType.GRASS, 120, 1)
    try_emove_each(epoks[2], 'タネばくだん', MCat.PHYSICAL, PType.GRASS, 35, 1)
    # ニードルガード






def main():
    init_poks()

   
  
    damage_to_enemy()
    damage_from_enemy()
    

main()
