from .parse import parse

def main1():
  rotations = parse("input.txt")
  num = 50
  num_zero = 0

  for rotation in rotations:
    num = (num + rotation) % 100
    if (num == 0):
      num_zero += 1

  print(f"Password {num_zero}")
  
if __name__ == "__main__":
  main1()