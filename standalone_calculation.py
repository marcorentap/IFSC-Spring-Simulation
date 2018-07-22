import numpy as np
def GetExactValues(step, springConstant, mass, initialDisplacement, velocity, timeStep):
    k = springConstant
    m = mass
    y_0 = initialDisplacement
    y_0_prime = velocity
    h = timeStep

    h_squared  = h**2
    omega_0 = np.sqrt(k/m)
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

    if step == 0:
        return results[0]
    elif step == 1:
        return results[1]

    for x in range(2, step + 1):
        Y1 = results[-2]
        Y2 = results[-1]
        
        sigma_i_3 = ref.GetValue("a31")*Y1*(-k/m) + ref.GetValue("a32")*Y2*(-k/m)
        Y3_front = results[-1]*(1 + ref.GetValue("c3")) - results[-2]*ref.GetValue("c3")
        Y3 = Y3_front + (h**2)*(sigma_i_3)
        # print("\n\n{}".format(x))
        # print("3: {} : {} : {}".format(sigma_i_3, Y3_front, Y3))

        sigma_i_4 = ref.GetValue("a41")*Y1*(-k/m) + ref.GetValue("a42")*Y2*(-k/m) + ref.GetValue("a43")*Y3*(-k/m)
        Y4_front = results[-1]*(1 + ref.GetValue("c4")) - results[-2]*ref.GetValue("c4")
        Y4 = Y4_front + (h**2)*(sigma_i_4)
        # print("4: {} : {} : {}".format(sigma_i_4, Y4_front, Y4))

        sigma_i_5 = ref.GetValue("a51")*Y1*(-k/m) + ref.GetValue("a52")*Y2*(-k/m) + ref.GetValue("a53")*Y3*(-k/m) + ref.GetValue("a54")*Y4*(-k/m)
        Y5_front = results[-1]*(1 + ref.GetValue("c5")) - results[-2]*ref.GetValue("c5")
        Y5 = Y5_front + (h**2)*(sigma_i_5)
        # print("5: {} : {} : {}".format(sigma_i_5, Y5_front, Y5))

        sigma_f_Y_i = ref.GetValue("b3")*Y3*(-k/m) + ref.GetValue("b4")*Y4*(-k/m) + ref.GetValue("b5")*Y5*(-k/m)
        Y_n_plus_1 = 2*results[-1] - results[-2] + h**2 * (ref.GetValue("b1")*results[-2]*(-k/m) + ref.GetValue("b2")*results[-1]*(-k/m) + sigma_f_Y_i)
        results.append(Y_n_plus_1)
    return(results)