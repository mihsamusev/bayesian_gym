import numpy as np
from filterpy.kalman import predict, update
from scipy.stats import multivariate_normal
from collections import namedtuple

class GaussianMixture:
    def __init__(self, xs, Ps, ws):
        self.xs = xs
        self.Ps = Ps
        self.ws = ws
        self.count = len(self.xs)

    def get_mixture(self, xval):
        mixture = np.zeros(xval.size)
        for i in range(self.count):
            mixture += self.get_component(i, xval)
        return mixture

    def get_components(self, xval):
        components = np.zeros((xval.size, self.count))
        for i in range(self.count):
            components[:,i] = self.get_component(i, xval)
        return components

    def get_component(self, i, xval):
        return self.ws[i] * multivariate_normal(self.xs[i], self.Ps[i]).pdf(xval)

    def get_pruned(self):
        i = np.argmax(self.ws)
        return self.xs[i], self.Ps[i]

    def get_merged(self):
        xm = np.tensordot(self.ws, np.array(self.xs), 1)
        Pm = np.zeros(self.Ps[0].shape)
        for x, P, w in zip(self.xs, self.Ps, self.ws):
            Pm += w * (P + np.dot(x - xm, x - xm)) 
        return xm, Pm

    def get_n_best(self, n_max):
        if self.count <= n_max:
            return self.xs, self.Ps, self.ws
        else:
            idx = np.argsort(self.ws)
            ws_out = np.array(self.ws)[idx[-n_max:]]
            ws_out = ws_out / np.sum(ws_out)
            xs_out = np.array(self.xs)[idx[-n_max:]]
            Ps_out = np.array(self.Ps)[idx[-n_max:]]
        return xs_out, Ps_out, ws_out

    def get_mmse_estimate(self):
        pass

def approximate_nn(xs, Ps, ws):
    pass

def approximate_pda(xs, Ps, ws):
    pass

def add_mixture(xs, Ps, ws):
    pass

def predict_measurement(x, P, z, R, H):
    x_pred, P_pred = predict(x, P, H, R)
    return multivariate_normal(x_pred, P_pred).pdf(z)

def predict_mixture(xs, Ps, F, Q):
    '''
    xs - list of state
    Ps - list of state covariance matrices
    F - transition matrix 
    Q - process noise matrix
    '''
    xs_pred, Ps_pred = [], []
    for x, P in zip(xs, Ps):
        x_pred, P_pred = predict(x, P, F, Q)
        xs_pred.append(x_pred)
        Ps_pred.append(P_pred)
    return xs_pred, Ps_pred

def update_mixture(xs, Ps, ws, z, R, H, Pd, lamc):
    '''
    xs - list of state
    Ps - list of state covariance matrices
    ws - list of weights
    z - list of measurments 
    R - measurement noise matrix
    H - measurement matrix 
    Pd - probability of detection
    lamc - clutter intensity function handle
    '''
    hypotheses = range(0, len(z) + 1)
    ws_u, xs_u, Ps_u = [],[],[]
    for x_prev, P_prev, w_prev in zip(xs, Ps, ws):
        for h in hypotheses:
            if h == 0:
                weight = w_prev * (1 - Pd)
                ws_u.append(weight)
                xs_u.append(x_prev)
                Ps_u.append(P_prev)
            else:
                zt = z[h - 1]
                weight = w_prev * Pd * predict_measurement(x_prev, P_prev, zt, R, H) / lamc(zt)
                x_u, P_u = update(x_prev, P_prev, zt, R, H)
                ws_u.append(weight)
                xs_u.append(x_u)
                Ps_u.append(P_u)

    # normalize weights
    ws_u = ws_u / np.sum(ws_u)
    return xs_u, Ps_u, ws_u

def run_example():
    Z = [
        [-1.3, 1.7],
        [1.3],
        [-0.3, 2.3],
        [-2, 3],
        [2.8],
        [-3.5, 2.8]
    ]

    lamc = lambda c: 0.4 if np.abs(c) < 4 else 0

    R = np.array([0.2])
    H = np.array([1])
    Q = np.array([0.35])
    F = np.array([1])
    PD = 0.9

    priors = [GaussianMixture(
        [np.array([0.5])],
        [np.array([0.5])],
        [np.array(1.0)])]
    posteriors = []

    # CALCULATE RECURSION
    for k, z in enumerate(Z):
        # update
        xs_u, Ps_u, ws_u = update_mixture(priors[k].xs, priors[k].Ps, priors[k].ws, z, R, H, PD, lamc)
        mixture = GaussianMixture(xs_u, Ps_u, ws_u)
        posteriors.append(mixture)
        # approximation
        xs_gsf, Ps_gsf, ws_gsf  = mixture.get_n_best(5)
        # prediction
        xs_p, Ps_p = predict_mixture(xs_gsf, Ps_gsf, F, Q)
        priors.append(GaussianMixture(xs_p, Ps_p, ws_gsf))

if __name__ == "__main__":
    run_example()