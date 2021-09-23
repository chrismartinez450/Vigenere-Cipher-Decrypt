import string

decrypted = ""
key = "thisisakey"
message = "Pomf wvorggn uweec ral kpsdyaq nzge, kw mom amn fczpvk lo wcm. Lice gykl lpst cmn lgv't gmfl lw kxsu, " \
          "i bzixk moil'k mejell zwgbir. Vgb wrer fwm lri mk ezil iss kw, lhbsszowmb a gyklnjmw issmo. Ql'c uahb ggu " \
          "hmg'b ggu'pj jwem ty pnl, ezex rbtm zwvoejl ql'k dvsmo. Bzebi bz oqkdyq mv tm hkh yywe eicxydlv egrnw tul " \
          "iutc. "
i = 0

for n in message:
    if n in string.ascii_lowercase:
        o = ord(key[i]) - ord('a')
        a = ord(n) - ord('a') - o

        if a < 0:
            a = a + 26

        b = chr(a + ord('a'))

        decrypted = decrypted + b
        i = (i + 1) % len(key)
    elif n in string.ascii_uppercase:
        o = ord(key[i]) - ord('a')
        a = ord(n) - ord('a') - o

        if a < 0:
            a = a + 26

        b = chr(a + ord('a'))

        decrypted = decrypted + b
        i = (i + 1) % len(key)

    else:
        decrypted = decrypted + n
        i = (i + 1) % len(key)

print("decrypted text: " + decrypted)