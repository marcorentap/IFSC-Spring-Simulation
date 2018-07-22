import numpy as np
def GetExactValues(step, springConstant, mass, initialDisplacement, velocity, timeStep):
    k = springConstant
    m = mass
    y_0 = initialDisplacement
    y_0_prime = velocity
    h = timeStep

    h_squared  = h**2
    omega_0 = np.sqrt(k/m)
    print(omega_0)
    gamma_1 = y_0
    gamma_2 = y_0_prime/omega_0

    results = []
    if step == 0:
        results.append(1.0)
        return results
    for t in np.arange(0, step*h + h, h):
        # HACK: Computers are bad at floating points
        ans = gamma_1 * np.cos(omega_0 * t) + gamma_2 * np.sin(omega_0 * t)
        results.append(ans)
    return results

def GetApproximateValues(step, springConstant, mass, initialDisplacement, velocity, timeStep, ref):
    k = springConstant
    m = mass
    y_0 = initialDisplacement
    y_0_prime = velocity
    h = timeStep

    omega_0 = np.sqrt(k/m)
    gamma_1 = y_0
    gamma_2 = y_0_prime/omega_0

    results = []
    results.append(y_0)
    y_1 = GetExactValues(step, k, m, y_0, y_0_prime, h)[1]
    results.append(y_1)

    Y1 = results[-2]
    Y2 = results[-1]

    if step == 0:
        return Y1
    elif step == 1:
        return Y2

    for x in range(2, step + 1):
        Y_n_plus_1 = 2*results[-1] - results[-2] + h**2 * (ref.GetValue("b1")*results[-2]*(-k/m) + ref.GetValue("b2")*results[-1]*(-k/m) + (ref.GetValue("b3")*((results[-1]*(1 + ref.GetValue("c3")) - results[-2]*ref.GetValue("c3")) + (h**2)*(ref.GetValue("a31")*(Y1)*(-k/m) + ref.GetValue("a32")*(Y2)*(-k/m)))*(-k/m) + ref.GetValue("b4")*((results[-1]*(1 + ref.GetValue("c4")) - results[-2]*ref.GetValue("c4")) + (h**2)*(ref.GetValue("a41")*(Y1)*(-k/m) + ref.GetValue("a42")*(Y2)*(-k/m) + ref.GetValue("a43")*((results[-1]*(1 + ref.GetValue("c3")) - results[-2]*ref.GetValue("c3")) + (h**2)*(ref.GetValue("a31")*(Y1)*(-k/m) + ref.GetValue("a32")*(Y2)*(-k/m)))*(-k/m)))*(-k/m) + ref.GetValue("b5")*((results[-1]*(1 + ref.GetValue("c5")) - results[-2]*ref.GetValue("c5")) + (h**2)*(ref.GetValue("a51")*(Y1)*(-k/m) + ref.GetValue("a52")*(Y2)*(-k/m) + ref.GetValue("a53")*((results[-1]*(1 + ref.GetValue("c3")) - results[-2]*ref.GetValue("c3")) + (h**2)*(ref.GetValue("a31")*(Y1)*(-k/m) + ref.GetValue("a32")*(Y2)*(-k/m)))*(-k/m) + ref.GetValue("a54")*((results[-1]*(1 + ref.GetValue("c4")) - results[-2]*ref.GetValue("c4")) + (h**2)*(ref.GetValue("a41")*(Y1)*(-k/m) + ref.GetValue("a42")*(Y2)*(-k/m) + ref.GetValue("a43")*((results[-1]*(1 + ref.GetValue("c3")) - results[-2]*ref.GetValue("c3")) + (h**2)*(ref.GetValue("a31")*(Y1)*(-k/m) + ref.GetValue("a32")*(Y2)*(-k/m)))*(-k/m)))*(-k/m)))*(-k/m)))

        results.append(Y_n_plus_1)
    return(results)
