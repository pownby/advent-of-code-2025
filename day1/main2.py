from .parse import parse

def get_num_zeros(n, rotation):
  raw_num = n + rotation
  num = raw_num % 100
  num_zeros = abs(raw_num // 100)

  # this seems a bit clumsy but it did the trick
  if rotation < 0:
    if num == 0:
      num_zeros += 1
    elif n == 0:
      num_zeros -= 1
  
  return num, num_zeros
  
def main2():
  rotations = parse("input.txt")
  num = 50
  total_zeros = 0

  for rotation in rotations:
    num, num_zeros = get_num_zeros(num, rotation)
    total_zeros += num_zeros

  print(f"Password {total_zeros}")

def run_tests():
  tests = [
    (50, 75, 1),
    (50, 175, 2),
    (50, 50, 1),
    (50, 150, 2),
    (50, 49, 0),
    (50, -75, 1),
    (50, -175, 2),
    (50, -50, 1),
    (50, -150, 2),
    (50, -49, 0),
    (0, 5, 0),
    (0, 105, 1),
    (0, -5, 0),
    (0, -105, 1)
  ]

  for test in tests:
    num, rotation, expected = test
    actual = get_num_zeros(num, rotation)[1]
    if (actual != expected):
      print(f"Failed: {num} {'>' if rotation > 0 else '<'} {rotation}. Expected {expected} but received {actual}")
  
if __name__ == "__main__":
   main2()