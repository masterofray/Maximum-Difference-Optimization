print('='*30+'\n')

def uji(Sz, n1, n2) :
     try:
          Sz = int(Sz)
     except ValueError :
         while (isinstance(Sz, int) == False) :
             print('\nAnda salah memasukkan besaran elemen.')
             Bsel = input('Masukkan kembali elemen berbilangan bulat : ')
             try :
                 Sz = int(Bsel)
                 break
             except ValueError :
                 pass

     if ((Sz<n1 or Sz>=n2) == True) :
          print('\nAnda salah memasukkan besaran Satuan.\n')
          while ((Sz<n1 and Sz>=n2) == False) :
               Sz = int(input('Masukkan kembali dengan besaran yang sesuai : '))
               try:
                    if ((Sz<n1 or Sz>=n2)==False) :
                         break
               except ValueError:
                    pass
               except EOFError:
                    pass
               except :
                    pass
     return int(Sz)

Boundary = int(input('Input Upper Boundary : '))

test = input('Input Banyaknya elemen : ')
Sizex = uji(test, 2, 1000)
print('Size = ',Sizex)
print('='*30+'\n')

test = input('Input Maxdiff : ')
Maxdiff = uji(test, 1, Boundary-1)
print('Maxdiff = ',Maxdiff)
print('='*30+'\n')

Element = []
for i in range(Sizex) :
     x = input('Masukkan elemen : ')
     x = uji(x, 1, Boundary)
     if (i == 0) :
          Element.append(x)
     elif (i>0 and i<(Sizex-1)) :
          a = Element[i-1]
          x = uji(x, a, Boundary)
          Element.append(x)
     elif (i == Sizex-1) :
          a2 = Maxdiff + Element[0]
          x = uji(x, a2, Boundary)
          Element.append(x)

A = Element
print('Vektor A = ',A)
print('\nElement 1 dari Vektor A : ',A[0])
print('='*30+'\n')

B = []
for i in range(Sizex) :
     B.append(A[i])
test1 = input('Masukkan element 1 yang telah optimal dari vektor B : ')
B[0] = uji(test1,1,A[1])
test2 = input('Masukkan element akhir yang telah optimal dari vektor B : ')
b = Sizex-1
Maxdiff_B = Maxdiff+B[0]
B[b] = uji(test2,A[b-1],Maxdiff_B+1)
print('\nVektor B = ',B)
print('='*30+'\n')

cost = []
for i in range(len(A)):
     y = (A[i] - B[i])**2
     cost.append(y)
costx = sum(cost)
print('Cost = ',costx)
print('='*30+'\n')
