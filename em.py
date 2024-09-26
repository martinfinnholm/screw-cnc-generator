cnc_file = "5500.cnc"
print("1:\tX12.3")
print("2:\tX21.5")
print("Choose 'End according to step file': ")
user_input = int(input(">>> "))

X_start = 12.3
if user_input == 2:
    X_start = 21.5

l = [[0, 0.06, 0.24, 0.54, 0.96, 1.51, 2.17, 2.97, 3.88, 4.92],
    [0, 0.1, 0.39, 0.78, 1.57, 2.45, 3.54, 4.82, 6.31, 8]
    ]

startEnd_X = l[user_input - 1]
#print(startEnd_X)
a_plus = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a_minus = [-0, -10, -20, -30, -40, -50, -60, -70, -80, -90]
pitch = float(input("Pitch: "))
#pitch = 54
revolutions = float(input("Revolutions: "))
#revolutions = 7
rev_full_pitch = (revolutions) -1
X_abs = X_start + (pitch * rev_full_pitch)
A_abs = (rev_full_pitch * 360) + 180
X_startEnd = round((X_start-startEnd_X[9]), 2)
plunge_feed = 50
startEnd_X.reverse()
a_minus.reverse()
a = 0
b = 0
p = []
f = 400
 

def start():
    p.append("%")
    p.append(":" + cnc_file[:4])
    p.append("T16M6")
    p.append("G54G90G0X" + str(X_start) + "Y0A-180")
    p.append("G43Z50H16S2600M3")
    p.append("Z2M16")
    p.append("G1Z-4F40")
    p.append("F" + str(f))


def end():
    p.append("G0Z50M9")
    p.append("M98P1")
    p.append("M30")
    p.append("%")


def sin_minus():
    p.append("X" + str(round(startEnd_X[a], 2))+ ("A") + str(a_minus[a]))


def sin_plus():
    p.append("X" + str(round(startEnd_X[b], 2)) + ("A") + str(a_plus[b])) 

#-------------------------------------------------------------

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

p.append("X" + str(X_start) + "A180")
p.append("X" + str(X_abs) + "A" + str(A_abs))
    
X_abs = X_abs + X_startEnd
A_abs += 90

#avslut börjar----------------------------

p.append("X" + str(round(X_abs, 2)) + "A" + str(A_abs))

a_plus.reverse()
a = 9
b = 8

for i in range(9):
    x_delta = startEnd_X[a] - startEnd_X[b]
    X_abs = X_abs + round(x_delta, 2)
    A_abs = A_abs + 10
    p.append ("X" + str(round(X_abs ,2)) + "A" + str(A_abs))
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
    p.append ("X"+ str(round (X_abs, 2)) + "A" + str(A_abs))
    if a<9:
        a = a + 1
        b = b + 1

X_abs = X_abs - X_startEnd
A_abs = A_abs + 90
p.append("X" + str(round(X_abs, 2)) + "A" + str(A_abs))

X_abs = round((X_abs - (rev_full_pitch * pitch)), 2)
A_abs = (A_abs + (rev_full_pitch * 360)) 
p.append("X" + str(round(X_abs, 2)) + "A" + str(A_abs))

p.append("Z-8" + "F" + str(plunge_feed))

X_abs = round((X_abs + (rev_full_pitch * pitch)), 2)
A_abs = (A_abs - (rev_full_pitch * 360)) 
p.append("X" + str(round(X_abs, 2)) + "A" + str(A_abs) + "F" + str(f))

X_abs = X_abs + X_startEnd
A_abs = A_abs - 90
p.append("X" + str(round(X_abs, 2)) + "A" + str(A_abs))

a = 9
b = 8
for i in range(9):
    xrev_delta =  startEnd_X[a] - startEnd_X[b]
    X_abs = X_abs + round(xrev_delta, 2)
    A_abs = A_abs - 10
    p.append ("X" + str(round(X_abs, 2)) + "A" + str(A_abs))
    if a>1:
        a = a - 1
        b = b - 1
        
a = 1
b = 0
for i in range(9):
    xrev_delta =  startEnd_X[a] - startEnd_X[b]
    X_abs = X_abs - round(xrev_delta, 2)
    A_abs = A_abs - 10
    p.append ("X" + str(round (X_abs , 2)) + "A" + str(A_abs))
    if a < 9:
        a = a + 1
        b = b + 1
        
X_abs = X_abs - X_startEnd
A_abs = A_abs - 90
p.append("X" + str(round(X_abs, 2)) + "A" + str(A_abs))

X_abs = X_abs - (pitch * rev_full_pitch)
A_abs = A_abs - (rev_full_pitch * 360)
p.append("X" + str(round(X_abs, 2)) + "A" + str(A_abs))

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
    
p.append("X" + str(round(X_start, 2)) + "A-180")
        

end()

with open(cnc_file, "w") as my_file:
    for line in p:
        my_file.write(line + "\n")

print(cnc_file + " outputted!")
