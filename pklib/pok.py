#!/usr/bin/python3
import sys
import re
import math
import codecs
import csv

class ConstMeta(type):
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError(f'Cannot rebind const ({name})')
        else:
            self.__setattr__(name, value)

class PType(metaclass=ConstMeta):
    NONE = 0

    NORMAL = 1
    FIRE = 2
    WATER= 3
    ELECTRIC = 4
    GRASS = 5

    ICE = 6
    FIGHTING = 7
    POISON = 8
    GROUND = 9
    FLYING = 10

    PSYCHIC = 11
    BUG = 12
    ROCK = 13
    GHOST = 14
    DRAGON = 15

    DARK = 16
    STEEL = 17
    FAIRY = 18


class MCat(metaclass=ConstMeta):
    PHYSICAL = 1
    SPECIAL = 2

class SIDX(metaclass=ConstMeta):
    H = 0
    A = 1
    B = 2
    C = 3
    D = 4
    S = 5

class PokBstat:
    def __init__(self, id, name, t1, t2, h, a, b, c, d, s):
        self.id = id
        self.name = name
        self.t1 = t1
        self.t2 = t2
        self.bstats = [h, a, b, c, d, s]
        
    def getStat(self, idx):
        return self.bstats[idx]

    decodeType = {
        ''       : PType.NONE,
        'ノーマル': PType.NORMAL, 
        'ほのお'  : PType.FIRE,
        'みず'    : PType.WATER,
        'でんき'  : PType.ELECTRIC,
        'くさ'    : PType.GRASS,
        'こおり'  : PType.ICE,
        'かくとう' : PType.FIGHTING,
        'どく'    : PType.POISON,
        'じめん'  : PType.GROUND,
        'ひこう'  : PType.FLYING,
        'エスパー' : PType.PSYCHIC,
        'むし'    : PType.BUG,
        'いわ'    : PType.ROCK,
        'ゴースト' : PType.GHOST,
        'ドラゴン' : PType.DRAGON,
        'あく'     : PType.DARK,
        'はがね'   : PType.STEEL,
        'フェアリー' : PType.FAIRY
    }
    type2Str = {}
    poks = []
    pdict = {}

    @classmethod
    def readPokCsv(cls, csvin):
        lc = 0
        for row in csvin:
            lc += 1
            if lc <= 1:
                continue # skip the first line
            p = PokBstat(int(row[0]), row[1], PokBstat.decodeType[row[2]], PokBstat.decodeType[row[3]],
                         int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]))
            #print("%u %s | %s %s | %u %u %u %u %u %u  %u" % (int(row[0]), row[1], row[2], row[3], int(row[4]), int(row[5]),int(row[6]),int(row[7]),int(row[8]),int(row[9]),int(row[10])))
            PokBstat.poks.append(p)
            if p.name in PokBstat.pdict:
                print('ERROR: %s alrady registered' % p.name, file=sys.stderr)
                sys.exit(1)
            PokBstat.pdict[p.name] = p

    @classmethod
    def open_csv(cls, fname, mode): # mode は 'w' か 'r'

	    ms = '書き込み' if mode == 'w' else '読み込み'

	    try:
		    f  = codecs.open(fname, mode, 'utf_8')
		    cw = csv.writer(f) if mode == 'w' else csv.reader(f)
		    return (f, cw)
	    except:
		    print('エラー:ファイル', fname, 'を', ms, 'モードで開けません', file=sys.stderr)
		    sys.exit(1)


    @classmethod
    def readPoks(cls):
        #print('reading')
        fname = 'pok_bstat_g9.csv'
        (f, cr) = PokBstat.open_csv(fname, 'r')
        PokBstat.readPokCsv(cr)

    @classmethod
    def buildTypeStr(cls):
        for x in PokBstat.decodeType.keys():
            PokBstat.type2Str[PokBstat.decodeType[x]] = x # reverse lookup
    @classmethod
    def init(cls):
        PokBstat.buildTypeStr()
        PokBstat.readPoks()

        
    

