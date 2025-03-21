class Gravity:
    def falling(y, v, a, dt):
        v -= (int)(a * dt)
        y -= (int)(v * dt)
        return (y, v)
    
    def lateralMovement(x, v, dt):
        x += (int)(v * dt)
        return x