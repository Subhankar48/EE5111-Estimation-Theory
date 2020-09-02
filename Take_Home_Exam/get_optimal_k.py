import numpy as np


P_PERISH = 0.1
CP = 70
SP = 100
P_SOLD = 0.9
K_START = 1
K_END = 1000
STEP_SIZE = 10
SIZE_OF_ARRAY = 100

def get_optimal_k(k_start=K_START, k_end=K_END, 
    p_perish=P_PERISH, p_sold=P_SOLD, step_size=STEP_SIZE, 
    size_of_array=SIZE_OF_ARRAY, cp=CP, sp=SP):
    best_k = 0
    max_avg_revenue = 0
    for k in range(k_start, k_end, step_size):
        count = 0
        total_sum = 0
        N_array = np.random.binomial(k, p_perish, size_of_array)
        for n in N_array:
            M_array = np.random.binomial(k-n, p_sold, size_of_array)
            for m in M_array:
                revenue = m*sp-k*cp
                total_sum+=revenue
                count+=1
        avg_revenue = total_sum/count
        if avg_revenue>max_avg_revenue:
            max_avg_revenue = avg_revenue
            best_k = k
    return max_avg_revenue, best_k

print(get_optimal_k())