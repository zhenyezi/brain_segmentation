__author__ = 'adeb'

import numpy as np


class PickTarget():
    def __init__(self, dataset):
        self.ds = dataset

    def pick_target(self, id0, id1, mri, label):
        raise NotImplementedError


class PickTgCentered(PickTarget):
    def __init__(self, dataset):
        PickTarget.__init__(self, dataset)

    def pick_target(self, id0, id1, mri, label):
        temp = self.ds.vx[id0:id1]
        self.ds.tg[np.arange(id0, id1), label[[temp[:, i] for i in xrange(3)]]] = 1


class PickTgProportion(PickTarget):
    def __init__(self, dataset):
        PickTarget.__init__(self, dataset)

    def pick_target(self, id0, id1, mri, label):
        lab_flat = label.ravel()
        for i in xrange(id0, id1):
            a = np.bincount(lab_flat[self.ds.idx_patch[i]])
            b = np.nonzero(a)[0]
            c = a[b].astype(float, copy=False)
            c = c / sum(c)
            self.ds.tg[i, b] = c