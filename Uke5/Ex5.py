import numpy as np

def getNAK_System(x_coords, y_coords):
    n = x_coords.size # Antall punkter

    # delta_i = x_(i+1) - x_i
    delta = np.array([x_coords[i]-x_coords[i-1] for i in range(1,n)])

    #BigDelta_i = y_(i+1) - y_i
    BigDelta = np.array([y_coords[i]-y_coords[i-1] for i in range(1,n)])


    A = np.zeros((n,n))
    #Man kan fylle diagonaler i numpy feks slik:
    lowerDiag = np.array([delta[i] for i in range(n-1)])
    #negativ indeksering indekserer baklengs x[-1] = siste element
    lowerDiag[-1] = 1
    #Før vi fyller diagonalen slicer vi matrisen A slik at  
    #diagonalen like under hoveddiagonal blir den nye hoveddiagonalen
    #(vi fyller hovediagonalen på matrisen vi får ved å fjerne øverste rad og siste kolonne)
    np.fill_diagonal(A[1:,:-1],lowerDiag)

    mainDiag = np.ones(n)
    mainDiag[-1] = -1
    mainDiag[1:-1] = np.array([2*delta[i]+2*delta[i+1] for i in range(n-2)])

    upperDiag = np.array([delta[i] for i in range(n-1)])
    upperDiag[0]=-1


    

    np.fill_diagonal(A,mainDiag)
    np.fill_diagonal(A[:-1,1:],upperDiag)


    b = np.zeros(n)
    b[1:-1]=1
    b[1:-1]=np.array([3*(BigDelta[i+1]/delta[i+1]-BigDelta[i]/delta[i]) for i in range(n-2)])

    return A, b


x = np.array([1,2,4,5.,7,9])
y = np.array([2,1,4,3.,0,2])
A, bs = getNAK_System(x,y)
print(A,bs)