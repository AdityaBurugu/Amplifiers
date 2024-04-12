import numpy as np


def Resonating_Freq_Design(R,C):
    f=1/(2*np.pi*eval(R)*eval(C))
    return f