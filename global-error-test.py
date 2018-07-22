import methods
import standalone_calculation_expanded as sce
import standalone_calculation as sc

# Case 1, 0.2
# Global error should be ~2.35155E-09
def GetCase1_0_2():
    k = 1
    m = 4
    y_0 = 1
    y_0_prime = 5
    h = 0.2
    step = 100
    ref = methods.ETSHM6_6_inf

    # Not expanded
    sc_exactResults = [(i, value) for i,value in enumerate(sc.GetExactValues(step, k, m, y_0, y_0_prime, h))]
    sc_approximateResults = [(i, value) for i,value in enumerate(sc.GetApproximateValues(step, k, m, y_0, y_0_prime, h, ref))]
    sc_differences = [(i, value) for i, value in enumerate([abs(sc_exactResults[i][1] - sc_approximateResults[i][1]) for i in range(step + 1)])]
    sc_diffValue = [value[1] for value in sc_differences]

    # Expanded
    sce_exactResults = [(i, value) for i,value in enumerate(sce.GetExactValues(step, k, m, y_0, y_0_prime, h))]
    sce_approximateResults = [(i, value) for i,value in enumerate(sce.GetApproximateValues(step, k, m, y_0, y_0_prime, h, ref))]
    sce_differences = [(i, value) for i, value in enumerate([abs(sce_exactResults[i][1] - sce_approximateResults[i][1]) for i in range(step + 1)])]
    sce_diffValue = [value[1] for value in sce_differences]

    print("Case 1, 0.2")
    # for i in range(step + 1):
    #     print("{} : {} : {}".format(exactResults[i], approximateResults[i], differences[i]))

    print("Global error (Not Expanded): {}".format(max(sc_diffValue)))
    print("Global error (Expanded): {}".format(max(sce_diffValue)))

GetCase1_0_2()
