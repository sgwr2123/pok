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
from pklib.pok import PokBstat

def init_poks():
    global epoks
    global mpoks
    pklib.pok.PokBstat.init()

    epoks = [    
    #    Pokemon('ヨクバリス', PType.NONE,      82,  120, 95, 95, 55, 75, 20,  'ほおぶくろ',   0,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('ブラッキー', PType.DARK,   PType.NONE,    PType.NONE,      84,   95, 65,110, 60,130, 65,  'シンクロ',     20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('ウツボット', PType.GRASS,  PType.POISON,  PType.NONE,      80,   80,105, 65,100, 70, 70,  'ようりょくそ', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),
    #    Pokemon('バサギリ',   PType.BUG,    PType.ROCK,    PType.NONE,      80,   70,135, 95, 45, 70, 85,  'きれあじ', 20,   0, 0, 0, 0, 0, 0, -1, -1, 'なし'),

        Pokemon('カメックス', '#NPC', PType.NONE, 99, 'げきりゅう',   31, 0, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('ラグラージ', '#NPC', PType.NONE, 99, 'げきりゅう',   31, 0, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('ゲッコウガ', '#NPC', PType.NONE, 99, 'げきりゅう',   31, 0, 0, 0, 0, 0, 0, 'がんばりや', 'なし')

    ]

    mpoks = [
        Pokemon('エンブオー', '#AD', PType.NONE, 100, 'もうか',     31, 4, 252,  0, 0, 252, 0,   'いじっぱり', 'かいがらのすず'),
        Pokemon('メガエンブオー', '#AD', PType.NONE, 100, 'もうか', 31, 4, 252, 0, 0, 252, 0,   'いじっぱり', 'オーダイルナイト'),
        Pokemon('メガエンブオー', '#HA', PType.NONE, 100, 'もうか', 31, 252, 252,0, 0, 4, 0,   'いじっぱり', 'オーダイルナイト')

     ]


    print('---------------------- epoks ----------------------')
    for x in epoks:
        x.print_stat()

    print('---------------------- mpoks ----------------------')
    for x in mpoks:
        x.print_stat()


def try_move_one(mpok, epok, mname, mcat, mtyp, mpower, scale):

    (d, f) = mpok.damage_to(epok, mname, mcat, mtyp, mpower, scale, 1)
    print ('    %-20s (%-10s %u) %s damage = %u (x%.3f), %u %% of HP' % (mname, PokBstat.type2Str[mtyp], mpower, epok.getName(), d, f, int(d*100/epok.get_stat(SIDX.H))))

def try_move_each(mpok, mname, mcat, mtyp, mpower, scale):

    for x in epoks:
        (d, f) = mpok.damage_to(x, mname, mcat, mtyp, mpower, scale, 1)
        print ('    %s damage = %u (x%.3f), %u %% of HP' % (x.getName(), d, f, int(d*100/x.get_stat(SIDX.H))))

def try_move(mpok, mname, mcat, mtyp, mpower, scale):
    print('%sの%s:' % (mpok.getName(), mname))   
    try_move_each(mpok, mname, mcat, mtyp, mpower, scale)

def damage_to_enemy():
    for i in range(3):
        for j in range(3):
            print('%s の %s への攻撃' % (mpoks[i].getName(), epoks[j].getName()))
            try_move_one(mpoks[i], epoks[j], 'くさわけ', MCat.PHYSICAL, PType.GRASS, 40, 0.7*1.3)
            try_move_one(mpoks[i], epoks[j], 'ソーラーブレード', MCat.PHYSICAL, PType.GRASS, 125, 0.7*1.3)
            try_move_one(mpoks[i], epoks[j], 'かみなりパンチ', MCat.PHYSICAL, PType.ELECTRIC, 75, 0.7*1.3)
            try_move_one(mpoks[i], epoks[j], 'ワイルドボルト', MCat.PHYSICAL, PType.ELECTRIC, 90, 0.7*1.3)
            try_move_one(mpoks[i], epoks[j], 'ドレインパンチ', MCat.PHYSICAL, PType.FIGHTING, 75, 0.7*1.2)
            try_move_one(mpoks[i], epoks[j], 'インファイト',   MCat.PHYSICAL, PType.FIGHTING, 120, 0.7*1.2)
            try_move_one(mpoks[i], epoks[j], 'あなをほる',     MCat.PHYSICAL, PType.GROUND, 80, 0.7*1.2)

    

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

    print ('-----カメックス-----')
    try_emove_each(epoks[0], 'ハイドロカノン', MCat.SPECIAL, PType.WATER, 150, 0.7) # 2.5s / 0.83s / 20s
    try_emove_each(epoks[0], 'なみのり',      MCat.SPECIAL, PType.WATER, 90, 0.7)  # 1.33s / 1.77s / 8s
    try_emove_each(epoks[0], 'ふぶき',        MCat.SPECIAL, PType.ICE, 110, 0.7)  # 1.83s / 1.33s / 12s
    try_emove_each(epoks[0], 'うずしお',      MCat.SPECIAL, PType.WATER, 20, 0.7)  # 1.00s / 1.33s / 7s
    # こうごうせい

    
    print ('-----ラグラージ-----')
    try_emove_each(epoks[1], 'ハイドロカノン', MCat.SPECIAL, PType.WATER, 150, 0.7) # 2.5s / 0.83s / 20s
    # アクアリング
    try_emove_each(epoks[1], 'たきのぼり',    MCat.PHYSICAL, PType.WATER, 80, 0.7) # 1.17s / 1.13s / 8s
    try_emove_each(epoks[1], 'だくりゅう',    MCat.SPECIAL, PType.WATER,  90, 0.7) # 1.33s / 2.67s / 8s
    
    print ('-----ゲッコウガ-----')
    try_emove_each(epoks[2], 'ハイドロカノン', MCat.SPECIAL, PType.WATER, 150, 0.7) # 2.5s / 0.83s / 20s
    # かげぶんしん
    try_emove_each(epoks[2], 'ハイドロポンプ', MCat.SPECIAL, PType.WATER, 110, 0.7) # 2.33s / 2.00s / 12s
    try_emove_each(epoks[2], 'みずしゅりけん', MCat.SPECIAL, PType.WATER, 75, 0.7)  # 0.67s / 1.17s / 3s
    





def main():
    init_poks()

   
  
    damage_to_enemy()
    damage_from_enemy()
    

main()
