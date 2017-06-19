#############################################################################
# Full Imports

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

def main():

    # Tentando abrir arquivo de casos
    data = np.loadtxt('caseBase.txt', delimiter=',', usecols=(1,2,3,5))

    Z = linkage(data, 'complete')

    print(Z)

    plt.figure(figsize=(25, 10))
    plt.title('Dendrograma')
    plt.xlabel('índice')
    plt.ylabel('distância')
    dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    plt.show()

if __name__ == "__main__":
    main()