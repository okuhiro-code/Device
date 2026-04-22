#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:15:52 2026

@author: hiro
"""

relay = [False for _ in range(40000)]
tim = [False for _ in range(100)]


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


def contact(x, y):
    if relay[x]:
        relay[y] = True
    else:
        relay[y] = False


def groun_open_condition():
    if relay[30000] and not relay[3007] and not relay[30911] and not relay[31807]:
        if relay[3004]:
            relay[31101] = True
            return

    x = [0 for _ in range(5)]
    x[0] = 4313
    x[1] = 4314
    x[2] = 4315
    x[3] = 4400
    x[4] = 4401

    for i in range(5):
        if relay[x[i]]:
            if relay[3004]:
                relay[31101] = True
                return


def horizontalOR1(x, y):
    h = int(len(x)/2)
    for i in range(h):
        if relay[x[i]] or relay[x[i]+h]:
            pass
        else:
            return
    relay[y] = True


def horizontalOR2(x, y):
    h = int(len(x)/2)
    for i in range(h):
        if relay[x[i]] or not relay[x[i]+h]:
            pass
        else:
            return
    relay[y] = True


def block1(x, y):
    if relay[x[0]] and not relay[33009]:
        relay[y] = True
    elif relay[x[1]] and relay[33009]:
        relay[y] = True
    elif relay[x[2]]:
        relay[y] = True


def block2(x, y):
    if relay[x[0]] or relay[x[1]] or relay[x[2]]:
        if not relay[30912] or not relay[x[2]]:
            relay[y] = True
            return


def block3(x, y):
    for i in range(len(x)):
        if relay[x[i]]:
            if not relay[3003] and not relay[3007] and not relay[30911]:
                relay[y] = True
                return


def block4(x1, x2, y):
    h = int(len(x1)/2)
    for i in range(h):
        if relay[x1[i]] or relay[x1[i]+h]:
            pass
        else:
            return
    if relay[x2]:
        relay[y] = True


def block5(x1, x2, y):
    h = int(len(x1)/2)
    for i in range(h):
        if relay[x1[i]] or relay[x1[i]+h]:
            pass
        else:
            return

    for i in range(len(x2)):
        if relay[x2[i]]:
            pass
        else:
            return
    relay[y] = True


def sequence1():
    x = [0 for _ in range(6)]
    x[0] = 3114
    x[1] = 3115
    x[2] = 3200
    x[3] = 3201
    x[4] = 3202
    x[5] = 3203
    verticalOR(x, 33000)

    for i in range(6):
        x[i] = 3204+i
    verticalOR(x, 33001)

    for i in range(6):
        x[i] = 3210+i
    verticalOR(x, 33002)

    for i in range(6):
        x[i] = 3300+i
    verticalOR(x, 33003)

    for i in range(6):
        x[i] = 3306+i
    verticalOR(x, 33004)

    x[0] = 3312
    x[1] = 3313
    x[2] = 3314
    x[3] = 3315
    x[4] = 3400
    x[5] = 3401
    verticalOR(x, 33005)

    for i in range(6):
        x[i] = 3402+i
    verticalOR(x, 33006)

    for i in range(6):
        x[i] = 3408+i
    verticalOR(x, 33007)

    x = [0 for _ in range(8)]
    for i in range(8):
        x[i] = 33000+i
    verticalOR(x, 33008)

    if relay[3002]:
        relay[33009] = True
    elif relay[33009] and relay[33008]:
        relay[33009] = True

    contact(3000, 30000)
    contact(3001, 30001)
    contact(3002, 30002)
    contact(3011, 30011)
    contact(3012, 30012)
    contact(3013, 30013)
    contact(3014, 30014)
    contact(3015, 30015)

    x = [0 for _ in range(2)]
    x[0] = 3100
    x[1] = 4402
    verticalOR(x, 30100)

    x[0] = 3101
    x[1] = 4403
    verticalOR(x, 30101)

    x[0] = 3102
    x[1] = 4404
    verticalOR(x, 30102)

    x[0] = 3103
    x[1] = 4405
    verticalOR(x, 30103)

    x[0] = 3104
    x[1] = 4406
    verticalOR(x, 30104)

    x[0] = 3105
    x[1] = 4407
    verticalOR(x, 30105)

    x[0] = 3106
    x[1] = 4408
    verticalOR(x, 30106)

    x[0] = 3107
    x[1] = 4409
    verticalOR(x, 30107)

    x[0] = 3108
    x[1] = 4410
    verticalOR(x, 30108)

    x[0] = 3109
    x[1] = 4411
    verticalOR(x, 30109)

    x[0] = 3110
    x[1] = 4412
    verticalOR(x, 30110)

    x[0] = 3111
    x[1] = 4413
    verticalOR(x, 30111)

    x[0] = 3112
    x[1] = 4414
    verticalOR(x, 30112)

    x[0] = 3113
    x[1] = 4415
    verticalOR(x, 30113)

    x = [0 for _ in range(3)]
    x[0] = 3114
    x[1] = 30114
    x[2] = 4500
    block1(x, 30114)

    x[0] = 3115
    x[1] = 30115
    x[2] = 4501
    block1(x, 30115)

    x[0] = 3200
    x[1] = 30200
    x[2] = 4502
    block1(x, 30200)

    x[0] = 3201
    x[1] = 30201
    x[2] = 4503
    block1(x, 30201)

    x[0] = 3202
    x[1] = 30202
    x[2] = 4504
    block1(x, 30202)

    x[0] = 3203
    x[1] = 30203
    x[2] = 4505
    block1(x, 30203)

    x[0] = 3204
    x[1] = 30204
    x[2] = 4506
    block1(x, 30204)

    x[0] = 3205
    x[1] = 30205
    x[2] = 4507
    block1(x, 30205)

    x[0] = 3206
    x[1] = 30206
    x[2] = 4508
    block1(x, 30206)

    x[0] = 3207
    x[1] = 30207
    x[2] = 4509
    block1(x, 30207)

    x[0] = 3208
    x[1] = 30208
    x[2] = 4510
    block1(x, 30208)

    x[0] = 3209
    x[1] = 30209
    x[2] = 4511
    block1(x, 30209)

    x[0] = 3210
    x[1] = 30210
    x[2] = 4512
    block1(x, 30210)

    x[0] = 3211
    x[1] = 30211
    x[2] = 4513
    block1(x, 30211)

    x[0] = 3212
    x[1] = 30212
    x[2] = 4514
    block1(x, 30212)

    x[0] = 3213
    x[1] = 30213
    x[2] = 4515
    block1(x, 30213)

    x[0] = 3214
    x[1] = 30214
    x[2] = 4600
    block1(x, 30214)

    x[0] = 3215
    x[1] = 30215
    x[2] = 4601
    block1(x, 30215)

    x[0] = 3300
    x[1] = 30300
    x[2] = 4602
    block1(x, 30300)

    x[0] = 3301
    x[1] = 30301
    x[2] = 4603
    block1(x, 30301)

    x[0] = 3302
    x[1] = 30302
    x[2] = 4604
    block1(x, 30302)

    x[0] = 3303
    x[1] = 30303
    x[2] = 4605
    block1(x, 30303)

    x[0] = 3304
    x[1] = 30304
    x[2] = 4606
    block1(x, 30304)

    x[0] = 3305
    x[1] = 30305
    x[2] = 4607
    block1(x, 30305)

    x[0] = 3306
    x[1] = 30306
    x[2] = 4608
    block1(x, 30306)

    x[0] = 3307
    x[1] = 30307
    x[2] = 4609
    block1(x, 30307)

    x[0] = 3308
    x[1] = 30308
    x[2] = 4610
    block1(x, 30308)

    x[0] = 3309
    x[1] = 30309
    x[2] = 4611
    block1(x, 30309)

    x[0] = 3310
    x[1] = 30310
    x[2] = 4612
    block1(x, 30310)

    x[0] = 3311
    x[1] = 30311
    x[2] = 4613
    block1(x, 30311)

    x[0] = 3312
    x[1] = 30312
    x[2] = 4614
    block1(x, 30312)

    x[0] = 3313
    x[1] = 30313
    x[2] = 4615
    block1(x, 30313)

    x[0] = 3314
    x[1] = 30314
    x[2] = 4700
    block1(x, 30314)

    x[0] = 3315
    x[1] = 30315
    x[2] = 4701
    block1(x, 30315)

    x[0] = 3400
    x[1] = 30400
    x[2] = 4702
    block1(x, 30400)

    x[0] = 3401
    x[1] = 30401
    x[2] = 4703
    block1(x, 30401)

    x[0] = 3402
    x[1] = 30402
    x[2] = 4704
    block1(x, 30402)

    x[0] = 3403
    x[1] = 30403
    x[2] = 4705
    block1(x, 30403)

    x[0] = 3404
    x[1] = 30404
    x[2] = 4706
    block1(x, 30404)

    x[0] = 3405
    x[1] = 30405
    x[2] = 4707
    block1(x, 30405)

    x[0] = 3406
    x[1] = 30406
    x[2] = 4708
    block1(x, 30406)

    x[0] = 3407
    x[1] = 30407
    x[2] = 4709
    block1(x, 30407)

    x[0] = 3408
    x[1] = 30408
    x[2] = 4710
    block1(x, 30408)

    x[0] = 3409
    x[1] = 30409
    x[2] = 4711
    block1(x, 30409)

    x[0] = 3410
    x[1] = 30410
    x[2] = 4712
    block1(x, 30410)

    x[0] = 3411
    x[1] = 30411
    x[2] = 4713
    block1(x, 30411)

    x[0] = 3412
    x[1] = 30412
    x[2] = 4714
    block1(x, 30412)

    x[0] = 3413
    x[1] = 30413
    x[2] = 4715
    block1(x, 30413)


def sequence2():
    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 4402+i
    verticalOR(x, 30901)

    for i in range(7):
        x[i] = 4409+i
    verticalOR(x, 30902)

    for i in range(7):
        x[i] = 4500+i
    verticalOR(x, 30903)

    for i in range(7):
        x[i] = 4507+i
    verticalOR(x, 30904)

    x[0] = 4514
    x[1] = 4515
    x[2] = 4600
    x[3] = 4601
    x[4] = 4602
    x[5] = 4603
    x[6] = 4604
    verticalOR(x, 30905)

    for i in range(7):
        x[i] = 4605+i
    verticalOR(x, 30906)

    x[0] = 4612
    x[1] = 4613
    x[2] = 4614
    x[3] = 4615
    x[4] = 4700
    x[5] = 4701
    x[6] = 4702
    verticalOR(x, 30907)

    for i in range(7):
        x[i] = 4703+i
    verticalOR(x, 30908)

    for i in range(6):
        x[i] = 4710+i
    x[6] = 30901
    verticalOR(x, 30909)

    for i in range(7):
        x[i] = 30902+i
    verticalOR(x, 30910)

    x = [0 for _ in range(2)]
    x[0] = 30909
    x[1] = 30910
    verticalOR(x, 30911)

    if relay[30911] and not tim[1]:
        tim[0] = True

    if tim[0]:
        tim[1] = True

    if tim[0]:
        relay[30912] = True

    if not relay[30901] and not relay[30902] and relay[30911]:
        relay[30913] = True

    x = [0 for _ in range(2)]
    x[0] = 30913
    x[1] = 30912
    horizontalAND(x, 31812)

    x = [0 for _ in range(5)]
    for i in range(4):
        x[i] = 30012+i
    x[4] = 30006
    verticalOR(x, 10000)

    x = [0 for _ in range(2)]
    x[0] = 10000
    x[1] = 30913
    verticalOR(x, 31900)

    if relay[3005] and not relay[30006]:
        relay[10001] = True
    elif relay[30011]:
        relay[10001] = True

    x = [0 for _ in range(3)]
    x[0] = 31901
    x[1] = 30902
    x[2] = 10001
    verticalOR(x, 31901)


def sequence3():
    x = [0 for _ in range(3)]
    x[0] = 30100
    x[1] = 30414
    x[2] = 4402
    block2(x, 10002)

    x[0] = 30101
    x[1] = 30415
    x[2] = 4403
    block2(x, 10003)

    x[0] = 30102
    x[1] = 30500
    x[2] = 4404
    block2(x, 10004)

    x[0] = 30103
    x[1] = 30501
    x[2] = 4405
    block2(x, 10005)

    x[0] = 30104
    x[1] = 30502
    x[2] = 4406
    block2(x, 10006)

    x[0] = 30105
    x[1] = 30503
    x[2] = 4407
    block2(x, 10007)


def sequence4():
    x = [0 for _ in range(3)]
    x[0] = 30306
    x[1] = 30504
    x[2] = 4608
    block2(x, 10008)

    x[0] = 30114
    x[1] = 30505
    x[2] = 4500
    block2(x, 10009)

    x[0] = 30210
    x[1] = 30506
    x[2] = 4512
    block2(x, 10010)

    x[0] = 30402
    x[1] = 30507
    x[2] = 4704
    block2(x, 10011)

    x[0] = 30307
    x[1] = 30508
    x[2] = 4609
    block2(x, 10012)

    x[0] = 30115
    x[1] = 30509
    x[2] = 4501
    block2(x, 10013)

    x[0] = 30211
    x[1] = 30510
    x[2] = 4513
    block2(x, 10014)

    x[0] = 30403
    x[1] = 30511
    x[2] = 4705
    block2(x, 10015)

    x[0] = 30308
    x[1] = 30512
    x[2] = 4610
    block2(x, 10100)

    x[0] = 30200
    x[1] = 30513
    x[2] = 4502
    block2(x, 10101)

    x[0] = 30212
    x[1] = 30514
    x[2] = 4514
    block2(x, 10102)

    x[0] = 30404
    x[1] = 30515
    x[2] = 4706
    block2(x, 10103)

    x[0] = 30309
    x[1] = 30600
    x[2] = 4611
    block2(x, 10104)

    x[0] = 30201
    x[1] = 30601
    x[2] = 4503
    block2(x, 10105)

    x[0] = 30213
    x[1] = 30602
    x[2] = 4515
    block2(x, 10106)

    x[0] = 30405
    x[1] = 30603
    x[2] = 4707
    block2(x, 10107)


def sequence5():
    x = [0 for _ in range(3)]
    x[0] = 30106
    x[1] = 30604
    x[2] = 4408
    block2(x, 10108)

    x[0] = 30107
    x[1] = 30605
    x[2] = 4409
    block2(x, 10109)

    x[0] = 30108
    x[1] = 30606
    x[2] = 4410
    block2(x, 10110)

    x[0] = 30109
    x[1] = 30607
    x[2] = 4411
    block2(x, 10111)


def sequence6():
    x = [0 for _ in range(3)]
    x[0] = 30310
    x[1] = 30608
    x[2] = 4612
    block2(x, 10112)

    x[0] = 30202
    x[1] = 30609
    x[2] = 4504
    block2(x, 10113)

    x[0] = 30214
    x[1] = 30610
    x[2] = 4600
    block2(x, 10114)

    x[0] = 30406
    x[1] = 30611
    x[2] = 4708
    block2(x, 10115)

    x[0] = 30311
    x[1] = 30612
    x[2] = 4613
    block2(x, 11000)

    x[0] = 30203
    x[1] = 30613
    x[2] = 4505
    block2(x, 11001)

    x[0] = 30215
    x[1] = 30614
    x[2] = 4601
    block2(x, 11002)

    x[0] = 30407
    x[1] = 30615
    x[2] = 4709
    block2(x, 11003)

    x[0] = 30312
    x[1] = 30700
    x[2] = 4614
    block2(x, 11004)

    x[0] = 30204
    x[1] = 30701
    x[2] = 4506
    block2(x, 11005)

    x[0] = 30300
    x[1] = 30702
    x[2] = 4602
    block2(x, 11006)

    x[0] = 30408
    x[1] = 30703
    x[2] = 4710
    block2(x, 11007)

    x[0] = 30313
    x[1] = 30704
    x[2] = 4615
    block2(x, 11008)

    x[0] = 30205
    x[1] = 30705
    x[2] = 4507
    block2(x, 11009)

    x[0] = 30301
    x[1] = 30706
    x[2] = 4603
    block2(x, 11010)

    x[0] = 30409
    x[1] = 30707
    x[2] = 4711
    block2(x, 11011)


def sequence7():
    x = [0 for _ in range(3)]
    x[0] = 30110
    x[1] = 30708
    x[2] = 4412
    block2(x, 11012)

    x[0] = 30111
    x[1] = 30709
    x[2] = 4413
    block2(x, 11013)

    x[0] = 30112
    x[1] = 30710
    x[2] = 4414
    block2(x, 11014)

    x[0] = 30113
    x[1] = 30711
    x[2] = 4415
    block2(x, 11015)


def sequence8():
    x = [0 for _ in range(3)]
    x[0] = 30314
    x[1] = 30712
    x[2] = 4700
    block2(x, 11100)

    x[0] = 30206
    x[1] = 30713
    x[2] = 4508
    block2(x, 11101)

    x[0] = 30302
    x[1] = 30714
    x[2] = 4604
    block2(x, 11102)

    x[0] = 30410
    x[1] = 30715
    x[2] = 4712
    block2(x, 11103)

    x[0] = 30315
    x[1] = 30800
    x[2] = 4701
    block2(x, 11104)

    x[0] = 30207
    x[1] = 30801
    x[2] = 4509
    block2(x, 11105)

    x[0] = 30303
    x[1] = 30802
    x[2] = 4605
    block2(x, 11106)

    x[0] = 30411
    x[1] = 30803
    x[2] = 4713
    block2(x, 11107)

    x[0] = 30400
    x[1] = 30804
    x[2] = 4702
    block2(x, 11108)

    x[0] = 30208
    x[1] = 30805
    x[2] = 4510
    block2(x, 11109)

    x[0] = 30304
    x[1] = 30806
    x[2] = 4606
    block2(x, 11110)

    x[0] = 30412
    x[1] = 30807
    x[2] = 4714
    block2(x, 11111)

    x[0] = 30401
    x[1] = 30808
    x[2] = 4703
    block2(x, 11112)

    x[0] = 30209
    x[1] = 30809
    x[2] = 4511
    block2(x, 11113)

    x[0] = 30305
    x[1] = 30810
    x[2] = 4607
    block2(x, 11114)

    x[0] = 30413
    x[1] = 30811
    x[2] = 4715
    block2(x, 11115)


def sequence9():
    x = [0 for _ in range(2)]
    x[0] = 30100
    x[1] = 30414
    verticalOR(x, 14000)

    x[0] = 30101
    x[1] = 30415
    verticalOR(x, 14001)

    x[0] = 30102
    x[1] = 30500
    verticalOR(x, 14002)

    x[0] = 30103
    x[1] = 30501
    verticalOR(x, 14003)

    x[0] = 30104
    x[1] = 30502
    verticalOR(x, 14004)

    x[0] = 30105
    x[1] = 30503
    verticalOR(x, 14005)

    x[0] = 30106
    x[1] = 30604
    verticalOR(x, 14006)

    x[0] = 30107
    x[1] = 30605
    verticalOR(x, 14007)

    x[0] = 30108
    x[1] = 30606
    verticalOR(x, 14008)

    x[0] = 30109
    x[1] = 30607
    verticalOR(x, 14009)

    x[0] = 30110
    x[1] = 30708
    verticalOR(x, 14010)

    x[0] = 30111
    x[1] = 30709
    verticalOR(x, 14011)

    x[0] = 30112
    x[1] = 30710
    verticalOR(x, 14012)

    x[0] = 30113
    x[1] = 30711
    verticalOR(x, 14013)


def sequence10():
    x = [0 for _ in range(2)]
    x[0] = 30114
    x[1] = 30505
    verticalOR(x, 14014)

    x[0] = 30115
    x[1] = 30509
    verticalOR(x, 14015)

    x[0] = 30200
    x[1] = 30513
    verticalOR(x, 14100)

    x[0] = 30201
    x[1] = 30601
    verticalOR(x, 14101)

    x[0] = 30202
    x[1] = 30609
    verticalOR(x, 14102)

    x[0] = 30203
    x[1] = 30613
    verticalOR(x, 14103)

    x[0] = 30204
    x[1] = 30701
    verticalOR(x, 14104)

    x[0] = 30205
    x[1] = 30705
    verticalOR(x, 14105)

    x[0] = 30206
    x[1] = 30713
    verticalOR(x, 14106)

    x[0] = 30207
    x[1] = 30801
    verticalOR(x, 14107)

    x[0] = 30208
    x[1] = 30805
    verticalOR(x, 14108)

    x[0] = 30209
    x[1] = 30809
    verticalOR(x, 14109)

    x[0] = 30210
    x[1] = 30506
    verticalOR(x, 14110)

    x[0] = 30211
    x[1] = 30510
    verticalOR(x, 14111)

    x[0] = 30212
    x[1] = 30514
    verticalOR(x, 14112)

    x[0] = 30213
    x[1] = 30602
    verticalOR(x, 14113)

    x[0] = 30214
    x[1] = 30610
    verticalOR(x, 14114)

    x[0] = 30215
    x[1] = 30614
    verticalOR(x, 14115)

    x[0] = 30300
    x[1] = 30702
    verticalOR(x, 15000)

    x[0] = 30301
    x[1] = 30706
    verticalOR(x, 15001)

    x[0] = 30302
    x[1] = 30714
    verticalOR(x, 15002)

    x[0] = 30303
    x[1] = 30802
    verticalOR(x, 15003)

    x[0] = 30304
    x[1] = 30806
    verticalOR(x, 15004)

    x[0] = 30305
    x[1] = 30810
    verticalOR(x, 15005)

    x[0] = 30306
    x[1] = 30504
    verticalOR(x, 15006)

    x[0] = 30307
    x[1] = 30508
    verticalOR(x, 15007)

    x[0] = 30308
    x[1] = 30512
    verticalOR(x, 15008)

    x[0] = 30309
    x[1] = 30600
    verticalOR(x, 15009)

    x[0] = 30310
    x[1] = 30608
    verticalOR(x, 15010)

    x[0] = 30311
    x[1] = 30612
    verticalOR(x, 15011)

    x[0] = 30312
    x[1] = 30700
    verticalOR(x, 15012)

    x[0] = 30313
    x[1] = 30704
    verticalOR(x, 15013)

    x[0] = 30314
    x[1] = 30712
    verticalOR(x, 15014)

    x[0] = 30315
    x[1] = 30800
    verticalOR(x, 15015)

    x[0] = 30400
    x[1] = 30804
    verticalOR(x, 15100)

    x[0] = 30401
    x[1] = 30808
    verticalOR(x, 15101)

    x[0] = 30402
    x[1] = 30507
    verticalOR(x, 15102)

    x[0] = 30403
    x[1] = 30511
    verticalOR(x, 15103)

    x[0] = 30404
    x[1] = 30515
    verticalOR(x, 15104)

    x[0] = 30405
    x[1] = 30603
    verticalOR(x, 15105)

    x[0] = 30406
    x[1] = 30611
    verticalOR(x, 15106)

    x[0] = 30407
    x[1] = 30615
    verticalOR(x, 15107)

    x[0] = 30408
    x[1] = 30703
    verticalOR(x, 15108)

    x[0] = 30409
    x[1] = 30707
    verticalOR(x, 15109)

    x[0] = 30410
    x[1] = 30715
    verticalOR(x, 15110)

    x[0] = 30411
    x[1] = 30803
    verticalOR(x, 15111)

    x[0] = 30412
    x[1] = 30807
    verticalOR(x, 15112)

    x[0] = 30413
    x[1] = 30811
    verticalOR(x, 15113)


def sequence11():
    if relay[30000] and not relay[3007] and not relay[30911] and not relay[31807]:
        if relay[3004]:
            relay[31101] = True
    elif relay[4313] or relay[4314] or relay[4315] or relay[4400] or relay[4401]:
        if relay[3004]:
            relay[31101] = True

    x = [0 for _ in range(2)]
    x[0] = 31101
    x[1] = 31108
    verticalOR(x, 31102)


def sequence12():
    for i in range(13):
        contact(14000+i, 12000+i)


def sequence13():
    contact(14014, 12014)
    contact(14015, 12015)

    for i in range(10):
        contact(14100+i, 12100+i)


def sequence14():
    for i in range(6):
        contact(14110+i, 12110+i)
        contact(15000+i, 13000+i)


def sequence15():

    for i in range(10):
        contact(15006+i, 13006+i)
    contact(15100, 13100)
    contact(15101, 13101)


def sequence16():

    for i in range(12):
        contact(15102+i, 13102+i)


def sequence17():
    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 12000+i
    block3(x, 31301)

    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 12007+i
    block3(x, 31302)

    x = [0 for _ in range(8)]
    x[0] = 31301
    x[1] = 30001
    x[2] = 30011
    x[3] = 30000
    x[4] = 31302
    x[5] = 30008
    x[6] = 3005
    x[7] = 31108
    horizontalOR1(x, 16101)

    x = [0 for _ in range(2)]
    x[0] = 16101
    x[1] = 16106
    block4(x, 31102, 16106)

    x = [0 for _ in range(7)]
    x[0] = 12014
    x[1] = 12015

    for i in range(5):
        x[2+i] = 12100+i
    verticalOR(x, 31303)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 12105+i
    x[5] = 31303
    block3(x, 31304)

    x = [0 for _ in range(6)]
    x[0] = 30002
    x[1] = 30012
    x[2] = 30000
    x[3] = 30008
    x[4] = 3005
    x[5] = 31112
    block4(x, 31304, 16102)

    x = [0 for _ in range(7)]
    for i in range(6):
        x[i] = 12110+i
    x[6] = 13000
    verticalOR(x, 31305)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 13001+i
    x[5] = 31305
    block3(x, 31306)

    x = [0 for _ in range(6)]
    x[0] = 30002
    x[1] = 30013
    x[2] = 30000
    x[3] = 30008
    x[4] = 3005
    x[5] = 31200
    block4(x, 31306, 16103)

    x = [0 for _ in range(7)]
    for i in range(6):
        x[i] = 13006+i
    verticalOR(x, 31307)

    x = [0 for _ in range(6)]
    x[0] = 13013
    x[1] = 13014
    x[2] = 13015
    x[3] = 13100
    x[4] = 13101
    x[5] = 31307
    block3(x, 31308)

    x = [0 for _ in range(6)]
    x[0] = 30002
    x[1] = 30014
    x[2] = 30000
    x[3] = 30008
    x[4] = 3005
    x[5] = 31204
    block4(x, 31308, 16104)

    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 13102+i
    verticalOR(x, 31309)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 13109+i
    x[5] = 31309
    block3(x, 31310)

    x = [0 for _ in range(6)]
    x[0] = 30002
    x[1] = 30015
    x[2] = 30000
    x[3] = 30008
    x[4] = 3005
    x[5] = 31208
    block4(x, 31310, 16105)

    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 3901+i
    verticalOR(x, 31311)

    for i in range(7):
        x[i] = 3908+i
    verticalOR(x, 31312)

    x = [0 for _ in range(2)]
    x[0] = 31311
    x[1] = 31312
    verticalOR(x, 31313)

    x = [0 for _ in range(12)]
    for i in range(6):
        x[i] = 3901+i
        x[i+6] = 12000+i
    horizontalOR2(x, 31314)

    for i in range(6):
        x[i] = 3907+i
        x[i+6] = 12006+i
    horizontalOR2(x, 31315)

    x1 = [0 for _ in range(4)]
    x1[0] = 3913
    x1[1] = 3914
    x1[2] = 12012
    x1[3] = 12013

    x2 = [0 for _ in range(4)]
    x2[0] = 31314
    x2[1] = 31315
    x2[2] = 31313
    x2[3] = 16101
    block5(x1, x2, 31504)

    x = [0 for _ in range(2)]
    x[0] = 31504
    x[1] = 4313
    horizontalAND(x, 16012)

    # FR100X
    x = [0 for _ in range(7)]
    x[0] = 3915
    for i in range(6):
        x[i+1] = 4000+i
    verticalOR(x, 31400)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 4006+i
    x[5] = 31400
    verticalOR(x, 31401)

    x = [0 for _ in range(12)]
    x[0] = 3915
    x[1] = 4000
    x[2] = 4001
    x[3] = 4002
    x[4] = 4003
    x[5] = 4004
    x[6] = 12014
    x[7] = 12015
    x[8] = 12100
    x[9] = 12101
    x[10] = 12102
    x[11] = 12103
    horizontalOR2(x, 31402)

    for i in range(6):
        x[i] = 4005+i
        x[6+i] = 12104+i
    horizontalOR2(x, 31403)

    x = [0 for _ in range(5)]
    x[0] = 31401
    x[1] = 31402
    x[2] = 31403
    x[3] = 16102
    x[4] = 4314
    horizontalAND(x, 16013)

    x = [0 for _ in range(7)]
    for i in range(5):
        x[i] = 4011+i
    x[5] = 4100
    x[6] = 4101
    verticalOR(x, 31404)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 4102+i
    x[5] = 31404
    verticalOR(x, 31405)

    x = [0 for _ in range(12)]
    for i in range(5):
        x[i] = 4011+i
    x[5] = 4100
    for i in range(6):
        x[6+i] = 12110+i
    horizontalOR2(x, 31406)

    for i in range(6):
        x[i] = 4101+i
        x[6+i] = 13000+i
    horizontalOR2(x, 31407)

    x = [0 for _ in range(5)]
    x[0] = 31405
    x[1] = 31406
    x[2] = 31407
    x[3] = 16103
    x[4] = 4315
    horizontalAND(x, 16014)

    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 4107+i
    verticalOR(x, 31408)

    x = [0 for _ in range(6)]
    x[0] = 4114
    x[1] = 4115
    x[2] = 4200
    x[3] = 4201
    x[4] = 4202
    x[5] = 31408
    verticalOR(x, 31409)

    x = [0 for _ in range(12)]
    for i in range(6):
        x[i] = 4107+i
        x[6+i] = 13006+i
    horizontalOR2(x, 31410)

    x[0] = 4113
    x[1] = 4114
    x[2] = 4115
    x[3] = 4200
    x[4] = 4201
    x[5] = 4202
    x[6] = 13012
    x[7] = 13013
    x[8] = 13014
    x[9] = 13015
    x[10] = 13100
    x[11] = 13101
    horizontalOR2(x, 31411)

    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 4203+i
    verticalOR(x, 31412)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 4210+i
    x[5] = 31412
    verticalOR(x, 31413)

    x = [0 for _ in range(12)]
    for i in range(6):
        x[i] = 4203+i
        x[6+i] = 13102+i
    horizontalOR2(x, 31414)

    for i in range(6):
        x[i] = 4209+i
        x[6+i] = 13108+i
    horizontalOR2(x, 31415)

    x = [0 for _ in range(5)]
    x[0] = 31413
    x[1] = 31414
    x[2] = 31415
    x[3] = 16105
    x[4] = 4401
    horizontalAND(x, 16100)

    x = [0 for _ in range(2)]
    x[0] = 16101
    x[1] = 31500
    block4(x, 31102, 31500)

    if not relay[16101] and not relay[4313] and relay[31500]:
        relay[31501] = True


def sequence18():
    contact(12000, 15114)
    contact(12001, 15115)
    for i in range(12):
        contact(12002+i, 16000+i)


def sequence19():
    x = [0 for _ in range(7)]
    x[0] = 15114
    x[1] = 15115
    for i in range(5):
        x[2+i] = 16000+i
    verticalOR(x, 31502)

    for i in range(7):
        x[i] = 16005+i
    verticalOR(x, 31503)

    x = [0 for _ in range(12)]

    x[0] = 4215
    for i in range(5):
        x[1+i] = 4300+i
    x[6] = 15114
    x[7] = 15115
    x[8] = 16000
    x[9] = 16001
    x[10] = 16002
    x[11] = 16003
    horizontalOR2(x, 31505)

    for i in range(6):
        x[i] = 4305+i
        x[6+i] = 16004+i
    horizontalOR2(x, 31506)

    if relay[4311] or not relay[16010]:
        if relay[4312] or not relay[16011]:
            if relay[31502] or relay[31503]:
                if relay[31505] and relay[31506]:
                    relay[31507] = True

    x = [0 for _ in range(6)]
    x[0] = 3915
    for i in range(5):
        x[1+i] = 4000+i
    verticalOR(x, 31510)

    x = [0 for _ in range(7)]
    for i in range(6):
        x[i] = 4005+i
    x[6] = 31510
    verticalOR(x, 31511)

    x = [0 for _ in range(6)]
    for i in range(5):
        x[i] = 4011+i
    x[5] = 4100
    verticalOR(x, 31512)

    x = [0 for _ in range(7)]
    for i in range(6):
        x[i] = 4101+i
    x[6] = 31512
    verticalOR(x, 31513)

    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 4107+i
    verticalOR(x, 31514)

    x = [0 for _ in range(7)]
    x[0] = 4113
    x[1] = 4114
    x[2] = 4115
    x[3] = 4200
    x[4] = 4201
    x[5] = 4202
    x[6] = 31514
    verticalOR(x, 31515)

    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 4203+i
    verticalOR(x, 31600)

    for i in range(6):
        x[i] = 4209+i
    verticalOR(x, 31601)

    x = [0 for _ in range(5)]
    x[0] = 31600
    x[1] = 31511
    x[2] = 31513
    x[3] = 31515
    x[4] = 31601
    verticalOR(x, 31602)

    x[0] = 4313
    x[1] = 4314
    x[2] = 4315
    x[3] = 4400
    x[4] = 4401
    verticalOR(x, 31503)

    if relay[30001] or relay[30002] or relay[31710]:
        if not relay[3003]:
            relay[31710] = True

    if relay[31710] and not relay[30001] and not relay[30002]:
        relay[31711] = True

    if relay[31711]:
        tim[22] = True

    if relay[31712] or tim[22]:
        relay[31807] = True


def main():
    if relay[3004]:
        interlock = True
    sequence1()
    interlock = False

    sequence2()

    if relay[31901]:
        interlock = True
    sequence3()
    interlock = False

    if relay[31900]:
        interlock = True
    sequence4()
    interlock = False

    if relay[31901]:
        interlock = True
    sequence5()
    interlock = False

    if relay[31900]:
        interlock = True
    sequence6()
    interlock = False

    if relay[31901]:
        interlock = True
    sequence7()
    interlock = False

    if relay[31900]:
        interlock = True
    sequence8()
    interlock = False

    if relay[31901]:
        interlock = True
    sequence9()
    interlock = False

    if relay[31900]:
        interlock = True
    sequence10()
    interlock = False

    sequence11()

    if relay[31102]:
        interlock = True
    sequence12()
    interlock = False

    x = [0 for _ in range(2)]
    x[0] = 31101
    x[1] = 31112
    verticalOR(x, 31103)

    if relay[31103]:
        interlock = True
    sequence13()
    interlock = False

    x = [0 for _ in range(2)]
    x[0] = 31101
    x[1] = 31200
    verticalOR(x, 31104)

    if relay[31104]:
        interlock = True
    sequence14()
    interlock = False

    x = [0 for _ in range(2)]
    x[0] = 31101
    x[1] = 31204
    verticalOR(x, 31105)

    if relay[31105]:
        interlock = True
    sequence15()
    interlock = False

    x = [0 for _ in range(2)]
    x[0] = 31101
    x[1] = 31208
    verticalOR(x, 31106)

    if relay[31106]:
        interlock = True
    sequence16()
    interlock = False

    sequence17()

    if relay[31501]:
        interlock = True
    sequence18()
    interlock = False

    sequence19()
