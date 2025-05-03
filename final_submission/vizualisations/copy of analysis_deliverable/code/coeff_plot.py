import matplotlib.pyplot as plt

variables = ['Average Watts', 'Variance Watts', 'Average Effective Length']
coefficients = [ 0.0082, -2.168e-05, -0.0076]
std_err = [ 0.000, 8.98e-06, 0.003]
lower_bound = [ 0.008, -3.93e-05, -0.013]
upper_bound = [ 0.009, -4.05e-06, -0.002]

lower_errors = [coef - low for coef, low in zip(coefficients, lower_bound)]
upper_errors = [up - coef for coef, up in zip(coefficients, upper_bound)]
asymmetric_error = [lower_errors, upper_errors]

plt.figure(figsize=(5, 10))
plt.errorbar(variables, coefficients, yerr=asymmetric_error, fmt='o', capsize=5, capthick=2, ecolor='red', marker='s', markersize=7, mfc='blue', mec='green')
plt.title('Coefficient Estimates and Confidence Intervals')
plt.xlabel('Variables')
plt.ylabel('Coefficients')
plt.axhline(0, color='grey', linewidth=0.8)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.savefig('Coeff Plot.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()
