from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from GalaxyGeneration import generateDiskGalaxy

import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D
def scatter3d(x,y,z, cs, colorsMap='jet'):
    cm = plt.get_cmap(colorsMap)
    cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter([x], [y], [z], c=scalarMap.to_rgba(cs))
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    scalarMap.set_array(cs)
    fig.colorbar(scalarMap)
    plt.show()

a,b = generateDiskGalaxy(1000,100)
x,y,z=np.hsplit(np.array(a),3)
scatter3d(x,y,z,b)
