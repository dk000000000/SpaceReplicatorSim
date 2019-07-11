import numpy as np
def generateDiskGalaxy(galaxySize):
    positions = generateDisk(galaxySize)
    charges = generateCharge(positions,maxcharge)
    return positions,charges

def generateCharge(positions,maxcharge):
    origins = np.zeros_like(positions)
    distances = np.linalg.norm(positions-origins) #calculate distance to the origin
    charges = [maxcharge*np.random.normal(d) for d in distances] # more close more likely to have a high charge
    return charges


def generateDisk(galaxySize):
    length = np.sqrt(np.random.uniform(0, 1, self.galaxySize))
    angle = np.pi * np.random.uniform(0, 2, self.galaxySize)
    x = length * np.cos(angle)
    y = length * np.sin(angle)
    z = np.random.uniform(-1, 1, self.galaxySize)
    return zip(x,y,z)
