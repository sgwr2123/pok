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
        #0  ネモ
        Pokemon('ルガルガンD',  '#ネモ', PType.NONE, 86, 'すなかき',   31, 252, 252, 0, 0, 0, 4, 'がんばりや', 'なし'),
        Pokemon('ジャラランガ', '#ネモ', PType.NONE, 86, 'ぼうおん',   31, 0, 252, 252, 0, 0, 4, 'がんばりや', 'なし'),
        Pokemon('パーモット',   '#ネモ', PType.NONE, 86, 'ちくでん',   31, 252, 252, 0, 0, 0, 4, 'がんばりや', 'なし'),
        Pokemon('ゴウカザル',   '#ネモ', PType.NONE, 86, 'もうか',     31, 252, 252, 0, 0, 0, 4, 'がんばりや', 'なし'),
        Pokemon('ミロカロス',   '#ネモ', PType.NONE, 86, 'かちき',     31, 252, 0, 0, 252, 0, 4, 'がんばりや', 'なし'),
        Pokemon('マスカーニャ', '#ネモ', PType.DARK, 87, 'しんりょく', 31, 252, 252, 0, 0, 0, 4, 'がんばりや', 'なし'),

        #6  ペパー
        Pokemon('ヨクバリス',  '#ペパー', PType.NONE, 82, 'ほおぶくろ',     0,  0, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('パルシェン',  '#ペパー', PType.NONE, 82, 'スキルリンク',   20, 0, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('スコヴィラン','#ペパー', PType.NONE, 82, 'ようりょくそ',   20, 0, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('リククラゲ',  '#ペパー', PType.NONE, 82, 'きんしのちから', 20, 0, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('キョジオーン','#ペパー', PType.NONE, 82, 'きよめのしお',   20, 0, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('マフィティフ', '#ペパー', PType.DARK, 83, 'いかく',       25, 252, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),

        #12 オモダカ
        Pokemon('キラフロル',   '#オモダカ', PType.NONE,   84, 'どくげしょう',  30,  252, 0, 0, 0, 0, 0, 'がんばりや', 'なし'),
        Pokemon('クエスパトラ', '#オモダカ', PType.NONE,   84, 'びんじょう',    25,  0, 0, 0, 0, 0, 0,   'がんばりや', 'なし'),
        Pokemon('ブリガロン',   '#オモダカ', PType.NONE,   84, 'ぼうだん',      25,  0, 0, 0, 0, 0, 0,  'がんばりや', 'なし'),
        Pokemon('クレベース',   '#オモダカ', PType.NONE,   84, 'マイペース',     25,  0, 0, 0, 0, 0, 0,  'がんばりや', 'なし'),
        Pokemon('ドラパルト',   '#オモダカ', PType.NONE,   84, 'クリアボディ',   25,  0, 0, 0, 0, 0, 0,  'がんばりや', 'なし'),
        Pokemon('ドドゲザン',   '#オモダカ', PType.FLYING, 85, 'そうだいしょう', 25,  0, 0, 0, 0, 0, 0,  'がんばりや', 'なし'),
        
        #18 サワロ
        Pokemon('パチリス',   '#サワロ', PType.NONE,   80, 'にげあし',       20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ママンボウ', '#サワロ', PType.NONE,   80, 'うるおいボディ',  20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('マホイップ', '#サワロ', PType.NONE,   80, 'スイートベール',  20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ビークイン', '#サワロ', PType.NONE,   80, 'プレッシャー',    20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ヌメルゴン', '#サワロ', PType.NONE,   80, 'そうしょく',      20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ブリムオン', '#サワロ', PType.FAIRY,  81, 'いやしのこころ',  25,  252, 0, 0, 0, 0, 0,  'がんばりや', 'なし'),

        #24 ミモザ
        Pokemon('スリーパー', '#ミモザ', PType.NONE,   80, 'ふみん',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('バチンウニ', '#ミモザ', PType.NONE,   80, 'ひらいしん',     20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('メガニウム', '#ミモザ', PType.NONE,   80, 'しんりょく',     20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('オニゴーリ', '#ミモザ', PType.NONE,   80, 'せいしんりょく', 20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('シビルドン', '#ミモザ', PType.NONE,   80, 'ふゆう',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ドヒドイデ', '#ミモザ', PType.POISON, 81, 'ひとでなし',     25, 252, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),

        #30 ジニア
        Pokemon('ウツボット', '#ジニア', PType.NONE,   80, 'ようりょくそ',   20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ウインディ', '#ジニア', PType.NONE,   80, 'いかく',         20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('マルノーム', '#ジニア', PType.NONE,   80, 'ヘドロえき',     20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('バンバドロ', '#ジニア', PType.NONE,   80, 'じきゅうりょく', 20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ヤドランG', '#ジニア', PType.NONE,    80,  'クイックドロウ',20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('リキキリン', '#ジニア', PType.PSYCHIC, 80, 'テイルアーマー', 25,  252, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        
        #36 キハダ
        Pokemon('カポエラー', '#キハダ', PType.NONE,     80, 'テクニシャン',  20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ケンタロスPB', '#キハダ', PType.NONE,   80, 'いかく',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ケンタロスPW', '#キハダ', PType.NONE,   80, 'いかく',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('チャーレム', '#キハダ', PType.NONE,     80, 'ヨガパワー',    20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ルチャブル', '#キハダ', PType.NONE,     80, 'じゅうなん',    20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ハリテヤマ', '#キハダ', PType.FIGHTING, 81, 'あついしぼう',  25,  252, 0, 0, 0, 0, 0,  'がんばりや', 'なし'),

        #42 ボタン
        Pokemon('ブラッキー', '#ボタン', PType.NONE,   84, 'シンクロ',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('シャワーズ', '#ボタン', PType.NONE,   84, 'ちょすい',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('サンダース', '#ボタン', PType.NONE,   84, 'はやあし',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ブースター', '#ボタン', PType.NONE,   84, 'もらいび',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('リーフィア', '#ボタン', PType.NONE,   84, 'リーフガード',    20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ニンフィア', '#ボタン', PType.FAIRY,  85, 'メロメロボディ',  25,  252, 0, 0, 0, 0, 0,  'がんばりや', 'なし'),

        #48 タイム
        Pokemon('バサギリ',     '#タイム', PType.NONE,   80, 'きれあじ',       20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ルガルガンE',  '#タイム', PType.NONE,   80, 'かたいツメ',      20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('カジリガメ',   '#タイム', PType.NONE,   80, 'がんじょうあご',  20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('イシヘンジン', '#タイム', PType.NONE,   80, 'パワースポット',  20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('セキタンザン', '#タイム', PType.NONE,   80, 'じょうききかん',  20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('キョジオーン', '#タイム', PType.ROCK,   81, 'きよめのしお',    25, 252, 0, 0, 0, 0, 0,   'がんばりや', 'なし'),

        #54 レホール
        Pokemon('ゾロアーク', '#レホール', PType.NONE,   80, 'イリュージョン',  20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ハブネーク', '#レホール', PType.NONE,   80, 'だっぴ',         20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ブーピッグ', '#レホール', PType.NONE,   80, 'あついしぼう',    20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('カラマネロ', '#レホール', PType.NONE,   80, 'あまのじゃく',    20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ハッサム',   '#レホール', PType.NONE,   80, 'テクニシャン',    20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ゲンガー',   '#レホール', PType.GHOST,  81, 'のろわれボディ',  25, 252, 0, 0, 0, 0, 0,   'がんばりや', 'なし'),

        #60 セイジ
        Pokemon('ゴチルゼル', '#セイジ', PType.NONE,     80, 'かちき',         20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ドンカラス', '#セイジ', PType.NONE,     80, 'きょううん',     20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ペルシアン', '#セイジ', PType.NONE,     80, 'テクニシャン',   20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('シロデスナ', '#セイジ', PType.NONE,     80, 'みずがため',     20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('サンドパンA', '#セイジ', PType.NONE,    80, 'ゆきがくれ',     20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),
        Pokemon('ライチュウ', '#セイジ', PType.ELECTRIC, 81, 'せいでんき',     25, 252, 0, 0, 0, 0, 0,   'がんばりや', 'なし')

        #66 クラベル
        #Pokemon('', '#クラベル', PType.NONE,   80, '',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),

        #72 ハッサク
        #Pokemon('', '#ハッサク', PType.NONE,   80, '',        20,  0, 0, 0, 0, 0, 0,    'がんばりや', 'なし'),

    ]

    mpoks = [
        Pokemon('ドーブル', '#CS', PType.NONE, 100, 'テクニシャン', 31, 4, 0, 0, 252, 0, 252, 'ひかえめ', 'おまもりこばん'),
        Pokemon('サーナイト', '#HC', PType.NONE, 100, 'シンクロ', 31, 4, 0, 252, 252, 0, 0,   'ひかえめ', 'かいがらのすず'),
        Pokemon('ハバタクカミ', '#BC', PType.NONE, 100, 'こだいかっせい', 31, 4, 0, 252, 252, 0, 0,   'ひかえめ', 'かいがらのすず'),
        Pokemon('ドーブル', '#HS', PType.NONE, 100, 'テクニシャン', 31, 252, 0, 176, 0, 0, 80, 'ようき', 'おまもりこばん'),
        Pokemon('ラウドボーン', '#BC', PType.NONE, 100, 'てんねん', 31, 4, 0, 252, 252, 0, 0, 'ひかえめ', 'なし'),

        Pokemon('カイリュー', '#AB', PType.NONE, 100, 'せいしんりょく', 31, 4, 252, 252, 0, 0, 0, 'いじっぱり', 'なし')
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

#    try_move(mpoks[0], 'ばくおんぱ', MCat.SPECIAL, PType.NORMAL, 140, 1)
#    try_move(mpoks[0], 'フレアソング', MCat.SPECIAL, PType.FIRE, 80, 1)
#    try_move(mpoks[0], 'ドレインキッス', MCat.SPECIAL, PType.FAIRY, 50, 1)
    try_move(mpoks[1], 'ムーンフォース', MCat.SPECIAL, PType.FAIRY, 95, 1)
    try_move(mpoks[1], 'サイコショック', MCat.SPECIAL, PType.PSYCHIC, 80, 1)
#    try_move(mpoks[1], '背水の陣アシストパワー', MCat.SPECIAL, PType.PSYCHIC, 120, 1.5)
#    try_move(mpoks[1], 'マジカルフレイム', MCat.SPECIAL, PType.FIRE, 75, 1)
#    try_move(mpoks[1], 'シャドーボール', MCat.SPECIAL, PType.GHOST, 80, 1)
    try_move(mpoks[1], '10まんボルト', MCat.SPECIAL, PType.ELECTRIC, 90, 1)
#    try_move(mpoks[1], 'はどうだん', MCat.SPECIAL, PType.FIGHTING, 80, 1)
    try_move(mpoks[2], 'ムーンフォース', MCat.SPECIAL, PType.FAIRY, 95, 1)
    try_move(mpoks[2], '10まんボルト',  MCat.SPECIAL, PType.ELECTRIC, 90, 1)
    try_move(mpoks[2], 'サイコショック', MCat.SPECIAL, PType.PSYCHIC, 80, 1)
    try_move(mpoks[4], 'フレアソング', MCat.SPECIAL, PType.FIRE, 80, 1)
    try_move(mpoks[4], 'だいちのちから', MCat.SPECIAL, PType.GROUND, 90, 1)
    try_move(mpoks[5], 'しんそく', MCat.PHYSICAL, PType.NORMAL, 80, 1)
#    try_move(mpoks[5], 'ドラゴンクロー', MCat.PHYSICAL, PType.DRAGON, 80, 1)
#    try_move(mpoks[5], 'つばめがえし', MCat.PHYSICAL, PType.FLYING, 60, 1)


def try_emove_each(epok, mname, mcat, mtyp, mpower, scale):
    print('%sの%s:' % (epok.getName(), mname))   
    for x in mpoks:
        (d, f) = epok.damage_to(x, mname, mcat, mtyp, mpower, scale, 0)
        print ('    %s rdamage = %u (x%.3f), %u %% of HP' % (x.getName(), d, f, int(d*100/x.get_stat(SIDX.H))))

def damage_from_enemy():
    print ("**************敵からの攻撃 ***************")

    print ('-----ネモ-----')
    try_emove_each(epoks[0], 'アクセルロック', MCat.PHYSICAL, PType.ROCK, 40, 1)
    try_emove_each(epoks[0], 'ドリルライナー', MCat.PHYSICAL, PType.GROUND, 80, 1)
    try_emove_each(epoks[0], 'じゃれつく', MCat.PHYSICAL, PType.FAIRY, 90, 1)
    try_emove_each(epoks[2], 'マッハパンチ', MCat.PHYSICAL, PType.FIGHTING, 40, 1)
    try_emove_each(epoks[3], 'マッハパンチ', MCat.PHYSICAL, PType.FIGHTING, 40, 1)

     #try_emove_each(epoks[0], 'ストーンエッジ', MCat.PHYSICAL, PType.ROCK, 100, 1)
    try_emove_each(epoks[4], 'ドレインキッス', MCat.SPECIAL, PType.FAIRY, 50, 1)
    try_emove_each(epoks[4], 'なみのり',       MCat.SPECIAL, PType.WATER, 90, 1)
    try_emove_each(epoks[4], 'れいとうビーム', MCat.SPECIAL, PType.ICE, 90, 1)
    try_emove_each(epoks[4], 'マッドショット', MCat.SPECIAL, PType.GROUND, 55, 1)

    print ('-----ペパー-----')
    try_emove_each(epoks[6], 'タネマシンガン', MCat.PHYSICAL, PType.GRASS, 125, 1)
    try_emove_each(epoks[6], 'のしかかり', MCat.PHYSICAL, PType.NORMAL, 85, 1)
    try_emove_each(epoks[6], 'サイコファング', MCat.PHYSICAL, PType.PSYCHIC, 85, 1)
    try_emove_each(epoks[6], 'じしん', MCat.PHYSICAL, PType.GROUND, 100, 1)

    print ('-----オモダカ-----')
    try_emove_each(epoks[12], 'パワージェム', MCat.SPECIAL, PType.ROCK, 80, 1)
    try_emove_each(epoks[12], 'ヘドロウェーブ', MCat.SPECIAL, PType.POISON, 95, 1)
    try_emove_each(epoks[12], 'だいちのちから', MCat.SPECIAL, PType.GROUND, 90, 1)
    try_emove_each(epoks[16], 'ふいうち', MCat.PHYSICAL, PType.DARK, 70, 1)

    print ('-----サワロ-----')
    try_emove_each(epoks[18], 'ほっぺすりすり', MCat.PHYSICAL, PType.ELECTRIC, 20, 1)
    try_emove_each(epoks[18], 'かみなり', MCat.SPECIAL, PType.ELECTRIC, 110, 1)
    try_emove_each(epoks[19], 'アクアジェット', MCat.PHYSICAL, PType.WATER, 40, 1)


    print ('-----ミモザ-----')
    try_emove_each(epoks[24], 'しねんのずつき', MCat.PHYSICAL, PType.PSYCHIC, 80, 1)
    try_emove_each(epoks[24], 'ドレインパンチ', MCat.PHYSICAL, PType.FIGHTING, 75, 1)
    try_emove_each(epoks[25], 'ふいうち', MCat.PHYSICAL, PType.DARK, 70, 1)
    try_emove_each(epoks[27], 'こおりのつぶて', MCat.PHYSICAL, PType.ICE, 40, 1)

    print ('-----ジニア-----')
    try_emove_each(epoks[30], 'ヘドロばくだん', MCat.SPECIAL, PType.POISON, 90, 1)
    try_emove_each(epoks[30], 'ウェザーボール普', MCat.SPECIAL, PType.NORMAL, 50, 1)
    try_emove_each(epoks[30], 'ウェザーボール晴', MCat.SPECIAL, PType.FIRE, 100, 1)
    try_emove_each(epoks[31], 'しんそく', MCat.PHYSICAL, PType.NORMAL, 80, 1)
    try_emove_each(epoks[34], 'サイコキネシス', MCat.SPECIAL, PType.PSYCHIC, 90, 1)
    try_emove_each(epoks[34], 'なみのり', MCat.SPECIAL, PType.WATER, 90, 1)
    try_emove_each(epoks[34], 'シェルアームズ', MCat.SPECIAL, PType.POISON, 90, 1)
    try_emove_each(epoks[34], 'パワージェム', MCat.SPECIAL, PType.ROCK, 80, 1)

    print ('-----キハダ-----')
    try_emove_each(epoks[36], 'ねこだまし', MCat.PHYSICAL, PType.NORMAL, 40, 1)
    try_emove_each(epoks[36], 'バレットパンチ', MCat.PHYSICAL, PType.STEEL, 40, 1)
    try_emove_each(epoks[36], 'マッハパンチ', MCat.PHYSICAL, PType.FIGHTING, 40, 1)
    try_emove_each(epoks[36], 'トリプルアクセル1回', MCat.PHYSICAL, PType.ICE, 20, 1)
    try_emove_each(epoks[36], 'トリプルアクセル3回', MCat.PHYSICAL, PType.ICE, 120, 1.5)
    try_emove_each(epoks[38], 'アクアジェット', MCat.PHYSICAL, PType.WATER, 40, 1)
    try_emove_each(epoks[39], 'バレットパンチ', MCat.PHYSICAL, PType.STEEL, 40, 1)

    print ('-----ボタン-----')
    try_emove_each(epoks[42], 'あくのはどう', MCat.SPECIAL, PType.DARK, 80, 1)
    try_emove_each(epoks[42], 'でんこうせっか', MCat.PHYSICAL, PType.NORMAL, 40, 1)
    try_emove_each(epoks[42], 'サイコキネシス', MCat.SPECIAL, PType.PSYCHIC, 90, 1)

    try_emove_each(epoks[43], 'でんこうせっか', MCat.PHYSICAL, PType.NORMAL, 40, 1)
    try_emove_each(epoks[44], 'でんこうせっか', MCat.PHYSICAL, PType.NORMAL, 40, 1)
    try_emove_each(epoks[45], 'でんこうせっか', MCat.PHYSICAL, PType.NORMAL, 40, 1)
    try_emove_each(epoks[46], 'でんこうせっか', MCat.PHYSICAL, PType.NORMAL, 40, 1)
    try_emove_each(epoks[47], 'でんこうせっか', MCat.PHYSICAL, PType.NORMAL, 40, 1)

    print ('-----タイム-----')
    try_emove_each(epoks[48], 'がんせきアックス', MCat.PHYSICAL, PType.ROCK, 65, 1.5)
    try_emove_each(epoks[48], 'れんぞくぎり1回目', MCat.PHYSICAL, PType.BUG, 40, 1.5)
    try_emove_each(epoks[48], 'れんぞくぎり2回目', MCat.PHYSICAL, PType.BUG, 80, 1.5)
    try_emove_each(epoks[48], 'つじぎり', MCat.PHYSICAL, PType.DARK, 70, 1.5)
    try_emove_each(epoks[48], 'つばめがえし', MCat.PHYSICAL, PType.FLYING, 60, 1.5)

    try_emove_each(epoks[49], 'アクセルロック', MCat.PHYSICAL, PType.ROCK, 40, 1)

    print ('-----レホール-----')

    try_emove_each(epoks[54], 'ナイトバースト', MCat.SPECIAL, PType.DARK, 85, 1)
    try_emove_each(epoks[54], 'ヘドロばくだん', MCat.SPECIAL, PType.POISON, 90, 1)
    try_emove_each(epoks[54], 'サイコキネシス', MCat.SPECIAL, PType.PSYCHIC, 90, 1)
    try_emove_each(epoks[54], 'かえんほうしゃ', MCat.SPECIAL, PType.FIRE, 90, 1)

    try_emove_each(epoks[58], 'バレットパンチ', MCat.PHYSICAL, PType.STEEL, 40, 1)

    print ('-----セイジ-----')
    try_emove_each(epoks[60], 'サイコキネシス', MCat.SPECIAL, PType.PSYCHIC, 90, 1)
    try_emove_each(epoks[60], 'くさむすび', MCat.SPECIAL, PType.GRASS, 80, 1) # power depends on weight, doble is 58kg
    try_emove_each(epoks[60], 'シャドーボール', MCat.SPECIAL, PType.GHOST, 80, 1)

    try_emove_each(epoks[61], 'ふいうち', MCat.PHYSICAL, PType.DARK, 70, 1)
    try_emove_each(epoks[62], 'ねこだまし', MCat.PHYSICAL, PType.NORMAL, 40, 1)
    
#    print ('-----クラベル-----')
#    try_emove_each(epok[10], 'サイコキネシス', MCat.SPECIAL, PType.PSYCHIC, 90, 1)
#    try_emove_each(epok[10], '10まんボルト', MCat.SPECIAL, PType.ELECTRIC, 90, 1)
#    try_emove_each(epok[10], 'イカサマ', MCat.PHYSICAL, PType.DARK, 95, 1)
#    print ('-----ハッサク-----')
#    try_emove_each(epok[12], 'ボディプレス', MCat.PHYSICAL, PType.FIGHTING, 80, 1)
#    try_emove_each(epok[12], '10まんボルト', MCat.SPECIAL, PType.ELECTRIC, 90, 1)
#    try_emove_each(epok[12], 'りゅうせいぐん', MCat.SPECIAL, PType.DRAGON, 130, 1)






def main():
    init_poks()

   
  
    damage_to_enemy()
    damage_from_enemy()
    

main()
