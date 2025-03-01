result = [n for n in range(100, 1000) if sum(int(d) for d in str(n)) % 3 == 0]
print(result)
