import lasio
import pandas as pd
import numpy as np

las = lasio.read("104.las")
df = las.df()


Start = las.well.strt.value
Stop = las.well.stop.value
Depth = las['DEPT']
Need = las['APS']
print('Введите значение глубины которое вас интересует от ',Start, ' до ',Stop)
a = float(input("Введите начало ") or Start)
b = float(input("Введите конец ") or Stop)

if a >= Start and b <= Stop:    
    inda = list(Depth).index(a)
    indb = list(Depth).index(b)
    i = 0
    t = inda
    sym = 0

    while t < indb:
        if Need[t] == Need[t]:
            sym = sym + Need[t]                      
            i += 1
        # else:

        t += 1
    
    if i == 0:
        print('Значения в заданном промежутке - NULL')
    else:
        sa = sym/i
        print('Среднее значение на промежутке',a,'-',b,' = ',sa) 
else: 
    print('Введенный интервал глубин не входит в анализируемый промежуток')

