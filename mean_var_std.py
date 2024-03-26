import numpy as np

def calculate(x):
    v = np.array([x])
    if v.size < 9:
        return "valueError => list must contain nine numbers"
    else:
        w = v.reshape(3,3)
        fg_mean = np.mean(w, axis=0).tolist(), np.mean(w, axis=1).tolist(), np.mean(v, axis=1).tolist()
        fg_var = np.var(w, axis=0).tolist(), np.var(w, axis=1).tolist(), np.var(v, axis=1).tolist()
        fg_std = np.std(w, axis=0).tolist(), np.std(w, axis=1).tolist(), np.std(v, axis=1).tolist()
        fg_max = np.max(w, axis=0).tolist(), np.max(w, axis=1).tolist(), np.max(v, axis=1).tolist()
        fg_min = np.min(w, axis=0).tolist(), np.min(w, axis=1).tolist(), np.min(v, axis=1).tolist()
        fg_sum = np.sum(w, axis=0).tolist(), np.sum(w, axis=1).tolist(), np.sum(v, axis=1).tolist()
        calculations = {'mean' :fg_mean, 'variance' : (fg_var), 'standard deviation': (fg_std),
                        'max': (fg_max), 'min':(fg_min), 'sum': (fg_sum)}
        return calculations