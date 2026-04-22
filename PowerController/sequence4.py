# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:47:17 2026

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


def verticalOR1(x, y):
    for i in range(len(x)):
        if relay[x[i]]:
            relay[y] = True
            return


def verticalOR2(x, t, y):
    for i in range(len(x)):
        if relay[x[i]] == t[i]:
            relay[y] = True
            return


def verticalOR3(x, y):
    for i in range(len(x)):
        if not relay[x[i]]:
            relay[y] = True
            return


def charge_command_memory():
    if relay[4615] or relay[30005]:
        if not relay[4700]:
            relay[30005] = True


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


def overtime1_wait_time():
    if relay[30012] and relay[30015]:
        if not relay[4702]:
            relay[15009] = True
    elif relay[4614] and relay[30013]:
        if not relay[4702]:
            relay[15009] = True
    elif relay[30014]:
        if not relay[4702]:
            relay[15009] = True
    elif relay[15009]:
        if not relay[4702]:
            relay[15009] = True


def block1(x):
    if relay[x[2]]:
        return
    if x[0] and not x[1]:
        relay[x[2]] = True


def block2(x, y):
    if not relay[x[-1]]:
        for i in range(len(x)-1):
            if not relay[x[i]]:
                return
        relay[y] = True
    else:
        return


def block3(x, y):
    if not relay[x[0]]:
        relay[y] = True

    for i in range(2):
        if relay[x[i+1]]:
            relay[y] = True

    if not relay[30509]:
        relay[y] = True

    if not relay[4609]:
        relay[y] = True


def sequence1():
    if not relay[4700]:
        interlock = True

    contact1(3003, 13108)
    contact1(3007, 13114)
    contact1(3011, 13000)
    contact1(3015, 13006)
    contact1(3103, 13012)
    contact1(3107, 13102)
    contact1(3111, 14004)
    contact1(3115, 14010)
    interlock = False


def sequence2():
    contact1(3911, 15001)

    for i in range(8):
        contact2(3308+i, 10000+i)
        contact2(3400+i, 10008+i)
        contact2(3408+i, 10100+i)
        contact2(3500+i, 10108+i)
        contact2(3508+i, 11100+i)
        contact2(3600+i, 11108+i)

    for i in range(16):
        contact2(3200+i, 11100+i)
        contact2(3700+i, 12100+i)

    if not relay[4701] and not relay[4702]:
        relay[30000] = True


def sequence3():
    if relay[30000]:
        interlock = True

    x = [0 for _ in range(2)]
    x[0] = 3010
    x[1] = 13001
    verticalOR1(x, x[1])

    x[0] = 3014
    x[1] = 13007
    verticalOR1(x, x[1])

    x[0] = 3102
    x[1] = 13013
    verticalOR1(x, x[1])

    x[0] = 3106
    x[1] = 13103
    verticalOR1(x, x[1])

    x[0] = 3002
    x[1] = 13109
    verticalOR1(x, x[1])

    x[0] = 3006
    x[1] = 13115
    verticalOR1(x, x[1])

    x[0] = 3110
    x[1] = 14005
    verticalOR1(x, x[1])

    x[0] = 3114
    x[1] = 14011
    verticalOR1(x, x[1])
    interlock = False


def sequence4():
    x = [0 for _ in range(6)]
    x[0] = 13001
    x[1] = 13007
    x[2] = 13013
    x[3] = 13103
    x[4] = 13109
    x[5] = 13115
    verticalOR1(x, 30001)

    x = [0 for _ in range(2)]
    x[0] = 14005
    x[1] = 14011
    verticalOR1(x, 30002)

    x[0] = 30001
    x[1] = 30002
    verticalOR1(x, 15110)

    x[0] = 15110
    x[1] = 4310
    verticalOR1(x, 14109)


def sequence5():
    if relay[30000]:
        interlock = True

    x = [0 for _ in range(2)]
    x[0] = 3009
    x[1] = 13002
    verticalOR1(x, x[1])

    x[0] = 3013
    x[1] = 13008
    verticalOR1(x, x[1])

    x[0] = 3101
    x[1] = 13014
    verticalOR1(x, x[1])

    x[0] = 3105
    x[1] = 13104
    verticalOR1(x, x[1])

    x[0] = 3001
    x[1] = 13110
    verticalOR1(x, x[1])

    x[0] = 3005
    x[1] = 14000
    verticalOR1(x, x[1])

    x[0] = 3109
    x[1] = 14006
    verticalOR1(x, x[1])

    x[0] = 3113
    x[1] = 14012
    verticalOR1(x, x[1])
    interlock = False


