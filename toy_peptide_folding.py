import collections
import numpy as np
from enthought.tvtk.tools import visual

## H-H: -2, P-P: -1, H-P: +1
scoring_dict = {('H','H'):-2, ('H','P'):+1, ('P','P'):-1, ('P','H'):+1}

for aa in 'HPPHPHPPH':
    print aa

class Conformation:
    def __init__(self,peptide):
        self.peptide = peptide
        self.conf_dict = collections.OrderedDict()
        for aa in self.peptide:
            self.conf_matrix[aa] = (0,0,0)
            if peptide.index(aa) == 1:
                self.conf_dict[aa] = (0,0,1)
    def score(self):
        self.score_matrix = np.zeros(len(self.peptide))
        for i in range(len(self.peptide)):
            for j in range(len(self.peptide)):
                if i == j:
                    self.score_matrix[(i,j)] = 0
                elif j == i+1 or j == i-1:
                    self.score_matrix[(i,j)] = 0
                else:
                    self.score_matrix[(i,j)] = 1  ## fix it to actually score: 0 if distance > 1; otherwise use score dict
        print self.score_matrix
        self.score = np.sum(self.score_matrix)
                

class Peptide:
    def __init__(self):
        self.seq = []
    def addAA(self,aa):
        self.seq.append(aa)
    def index(self,aa):
        return self.seq.index(aa)
        

class AA:
    def __init__(self,HorP):
        self.name = HorP
        
s = visual.sphere()
t = visual.sphere()
s.color = (0.0,0.5,1.0)
t.axis = (10,10,10)

s.edit_traits()
##visual.show()
