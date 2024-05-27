alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
in_string = input("Enter message, Hint HELLO: ")
shift = int(input("Enter a shift number :"))
n = len(in_string)
out_string = ""
for i in range(n):
   c = in_string[i]
   loc = alpha.find(c.upper())
   new_loc = loc + shift
   if new_loc >= 26:
       new_loc -= 26   
   out_string += alpha[new_loc]
   print (i, c, loc, new_loc, out_string)
print ("Output After Encryption :", out_string)


# Used to subtract the number after exceeding limit of 26
#   if new_loc >= 26:
#        new_loc -= 26   