class WaterJugProblem:
    def __init__(self):
        self.Jug_3 = 0
        self.Jug_4 = 0
        self.solution = []  # To store the sequence of actions
    
    def FillComplete_4L(self):
        if self.Jug_4 < 4:
            self.Jug_4 = 4
            self.solution.append(f"Fill 4L Jug: (Jug3: {self.Jug_3}, Jug4: {self.Jug_4})")
       
    def FillComplete_3L(self):
        if self.Jug_3 < 3:
            self.Jug_3 = 3
            self.solution.append(f"Fill 3L Jug: (Jug3: {self.Jug_3}, Jug4: {self.Jug_4})")
            
    def Empty_4L(self):
        if self.Jug_4 > 0:
            self.Jug_4 = 0
            self.solution.append(f"Empty 4L Jug: (Jug3: {self.Jug_3}, Jug4: {self.Jug_4})")
            
    def Empty_3L(self):
        if self.Jug_3 > 0:
            self.Jug_3 = 0
            self.solution.append(f"Empty 3L Jug: (Jug3: {self.Jug_3}, Jug4: {self.Jug_4})")
            
    def Pour_3L_to_4L(self):
        if self.Jug_3 > 0:
            transfer = min(self.Jug_3, 4 - self.Jug_4)
            self.Jug_4 += transfer
            self.Jug_3 -= transfer
            self.solution.append(f"Pour 3L Jug to 4L Jug: (Jug3: {self.Jug_3}, Jug4: {self.Jug_4})")
            
    def Pour_4L_to_3L(self):
        if self.Jug_4 > 0:
            transfer = min(self.Jug_4, 3 - self.Jug_3)
            self.Jug_3 += transfer
            self.Jug_4 -= transfer
            self.solution.append(f"Pour 4L Jug to 3L Jug: (Jug3: {self.Jug_3}, Jug4: {self.Jug_4})")
    
    def solve(self, target):
        """
        Solve the water jug problem to achieve the target in either jug.
        """
        while self.Jug_3 != target and self.Jug_4 != target:
            if self.Jug_4 == 0:  # Fill 4L jug if it's empty
                self.FillComplete_4L()
            elif self.Jug_3 == 3:  # Empty 3L jug if it's full
                self.Empty_3L()
            else:  # Pour from 4L to 3L jug
                self.Pour_4L_to_3L()
        
        # Print the solution steps
        print("Solution:")
        for step in self.solution:
            print(step)
        print(f"Final State: Jug3: {self.Jug_3}, Jug4: {self.Jug_4}")

# Example Usage
if __name__ == "__main__":
    problem = WaterJugProblem()
    target = 2  # Target amount of water
    problem.solve(target)
