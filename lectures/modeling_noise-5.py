mean_vol = np.mean(data, axis=-1)
plt.hist(np.ravel(mean_vol), bins=100)
# (...)
