import time

def time_measure_decorator(f):
    def wrapper(*args):
        s = time.time()
        r = f(*args)
        e = time.time()
        print(e-s)
        return r
    return wrapper

@time_measure_decorator
def one_to_n_loop(n):                   #decorator를 사용하면 안쪽 코드를 손을 안 대고 수정가능
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result

@time_measure_decorator
def one_to_n_math(n):
    r = n * (n + 1) // 2
    return r

number = int(input("Input Number : "))

print(one_to_n_math(number))
print(one_to_n_loop(number))

#def outf(a):
#   def innerf():
 #       print(a)
  #  return innerf

#print(outf(7))
#f = outf(7)
#f() #기억을한다