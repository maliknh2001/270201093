# Harmonic sum
def harmonic(n):
  if n == 0:
    return 0
  else:
    return 1/n + harmonic(n-1)

# Reversing a list
def get_reversed(alist):
  if len(alist) == 0:
    return []
  else:
    return [alist[-1]] + get_reversed(alist[:-1])

print(get_reversed([1,2,3,4]))

# Finding even numbers:

def get_evens(alist):
  if len(alist) == 0:
    return 0
  else:
    if alist[0]%2 == 0:
      return 1 +get_evens(alist[1:])
    else:
      return get_evens(alist[1:])

print(get_evens([0,1,2,3,4,5]))

# Simple timer I have done it a lot already so i didnt do it again.
