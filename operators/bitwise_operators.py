'''
Bitwise operators:
these operators are used to perform operations on bits.

& Bitwise And --> Returns 1 if both bits are 1 else it returns 0

| Bitwise OR  --> If any one of the bits is 1 or both bits are 1 it returns 1 else it ruturns 0

^ Bitwise XOR  --> Returns 1 if one of the bits is 1 and other bit is 0 else returns 0

<<  Bitwise left shift --> shifts the bits of the number to the left and fills 0 at the right side

>> Bitwise right shift --> shifts the bits of the number to the right and fills 0 at the left side

1 byte = 8 bits ==> 0000 0000

Converting a decimal number to binary

x = 7 ---> 0111
x = 10 --> 1010
x = 17 --> 10001

 pow(2,5)+pow(2,4)+pow(2,3)+pow(2,2)+pow(2,1)+pow(2,0)
                        32+16+8+4+2+1
                         1 0 0 0 1

Converting a binary to decimal
1010 --> 10

a   b   a&b     a|b     a^b
1   1   1       1       0
1   0   0       1       1
0   1   0       1       1
0   0   0       0       0

1010
0111
a&b = 0010 ==>2
a|b = 1111 ==>15
a^b = 1101 ==>

'''

a=10
b=7
print(a&b)

print(a|b)
print(a^b)

p=10
print(p<<2)  #0000 1010  #0010 1000 > remove 2 bits from the left side and add 2 0's at the right side

q=10
print(q>>2)
#00001010 --> #00000010 == 2  > remove 2 bits from the right side and add 2 0's at the left side

p=20
print(p<<3)
print(p>>3)