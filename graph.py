class Vertex():
    def __init__(self, y, x, weight):
        self.x_ = x
        self.y_ = y
        self.weight_ = weight
        self.neighbors = []

    def addNeighbor (self, vertex):
        self.neighbors.append(vertex)

    def getNeighbor(self):
        return self.neighbors
    
    def getX(self):
        return self.x_
    
    def getY(self):
        return self.y_
    
    def setX(self, x):
        self.x_ = x

    def setX(self, y):
        self.y_ = y
 
    def setWeight(self, weight):
        self.weight_ = weight

    def getWeight(self):
        return self.weight_

class Graph():
    def __init__(self):
        self.vertics_ = {}

    def addVertex_(self, vertex):
        key = (vertex.getY(), vertex.getX())
        self.vertics_[key] = vertex

    def buildGraphFromGrid(self, occupancy_grid):
        height, width = occupancy_grid.shape
        for y in range(height):
            for x in range(width):
                if occupancy_grid [y, x] == 0:
                    vertex = Vertex(y, x, occupancy_grid[y, x])
                    self.addVertex_(vertex)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for y in range(height):
            for x in range(width):
                
                if occupancy_grid[y, x] != 0:
                    continue
                
                current_key = (y, x)
                
                if current_key not in self.vertics_:
                    continue
                
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
   
                    if 0 <= ny < height and 0 <= nx < width:
                        
                        if occupancy_grid[ny, nx] == 0:
                            neighbor_key = (ny, nx)

                            if neighbor_key in self.vertics_:
                                self.vertics_[current_key].addNeighbor(self.vertics_[neighbor_key])
    
    
    def getGraph(self):
        return self.vertics_
        

        
