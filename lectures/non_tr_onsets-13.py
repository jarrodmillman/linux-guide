high_res_hemo = np.convolve(high_res_neural, hrf_at_hr)[:len(high_res_neural)]
plt.plot(high_res_times, high_res_hemo)
# [...]
plt.xlabel('Time (seconds)')
# <...>
plt.ylabel('High resolution convolved values')
# <...>
len(high_res_times)
# 17300
