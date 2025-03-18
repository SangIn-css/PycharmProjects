import time

def one_to_n_loop(n):
    s = time.time()
    result = 0
    for i in range(1, n+1):
        result = result + i
    e = time.time()
    print(e-s)
    return result

def one_to_n_math(n):
    s = time.time()
    r = n * (n + 1) // 2
    e = time.time()
    print(e - s)
    return r

number = int(input("정수 입력 : "))

print(one_to_n_math(number))
print(one_to_n_loop(number))

#def outf(a):
#   def innerf():
 #       print(a)
  #  return innerf

#print(outf(7))
#f = outf(7)
#f() #기억을한다