class Pokemon:
    
    dftable = [ 
        [ 0], # NONE
        #     N  F  W  E  G    I  F  P  G  F   P  B  R  G  D   D  S  F
        [ 0,  2, 2, 2, 2, 2,   2, 2, 2, 2, 2,  2, 2, 1, 0, 2,  2, 1, 2], # NORMAL
        [ 0,  2, 1, 1, 2, 4,   2, 2, 2, 2, 2,  2, 4, 1, 2, 1,  2, 4, 2], # FIRE
        [ 0,  2, 4, 1, 2, 1,   2, 2, 2, 4, 2,  2, 2, 4, 2, 1,  2, 2, 2], # WATER
        [ 0,  2, 2, 4, 1, 1,   2, 2, 2, 0, 4,  2, 2, 2, 2, 1,  2, 2, 2], # ElECTRIC
        [ 0,  2, 1, 4, 2, 1,   2, 2, 1, 4, 1,  2, 1, 4, 2, 1,  2, 1, 2], # GRASS

        [ 0,  2, 1, 1, 2, 4,   1, 2, 2, 4, 4,  2, 2, 2, 2, 4,  2, 1, 2], # ICE
        [ 0,  4, 2, 2, 2, 2,   4, 2, 1, 2, 1,  1, 1, 4, 0, 2,  4, 4, 1], # FIGHTING
        [ 0,  2, 2, 2, 2, 4,   2, 2, 1, 1, 2,  1, 2, 1, 1, 2,  2, 0, 4], # POISON
        [ 0,  2, 4, 2, 4, 1,   2, 2, 4, 2, 0,  2, 1, 4, 2, 2,  2, 4, 2], # GROUND
        [ 0,  2, 2, 2, 1, 4,   2, 4, 2, 2, 2,  2, 4, 1, 2, 2,  2, 1, 2], # FLYING

        [ 0,  2, 2, 2, 2, 2,   2, 4, 4, 2, 2,  1, 2, 2, 2, 2,  0, 1, 2], # PSYCHIC
        [ 0,  2, 1, 2, 2, 4,   2, 1, 1, 2, 1,  4, 2, 2, 1, 2,  4, 1, 1], # BUG
        [ 0,  2, 4, 2, 2, 2,   4, 1, 2, 1, 4,  2, 4, 2, 2, 2,  2, 1, 2], # ROCK
        [ 0,  0, 2, 2, 2, 2,   2, 2, 2, 2, 2,  4, 2, 2, 4, 2,  1, 2, 2], # GHOST
        [ 0,  2, 2, 2, 2, 2,   2, 2, 2, 2, 2,  2, 2, 2, 2, 4,  2, 1, 0], # DRAGON

        [ 0,  2, 2, 2, 2, 2,   2, 1, 2, 2, 2,  4, 2, 2, 4, 2,  1, 2, 1], # DARK
        [ 0,  2, 1, 1, 1, 2,   4, 2, 2, 2, 2,  2, 2, 4, 2, 2,  2, 1, 4], # STEEL
        [ 0,  2, 1, 2, 2, 2,   2, 4, 1, 2, 2,  2, 2, 2, 2, 4,  4, 1, 2]  # FAIRY

    ]

    nature = {
        'さみしがり' : [ SIDX.A, SIDX.B],
        'いじっぱり' : [ SIDX.A, SIDX.C],
        'やんちゃ'   : [ SIDX.A, SIDX.D],
        'ゆうかん'   : [ SIDX.A, SIDX.S],
        'ずぶとい'   : [ SIDX.B, SIDX.A],
        'わんぱく'   : [ SIDX.B, SIDX.C],
        'のうてんき' : [ SIDX.B, SIDX.D],
        'のんき'     : [ SIDX.B, SIDX.S],
        'ひかえめ'   : [ SIDX.C, SIDX.A],
        'おっとり'   : [ SIDX.C, SIDX.B],
        'うっかりや' : [ SIDX.C, SIDX.D],
        'れいせい'   : [ SIDX.C, SIDX.S],
        'おだやか'   : [ SIDX.D, SIDX.A],
        'おとなしい' : [ SIDX.D, SIDX.B],
        'しんちょう' : [ SIDX.D, SIDX.C],
        'なまいき'   : [ SIDX.D, SIDX.S],
        'おくびょう' : [ SIDX.S, SIDX.A],
        'せっかち'   : [ SIDX.S, SIDX.B],
        'ようき'     : [ SIDX.S, SIDX.C],
        'むじゃき'   : [ SIDX.S, SIDX.D],
        'がんばりや' : [ SIDX.A, SIDX.A],
        'すなお'     : [ SIDX.B, SIDX.B],
        'てれや'     : [ SIDX.C, SIDX.C],
        'きまぐれ'   : [ SIDX.D, SIDX.D],
        'まじめ'     : [ SIDX.S, SIDX.S],

        
    }

    def __init__(self, pname, nname, ttype, lv, feature, pl, eh, ea, eb, ec, ed, es, nat, item):
        if not (pname in PokBstat.pdict):
            print ('Pokemon %s not found' % pname, file=sys.stderr)
            sys.exit(1)
        if not (nat in Pokemon.nature):
            print ('Unknown nature %s for Pokemon %s%s' % (nat, pname, nname))
            sys.exit(1)

        p = PokBstat.pdict[pname]
        self.p = p 
        self.nname = nname
        self.lv = lv
        self.feature = feature
        self.el = [eh,ea,eb,ec,ed,es]
        self.pl = [pl, pl, pl, pl, pl, pl] # set everything to same value first
        x = Pokemon.nature[nat]
        self.upi = x[0]
        self.dni = x[1]
        self.item = item
        self.ttype = ttype
        self.rankf = [1, 1, 1, 1, 1, 1] # adjustment for rank

    def getName(self):
        return self.p.name + self.nname

    def set_plevel(self, mask, val):
        for i in range(0, 6):
            if mask & (1 << i):
                self.pl[i] = val

    def set_elevel(self, h, a, b, c, d, s):
        if h >= 0: self.el[SIDX.H] = h
        if a >= 0: self.el[SIDX.A] = a
        if b >= 0: self.el[SIDX.B] = b
        if c >= 0: self.el[SIDX.C] = c
        if d >= 0: self.el[SIDX.D] = d
        if s >= 0: self.el[SIDX.S] = s

    def get_stat(self, idx):
        if (idx == SIDX.H):
            x = math.floor(self.p.getStat(idx)*2 + self.pl[idx] + self.el[idx]/4)
            x = math.floor(x * self.lv /100 + self.lv + 10)
            return x
        else:
            x = math.floor(self.p.getStat(idx)*2 + self.pl[idx] + self.el[idx]/4)
            x = math.floor(x * self.lv / 100 + 5)
            if (self.upi == idx) and (self.dni != idx):
                x = math.floor(x * 1.1)
            elif (self.dni == idx) and (self.upi != idx):
                x = math.floor(x * 0.9)

            if (self.item == 'とつげきチョッキ') and (idx == SIDX.D):
                #print ('DEBUG: D increased from %f to %f' % (x, math.floor(x*1.5)))
                x = math.floor(x * 1.5)
            x = math.floor(x * self.rankf[idx])
            return x

    def print_stat(self):
        et = self.el[SIDX.H] + self.el[SIDX.A] + self.el[SIDX.B] + \
             self.el[SIDX.C] + self.el[SIDX.D] + self.el[SIDX.S]

        print ('%-20s %-10s %-10s Lv.%u H:%u A:%u B:%u C:%u D:%u S:%u 努力値合計:%u' % 
                (self.getName(),
                PokBstat.type2Str[self.p.t1],
                PokBstat.type2Str[self.p.t2 ],
                self.lv, 
                self.get_stat(SIDX.H), 
                self.get_stat(SIDX.A), 
                self.get_stat(SIDX.B), 
                self.get_stat(SIDX.C), 
                self.get_stat(SIDX.D),
                self.get_stat(SIDX.S),
                et))
    def dfactor(self, mtype):
        if self.ttype != PType.NONE: # Terastal
            f1 = Pokemon.dftable[mtype][self.ttype]
            f2 = 2
        else:
            f1 = Pokemon.dftable[mtype][self.p.t1]
            f2 = Pokemon.dftable[mtype][self.p.t2] if self.p.t2 != PType.NONE else 2
        
        x = f1 * f2 * 0.25
        if (x >= 2) and (self.feature == 'ハードロック'):
            x = x * 0.75
        if (mtype == PType.WATER) and (self.feature == 'ちょすい'):
            x = 0 # any water type weapons are disabled
        if ((mtype == PType.FIRE) or (mtype == PType.ICE)) and (self.feature == 'あついしぼう'):
            x = x * 0.5

        return x


    def damage_to(self, target, mname, mcat, mtype, mpower, scale, is_min):
        df = target.dfactor(mtype)
        x = math.floor(self.lv * 2/5 + 2)

        a = self.get_stat(SIDX.A) if mcat == MCat.PHYSICAL else self.get_stat(SIDX.C)
        if mname == 'イカサマ':
            a = target.get_stat(SIDX.A) # use A of the target instead
        if mname == 'ボディプレス':
            a = self.get_stat(SIDX.B) # use B instead
            
        dcat = mcat # default same as move cat
        if mname == 'サイコショック':
            dcat = MCat.PHYSICAL # use B instead of D
        if self.feature == 'すてみ':
            if (mname == 'ワイルドボルト') or (mname == 'もろはのずつき') or (mname == 'フレアドライブ'):
                mpower = int(mpower * 1.2)
        if self.feature == 'テクニシャン':
            if mpower <= 60:
                mpower = int(mpower * 1.5)
        if (self.feature == 'ヨガパワー') or (self.feature == 'ちからもち'):
            if mcat == MCat.PHYSICAL:
                a *= 2.0 # physical attack is doubled

        
        d = target.get_stat(SIDX.B) if dcat == MCat.PHYSICAL else target.get_stat(SIDX.D)
        tmatchf = 1.5 if (mtype == self.p.t1) or (mtype == self.p.t2) else 1.0
        if mtype == self.ttype:
            tmatchf += 0.5
            
     #   print ('    debug a=%u d=%u df=%f tmatchf=%f scale=%f' % (a, d, df, tmatchf, scale))
        x = math.floor(x * mpower * a/d)
        x = math.floor(x/50 + 2)
        r = 0.85 if is_min else 1.0
     #   print ('DEBUG %f %f %f %f %f' % (scale, scale, scale, scale, scale))
        x = math.floor(x * df * tmatchf *scale*r)
        return (x, df*tmatchf)

