"""Read file from web and do analysis of data
"""
import urllib.request
import urllib
from urllib.request import urlopen


def count_words(url):
  count = 0
  for line in urllib.request.urlopen(url):
    count += line.decode('utf-8').count(" ") + 1
  return count

def main():
  """Driven Function
  """
  # TODO: Read file from web
  file_address = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'

  # TODO: Count number of words
  print(count_words(file_address))


if __name__ == '__main__':
  main()