from PIL import Image
from numpy import array
import pandas as pd

# splitting image into matrices
'''
def splitting():
    img = Image.open(r"sample.jpeg")
    ar = array(img)
    print(ar)
'''


def colour_space_transform():
    # splitting

    img = Image.open(r"sample.jpeg")
    ar = array(img)
    print(ar)



    # colour space transform
    '''sub_arr = pd.DataFrame(ar)
    sr = sub_arr - 128
    print(sr)'''

    # Get size of actual array
    '''size = ar.shape

    for data in range(len(size)):
        M = size[data]
        N = size[data + 1]
        O = size[data + 2]
        break

    print(M, N, O)
    for i in range(M):
        for j in range(N):
            ar[i][j] = ar[i][j]-128

    print(ar)
    print("Subtract each row of  matrix:")'''


# splitting()


if __name__ == "__main__":
    colour_space_transform()
