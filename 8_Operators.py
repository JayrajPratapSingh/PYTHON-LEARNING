# Operators

'''
        <---------------------------OPERATORS--------------------------->
        <--------------------Arithmatic Operators----------------------->

                +   => Addition
                -   => Subtraction
                *   => Multiplication
                /   => Division
                %   => Modulus (returns rimender)
                **  => Exponentiation
                //  => Floor division (Returns nearest whole number like  4//3 = 1)


     <---------------------Assignment Operators-------------------------->

                =  => right value assigned to left 
                += => n2 += n1  means n2 = n2 + n1
                -= => n2 -= n1  means n2 = n2 - n1
                *= => n2 -= n1  means n2 = n2 * n1
                /= => n2 -= n1  means n2 = n2 / n1
                %= => n2 -= n1  means n2 = n2 % n1
                -= => n2 -= n1  means n2 = n2 - n1
                **= => n2 -= n1  means n2 = n2 ** n1
                &= => n2 -= n1  means n2 = n2 & n1
                |= => n2 -= n1  means n2 = n2 | n1
                ^= => n2 -= n1  means n2 = n2 ^ n1
                >>= => n2 -= n1  means n2 = n2 >> n1
                <<= => n2 -= n1  means n2 = n2 << n1

    <---------------------Comparison Operators-------------------------->

              == => Equal
              != => Not Equal
              >  => Greater than
              <  => Less than
              >= => Greater than or equal to 
              <= => Less than or equal to


    <---------------------Logical Operators-------------------------->



                   
              and   => Returns True if both statements are true
              Or   => Returns True if one of the statements is true
              Not  => Reverse the result, returns False if the result is true

    <---------------------Identity Operators-------------------------->




    checks boolean value

              is       => Returns True if both variables are the same object
              is not   => Returns True if both varuables are not the same object



    <---------------------Membership Operators-------------------------->




              in       => Return true if a sequence with the specified value is present in the object
              not in   => Returns True if a sequence with the specified value is not presen in        
                          the object

                          
    <---------------------Bitwise Operators-------------------------->               

            & => AND   0 0 = 0 , 1 1 = 1, 0 1 = 0
            | => OR   0 0 = 0 , 1 1 = 1, 0 1 = 1
            ^ => XOR  0 0 = 0 , 1 1 = 1, 0 1 = 1
            ~ => NOT     ~0 = 1 , ~1 =0
            << => Zero fill left shift   011011 << = 110110
            >> => Zero fill left shift   101010 >> = 010101

            0, 1 are bits in computer 
            Binary system

            
            Desimal   to     Binary

            0        =>      0
            1        =>      1
            2        =>      1 0         => 2 => 1 0
            3        =>      1 1         => 3 => 1 1
            4        =>      1 0 0       
            5        =>      1 0 1
            6        =>      1 1 0
            7        =>      1 1 1
            8        =>      1 0 0 0
            9        =>      1 0 0 1
            14       =>      1 1 1 0

            
            Binary   to      Desimal

            10110    =>      1*2poewr4 + 0*2power3 + 1*2power2 + 1*2power1 + 0 =>22

            and  =>  101 
                     011
                     ---
                     001


'''

print("Addition:",4+3)
print("Substraction:",4-3)
print("Product:",4*3)
print("Division:",4/2)
print("Modulus:", 5%3)
print("Whole Number:", 4//3)
print("Exponentiation:",2**4)


# identity operator

x=5
y=5
print("if x is y:", x is y)
print("if x is not y:", x is not y)


#   <------------------membership operator--------------------->

fruits = ["apple", "banana", "potato", "guavava"]

print("if banana is present in fruits:", "banana" in fruits)
print("if mango is not present in fruits", "mango" not in fruits)

#    <---------------------------Bitwise Operator------------------->


a = 5
b = 3

print("a and b :",  a & b  )
print("a or b :",  a | b  )
print("a xor b :",  a ^ b  )


#    <---------------------------Operators Precedence------------------->

'''
1. ()
2. **
3. /,//,%
4.  *
5.  +
6. Bitwise Shift - >>, <<
8. Comparison - ==, !=,>, <

'''


# <-----------------------------Type Function------------------------->
'''
To know data type we use type()
'''


roll_number = 17
name = "Jayraj"

print(type(name))
print(type(roll_number)) 


# <-----------------------------Typecasting------------------------->


'''
Converting One data type to another datatype
'''

a = "123"
b= 345
print(int(a),float(a), str(b))