N=int(input())

row=1
print("*"*(N))
while row<=(N-1)/2:
	print("*"*(N//2-row+1),end="")
	print(" "*(2*row-1),end="")
	print("*"*(N//2-row+1))
	row += 1


while row<N -1:
	print("*"*(row-N//2+1),end="")
	print(" "*(2*(N-row-1)-1),end="")
	print("*"*(row-N//2+1))
	row+=1

print("*"*(N))
print("end")
#---------------------------------------------------------------------------------------------------------------------

N=int(input())

print("*")
row=1
while row<=(N-1)/2:
	print(" "*(2*row-1),end="")
	print("* "*(row),end="")
	print("*")
	row+=1

while row<N-1:
	print(" "*(2*(N-row-1)-1),end="")
	print("* "*(N-row-1),end="")
	print("*")
	row+=1
print("*")
print("end")

#--------------------------------------------------------------------------------------------------------

N=int(input())

row=1
while row<=(N+1)/2:
	print((" ")*(row-1),end="")
	print((row),end="")
	if row!=(N+1)/2:
	    print((" ")*(N-(2*row-1)-1),end="")
	    print(row)
	else:
		print("")

	row+=1

while row<=N:
	print((" ")*(N-row),end="")
	print((N-row+1),end="")
	print(" "*(2*row-N-2),end="")
	print(N-row+1)
	row+=1
print("end")

#----------------------------------------------------------------------------------------------------------

N=int(input())


row=1
i=1

while row<=N:
	if row%2!=0:
		while i<=5*row:
			print((i) , end=" ")
			i+=1
			
		print("")

	else:
		j=i
		while i<=5*row:
			print(j+4, end=" ")
			j-=1
			i+=1

		print("")

	row+=1        		