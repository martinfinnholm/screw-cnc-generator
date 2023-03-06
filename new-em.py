

startEnd_X = [0, 0.06, 0.24, 0.54, 0.96, 1.51, 2.17, 2.97, 3.88, 4.92]
a_plus = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a_minus = [-0, -10, -20, -30, -40, -50, -60, -70, -80, -90]
X_start = 12.3
pitch = 26
revolutions = 7
rev_full_pitch = (revolutions) -1
X_abs = X_start + (pitch*rev_full_pitch)
A_abs = (rev_full_pitch*360)+180
X_startEnd = round((X_start-startEnd_X[9]), 2)
plunge_feed = 50
startEnd_X.reverse()
a_minus.reverse()
a = 0
b = 0

 
def end():
    print("G0Z50M9")
    print("M98P1")
    print("M30")
    print("%")


def start():
    print("T16M6")
    print("G54G90G0X12.3Y0A-180")
    print("G43Z50H16S2600M3")
    print("Z2M16")
    print("G1Z-4F40")


def sin_minus():
    print("X"+ str(startEnd_X[a])+ ("A")+ str(a_minus[a]))


def sin_plus():
    print("X"+ str(startEnd_X[b])+ ("A")+ str(a_plus[b])) 


start()

a = 0
b = 0
while a < 9:
    sin_minus()
    a += 1

startEnd_X.reverse()

while b < 10:
    sin_plus()
    b += 1

print("X" + str(X_start) + "A180")
print("X" + str(X_abs) + "A" + str(A_abs))
    
X_abs = X_abs + X_startEnd
A_abs += 90

#avslut börjar----------------------------

print("X" + str(X_abs) + "A" + str(A_abs))

a_plus.reverse()
a = 9
b = 8

for i in range(9):
    x_delta = startEnd_X[a] - startEnd_X[b]
    X_abs = X_abs + round(x_delta, 2)
    A_abs = A_abs + 10
    print ("X" + str(round(X_abs ,2)) + "A" + str(A_abs))
    if a>1:
        a = a - 1
        b = b - 1
#reverse X from here
    

a = 1
b = 0
for i in range(9):
    xrev_delta =  startEnd_X[a] - startEnd_X[b]
    X_abs = X_abs - round(xrev_delta, 2)
    A_abs = A_abs + 10
    print ("X"+ str(round (X_abs ,2))+ "A"+ str(A_abs))
    if a<9:
        a = a + 1
        b = b + 1

X_abs = X_abs - X_startEnd
A_abs = A_abs + 90
print("X" + str(X_abs) + "A" + str(A_abs))

X_abs = round((X_abs - (rev_full_pitch * pitch)), 2)
A_abs = (A_abs + (rev_full_pitch * 360)) 
print("X" + str(X_abs) + "A" + str(A_abs))

print("Z-8" + "F" + str(plunge_feed))

X_abs = round((X_abs + (rev_full_pitch * pitch)), 2)
A_abs = (A_abs - (rev_full_pitch * 360)) 
print("X" + str(X_abs) + "A" + str(A_abs))

X_abs = X_abs + X_startEnd
A_abs = A_abs - 90
print("X" + str(X_abs) + "A" + str(A_abs))

a = 9
b = 8
for i in range(9):
    xrev_delta =  startEnd_X[a] - startEnd_X[b]
    X_abs = X_abs + round(xrev_delta, 2)
    A_abs = A_abs - 10
    print ("X" + str(round(X_abs, 2)) + "A" + str(A_abs))
    if a>1:
        a = a - 1
        b = b - 1
        
a = 1
b = 0
for i in range(9):
    xrev_delta =  startEnd_X[a] - startEnd_X[b]
    X_abs = X_abs - round(xrev_delta, 2)
    A_abs = A_abs - 10
    print ("X" + str(round (X_abs , 2)) + "A" + str(A_abs))
    if a < 9:
        a = a + 1
        b = b + 1
        
X_abs = X_abs - X_startEnd
A_abs = A_abs - 90
print("X" + str(X_abs) + "A" + str(A_abs))

X_abs = X_abs - (pitch * rev_full_pitch)
A_abs = A_abs - (rev_full_pitch * 360)
print("X" + str(round(X_abs, 2)) + "A" + str(A_abs))

a = 1
b = 0

startEnd_X.reverse()
while b < 10:
    sin_plus()
    b += 1

a_minus.reverse()
startEnd_X.reverse()

while a < 10:
    sin_minus()
    a += 1
    
print("X" + str(X_start) + "A-180")

end()