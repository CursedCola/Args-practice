def my_sum(*cats):
  print(cats)
print(my_sum(3,4,5))
# args are for entering 
# as many arguements as possible
def a_sum (*args):
  for num in args:
    print (num)

print(a_sum(1))
print(a_sum(1,3))
print(a_sum(1,3,4,5,6))
