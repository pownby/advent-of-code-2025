import os
from common_utils.readFileLines import readFileLines

CURRENT_DIR = os.path.dirname(__file__)
DEFAULT_FILE = "input.txt"

def parse(file_name = DEFAULT_FILE):
  lines = readFileLines(f"{CURRENT_DIR}/{file_name}")
  ranges = [range.split('-') for range in lines[0].split(',')]
  return [(int(range[0]), int(range[1])) for range in ranges]

# Example usage
if __name__ == "__main__":
  print(parse(DEFAULT_FILE))