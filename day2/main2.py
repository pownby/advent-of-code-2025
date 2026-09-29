from .parse import parse
import math

def is_invalid(id):
  l = len(id)
  if (l < 2):
    return False
  
  half = math.floor(l / 2)

  for i in range(half, 0, -1):
    if l % i == 0:
      chunks = [id[j:j + i] for j in range(0, l, i)]
      invalid = all(chunk == chunks[0] for chunk in chunks)
      if invalid:
        return True
  return False

def main2():
  ranges = parse("input.txt")
  sum = 0

  for r in ranges:
    for n in range(r[0], r[1] + 1):
      if is_invalid(str(n)):
        sum += n

  print(f"{sum}")
  
if __name__ == "__main__":
  main2()