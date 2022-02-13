import random
n = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
nc = 0
mais = 0
menos = 0
for r in n:
     nc += 1
     if nc == 1:
          mais = r
          menos = r
     else:
          if r > mais:
               mais = r
          if r < menos:
               menos = r
print(f'''o maior numero digitado foi "{mais}"
e o menor numero digitado foi "{menos}"''')
print(n)