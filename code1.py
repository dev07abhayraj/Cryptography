alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
in_string = input("Enter message, hint HELLO: ")
n = len(in_string)
out_string = ""
for i in range(n):
   c = in_string[i]
   loc = alpha.find(c.upper())
   new_loc = loc + 3
   out_string += alpha[new_loc]
   print (i, c, loc, new_loc, out_string)
print ("Output After Encryption :", out_string)


# ------------------------------TESTING--------------------


# alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# in_string = "HElLO"

# c = in_string[2]
# loc = alpha.find(c.upper)

# print(in_string)
# print(c)
# print(loc)