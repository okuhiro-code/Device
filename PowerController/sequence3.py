# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:44:18 2026

@author: oku-hiro
"""
interlock = False
relay = [False for _ in range(40000)]


def contact1(x, y):
    if relay[x]:
        relay[y] = True
    else:
        relay[y] = False


def contact2(x, y):
    if not relay[x]:
        relay[y] = True
    else:
        relay[y] = False


def verticalOR(x, y):
    for i in range(len(x)):
        if relay[x[i]]:
            relay[y] = True
            return


def horizontalOR(x, y):
    h = int(len(x)/2)
    for i in range(h):
        if relay[x[i]] or not relay[x[i]+h]:
            pass
        else:
            return
    relay[y] = True


def horizontalAND(x, y):
    for i in range(len(x)):
        if not relay[x[i]]:
            return
    relay[y] = True


def block1(x):
    if relay[x[2]]:
        return
    if x[0] and not x[1]:
        relay[x[2]] = True


def sequence1():
    for i in range(15):
        contact1(10000+i, 4000+i)
        contact1(10100+i, 4100+i)
        contact1(11000+i, 4200+i)
        contact1(11100+i, 4300+i)
        contact1(12000+i, 4400+i)
        contact1(12100+i, 4500+i)
        contact1(13000+i, 4600+i)

    for i in range(12):
        contact1(13100+i, 4700+i)

    if not relay[13112]:
        interlock = True

    contact1(14003, 3212)
    contact1(14007, 3302)
    contact1(14011, 3308)
    contact1(14015, 3314)
    contact1(14103, 3404)
    contact1(14107, 3410)
    contact1(14111, 3500)
    contact1(14115, 3506)
    contact1(15003, 3512)
    contact1(15007, 3602)
    contact1(15011, 3608)
    contact1(15015, 3614)
    contact1(15103, 3704)
    contact1(15107, 3710)
    contact1(15111, 3200)
    interlock = False


def sequence2():
    contact1(16011, 3300)
    contact1(16012, 3306)
    contact1(16013, 3312)
    contact1(16014, 3402)
    contact1(16015, 3408)
    contact1(16100, 3414)
    contact1(16101, 3504)
    contact1(16102, 3510)
    contact1(16103, 3600)
    contact1(16104, 3606)
    contact1(16105, 3612)
    contact1(16106, 3702)
    contact1(16107, 3708)
    contact1(16108, 3714)
    contact1(16109, 3204)
    contact1(4000, 3000)
    contact1(4001, 3001)

    x = [0 for _ in range(5)]
    x[0] = 4002
    x[1] = 4014
    x[2] = 4110
    x[3] = 4206
    x[4] = 4302
    verticalOR(x, 30000)

    x = [0 for _ in range(4)]
    x[0] = 4314
    x[1] = 4410
    x[2] = 4506
    x[3] = 4602
    verticalOR(x, 30001)

    x = [0 for _ in range(2)]
    x[0] = 30000
    x[1] = 30001
    verticalOR(x, 3002)

    x = [0 for _ in range(5)]
    x[0] = 4003
    x[1] = 4015
    x[2] = 4111
    x[3] = 4207
    x[4] = 4303
    verticalOR(x, 30002)

    x = [0 for _ in range(4)]
    x[0] = 4315
    x[1] = 4411
    x[2] = 4507
    x[3] = 4603
    verticalOR(x, 30003)

    x = [0 for _ in range(2)]
    x[0] = 30002
    x[1] = 30003
    verticalOR(x, 3003)

    x = [0 for _ in range(5)]
    x[0] = 4004
    x[1] = 4100
    x[2] = 4112
    x[3] = 4208
    x[4] = 4304
    verticalOR(x, 30004)

    x = [0 for _ in range(4)]
    x[0] = 4400
    x[1] = 4412
    x[2] = 4508
    x[3] = 4604
    verticalOR(x, 30005)

    x = [0 for _ in range(2)]
    x[0] = 30004
    x[1] = 30005
    verticalOR(x, 3004)

    x = [0 for _ in range(5)]
    x[0] = 4005
    x[1] = 4101
    x[2] = 4113
    x[3] = 4209
    x[4] = 4305
    verticalOR(x, 30006)

    x = [0 for _ in range(4)]
    x[0] = 4401
    x[1] = 4413
    x[2] = 4509
    x[3] = 4605
    verticalOR(x, 30007)

    x = [0 for _ in range(2)]
    x[0] = 30006
    x[1] = 30007
    verticalOR(x, 3005)

    x = [0 for _ in range(5)]
    x[0] = 4006
    x[1] = 4102
    x[2] = 4114
    x[3] = 4210
    x[4] = 4306
    verticalOR(x, 30008)

    x = [0 for _ in range(4)]
    x[0] = 4402
    x[1] = 4414
    x[2] = 4510
    x[3] = 4606
    verticalOR(x, 30009)

    x = [0 for _ in range(2)]
    x[0] = 30008
    x[1] = 30009
    verticalOR(x, 3006)

    x = [0 for _ in range(5)]
    x[0] = 4007
    x[1] = 4103
    x[2] = 4115
    x[3] = 4211
    x[4] = 4307
    verticalOR(x, 30010)

    x = [0 for _ in range(4)]
    x[0] = 4403
    x[1] = 4415
    x[2] = 4511
    x[3] = 4607
    verticalOR(x, 30011)

    x = [0 for _ in range(2)]
    x[0] = 30010
    x[1] = 30011
    verticalOR(x, 3007)

    x = [0 for _ in range(5)]
    x[0] = 4008
    x[1] = 4104
    x[2] = 4200
    x[3] = 4212
    x[4] = 4308
    verticalOR(x, 30012)

    x = [0 for _ in range(4)]
    x[0] = 4404
    x[1] = 4500
    x[2] = 4512
    x[3] = 4608
    verticalOR(x, 30013)

    x = [0 for _ in range(2)]
    x[0] = 30012
    x[1] = 30013
    verticalOR(x, 3008)

    x = [0 for _ in range(5)]
    x[0] = 4009
    x[1] = 4105
    x[2] = 4201
    x[3] = 4213
    x[4] = 4309
    verticalOR(x, 30014)

    x = [0 for _ in range(4)]
    x[0] = 4405
    x[1] = 4501
    x[2] = 4513
    x[3] = 4609
    verticalOR(x, 30015)

    x = [0 for _ in range(2)]
    x[0] = 30014
    x[1] = 30015
    verticalOR(x, 3009)

    x = [0 for _ in range(5)]
    x[0] = 4010
    x[1] = 4106
    x[2] = 4202
    x[3] = 4214
    x[4] = 4310
    verticalOR(x, 30100)

    x = [0 for _ in range(4)]
    x[0] = 4406
    x[1] = 4502
    x[2] = 4514
    x[3] = 4610
    verticalOR(x, 30101)

    x = [0 for _ in range(2)]
    x[0] = 30100
    x[1] = 30101
    verticalOR(x, 3010)

    x = [0 for _ in range(5)]
    x[0] = 4011
    x[1] = 4107
    x[2] = 4203
    x[3] = 4215
    x[4] = 4311
    verticalOR(x, 30102)

    x = [0 for _ in range(4)]
    x[0] = 4407
    x[1] = 4503
    x[2] = 4515
    x[3] = 4611
    verticalOR(x, 30103)

    x = [0 for _ in range(2)]
    x[0] = 30102
    x[1] = 30103
    verticalOR(x, 3011)

    x = [0 for _ in range(5)]
    x[0] = 4012
    x[1] = 4108
    x[2] = 4204
    x[3] = 4300
    x[4] = 4312
    verticalOR(x, 30104)

    x = [0 for _ in range(4)]
    x[0] = 4408
    x[1] = 4504
    x[2] = 4600
    x[3] = 4612
    verticalOR(x, 30105)

    x = [0 for _ in range(2)]
    x[0] = 30104
    x[1] = 30105
    verticalOR(x, 3012)

    x = [0 for _ in range(5)]
    x[0] = 4013
    x[1] = 4109
    x[2] = 4205
    x[3] = 4301
    x[4] = 4313
    verticalOR(x, 30106)

    x = [0 for _ in range(4)]
    x[0] = 4409
    x[1] = 4505
    x[2] = 4601
    x[3] = 4613
    verticalOR(x, 30107)

    x = [0 for _ in range(2)]
    x[0] = 30106
    x[1] = 30107
    verticalOR(x, 3013)

    contact1(4700, 3014)
    contact1(4701, 3015)

    for i in range(10):
        contact1(4702+i, 3100+i)

    x = [0 for _ in range(7)]
    for i in range(7):
        x[i] = 3000+i
    verticalOR(x, 30108)

    for i in range(7):
        x[i] = 3007+i
    verticalOR(x, 30109)

    x[0] = 4614
    x[1] = 4615
    x[2] = 3014
    x[3] = 3015
    x[4] = 3100
    x[5] = 3101
    x[6] = 3102
    verticalOR(x, 30110)

    for i in range(7):
        x[i] = 3103+i
    verticalOR(x, 30111)

    x = [0 for _ in range(4)]
    for i in range(4):
        x[i] = 30108+i
    verticalOR(x, 3903)

    x = [0 for _ in range(12)]
    x[0] = 3212
    x[1] = 3302
    x[2] = 3308
    x[3] = 3314
    x[4] = 3404
    x[5] = 3410
    x[6] = 15112
    x[7] = 15113
    x[8] = 15114
    x[9] = 15115
    x[10] = 16000
    x[11] = 16001
    horizontalOR(x, 30112)

    x[0] = 3500
    x[1] = 3506
    x[2] = 3512
    x[3] = 3602
    x[4] = 3608
    x[5] = 3614
    x[6] = 16002
    x[7] = 16003
    x[8] = 16004
    x[9] = 16005
    x[10] = 16006
    x[11] = 16007
    horizontalOR(x, 30113)

    x = [0 for _ in range(4)]
    x[0] = 3704
    x[1] = 3710
    x[2] = 16008
    x[3] = 16009
    horizontalOR(x, 30114)

    x = [0 for _ in range(3)]
    x[0] = 30112
    x[1] = 30113
    x[2] = 30114
    horizontalAND(x, 30115)

    if relay[3200] or not relay[16010]:
        if relay[30115]:
            relay[3904] = True

    x = [0 for _ in range(2)]
    x[0] = 16110
    x[1] = 30115
    horizontalAND(x, 3206)

    if not relay[13113] and not relay[13114]:
        relay[30200] = True


def sequence3():
    if relay[30200]:
        interlock = True
    x = [0 for _ in range(2)]
    x[0] = 15110
    x[1] = 3201
    verticalOR(x, x[1])

    x[0] = 14002
    x[1] = 3213
    verticalOR(x, x[1])

    x[0] = 14006
    x[1] = 3303
    verticalOR(x, x[1])

    x[0] = 14010
    x[1] = 3309
    verticalOR(x, x[1])

    x[0] = 14014
    x[1] = 3315
    verticalOR(x, x[1])

    x[0] = 14102
    x[1] = 3405
    verticalOR(x, x[1])

    x[0] = 14106
    x[1] = 3411
    verticalOR(x, x[1])

    x[0] = 14110
    x[1] = 3501
    verticalOR(x, x[1])

    x[0] = 14114
    x[1] = 3507
    verticalOR(x, x[1])

    x[0] = 15002
    x[1] = 3513
    verticalOR(x, x[1])

    x[0] = 15006
    x[1] = 3603
    verticalOR(x, x[1])

    x[0] = 15010
    x[1] = 3609
    verticalOR(x, x[1])

    x[0] = 15014
    x[1] = 3615
    verticalOR(x, x[1])

    x[0] = 15102
    x[1] = 3705
    verticalOR(x, x[1])

    x[0] = 15106
    x[1] = 3711
    verticalOR(x, x[1])
    interlock = False


def sequence4():
    x = [0 for _ in range(7)]
    x[0] = 3213
    x[1] = 3303
    x[2] = 3309
    x[3] = 3315
    x[4] = 3405
    x[5] = 3411
    x[6] = 3501
    verticalOR(x, 30201)

    x[0] = 3507
    x[1] = 3513
    x[2] = 3603
    x[3] = 3609
    x[4] = 3615
    x[5] = 3705
    x[6] = 3711
    verticalOR(x, 30202)

    x = [0 for _ in range(3)]
    x[0] = 30201
    x[1] = 30202
    x[2] = 3201
    verticalOR(x, 3900)

    x[0] = 30201
    x[1] = 30202
    x[2] = 16111
    verticalOR(x, 3207)


def sequence5():
    if relay[30200]:
        interlock = True

    x = [0 for _ in range(2)]
    x[0] = 15109
    x[1] = 3202
    verticalOR(x, x[1])

    x[0] = 14001
    x[1] = 3214
    verticalOR(x, x[1])

    x[0] = 14005
    x[1] = 3304
    verticalOR(x, x[1])

    x[0] = 14009
    x[1] = 3310
    verticalOR(x, x[1])

    x[0] = 14013
    x[1] = 3400
    verticalOR(x, x[1])

    x[0] = 14101
    x[1] = 3406
    verticalOR(x, x[1])

    x[0] = 14105
    x[1] = 3412
    verticalOR(x, x[1])

    x[0] = 14109
    x[1] = 3502
    verticalOR(x, x[1])

    x[0] = 14113
    x[1] = 3508
    verticalOR(x, x[1])

    x[0] = 15001
    x[1] = 3514
    verticalOR(x, x[1])

    x[0] = 15005
    x[1] = 3604
    verticalOR(x, x[1])

    x[0] = 15009
    x[1] = 3610
    verticalOR(x, x[1])

    x[0] = 15013
    x[1] = 3700
    verticalOR(x, x[1])

    x[0] = 15101
    x[1] = 3706
    verticalOR(x, x[1])

    x[0] = 15105
    x[1] = 3712
    verticalOR(x, x[1])
    interlock = False


def sequence6():
    x = [0 for _ in range(7)]
    x[0] = 3214
    x[1] = 3304
    x[2] = 3310
    x[3] = 3400
    x[4] = 3406
    x[5] = 3412
    x[6] = 3502
    verticalOR(x, 30203)

    x[0] = 3508
    x[1] = 3514
    x[2] = 3604
    x[3] = 3610
    x[4] = 3700
    x[5] = 3706
    x[6] = 3712
    verticalOR(x, 30204)

    x = [0 for _ in range(3)]
    x[0] = 30203
    x[1] = 30204
    x[2] = 3202
    verticalOR(x, 3901)

    x[0] = 30203
    x[1] = 30204
    x[2] = 16112
    verticalOR(x, 3208)

    if not relay[13112] or relay[13115]:
        relay[30205] = True


def sequence7():
    if relay[30205]:
        interlock = True

    x = [0 for _ in range(2)]
    x[0] = 3200
    x[1] = 30206
    verticalOR(x, x[1])

    x[0] = 3212
    x[1] = 30207
    verticalOR(x, x[1])

    x[0] = 3302
    x[1] = 30208
    verticalOR(x, x[1])

    x[0] = 3308
    x[1] = 30209
    verticalOR(x, x[1])

    x[0] = 3314
    x[1] = 30210
    verticalOR(x, x[1])

    x[0] = 3404
    x[1] = 30211
    verticalOR(x, x[1])

    x[0] = 3410
    x[1] = 30212
    verticalOR(x, x[1])

    x[0] = 3500
    x[1] = 30213
    verticalOR(x, x[1])

    x[0] = 3506
    x[1] = 30214
    verticalOR(x, x[1])

    x[0] = 3512
    x[1] = 30215
    verticalOR(x, x[1])

    x[0] = 3602
    x[1] = 30300
    verticalOR(x, x[1])

    x[0] = 3608
    x[1] = 30301
    verticalOR(x, x[1])

    x[0] = 3614
    x[1] = 30302
    verticalOR(x, x[1])

    x[0] = 3704
    x[1] = 30303
    verticalOR(x, x[1])

    x[0] = 3710
    x[1] = 30304
    verticalOR(x, x[1])
    interlock = False


def sequence8():
    if relay[13115]:
        interlock = True

    x = [0 for _ in range(3)]
    x[0] = 16010
    x[1] = 30206
    x[2] = 3203
    block1(x)

    x[0] = 15112
    x[1] = 30207
    x[2] = 3215
    block1(x)

    x[0] = 15113
    x[1] = 30208
    x[2] = 3305
    block1(x)

    x[0] = 15114
    x[1] = 30209
    x[2] = 3311
    block1(x)

    x[0] = 15115
    x[1] = 30210
    x[2] = 3401
    block1(x)

    x[0] = 16000
    x[1] = 30211
    x[2] = 3407
    block1(x)

    x[0] = 16001
    x[1] = 30212
    x[2] = 3413
    block1(x)

    x[0] = 16002
    x[1] = 30213
    x[2] = 3503
    block1(x)

    x[0] = 16003
    x[1] = 30214
    x[2] = 3509
    block1(x)

    x[0] = 16004
    x[1] = 30215
    x[2] = 3515
    block1(x)

    x[0] = 16005
    x[1] = 30300
    x[2] = 3605
    block1(x)

    x[0] = 16006
    x[1] = 30301
    x[2] = 3611
    block1(x)

    x[0] = 16007
    x[1] = 30302
    x[2] = 3701
    block1(x)

    x[0] = 16008
    x[1] = 30303
    x[2] = 3707
    block1(x)

    x[0] = 16009
    x[1] = 30304
    x[2] = 3713
    block1(x)
    interlock = False


def sequence9():
    x = [0 for _ in range(7)]
    x[0] = 3215
    x[1] = 3305
    x[2] = 3311
    x[3] = 3401
    x[4] = 3407
    x[5] = 3413
    x[6] = 3503
    verticalOR(x, 30305)

    x[0] = 3509
    x[1] = 3515
    x[2] = 3605
    x[3] = 3611
    x[4] = 3701
    x[5] = 3707
    x[6] = 3713
    verticalOR(x, 30306)

    x = [0 for _ in range(3)]
    x[0] = 30305
    x[1] = 30306
    x[2] = 3203
    verticalOR(x, 3902)

    x[0] = 30305
    x[1] = 30306
    x[2] = 16113
    verticalOR(x, 3209)

    x = [0 for _ in range(7)]
    x[0] = 3300
    x[1] = 3306
    x[2] = 3312
    x[3] = 3402
    x[4] = 3408
    x[5] = 3414
    x[6] = 3504
    verticalOR(x, 30307)

    x[0] = 3510
    x[1] = 3600
    x[2] = 3606
    x[3] = 3612
    x[4] = 3702
    x[5] = 3708
    x[6] = 3714
    verticalOR(x, 30308)

    x = [0 for _ in range(3)]
    x[0] = 30307
    x[1] = 30308
    x[2] = 3204
    verticalOR(x, 3905)

    x[0] = 30307
    x[1] = 30308
    x[2] = 16114
    verticalOR(x, 3210)

    contact2(14000, 3301)
    contact2(14004, 3307)
    contact2(14008, 3313)
    contact2(14012, 3403)
    contact2(14100, 3409)
    contact2(14104, 3415)
    contact2(14108, 3505)
    contact2(14112, 3511)
    contact2(15000, 3601)
    contact2(15004, 3607)
    contact2(15008, 3613)
    contact2(15012, 3703)
    contact2(15100, 3709)
    contact2(15104, 3715)
    contact2(15108, 3205)

    x = [0 for _ in range(7)]
    x[0] = 3301
    x[1] = 3307
    x[2] = 3313
    x[3] = 3403
    x[4] = 3409
    x[5] = 3415
    x[6] = 3505
    verticalOR(x, 30309)

    x[0] = 3511
    x[1] = 3601
    x[2] = 3607
    x[3] = 3613
    x[4] = 3703
    x[5] = 3709
    x[6] = 3715
    verticalOR(x, 30310)

    x = [0 for _ in range(3)]
    x[0] = 30309
    x[1] = 30310
    x[2] = 3205
    verticalOR(x, 3906)

    x[0] = 30309
    x[1] = 30310
    x[2] = 16115
    verticalOR(x, 3211)

    contact1(3200, 3800)
    contact1(3212, 3801)
    contact1(3302, 3802)
    contact1(3308, 3803)
    contact1(3314, 3804)
    contact1(3404, 3805)
    contact1(3410, 3806)
    contact1(3500, 3807)
    contact1(3506, 3808)
    contact1(3512, 3809)
    contact1(3602, 3810)
    contact1(3608, 3811)
    contact1(3614, 3812)
    contact1(3704, 3813)
    contact1(3710, 3814)

def main():
    sequence1()
    sequence2()
    sequence3()
    sequence4()
    sequence5()
    sequence6()
    sequence7()
    sequence8()
    sequence9()
