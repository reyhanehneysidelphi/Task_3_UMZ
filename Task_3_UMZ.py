SuspectA ={'a1':True, 'a2':True, 'a3':True}
SuspectB ={'b1':True, 'b2':True, 'b3':True}
SuspectC ={'c1':True, 'c2':True, 'c3':True}
SuspectD ={'d1':True, 'd2':True, 'd3':True}

Suspects = [SuspectA, SuspectB, SuspectC, SuspectD]

for item in Suspects:
    for i in item:
        if SuspectA['a1'] == True:
            SuspectC.update({'c1':False})
        else:
            SuspectA['a1'] == False
            SuspectC.update({'c1':True})

        if SuspectA['a2'] == True:
            SuspectB.update({'b3':False})
            SuspectC.update({'c2':False})
            SuspectD.update({'d3':False})
        
        else:
            SuspectA['a2'] == False
            SuspectB.update({'b3':True})
            SuspectC.update({'c2':True})

        if SuspectB['b1'] == True:
            SuspectD.update({'d1':False})
        else:
            SuspectB['b1'] == False
            SuspectD.update({'d1':True})

        if SuspectB['b2'] == True:
            SuspectD.update({'d3':False})
        else:
            SuspectB['b2'] == False
            SuspectD.update({'d3':True})

        if SuspectC['c3'] == True:
            SuspectD.update({'d2':False})
        else:
            SuspectC['c3'] == False
            SuspectD.update({'d2':True})

if SuspectA['a1'] == True or SuspectB['b3'] == False or SuspectC['c2']:
    print('B stole the car.')
elif SuspectD['d3'] == True:
    print('A stole the car.')
elif SuspectB['b1']:
    print('D stole the car.')
else:
    print('C stole the car.')