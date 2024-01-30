#Write a program to count the numberof vowels and consonants present in an input string.
def vowel_consonant_count(input_str):
    vowel_count=0
    consonant_count=0
    input_str=input_str.lower()#converting string to lower case
    str_length=len(input_str)#length of the string
    for i in range(0,str_length):#iterating through each character of the string
        if input_str[i] in {'a','e','i','o','u'}:#checking if the character is a vowel
            vowel_count=vowel_count+1   #incrementing the count value by 1 if vowel found
            
        elif input_str[i]>='a' and input_str[i]<='z': #checking for consonants
            consonant_count=consonant_count+1  #incrementing count if consonant
    return vowel_count,consonant_count


input_str=input("Enter a string:")
Vowel_consonant=vowel_consonant_count(input_str)
print(Vowel_consonant[0])
print(Vowel_consonant[1])


#Write a program that accepts two matrices A and B as input and returns their product AB.Check if A & B aremultipliable; if not, return error message
import numpy
def Product(A,B):
    product=[[0,0,0],[0,0,0],[0,0,0]]
    dim_A=numpy.shape(A) # dimension of matrix A
    dim_B=numpy.shape(B) #dimension of matrix B
    if(dim_A[1]==dim_B[0]): # checking if the col of A and row of B are of same no.
        for i in range(len(A)):
            for j in range(len(B[0])):
                for a in range(len(B)):
                    product[i][j]=product[i][j]+ (A[i][j]*B[j][a]) # adding the product to the variable
        return product

    else:
        return False
    
A=eval(input("Enter matrix A:"))
B=eval(input("Enter matrix B:"))

p1=Product(A,B)
if p1:
    print(p1)
else:
    print("Matrices are not multipliable")
    
#Write a program to find the number of common elements between two lists. The lists contain integers.
def common_num(List1,List2):
    count=0
    for i in List1:
        for j in List2: # iterating through both the lists and checking for common elements 
            if (i==j):
                count=count+1 # increment by 1 if commonality found
    return count


List1=eval(input("Enter an integer list:"))
List2=eval(input("Enter an integer list:"))
common_number=common_num(List1,List2)
if common_number:
    print(common_number)
else:
    print("No common integers in the lists.")
            
#Write a program that accepts a matrix as input and returns its transpose
def Transpose(Matrix):
    transpose=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(A)): #iterating through the columns of matrix 
        for j in range(len(A[0])):#iterating through the rows of the matrix
            transpose[j][i]=A[i][j]
    return transpose

Matrix=eval(input("enter a Matrix:"))
Tpose=Transpose(Matrix)
print(Tpose)
            
