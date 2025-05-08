import matplotlib.pyplot as plt

# Peach Innovators

variables = ['Average Watts', 'Variance Watts', 'Average Effective Length']
coefficients = [0.0082, -2.168e-05, -0.0076]
lower_bound = [0.008, -3.93e-05, -0.013]
upper_bound = [0.009, -4.05e-06, -0.002]

lower_errors = [coef - low for coef, low in zip(coefficients, lower_bound)]
upper_errors = [up - coef for coef, up in zip(coefficients, upper_bound)]
asymmetric_error = [lower_errors, upper_errors]

plt.figure(figsize=(5, 10))
plt.errorbar(variables, coefficients, yerr=asymmetric_error, fmt='o', capsize=5, capthick=2,
             ecolor='red', marker='s', markersize=7, mfc='blue', mec='green')
plt.title('Coefficient Estimates and Confidence Intervals\n(Raw Speed)')
plt.xlabel('Variables')
plt.ylabel('Coefficients')
plt.axhline(0, color='grey', linewidth=0.8)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig('Coeff_Plot_Raw_Speed.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()

# Peach Innovators 2.0

variables = ['Average Watts', 'Variance Watts', 'Average Effective Length']
coefficients = [0.0033, 2.208e-05, -0.0011]
lower_bound = [0.003, 1.47e-05, -0.004]
upper_bound = [0.004, 2.94e-05, 0.001]

lower_errors = [coef - low for coef, low in zip(coefficients, lower_bound)]
upper_errors = [up - coef for coef, up in zip(coefficients, upper_bound)]
asymmetric_error = [lower_errors, upper_errors]

plt.figure(figsize=(5, 10))
plt.errorbar(variables, coefficients, yerr=asymmetric_error, fmt='o', capsize=5, capthick=2,
             ecolor='red', marker='s', markersize=7, mfc='blue', mec='green')
plt.title('Coefficient Estimates and Confidence Intervals\n(Average Normalized Speed)')
plt.xlabel('Variables')
plt.ylabel('Coefficients')
plt.axhline(0, color='grey', linewidth=0.8)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig('Coeff_Plot_Normalized_Speed.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()