def sequence6():
    x = [0 for _ in range(6)]
    x[0] = 13002
    x[1] = 13008
    x[2] = 13014
    x[3] = 13104
    x[4] = 13110
    x[5] = 14000
    verticalOR1(x, 30003)

    x = [0 for _ in range(2)]
    x[0] = 14006
    x[1] = 14012
    verticalOR1(x, 30004)

    x[0] = 30003
    x[1] = 30004
    verticalOR1(x, 15111)

    x[0] = 4311
    x[1] = 15111
    verticalOR1(x, 14110)

    charge_command_memory()

    x = [0 for _ in range(12)]
    x[0] = 13108
    x[1] = 13114
    x[2] = 13000
    x[3] = 13006
    x[4] = 13012
    x[5] = 13102
    x[6] = 4604
    x[7] = 4605
    x[8] = 4600
    x[9] = 4601
    x[10] = 4602
    x[11] = 4603
    horizontalOR(x, 3006)

    x = [0 for _ in range(4)]
    x[0] = 14004
    x[1] = 14010
    x[2] = 4606
    x[3] = 4607
    horizontalOR(x, 30007)

    x = [0 for _ in range(4)]
    x[0] = 30006
    x[1] = 30007
    x[2] = 4606
    x[3] = 4607
    horizontalOR(x, 30007)

    x = [0 for _ in range(3)]
    x[0] = 30006
    x[1] = 30007
    x[2] = 30005
    horizontalAND(x, 15109)

    x = [0 for _ in range(2)]
    x[0] = 15109
    x[1] = 4704
    horizontalAND(x, 14108)

    if relay[30005]:
        if not relay[14108]:
            if not relay[15009]:
                relay[30008] = True

    overtime1_wait_time()

    x = [0 for _ in range(3)]
    x[0] = 4700
    x[1] = 4701
    x[2] = 14108
    horizontalOR(x, 30208)

    if not relay[4700] or relay[15009]:
        relay[30209] = True


def sequence7():
    if relay[30209]:
        interlock = True

    x = [0 for _ in range(2)]
    x[0] = 13000
    x[1] = 30210
    verticalOR1(x, x[1])

    x[0] = 13006
    x[1] = 30211
    verticalOR1(x, x[1])

    x[0] = 13012
    x[1] = 30212
    verticalOR1(x, x[1])

    x[0] = 13102
    x[1] = 30213
    verticalOR1(x, x[1])

    x[0] = 13108
    x[1] = 30214
    verticalOR1(x, x[1])

    x[0] = 13114
    x[1] = 30215
    verticalOR1(x, x[1])

    x[0] = 14004
    x[1] = 30300
    verticalOR1(x, x[1])

    x[0] = 14010
    x[1] = 30301
    verticalOR1(x, x[1])
    interlock = False


def sequence8():
    if relay[15009]:
        interlock = True

    x = [0 for _ in range(3)]
    x[0] = 4600
    x[1] = 30210
    x[2] = 13003
    block1(x)

    x[0] = 4601
    x[1] = 30211
    x[2] = 13009
    block1(x)

    x[0] = 4602
    x[1] = 30212
    x[2] = 13015
    block1(x)

    x[0] = 4603
    x[1] = 30213
    x[2] = 13105
    block1(x)

    x[0] = 4604
    x[1] = 30214
    x[2] = 13111
    block1(x)

    x[0] = 4605
    x[1] = 30215
    x[2] = 14001
    block1(x)

    x[0] = 4606
    x[1] = 30300
    x[2] = 14007
    block1(x)

    x[0] = 4607
    x[1] = 30301
    x[2] = 14013
    block1(x)
    interlock = False


def sequence9():
    x = [0 for _ in range(6)]
    x[0] = 13003
    x[1] = 13009
    x[2] = 13015
    x[3] = 13105
    x[4] = 13111
    x[5] = 14001
    verticalOR1(x, 30302)

    x = [0 for _ in range(2)]
    x[0] = 14007
    x[1] = 14013
    verticalOR1(x, 30303)

    x[0] = 30302
    x[1] = 30303
    verticalOR1(x, 15112)

    x[0] = 4312
    x[1] = 15112
    verticalOR1(x, 14111)

    if relay[14108]:
        if not relay[14113]:
            if not relay[14112]:
                relay[30304] = True

    if relay[4700] or relay[4701] or relay[14113]:
        relay[30503] = True


