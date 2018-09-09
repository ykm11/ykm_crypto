from Crypto.Util.number import *
import gmpy
import random
from keys import flag

def gen_key(k):
    p = getPrime(k)
    g = 2
    x = getRandomNumber(16)
    h = pow(g, x, p)
    assert g**x > p 

    return p, g, h

def enc(pk, m):
    p, g, h = pk
    r = getRandomNumber(16)

    c1 = pow(g, r, p)
    c2 = 17*m * pow(h, r, p) % p

    return c1, c2

pk = gen_key(1024)
m = bytes_to_long(flag)

print("[+] PubKey :", pk)
c1, c2 = enc(pk, m)
print("[+] c1, c2 :", (c1, c2))


# [+] PubKey : (140969531702276155448103246114478091725378661636662449997553410887493703383534220430068982847482245885743431453576380844929210717508369470205473918149777507520264947370873081657364162957918776876091005103072154098647644265635258225648894957225271310642744330597800725351848210191556982786419597233397584912423, 2, 121960557335594087942948498678869036153299775004295264104656415197399825063753886929904632313007463757773945749222038443060562693356948463307749236414226821205171204536287984191105384761649793150897468474639079479879394047074349411948504583960487661168262174558495068260698534531740255980434327116168839818125)
# [+] c1, c2 : (79443312981739807977625577089354338584494906283931740266512648132218171616084645102184172560034666395621826905915239888694149096477447500950922791631308190555760632577676655275458662508180624586849456814587753657358732984158401526266256063550221724198749424515827465320038975973844289877287092864647337052632, 83059509413459839516076429747548497912344634874524697111293355813482825972926115208528257632764126475445951881072267111183320072651233473513023935176087864512363030217387525957316188541731272632527840808196481229065781466468724742888708790368240771943717547582823606802832388601633077132046314575296561415830)

import hashlib
print(hashlib.sha1(flag).hexdigest())
# 4328e994b99c6c22e84e869088890a65adf9c128