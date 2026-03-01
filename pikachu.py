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

    #    Pokemon('ゾロアーク', PType.DARK,   PType.NONE,    PType.NONE,      80,   60,105, 60,120, 60,105,  'イリュージョン', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('ゴチルゼル', PType.PSYCHIC, PType.NONE,   PType.NONE,      80,   70, 55, 95, 95,110, 65,  'かちき', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('カポエラー', PType.FIGHTING, PType.NONE,  PType.NONE,      80,   50, 95, 95, 35,110, 70,  'テクニシャン', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('パチリス',   PType.ELECTRIC, PType.NONE,  PType.NONE,      80,   60, 45, 70, 45, 90, 95,  'にげあし', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),

    #    Pokemon('スリーパー', PType.PSYCHIC, PType.NONE,  PType.NONE,       80,   85, 73, 70, 73,115, 67,  'ふみん', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('キラルロフ', PType.ROCK, PType.POISON,   PType.NONE,       84,   83, 55, 90,130, 81, 86,  'どくげしょう', 30,   252, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('ヤレユータン', PType.NORMAL, PType.PSYCHIC, PType.NONE,    80,   90, 60, 80, 90,110, 60,  'せいしんりょく', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('ルガルガン昼', PType.ROCK, PType.NONE, PType.NONE,         86,   75,115, 65, 55, 65,112,  'すなかき', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
   
    #    Pokemon('ジュラルドン', PType.DRAGON, PType.STEEL, PType.NONE,      82,   70, 95,115,120, 50, 85,  'すじがねいり', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし')

        Pokemon('ピカチュウ',  '#NPC', PType.NONE, 66, 'ひらいしん',   31, 0, 0, 0, 0, 0, 0, 'がんばりや', 'でんきだま'),
        Pokemon('ライチュウA', '#NPC', PType.NONE, 66, 'ひらいしん',   31, 0, 0, 0, 0, 0, 4, 'がんばりや', 'なし'),

    ]

    mpoks = [
        Pokemon('ピカチュウ', '#HA', PType.NONE, 70, 'ひらいしん', 31, 252, 252,   4, 0, 0, 0,   'いじっぱり', 'ゴツゴツメット'),
        Pokemon('ピカチュウ', '#AB', PType.NONE, 70, 'ひらいしん', 31, 4,   252, 252, 0, 0, 0,   'いじっぱり', 'ゴツゴツメット'),
        Pokemon('ピカチュウ', '#HC', PType.NONE, 70, 'ひらいしん', 31, 252,   0,   4, 252, 0, 0, 'ひかえめ', 'ゴツゴツメット'),
        Pokemon('ライチュウ', '#HA', PType.NONE, 70, 'ひらいしん', 31, 252, 252,   4, 0, 0, 0,   'いじっぱり', 'ゴツゴツメット')

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
    try_move(mpoks[0], 'あなをほる', MCat.PHYSICAL, PType.GROUND, 80, 1)
    try_move(mpoks[0], 'アイアンテール', MCat.PHYSICAL, PType.STEEL, 100, 1)
    try_move(mpoks[0], 'じゃれつく', MCat.PHYSICAL, PType.FAIRY, 90, 1)

    try_move(mpoks[2], 'ドレインキッス', MCat.SPECIAL, PType.FAIRY, 50, 1)
    try_move(mpoks[2], 'なみのり', MCat.SPECIAL, PType.WATER, 90, 1)
    try_move(mpoks[2], 'スピードスター', MCat.SPECIAL, PType.NORMAL, 60, 1)

    try_move(mpoks[3], 'あなをほる', MCat.PHYSICAL, PType.GROUND, 80, 1)
    try_move(mpoks[3], 'アイアンテール', MCat.PHYSICAL, PType.STEEL, 100, 1)
    try_move(mpoks[3], 'じゃれつく', MCat.PHYSICAL, PType.FAIRY, 90, 1)

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

    print ('-----ピカチュウ-----')
    try_emove_each(epoks[0], 'あなをほる', MCat.PHYSICAL, PType.GROUND, 80, 1)
    try_emove_each(epoks[0], 'じゃれつく', MCat.PHYSICAL, PType.FAIRY, 90, 1)
    try_emove_each(epoks[0], 'アイアンテール', MCat.PHYSICAL, PType.STEEL, 100, 1)

     #try_emove_each(epoks[0], 'ストーンエッジ', MCat.PHYSICAL, PType.ROCK, 100, 1)

    print ('-----ライチュウ-----')
    try_emove_each(epoks[1], 'あなをほる', MCat.PHYSICAL, PType.GROUND, 80, 1)
    try_emove_each(epoks[1], 'じゃれつく', MCat.PHYSICAL, PType.FAIRY, 90, 1)
    try_emove_each(epoks[1], 'アイアンテール', MCat.PHYSICAL, PType.STEEL, 100, 1)







def main():
    init_poks()

   
  
    damage_to_enemy()
    damage_from_enemy()
    

main()
