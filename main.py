import time
import matplotlib.pyplot as plt

#?? O(n)?
def complexidade(n):
  inicio = time.time()
  while n > 0:
    n -= 1
  fim = time.time()
  return fim-inicio

#?? O(log*n)?
def complexidade2(n):
  inicio = time.time()
  while n > 0:
    n = n/2
  fim = time.time()
  return fim-inicio




#?? O(1)?
def complexidade3(n):
  inicio = time.time()
  n = n**2
  n = n**2
  fim = time.time()
  return fim-inicio

temp_comp = []
temp_comp2 = []
temp_comp3 = []

for i in range(1, 100000, 1000):
  temp_comp.append(complexidade(i))

for i in range(1, 100000, 1000):
  temp_comp2.append(complexidade2(i))

for i in range(1, 100000, 1000):
  temp_comp3.append(complexidade3(i))

'''
print(temp_comp)
print()
print(temp_comp2)
print()
print(temp_comp3)
'''

x = range(1, 100000, 1000)

plt.plot(x, temp_comp)
plt.plot(x, temp_comp2)
plt.plot(x, temp_comp3)
plt.show()

