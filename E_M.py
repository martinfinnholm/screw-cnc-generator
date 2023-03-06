

x12      = [0, 0.06, 0.24, 0.54, 0.96, 1.51, 2.17, 2.97, 3.88, 4.92]
A        = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
A_minus  = [-0, -10, -20, -30, -40, -50, -60, -70, -80, -90]
x_start  = 12.3
stigning = 26
varv     = 7
varv_rel     = (varv) -1
snurr    = x_start + (stigning*varv_rel)
snurr_A  = (varv_rel*360)+180
x_90     = round((x_start-x12[9]), 2)
plunge_feed = 50
x12.reverse()
A_minus.reverse()



a=0
b=0
T=str(16)

N1 = ("G54G90G0X12.3Y0A-180")
N2 = ("G43Z50"+ "H"+ T+ "M3")
N3 = ("Z2M16")
N4 = ("G1Z-4F40")  
    
    
def end():
    print("G0Z50M9")
    print("M98P1")
    print("M30")
    print("%")
    

def start():
    print(N1)
    print(N2)
    print(N3)
    print(N4)
def sin_minus():
    print("X"+ str(x12[a])+ ("A")+ str(A_minus[a]))
def sin_plus():
    print("X"+ str(x12[b])+ ("A")+ str(A[b])) 

start()
a=0
b=0
while a <9:
    sin_minus()
    a=a+1

x12.reverse()

while b <10:
    sin_plus()
    b=b+1
    
def med():
    print("X"+ str(x_start)+ "A180")
    print("X"+str(snurr)+ "A"+ str(snurr_A))
    
med()
snurr = snurr+x_90
snurr_A = snurr_A + 90
#avslut börjar
print("X"+str(snurr)+ "A"+ str(snurr_A))

A.reverse()
a1=9
b1=8

for i in range(9):
    x_delta =  x12[a1] - x12[b1]
    snurr = snurr + round(x_delta, 2)
    snurr_A = snurr_A + 10
    print ("X"+ str(round (snurr ,2)) + "A"+ str(snurr_A))
    if a1>1:
        a1= a1-1
        b1= b1-1
#reverse X from here
    

a2=1
b2=0
for i in range(9):
    xrev_delta =  x12[a2] - x12[b2]
    snurr = snurr - round(xrev_delta, 2)
    snurr_A = snurr_A + 10
    print ("X"+ str(round (snurr ,2))+ "A"+ str(snurr_A))
    if a2<9:
        a2= a2+1
        b2= b2+1

snurr = snurr - x_90
snurr_A = snurr_A +90
print("X"+ str(snurr)+ "A"+ str(snurr_A))

snurr = round((snurr-(varv_rel*stigning)),2)
snurr_A = (snurr_A + (varv_rel*360)) 
print("X"+ str(snurr)+ "A"+ str(snurr_A))

print("Z-8"+ "F"+ str(plunge_feed))

snurr = round((snurr+(varv_rel*stigning)),2)
snurr_A = (snurr_A - (varv_rel*360)) 
print("X"+ str(snurr)+ "A"+ str(snurr_A))

snurr = snurr + x_90
snurr_A = snurr_A -90
print("X"+ str(snurr)+ "A"+ str(snurr_A))

a3 = 9
b3 = 8
for i in range(9):
    xrev_delta1 =  x12[a3] - x12[b3]
    snurr = snurr + round(xrev_delta1, 2)
    snurr_A = snurr_A - 10
    print ("X"+ str(round (snurr ,2))+ "A"+ str(snurr_A))
    if a3>1:
        a3= a3-1
        b3= b3-1
        
a4 = 1
b4 = 0
for i in range(9):
    xrev_delta2 =  x12[a4] - x12[b4]
    snurr = snurr - round(xrev_delta2, 2)
    snurr_A = snurr_A - 10
    print ("X"+ str(round (snurr ,2))+ "A"+ str(snurr_A))
    if a4<9:
        a4= a4+1
        b4= b4+1
        
snurr = snurr - x_90
snurr_A = snurr_A -90
print("X"+ str(snurr)+ "A"+ str(snurr_A))

snurr = snurr-(stigning*varv_rel)
snurr_A = snurr_A-(varv_rel*360)
print("X"+ str(round (snurr ,2))+ "A"+ str(snurr_A))


a=1
b=0
#A.reverse()
x12.reverse()
while b <10:
    sin_plus()
    b=b+1
A_minus.reverse()
x12.reverse()
while a <10:
    sin_minus()
    a=a+1
    
print("X"+ str(x_start)+ "A-180")

end()