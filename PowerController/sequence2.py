# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:52:24 2026

@author: oku-hiro
"""

interlock = False
relay = [False for _ in range(40000)]


def contact(x, y):
    if relay[x]:
        relay[y] = True
    else:
        relay[y] = False


def verticalOR(x, y):
    for i in range(len(x)):
        if relay[x[i]]:
            relay[y] = True
            return


def horizontalAND(x, y):
    for i in range(len(x)):
        if not relay[x[i]]:
            return
    relay[y] = True


def block1(x, y):
    if relay[x[0]] and not relay[33009]:
        relay[y] = True
    elif relay[x[2]] and relay[33009]:
        relay[y] = True
    elif relay[x[2]]:
        relay[y] = True


def block2(x, y):
    if relay[x[0]] or relay[x[1]] or relay[x[2]]:
        if not relay[31411] or relay[x[2]]:
            relay[y] = True


def block3(x, y):
    if relay[32100] or relay[x[0]]:
        if relay[x[1]]:
            relay[y] = True


def block4(x, y):
    if relay[30000]:
        if relay[x]:
            if not relay[3003]:
                if not relay[3007]:
                    if not relay[31410]:
                        relay[y] = True


def block5(x, y):
    for i in range(len(x)):
        if relay[x[i]]:
            pass
        else:
            return
    if not relay[3003]:
        if not relay[3007]:
            if not relay[31410]:
                relay[y] = True


def horizontalOR(x, y):
    h = int(len(x)/2)
    for i in range(h):
        if relay[x[i]] or not relay[x[i]+h]:
            pass
        else:
            return
    relay[y] = True


def charge_setting_hold():
    if relay[30001] or relay[30002] or relay[16110]:
        if not relay[3003]:
            relay[16110] = True


def sequence1():
    contact(3004, 16108)

    if relay[16108]:
        interlock = True

    for i in range(3):
        contact(3000+i, 30000+i)

    x = [0 for _ in range(2)]
    x[0] = 3011
    x[1] = 3012
    verticalOR(x, 33000)

    x = [0 for _ in range(6)]
    x[0] = 3013
    x[1] = 3014
    x[2] = 3015
    x[3] = 3100
    x[4] = 3101
    x[5] = 3102
    verticalOR(x, 33001)

    for i in range(6):
        x[i] = 3103+i
    verticalOR(x, 33002)

    for i in range(3):
        x[i] = 3113+i
        x[i+3] = 3200+i
    verticalOR(x, 33003)

    for i in range(6):
        x[i] = 3203+i
    verticalOR(x, 33004)

    for i in range(6):
        x[i] = 3209+i
    verticalOR(x, 33005)

    x[0] = 3215
    for i in range(5):
        x[i+1] = 3300+i
    verticalOR(x, 33006)

    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 33000+i
    verticalOR(x, 33008)

    if relay[3002]:
        relay[33009] = True
    elif relay[33009] and relay[33008]:
        relay[33009] = True

    x = [0 for _ in range(3)]
    x[0] = 3011
    x[1] = 30003
    x[2] = 4315
    block1(x, 30003)

    x[0] = 3012
    x[1] = 30004
    x[2] = 4400
    block1(x, 30004)

    x[0] = 3013
    x[1] = 30005
    x[2] = 4401
    block1(x, 30005)

    x[0] = 3014
    x[1] = 30006
    x[2] = 4402
    block1(x, 30006)

    x[0] = 3015
    x[1] = 30007
    x[2] = 4403
    block1(x, 30007)

    x[0] = 3100
    x[1] = 30008
    x[2] = 4404
    block1(x, 30008)

    x[0] = 3101
    x[1] = 30009
    x[2] = 4405
    block1(x, 30009)

    x[0] = 3102
    x[1] = 30010
    x[2] = 4406
    block1(x, 30010)

    x[0] = 3103
    x[1] = 30011
    x[2] = 4407
    block1(x, 30011)

    x[0] = 3104
    x[1] = 30012
    x[2] = 4408
    block1(x, 30012)

    x[0] = 3105
    x[1] = 30013
    x[2] = 4409
    block1(x, 30013)

    x[0] = 3106
    x[1] = 30014
    x[2] = 4410
    block1(x, 30014)

    x[0] = 3107
    x[1] = 30015
    x[2] = 4411
    block1(x, 30015)

    x[0] = 3108
    x[1] = 30100
    x[2] = 4412
    block1(x, 30100)

    for i in range(4):
        contact(3109+i, 30101+i)

    x[0] = 3113
    x[1] = 30105
    x[2] = 4413
    block1(x, 30105)

    x[0] = 3114
    x[1] = 30106
    x[2] = 4414
    block1(x, 30106)

    x[0] = 3115
    x[1] = 30107
    x[2] = 4415
    block1(x, 30107)

    x[0] = 3200
    x[1] = 30108
    x[2] = 4500
    block1(x, 30108)

    x[0] = 3201
    x[1] = 30109
    x[2] = 4501
    block1(x, 30109)

    x[0] = 3202
    x[1] = 30110
    x[2] = 4502
    block1(x, 30110)

    x[0] = 3203
    x[1] = 30111
    x[2] = 4503
    block1(x, 30111)

    x[0] = 3204
    x[1] = 30112
    x[2] = 4504
    block1(x, 30112)

    x[0] = 3205
    x[1] = 30113
    x[2] = 4505
    block1(x, 30113)

    x[0] = 3206
    x[1] = 30114
    x[2] = 4506
    block1(x, 30114)

    x[0] = 3207
    x[1] = 30115
    x[2] = 4507
    block1(x, 30115)

    x[0] = 3208
    x[1] = 30200
    x[2] = 4508
    block1(x, 30200)

    x[0] = 3209
    x[1] = 30201
    x[2] = 4509
    block1(x, 30201)

    x[0] = 3210
    x[1] = 30202
    x[2] = 4510
    block1(x, 30202)

    x[0] = 3211
    x[1] = 30203
    x[2] = 4511
    block1(x, 30203)

    x[0] = 3212
    x[1] = 30204
    x[2] = 4512
    block1(x, 30204)

    x[0] = 3213
    x[1] = 30205
    x[2] = 4513
    block1(x, 30205)

    x[0] = 3214
    x[1] = 30206
    x[2] = 4514
    block1(x, 30206)

    x[0] = 3215
    x[1] = 30207
    x[2] = 4515
    block1(x, 30207)

    x[0] = 3300
    x[1] = 30208
    x[2] = 4600
    block1(x, 30208)

    x[0] = 3301
    x[1] = 30209
    x[2] = 4601
    block1(x, 30209)

    x[0] = 3302
    x[1] = 30210
    x[2] = 4602
    block1(x, 30210)

    x[0] = 3303
    x[1] = 30211
    x[2] = 4603
    block1(x, 30211)

    x[0] = 3304
    x[1] = 30212
    x[2] = 4604
    block1(x, 30212)

    x = [0 for _ in range(2)]
    x[0] = 3305
    x[1] = 4605
    verticalOR(x, 30213)

    x[0] = 3306
    x[1] = 4606
    verticalOR(x, 30214)

    x[0] = 3307
    x[1] = 4607
    verticalOR(x, 30215)

    x[0] = 3308
    x[1] = 4608
    verticalOR(x, 30300)

    x[0] = 3309
    x[1] = 4609
    verticalOR(x, 30301)

    x[0] = 3310
    x[1] = 4610
    verticalOR(x, 30302)

    x[0] = 3311
    x[1] = 4611
    verticalOR(x, 30303)

    x[0] = 3312
    x[1] = 4612
    verticalOR(x, 30304)

    x[0] = 3313
    x[1] = 4613
    verticalOR(x, 30305)

    x[0] = 3314
    x[1] = 4614
    verticalOR(x, 30306)

    x[0] = 3315
    x[1] = 4615
    verticalOR(x, 30307)

    x[0] = 3400
    x[1] = 4700
    verticalOR(x, 30308)

    x[0] = 3401
    x[1] = 4701
    verticalOR(x, 30309)

    x[0] = 3402
    x[1] = 4702
    verticalOR(x, 30310)

    x[0] = 3403
    x[1] = 4703
    verticalOR(x, 30311)

    x[0] = 3404
    x[1] = 4704
    verticalOR(x, 30312)

    x[0] = 3405
    x[1] = 4705
    verticalOR(x, 30313)

    x[0] = 3406
    x[1] = 4706
    verticalOR(x, 30314)

    x[0] = 3407
    x[1] = 4707
    verticalOR(x, 30315)

    x[0] = 3408
    x[1] = 4708
    verticalOR(x, 30800)

    x[0] = 3409
    x[1] = 4709
    verticalOR(x, 30801)

    x[0] = 3410
    x[1] = 4710
    verticalOR(x, 30802)

    x[0] = 3411
    x[1] = 4711
    verticalOR(x, 30803)

    x[0] = 3412
    x[1] = 4712
    verticalOR(x, 30804)

    x = [0 for _ in range(7)]
    x[0] = 4315
    for i in range(6):
        x[i+1] = 4400+i
    verticalOR(x, 31400)

    for i in range(7):
        x[i] = 4406+i
    verticalOR(x, 31401)

    for i in range(3):
        x[i] = 4413+i
    for i in range(4):
        x[i+3] = 4500+i
    verticalOR(x, 31402)

    for i in range(7):
        x[i] = 4504+i
    verticalOR(x, 31403)

    for i in range(5):
        x[i] = 4511+i
    x[5] = 4600
    x[6] = 4601
    verticalOR(x, 31404)

    for i in range(7):
        x[i] = 4602+i
    verticalOR(x, 31405)

    for i in range(7):
        x[i] = 4609+i
    verticalOR(x, 31406)

    for i in range(7):
        x[i] = 4700+i
    verticalOR(x, 31407)

    for i in range(6):
        x[i] = 4707+i
    x[6] = 31400
    verticalOR(x, 31408)

    for i in range(7):
        x[i] = 31401+i
    verticalOR(x, 31409)

    x = [0 for _ in range(2)]
    x[0] = 31408
    x[1] = 31409
    verticalOR(x, 30410)

    # timer
    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 30003+i
    verticalOR(x, 31412)

    for i in range(6):
        x[i] = 30010+i
    x[6] = 30100
    verticalOR(x, 31413)

    x = [0 for _ in range(6)]
    for i in range(4):
        x[i] = 30101+i
    x[4] = 31412
    x[5] = 31413
    verticalOR(x, 10000)


def sequence2():
    if relay[3006] or relay[10000] or relay[31410]:
        interlock = True

    x = [0 for _ in range(3)]
    x[0] = 30003
    x[1] = 30813
    x[2] = 4315
    block2(x, 10002)

    x[0] = 30004
    x[1] = 30814
    x[2] = 4400
    block2(x, 10003)

    x[0] = 30005
    x[1] = 30815
    x[2] = 4401
    block2(x, 10004)

    x[0] = 30105
    x[1] = 30900
    x[2] = 4413
    block2(x, 10005)

    x[0] = 30201
    x[1] = 30901
    x[2] = 4509
    block2(x, 10006)

    x[0] = 30006
    x[1] = 30902
    x[2] = 4402
    block2(x, 10007)

    x[0] = 30106
    x[1] = 30903
    x[2] = 4414
    block2(x, 10008)

    x[0] = 30202
    x[1] = 30904
    x[2] = 4510
    block2(x, 10009)

    x[0] = 30007
    x[1] = 30905
    x[2] = 4403
    block2(x, 10010)

    x[0] = 30107
    x[1] = 30906
    x[2] = 4415
    block2(x, 10011)

    x[0] = 30203
    x[1] = 30907
    x[2] = 4511
    block2(x, 10012)

    x[0] = 30008
    x[1] = 30908
    x[2] = 4404
    block2(x, 10013)

    x[0] = 30108
    x[1] = 30909
    x[2] = 4500
    block2(x, 10014)

    x[0] = 30204
    x[1] = 30910
    x[2] = 4512
    block2(x, 10015)

    x[0] = 30009
    x[1] = 30911
    x[2] = 4405
    block2(x, 10100)

    x[0] = 30109
    x[1] = 30912
    x[2] = 4501
    block2(x, 10101)

    x[0] = 30205
    x[1] = 30913
    x[2] = 4513
    block2(x, 10102)

    x[0] = 30010
    x[1] = 30914
    x[2] = 4406
    block2(x, 10103)

    x[0] = 30110
    x[1] = 30915
    x[2] = 4502
    block2(x, 10104)

    x[0] = 30206
    x[1] = 31000
    x[2] = 4514
    block2(x, 10105)

    x[0] = 30011
    x[1] = 31001
    x[2] = 4407
    block2(x, 10106)

    x[0] = 30111
    x[1] = 31002
    x[2] = 4503
    block2(x, 10107)

    x[0] = 30207
    x[1] = 31003
    x[2] = 4515
    block2(x, 10108)

    x[0] = 30012
    x[1] = 31004
    x[2] = 4408
    block2(x, 10109)

    x[0] = 30112
    x[1] = 31005
    x[2] = 4504
    block2(x, 10110)

    x[0] = 30208
    x[1] = 31006
    x[2] = 4600
    block2(x, 10111)

    x[0] = 30013
    x[1] = 31007
    x[2] = 4409
    block2(x, 10112)

    x[0] = 30113
    x[1] = 31008
    x[2] = 4505
    block2(x, 10113)

    x[0] = 30209
    x[1] = 31009
    x[2] = 4601
    block2(x, 10114)

    x[0] = 30014
    x[1] = 31010
    x[2] = 4410
    block2(x, 10115)

    x[0] = 30114
    x[1] = 31011
    x[2] = 4506
    block2(x, 11000)

    x[0] = 30210
    x[1] = 31012
    x[2] = 4602
    block2(x, 11001)

    x[0] = 30015
    x[1] = 31013
    x[2] = 4411
    block2(x, 11002)

    x[0] = 30115
    x[1] = 31014
    x[2] = 4507
    block2(x, 11003)

    x[0] = 30211
    x[1] = 31015
    x[2] = 4603
    block2(x, 11004)

    x[0] = 30100
    x[1] = 31100
    x[2] = 4412
    block2(x, 11005)

    x[0] = 30200
    x[1] = 31101
    x[2] = 4508
    block2(x, 11006)

    x[0] = 30212
    x[1] = 31102
    x[2] = 4604
    block2(x, 11007)

    x[0] = 30213
    x[1] = 31103
    x[2] = 4605
    block2(x, 11008)

    x[0] = 30214
    x[1] = 31104
    x[2] = 4606
    block2(x, 11009)

    x[0] = 30215
    x[1] = 31105
    x[2] = 4607
    block2(x, 11010)

    x[0] = 30300
    x[1] = 31106
    x[2] = 4608
    block2(x, 11011)

    x[0] = 30301
    x[1] = 31107
    x[2] = 4609
    block2(x, 11012)

    x[0] = 30302
    x[1] = 31108
    x[2] = 4610
    block2(x, 11013)

    x[0] = 30303
    x[1] = 31109
    x[2] = 4611
    block2(x, 11014)

    x[0] = 30304
    x[1] = 31110
    x[2] = 4612
    block2(x, 11015)

    x[0] = 30305
    x[1] = 31111
    x[2] = 4613
    block2(x, 11100)

    x[0] = 30306
    x[1] = 31112
    x[2] = 4614
    block2(x, 11101)

    x[0] = 30307
    x[1] = 31113
    x[2] = 4615
    block2(x, 11102)

    x[0] = 30308
    x[1] = 31114
    x[2] = 4700
    block2(x, 11103)

    x[0] = 30309
    x[1] = 31115
    x[2] = 4701
    block2(x, 11104)

    x[0] = 30310
    x[1] = 31200
    x[2] = 4702
    block2(x, 11105)

    x[0] = 30311
    x[1] = 31201
    x[2] = 4703
    block2(x, 11106)

    x[0] = 30312
    x[1] = 31202
    x[2] = 4704
    block2(x, 11107)

    x[0] = 30313
    x[1] = 31203
    x[2] = 4705
    block2(x, 11108)

    x[0] = 30314
    x[1] = 31204
    x[2] = 4706
    block2(x, 11109)

    x[0] = 30315
    x[1] = 31205
    x[2] = 4707
    block2(x, 11110)

    x[0] = 30800
    x[1] = 31206
    x[2] = 4708
    block2(x, 11111)

    x[0] = 30801
    x[1] = 31207
    x[2] = 4709
    block2(x, 11112)

    x[0] = 30802
    x[1] = 31208
    x[2] = 4710
    block2(x, 11113)

    x[0] = 30803
    x[1] = 31209
    x[2] = 4711
    block2(x, 11114)

    x[0] = 30804
    x[1] = 31210
    x[2] = 4712
    block2(x, 11115)

    x = [0 for _ in range(2)]
    x[0] = 30105
    x[1] = 30900
    verticalOR(x, 14000)

    x[0] = 30106
    x[1] = 30903
    verticalOR(x, 14001)

    x[0] = 30107
    x[1] = 30906
    verticalOR(x, 14002)

    x[0] = 30108
    x[1] = 30909
    verticalOR(x, 14003)

    x[0] = 30109
    x[1] = 30912
    verticalOR(x, 14004)

    x[0] = 30110
    x[1] = 30915
    verticalOR(x, 14005)

    x[0] = 30111
    x[1] = 31002
    verticalOR(x, 14006)

    x[0] = 30112
    x[1] = 31005
    verticalOR(x, 14007)

    x[0] = 30113
    x[1] = 31008
    verticalOR(x, 14008)

    x[0] = 30114
    x[1] = 31011
    verticalOR(x, 14009)

    x[0] = 30115
    x[1] = 31014
    verticalOR(x, 14010)

    x[0] = 30200
    x[1] = 31101
    verticalOR(x, 14011)

    x[0] = 30201
    x[1] = 30901
    verticalOR(x, 14012)

    x[0] = 30202
    x[1] = 30904
    verticalOR(x, 14013)

    x[0] = 30203
    x[1] = 30907
    verticalOR(x, 14014)

    x[0] = 30204
    x[1] = 30910
    verticalOR(x, 14015)

    x[0] = 30205
    x[1] = 30913
    verticalOR(x, 14100)

    x[0] = 30206
    x[1] = 31000
    verticalOR(x, 14101)

    x[0] = 30207
    x[1] = 31003
    verticalOR(x, 14102)

    x[0] = 30208
    x[1] = 31006
    verticalOR(x, 14103)

    x[0] = 30209
    x[1] = 31009
    verticalOR(x, 14104)

    x[0] = 30210
    x[1] = 31012
    verticalOR(x, 14105)

    x[0] = 30211
    x[1] = 31015
    verticalOR(x, 14106)

    x[0] = 30212
    x[1] = 31102
    verticalOR(x, 14107)

    x[0] = 30213
    x[1] = 31103
    verticalOR(x, 14108)

    x[0] = 30214
    x[1] = 31104
    verticalOR(x, 14109)

    x[0] = 30215
    x[1] = 31105
    verticalOR(x, 14110)

    x[0] = 30300
    x[1] = 31106
    verticalOR(x, 14111)

    x[0] = 30301
    x[1] = 31107
    verticalOR(x, 14112)

    x[0] = 30302
    x[1] = 31108
    verticalOR(x, 14113)

    x[0] = 30303
    x[1] = 31109
    verticalOR(x, 14114)

    x[0] = 30304
    x[1] = 31110
    verticalOR(x, 14115)

    x[0] = 30305
    x[1] = 31111
    verticalOR(x, 15000)

    x[0] = 30306
    x[1] = 31112
    verticalOR(x, 15001)

    x[0] = 30307
    x[1] = 31113
    verticalOR(x, 15002)

    x[0] = 30308
    x[1] = 31114
    verticalOR(x, 15003)

    x[0] = 30309
    x[1] = 31115
    verticalOR(x, 15004)

    x[0] = 30310
    x[1] = 31200
    verticalOR(x, 15005)

    x[0] = 30311
    x[1] = 31201
    verticalOR(x, 15006)

    x[0] = 30312
    x[1] = 31202
    verticalOR(x, 15007)

    x[0] = 30313
    x[1] = 31203
    verticalOR(x, 15008)

    x[0] = 30314
    x[1] = 31204
    verticalOR(x, 15009)

    x[0] = 30315
    x[1] = 31205
    verticalOR(x, 15010)

    x[0] = 30800
    x[1] = 31206
    verticalOR(x, 15011)

    x[0] = 30801
    x[1] = 31207
    verticalOR(x, 15012)

    x[0] = 30802
    x[1] = 31208
    verticalOR(x, 15013)

    x[0] = 30803
    x[1] = 31209
    verticalOR(x, 15014)

    x[0] = 30804
    x[1] = 31210
    verticalOR(x, 15015)


def sequence3():
    x = [0 for _ in range(7)]
    x[0] = 4213
    x[1] = 4214
    x[2] = 4215
    x[3] = 4300
    x[4] = 4301
    x[5] = 4302
    x[6] = 4303
    block2(x, 31600)

    for i in range(7):
        x[i] = 4304+i
    block2(x, 31601)

    x = [0 for _ in range(7)]
    for i in range(4):
        x[i] = 4311+i
    x[4] = 31600
    x[5] = 31601
    block2(x, 31602)


def sequence4():
    if not relay[32715] and relay[30000] and not relay[3007] and not relay[31410]:
        if relay[16108]:
            relay[32100] = True
    elif relay[31602]:
        if relay[16108]:
            relay[32100] = True

    x = [0 for _ in range(2)]
    x[0] = 31608
    x[1] = 10002
    block3(x, 12000)

    x[0] = 31612
    x[1] = 10003
    block3(x, 12001)

    x[0] = 31700
    x[1] = 10004
    block3(x, 12002)

    x[0] = 31704
    x[1] = 10007
    block3(x, 12003)

    x[0] = 31708
    x[1] = 10010
    block3(x, 12004)

    x[0] = 31712
    x[1] = 10013
    block3(x, 12005)

    x[0] = 31800
    x[1] = 10100
    block3(x, 12006)

    x[0] = 31804
    x[1] = 10103
    block3(x, 12007)

    x[0] = 31808
    x[1] = 10106
    block3(x, 12008)

    x[0] = 31812
    x[1] = 10109
    block3(x, 12009)

    x[0] = 31900
    x[1] = 10112
    block3(x, 12010)

    x[0] = 31904
    x[1] = 10115
    block3(x, 12011)

    x[0] = 31908
    x[1] = 11002
    block3(x, 12012)

    x[0] = 31912
    x[1] = 11005
    block3(x, 12013)

    x[0] = 32100
    x[1] = 32000
    verticalOR(x, 32108)


def sequence5():
    if relay[32108]:
        interlock = True

    contact(14000, 12014)
    contact(14001, 12015)
    for i in range(10):
        contact(14002+i, 12100+i)
    interlock = False


def sequence6():
    x = [0 for _ in range(2)]
    x[0] = 32100
    x[1] = 32004
    verticalOR(x, 32109)

    if relay[32109]:
        interlock = True

    for i in range(4):
        contact(14012+i, 12110+i)
    contact(14100, 12114)
    contact(14101, 12115)

    for i in range(6):
        contact(14102+i, 13000+i)


def sequence7():
    block4(12000, 32200)

    x = [0 for _ in range(3)]
    x[0] = 30002
    x[1] = 30003
    x[2] = 32200
    horizontalAND(x, 16008)

    block4(12001, 32201)
    x[0] = 30002
    x[1] = 30004
    x[2] = 32201
    horizontalAND(x, 16009)

    block4(12002, 32202)
    x[0] = 30002
    x[1] = 30005
    x[2] = 32202
    horizontalAND(x, 16010)

    block4(12003, 32203)
    x[0] = 30002
    x[1] = 30006
    x[2] = 32203
    horizontalAND(x, 16011)

    block4(12004, 32204)
    x[0] = 30002
    x[1] = 30007
    x[2] = 32204
    horizontalAND(x, 16012)

    block4(12005, 32205)
    x[0] = 30002
    x[1] = 30008
    x[2] = 32205
    horizontalAND(x, 16013)

    block4(12006, 32206)
    x[0] = 30002
    x[1] = 30009
    x[2] = 32206
    horizontalAND(x, 16014)

    block4(12007, 32207)
    x[0] = 30002
    x[1] = 30010
    x[2] = 32207
    horizontalAND(x, 16015)

    block4(12008, 32208)
    x[0] = 30002
    x[1] = 30011
    x[2] = 32208
    horizontalAND(x, 16100)

    block4(12009, 32209)
    x[0] = 30002
    x[1] = 30012
    x[2] = 32209
    horizontalAND(x, 16101)

    block4(12010, 32210)
    x[0] = 30002
    x[1] = 30013
    x[2] = 32210
    horizontalAND(x, 16102)

    block4(12011, 32211)
    x[0] = 30002
    x[1] = 30014
    x[2] = 32211
    horizontalAND(x, 16103)

    block4(12012, 32212)
    x[0] = 30002
    x[1] = 30015
    x[2] = 32212
    horizontalAND(x, 16104)

    block4(12013, 32213)
    x[0] = 30002
    x[1] = 30100
    x[2] = 32213
    horizontalAND(x, 16105)

    x = [0 for _ in range(7)]
    x[0] = 12014
    x[1] = 12015
    x[2] = 12100
    x[3] = 12101
    x[4] = 12102
    x[5] = 12103
    x[6] = 12104
    verticalOR(x, 32214)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 12105+i
    x[5] = 32214
    block5(x, 32215)

    x = [0 for _ in range(4)]
    x[0] = 30002
    x[1] = 30101
    x[2] = 30000
    x[3] = 32215
    horizontalAND(x, 16106)

    x = [0 for _ in range(7)]
    for i in range(6):
        x[i] = 12110+i
    x[6] = 13000
    verticalOR(x, 32300)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 13001+i
    x[5] = 32300
    block5(x, 32301)

    x = [0 for _ in range(4)]
    x[0] = 30002
    x[1] = 30102
    x[2] = 30000
    x[3] = 32301
    horizontalAND(x, 16107)

    x = [0 for _ in range(2)]
    x[0] = 4213
    x[1] = 16008
    horizontalAND(x, 15108)

    x[0] = 4214
    x[1] = 16009
    horizontalAND(x, 15109)

    x[0] = 4215
    x[1] = 16010
    horizontalAND(x, 15110)

    x[0] = 4300
    x[1] = 16011
    horizontalAND(x, 15111)

    x[0] = 4301
    x[1] = 16012
    horizontalAND(x, 15112)

    x[0] = 4302
    x[1] = 16013
    horizontalAND(x, 15113)

    x[0] = 4303
    x[1] = 16014
    horizontalAND(x, 15114)

    x[0] = 4304
    x[1] = 16015
    horizontalAND(x, 15115)

    x[0] = 4305
    x[1] = 16100
    horizontalAND(x, 16000)

    x[0] = 4306
    x[1] = 16101
    horizontalAND(x, 16001)

    x[0] = 4307
    x[1] = 16102
    horizontalAND(x, 16002)

    x[0] = 4308
    x[1] = 16103
    horizontalAND(x, 16003)

    x[0] = 4309
    x[1] = 16104
    horizontalAND(x, 16004)

    x[0] = 4310
    x[1] = 16105
    horizontalAND(x, 16005)

    x = [0 for _ in range(7)]
    for i in range(3):
        x[i] = 3913+i
    for i in range(4):
        x[i+3] = 4000+i
    verticalOR(x, 32308)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 4004+i
    x[5] = 32308
    verticalOR(x, 32309)

    x = [0 for _ in range(12)]
    x[0] = 3913
    x[1] = 3914
    x[2] = 3915
    x[3] = 4000
    x[4] = 4001
    x[5] = 4002
    x[6] = 12014
    x[7] = 12015
    x[8] = 12100
    x[9] = 12101
    x[10] = 12102
    x[11] = 12103
    horizontalOR(x, 32310)

    for i in range(6):
        x[i] = 4003+i
        x[i+6] = 12104+i
    horizontalOR(x, 32311)

    x = [0 for _ in range(5)]
    x[0] = 32309
    x[1] = 32310
    x[2] = 32311
    x[3] = 16106
    x[4] = 4311
    horizontalAND(x, 16006)

    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 4009+i
    verticalOR(x, 32312)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 4100+i
    x[5] = 32312
    verticalOR(x, 32313)

    x = [0 for _ in range(12)]
    for i in range(6):
        x[i] = 4009+i
        x[i+6] = 12110+i
    horizontalOR(x, 32314)

    x[0] = 4015
    for i in range(5):
        x[i+1] = 4100+i
    for i in range(6):
        x[i+6] = 13000+i
    horizontalOR(x, 32315)

    x = [0 for _ in range(5)]
    x[0] = 32313
    x[1] = 32314
    x[2] = 32315
    x[3] = 16107
    x[4] = 4312
    horizontalAND(x, 16007)

    charge_setting_hold()

    tim5 = False
    if relay[3003]:
        tim5 = True

    if tim5 and not relay[16112]:
        relay[16109] = True

    if tim5:
        relay[16112] = True

    x = [0 for _ in range(6)]
    x[0] = 3913
    x[1] = 3914
    x[2] = 3915
    x[3] = 4000
    x[4] = 4001
    x[5] = 4002
    verticalOR(x, 32408)

    x = [0 for _ in range(7)]
    for i in range(6):
        x[i] = 4003+i
    x[6] = 32408
    verticalOR(x, 32409)

    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 4009+i
    verticalOR(x, 32410)

    x = [0 for _ in range(7)]
    x[0] = 4015
    for i in range(5):
        x[i+1] = 4100+i
    x[6] = 32410
    verticalOR(x, 32411)

    x = [0 for _ in range(4)]
    x[0] = 32409
    x[1] = 32411
    x[2] = 32413
    x[3] = 32415
    verticalOR(x, 32500)

    if relay[30001] or relay[30002] or relay[32512]:
        if not relay[3003]:
            relay[32512] = True

    if relay[32512] and not relay[30001] and not relay[30002]:
        relay[32513] = True

    tim4 = False
    if relay[32513]:
        tim4 = True

    if relay[32511] or tim4:
        relay[32715] = True


sequence1()
sequence2()
sequence3()
sequence4()
sequence5()
sequence6()
sequence7()
