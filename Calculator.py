class Calculator:
    def reset(self):
        self.x = 20
        self.y = 10
        self.sum = self.x + self.y
        self.minus = self.x - self.y
        self.divide = self.x / self.y
        self.mult = self.x * self.y


sim = Calculator()
sim.reset()
print(sim.sum,sim.minus,sim.divide,sim.mult)