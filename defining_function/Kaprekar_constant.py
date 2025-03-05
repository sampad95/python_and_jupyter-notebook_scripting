import random

# n=random.randint(1001, 9999)
# print("Initial n = ", n)
# i = 0
# while(n!=6174):
#     min_n=int(''.join(sorted(str(n))))
#     max_n=int(''.join(sorted(str(n), reverse=True)))   
#     diff = max_n - min_n
#     i = i+1
    
#     print(max_n, min_n, diff)

#     n = diff
        
#     print("Next n=", n, "Step = ", i)


#############################################################################

# n=random.randint(100, 10000)
# # n = 2045
# print("Initial n = ", n)
# i = 0
# if len(str(n)) == 4:
#     while(int(n)!=6174):
#         min_n=int(''.join(sorted(str(n))))
#         max_n=int(''.join(sorted(str(n), reverse=True)))
#         if min_n == max_n:
#             print("Invalid")
#             break
#         else:
#             diff = max_n - min_n
#             i +=1
    
#             print("Step = ", i)
#             print(max_n, min_n, diff)
                
#             if len(str(diff)) == 4:
#                 n = diff
#             elif len(str(diff)) == 3:
#                 n = '0'+str(diff)
#             elif len(str(diff)) == 2:
#                 n = '00'+str(diff)
#             else:
#                 n = '000'+str(diff)
                
#             print("Next n=", n)

# else:
#     print("Invalid")     


######################################################################

def Kaprekar_routine(n):
    if len(str(n)) == 4:
        while(int(n)!=6174):
            min_n=int(''.join(sorted(str(n))))
            max_n=int(''.join(sorted(str(n), reverse=True)))   
            diff = max_n - min_n

            if len(str(diff)) == 4:
                n = diff
            elif len(str(diff)) == 3:
                n = '0'+str(diff)
            elif len(str(diff)) == 2:
                n = '00'+str(diff)
            else:
                n = '000'+str(diff)

            print(n)
    else:
        print("Invalid")


Kaprekar_routine(1000)