def sequence10():
    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 3800+i
    horizontalAND(x, 30504)

    for i in range(6):
        x[i] = 3806+i
    horizontalAND(x, 30505)

    for i in range(4):
        x[i] = 3812+i
    x[4] = 3900
    x[5] = 3901
    horizontalAND(x, 30506)

    x = [0 for _ in range(3)]
    for i in range(3):
        x[i] = 3902+i
    horizontalAND(x, 30507)

    x = [0 for _ in range(6)]
    x[0] = 3907
    x[1] = 3908
    x[2] = 3909
    x[3] = 3910
    x[4] = 4314
    x[5] = 4707
    block2(x, 15000)

    x = [0 for _ in range(5)]
    for i in range(5):
        x[i] = 30504+i
    horizontalAND(x, 15000)

    x = [0 for _ in range(3)]
    for i in range(3):
        x[i] = 4608+i
    horizontalAND(x, 14115)

    x = [0 for _ in range(5)]
    x[0] = 3800
    x[1] = 3912
    x[2] = 4111
    x[3] = 30509
    x[4] = 4609

    t = [True for _ in range(5)]
    x[0] = False
    x[1] = False
    x[2] = False

    verticalOR2(x, t, 15010)

    x[0] = 3801
    x[1] = 3913
    x[2] = 4112
    verticalOR2(x, t, 15011)

    x[0] = 3802
    x[1] = 3914
    x[2] = 4113
    verticalOR2(x, t, 15012)

    x[0] = 3803
    x[1] = 3915
    x[2] = 4114
    verticalOR2(x, t, 15013)

    x[0] = 3804
    x[1] = 4000
    x[2] = 4115
    verticalOR2(x, t, 15014)

    x[0] = 3805
    x[1] = 4001
    x[2] = 4200
    verticalOR2(x, t, 15015)

    x[0] = 3806
    x[1] = 4002
    x[2] = 4201
    verticalOR2(x, t, 15100)

    x[0] = 3807
    x[1] = 4003
    x[2] = 4202
    verticalOR2(x, t, 15101)

    x[0] = 3808
    x[1] = 4004
    x[2] = 4203
    verticalOR2(x, t, 15102)

    x[0] = 3809
    x[1] = 4005
    x[2] = 4204
    verticalOR2(x, t, 15103)

    x[0] = 3810
    x[1] = 4006
    x[2] = 4205
    verticalOR2(x, t, 15104)

    x[0] = 3811
    x[1] = 4007
    x[2] = 4206
    verticalOR2(x, t, 15105)

    x[0] = 3812
    x[1] = 4008
    x[2] = 4207
    verticalOR2(x, t, 15106)

    x[0] = 3813
    x[1] = 4009
    x[2] = 4208
    verticalOR2(x, t, 15107)

    x = [0 for _ in range(6)]
    x[0] = 3814
    x[1] = 4010
    x[2] = 4209
    x[3] = 30509
    x[4] = 4608
    x[5] = 4708

    t = [True for _ in range(6)]
    x[0] = False
    x[3] = False
    x[4] = False
    verticalOR2(x, t, 15108)

    x = [0 for _ in range(7)]
    x[0] = 3901
    x[1] = 4013
    x[2] = 4105
    x[3] = 4212
    x[4] = 30509
    x[5] = 4609
    x[6] = 4710

    t = [True for _ in range(7)]
    t[0] = False
    t[4] = False
    t[5] = False
    verticalOR2(x, t, 13004)

    x = [0 for _ in range(7)]
    x[0] = 3902
    x[1] = 4014
    x[2] = 4106
    x[3] = 4213
    x[6] = 4711
    verticalOR2(x, t, 13010)

    x[0] = 3903
    x[1] = 4015
    x[2] = 4107
    x[3] = 4213
    x[6] = 4712
    verticalOR2(x, t, 13100)

    x[0] = 3904
    x[1] = 4100
    x[2] = 4108
    x[3] = 4215
    x[6] = 4713
    verticalOR2(x, t, 13106)

    x = [0 for _ in range(6)]
    x[0] = 3815
    x[1] = 4011
    x[2] = 4103
    x[3] = 4210
    x[4] = 30509
    x[5] = 4610

    t = [True for _ in range(6)]
    t[0] = False
    t[4] = False
    t[5] = False
    verticalOR2(x, t, 13112)

    x = [0 for _ in range(7)]
    x[0] = 3900
    x[1] = 4012
    x[2] = 4104
    x[3] = 4211
    x[4] = 30509
    x[5] = 4610
    x[6] = 4709

    t = [True for _ in range(7)]
    t[0] = False
    t[4] = False
    t[5] = False
    verticalOR2(x, t, 14002)

    x = [0 for _ in range(6)]
    x[0] = 13004
    x[1] = 13010
    x[2] = 13100
    x[3] = 13106
    x[4] = 13112
    x[5] = 14002
    verticalOR1(x, 30510)

    x = [0 for _ in range(2)]
    x[0] = 14008
    x[1] = 14014
    verticalOR1(x, 30511)

    contact1(30410, 15113)

    x = [0 for _ in range(2)]
    x[0] = 15113
    x[1] = 4705
    verticalOR1(x, 30512)

    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 3308+i
    verticalOR3(x, 30513)

    x[0] = 3314
    x[1] = 3315
    for i in range(4):
        x[i+2] = 3400+i
    verticalOR3(x, 30514)

    x = [0 for _ in range(3)]
    x[0] = 30513
    x[1] = 30514
    x[2] = 3008

    t = [True for _ in range(3)]
    t[2] = False
    verticalOR2(x, t, 13005)

    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 3404+i
    verticalOR3(x, 30515)

    for i in range(6):
        x[i] = 3410+i
    verticalOR3(x, 30600)

    x = [0 for _ in range(3)]
    x[0] = 30515
    x[1] = 30600
    x[2] = 3012
    verticalOR2(x, t, 13011)

    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 3500+i
    verticalOR3(x, 30601)

    for i in range(6):
        x[i] = 3506+i
    verticalOR3(x, 30602)

    x = [0 for _ in range(3)]
    x[0] = 30601
    x[1] = 30602
    x[2] = 3100
    verticalOR2(x, t, 13101)

    x = [0 for _ in range(6)]
    for i in range(4):
        x[i] = 3512+i
    x[4] = 3600
    x[5] = 3601
    verticalOR3(x, 30603)

    for i in range(6):
        x[i] = 3602+i
    verticalOR3(x, 30604)

    x = [0 for _ in range(3)]
    x[0] = 30603
    x[1] = 30604
    x[2] = 3104
    verticalOR2(x, t, 13107)

    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 3200+i
    verticalOR3(x, 30605)

    for i in range(6):
        x[i] = 3206+i
    verticalOR3(x, 30606)

    x = [0 for _ in range(3)]
    x[0] = 30605
    x[1] = 30606
    x[2] = 3000
    verticalOR2(x, t, 13113)

    x = [0 for _ in range(6)]
    for i in range(4):
        x[i] = 3212+i
    x[4] = 3300
    x[5] = 3301
    verticalOR3(x, 30607)

    for i in range(6):
        x[i] = 3302+i
    verticalOR3(x, 30608)

    x = [0 for _ in range(3)]
    x[0] = 30607
    x[1] = 30608
    x[2] = 3004
    verticalOR2(x, t, 14003)

    for i in range(6):
        x[i] = 3608+i
    verticalOR3(x, 30609)

    x[0] = 3614
    x[1] = 3615
    for i in range(4):
        x[i+2] = 3700+i
    verticalOR3(x, 30610)

    x = [0 for _ in range(2)]
    x[0] = 30609
    x[1] = 30610
    verticalOR1(x, 14009)

    x = [0 for _ in range(6)]
    for i in range(6):
        x[i] = 3704+i
    verticalOR3(x, 30611)

    for i in range(6):
        x[i] = 3710+i
    verticalOR3(x, 30612)

    x = [0 for _ in range(2)]
    x[0] = 30611
    x[1] = 30612
    verticalOR1(x, 14015)

    x = [0 for _ in range(6)]
    x[0] = 13005
    x[1] = 13011
    x[2] = 13101
    x[3] = 13107
    x[4] = 13113
    x[5] = 14003
    verticalOR1(x, 30613)

    x = [0 for _ in range(2)]
    x[0] = 14009
    x[1] = 14015
    verticalOR1(x, 30614)

    contact1(30613, 15114)

    if not relay[15114] and not relay[4706]:
        relay[14113] = True

    contact1(4308, 16000)
    contact2(16000, 15003)

    contact1(4309, 30709)
    contact2(30709, 15004)
    contact1(4313, 14114)
    
    x = [0 for _ in range(3)]
    x[0] = 4611
    x[1] = 4612
    x[2] = 4613
    verticalOR1(x, 30710)


sequence1()
sequence2()
sequence3()
sequence4()
sequence5()
sequence6()
sequence7()
sequence8()
sequence9()
sequence10()
