import numpy as np
def generateDiskGalaxy(galaxySize,maxcharge,galaxyHeight=0.01):
    positions = generateDisk(galaxySize,galaxyHeight)
    charges = generateCharge(positions,maxcharge)
    return positions,charges

def generateCharge(positions,maxcharge):
    origins = np.zeros_like(positions)
    distances = np.linalg.norm(positions-origins,axis=1) #calculate distance to the origin
    maxdis = np.max(distances)
    norm_distance = distances/(maxdis*1.001)
    charges = [maxcharge*(1-d) for d in norm_distance] # more close more likely to have a high charge
    return charges


def generateDisk(galaxySize,galaxyHeight):
    length = np.sqrt(np.random.uniform(0, 1, galaxySize))
    angle = np.pi * np.random.uniform(0, 2,galaxySize)
    x = length * np.cos(angle)
    y = length * np.sin(angle)
    z = galaxyHeight * np.random.uniform(-1, 1, galaxySize)
    return list(zip(x,y,z))
