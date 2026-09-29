from .parse import parse

def is_invalid(id):
  l = len(id)
  if l % 2:
    return False
  half = l // 2
  first, second = id[:half], id[half:]
  return first == second

def main1():
  ranges = parse("input.txt")
  sum = 0

  for r in ranges:
    for n in range(r[0], r[1] + 1):
      if is_invalid(str(n)):
        sum += n

  print(f"{sum}")
  
if __name__ == "__main__":
  main1()