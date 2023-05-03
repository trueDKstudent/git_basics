class Entity:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def update(self, dx, dy, dz):
        self.position[0] += dx
        self.position[1] += dy
        self.position[2] += dz
        return f"{self.name}'s position was updated"
        
    def draw(self):
        return f"{self.name}'s currnet coords are {self.position}"
        
    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, position={self.position})"
        
        
class Player(Entity):
    def __init__(self, name, position, health):
        super().__init__(name, position)
        self.health = health
        
    def update(self, dx, dy, dz, dH):
        super().update(dx, dy, dz)
        self.health += dH
        return f"{self.name} now has {self.health} health."
        
    def draw(self):
        super().draw()
        return f"{self.name} is being drawn as a player."
        
    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, position={self.position}, health={self.health})"
