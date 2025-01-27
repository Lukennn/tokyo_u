h = 900.0

print(h)

w = 162.0

print(w/(h/100.0)**2)
#計算順序を確認
print((h/100.0)**2)

#hを再定義(再代入)
h = 700 + 100
print(h)
#hを自己参照しつつ100加算
h = h + 100
print(h)
#累積代入(increment演算子)
h +=100
print(h)
#pythonの場合の関数の定義はdef(他もあるだろうが)ググったらdefineの略らしい
def bmi(height, weight):
    #return weight / (height/100) ** 2
    bmi_result = weight / (height/100) ** 2
    return bmi_result #このように変数に下ほうが見やすくない…？無駄なのだろうか



#身長を再代入
h = 174
#体重を再代入
w = 57.5
print(bmi(h,w))

def felt_air_temperatire(temperature, humidity):
    return temperature -1 / 2.3 * (temperature-10) * (0.8 - humidity / 100)

print(felt_air_temperatire(28,50))


#pythonの場合はネストで関数の終わりを認識するため以下のままのネストでは関数が使えない。
# def felt_air_temperatire2(temperature, humidity):
# return temperature -1 / 2.3 * (temperature-10) * (0.8 - humidity / 100)
# print(felt_air_temperatire2(28,50))

FEAT = 30.48 

def ft_to_cm(f,i):
    total_inch = 12 * f + i
    cm = total_inch * FEAT / 12
    return cm

print(round(ft_to_cm(5, 2) - 157.48, 6) == 0)
print(round(ft_to_cm(6, 5) - 195.58, 6) == 0)

def quadratic(a,b,c,x):
    result = a * x **2 + b *x + c
    return result

print(quadratic(1,2,1,3)==16)
print(quadratic(1,-5,-2,7)==12)

import math

def heron(a,b,c):
    s = 0.5*(a+b+c)
    return math.sqrt(s*(s-a)* (s-b)* (s-c))

print(heron(3,4,5))

#練習

def qe_disc(a,b,c):
    result = b**2-4*a*c
    return result

def qe_solution1(a,b,c):
    disc = qe_disc(a,b,c)
    result = (-b + math.sqrt(disc))/(2*a) 
    return result

def qe_solution2(a,b,c):
    disc = qe_disc(a,b,c)
    result = (-b-math.sqrt(disc))/(2*a)
    return result

print(qe_disc(1,-2,1))
print(qe_disc(1,-5,6))
print(qe_solution1(1,-2,1))
print(qe_solution2(1,-2,1))
print(qe_solution1(1,-5,6))
print(qe_solution2(1,-5,6))
