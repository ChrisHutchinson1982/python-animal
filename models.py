class Animal:
  def __init__(self, id, available, name, food, timestamp):
    self.id = id
    self.name = name
    self.food = food
    self.available = available
    self.timestamp = timestamp

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'food': self.food,
      'available': self.available,
      'timestamp':self.timestamp
    }