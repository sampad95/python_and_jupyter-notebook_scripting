start=eval(input('Enter the starting digit of the range\n'))
stop=eval(input('Enter the end digit of the range\n'))
step=eval(input('Enter the step of the range\n'))
r=range(start,stop,step)
print('range r=',r)
print('number of elements in',r, '=',len(r))      # 'len' is another built-in function
print('smallest element of the',r,'=',min(r))     # 'min' is another built-in function
print('largest element of the',r,'=',max(r))      # 'max' is another built-in function

print('list of', r, '=',list(r))                  # 'list' is another built-in function
print('tuple of', r, '=',tuple(r))                # 'tuple' is another built-in function

#print('Enter any number to check whether it belongs to',r)
#x=eval(input())                                             # 'eval' and 'input' are also built-in functions
#print(x in r)

#print(r.index(x))

#m=eval(input('Enter the index number for which you want the number in the list\n'))
#print(m,'th element is',r[m])

p,q=eval(input('Enter the index numbers with commas for slicing\n')) 
print('(',p,',',q,') sliced range is =',r[p:q])
print('smallest element of the',r[p:q],'=',min(r[p:q]))
print('largest element of the',r[p:q],'=',max(r[p:q]))
print('list of (',p,',',q,') sliced range is =',list(r[p:q]))
