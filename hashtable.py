class HashTable:
  def __init__(self, size):
    self.data = [ None ] * size
  
  def get(self, key):
    address = self.__hash_function(key)
    current_bucket = self.data[address]
    if current_bucket:
      for element in current_bucket:
        if element[0] == key:
          return element[1]
    return None

  def set(self, key, val):
    key_value_pair = [key, val]
    address = self.__hash_function(key)
    if self.data[address] is None:
      self.data[address] = [key_value_pair]
    else:
      self.data[address].append(key_value_pair)
    
  def keys(self):
    all_buckets = [ bucket for bucket in self.data if bucket ]
    return [element[0] for each_bucket in all_buckets for element in each_bucket]

  def __hash_function(self, key):
    hash = 0
    for i in range(len(key)):
      hash = (hash + ord(key[i]) * i) % len(self.data)
    return hash
