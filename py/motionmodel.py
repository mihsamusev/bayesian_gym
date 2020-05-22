class MotionModel:
    def __init__(self, T, accuracy="exact"):
        self.state_size = 0
        self.T = T
        self.accuracy = accuracy

    def get_system_matrix(self):
        pass

    def size(self):
        return self.state_size

class ConstantVel2d(MotionModel):
    '''
    state with position and velocity
    '''
    def __init__(self, T, accuracy="exact"):
        super().__init__(T, accuracy)
        self.A = [[1, self.T],[0, 1]]
        # 1 becomes identity of size N in N dimentions

class ConstantAcc2d(MotionModel):
    '''
    Constant acceleration model
    state with position velocity and acceleration
    '''
    def __init__(self, T, accuracy="exact"):
        super().__init__(T, accuracy)
        if self.accuracy == "euler":
        self.A = [
            [1, self.T, 0],
            [0, 1, self.T],
            [0, 0, 1]]
        elif self.accuracy == "exact":
        self.A = [
            [1, self.T, self.T ** 2 / 2],
            [0, 1, self.T],
            [0, 0, 1]]
        else:
            ValueError("wrong accuracy input, should be euler or exact")

class CoordinatedTurn(MotionModel):
    '''
    Coordinated turn model
    state with x y position velocity rotation and rotational speed