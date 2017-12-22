def main():
    grid = []
    rows = 0
    cols = 0
    try:
        while True:
            arg = raw_input()
            rows += 1
            cols = len(arg)
            grid.append(list(arg))
    except EOFError:
        solve(grid)

def solve(arg):
    vc = VirusCarrier(arg)
    vc.display_grid(5)
    for i in range(10000):
        vc.burst()
    vc.display_grid(5)
    print vc.infect_counter

def get_fromgrid(grid,x,y):
    rows = len(grid)
    cols = len(grid[0])
    try:
        return grid[rows/2-y][cols/2+x]
    except IndexError:
        #print "tried to access coords,",x,y
        return '.'

UP,DOWN,LEFT,RIGHT = 1,2,3,4

class VirusCarrier():
    """Virus Carrier"""
    def __init__(self,grid):
        self.grid = {}
        self.position = (0,0)
        self.facing = UP
        self.infect_counter = 0
        for y in range(-len(grid)/2+1,len(grid)/2+1):
            for x in range(-len(grid[0])/2+1,len(grid[0])/2+1):
                self.grid[(x,y)] = get_fromgrid(grid,x,y)
    def display_grid(self, size):
        out = ""
        for y in range(size,-size,-1):
            for x in range(-size,size):
                out += (" %c " % self.get((x,y))
                        if (x,y)!=self.position
                        else "[%c]" % self.get((x,y)))
            out += "\n"
        print out
    def get(self, coord):
        try:
            return self.grid[coord]
        except KeyError as e:
            self.grid[coord] = '.'
            return '.'
    def set(self, coord, val):
        try:
            self.grid[coord] = val
        except KeyError as e:
            self.grid[coord] = val
    def move_fwd(self):
        x,y = self.position
        if self.facing == UP:
            y += 1
        elif self.facing == LEFT:
            x -= 1
        elif self.facing == DOWN:
            y -= 1
        elif self.facing == RIGHT:
            x += 1
        self.position = x,y
    def turn(self, arg):
        if arg == LEFT:
            if self.facing == UP:
                self.facing = LEFT
            elif self.facing == LEFT:
                self.facing = DOWN
            elif self.facing == DOWN:
                self.facing = RIGHT
            elif self.facing == RIGHT:
                self.facing = UP
        if arg == RIGHT:
            if self.facing == UP:
                self.facing = RIGHT
            elif self.facing == RIGHT:
                self.facing = DOWN
            elif self.facing == DOWN:
                self.facing = LEFT
            elif self.facing == LEFT:
                self.facing = UP
    def burst(self):
        pt = self.position
        if self.get(pt)=='#':
            self.turn(RIGHT)
            self.set(pt, '.')
        else:
            self.turn(LEFT)
            self.set(pt, '#')
            self.infect_counter += 1
        self.move_fwd()

main()
