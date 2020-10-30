class HashTable:
  def __init__(self, size):
    self.data = [ None ] * size
  
  def get(self, key):
    index = self.__hash_function(key)
    return self.data[index][1]

  def set(self, key, val):
    key_value_pair = [key, val]
    # handle key isExisting
    index = self.__hash_function(key)
    self.data[index] = key_value_pair

  def __hash_function(self, key):
    hash = 0
    for i in range(len(key)):
      hash = (hash + ord(key[i]) * i) % len(self.data)
    return hash
