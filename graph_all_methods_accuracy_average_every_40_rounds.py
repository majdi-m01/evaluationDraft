import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data from the table (all lists have 50 elements)
data = {
    'Iteration': list(range(50)),
    'Plaintext_Min': [0.00, 10.00, 15.34, 23.10, 26.95, 29.51, 32.22, 33.48, 34.89, 35.91, 38.28, 37.61, 37.41, 38.67,
                      40.47, 39.53, 40.37, 42.36, 43.49, 43.20, 39.10, 38.30, 43.48, 43.99, 43.09, 42.37, 42.29, 43.33,
                      43.78, 44.17, 44.26, 44.41, 44.89, 45.56, 45.02, 44.66, 44.98, 44.43, 44.17, 44.29, 44.24, 45.84,
                      47.51, 44.59, 44.53, 44.89, 44.80, 44.25, 44.80, 44.25],
    'Re-Encryption_Min': [0.00, 10.74, 18.69, 23.78, 28.56, 30.38, 31.78, 32.20, 33.87, 35.77, 37.63, 38.50, 38.16,
                          37.37, 41.48, 42.62, 44.09, 43.98, 43.78, 43.79, 43.24, 42.47, 42.19, 46.30, 42.49, 42.46,
                          42.84, 46.89, 46.90, 47.92, 47.90, 47.24, 43.14, 44.46, 46.20, 48.73, 48.74, 47.83, 46.33,
                          43.94, 46.21, 46.70, 45.87, 48.36, 43.84, 43.44, 42.42, 47.58, 42.42, 47.58],
    'Client-Assisted_Min': [0.00, 10.00, 16.35, 24.42, 27.06, 28.67, 31.38, 33.23, 34.15, 35.43, 37.95, 36.13, 36.51,
                            37.65, 42.21, 42.06, 42.19, 42.76, 43.82, 43.24, 43.81, 41.21, 44.45, 46.81, 41.36, 41.46,
                            44.36, 43.59, 43.85, 45.29, 45.98, 43.30, 44.56, 44.55, 44.65, 45.91, 45.11, 43.84, 44.34,
                            43.37, 44.34, 45.70, 45.12, 45.66, 43.84, 43.49, 45.54, 45.72, 45.54, 45.72],
    'Encrypted Gradients_Min': [0.00, 10.54, 19.03, 25.93, 28.36, 30.48, 33.69, 34.62, 37.58, 37.58, 39.43, 38.33,
                                38.09, 38.35, 42.94, 43.01, 43.07, 44.27, 44.29, 43.80, 46.21, 44.45, 47.12, 46.13,
                                43.27, 43.87, 43.68, 44.90, 48.83, 45.12, 45.09, 43.47, 45.02, 45.14, 46.40, 43.82,
                                43.88, 43.15, 45.15, 43.45, 45.55, 45.59, 44.83, 48.74, 43.84, 43.59, 42.92, 44.23,
                                42.92, 44.23],
    'Plaintext_Max': [0.00, 11.34, 20.76, 25.67, 31.55, 31.84, 32.58, 33.90, 35.53, 36.89, 38.62, 39.93, 41.78, 41.29,
                      41.95, 43.55, 44.64, 44.61, 44.55, 46.49, 46.21, 47.12, 47.54, 46.91, 47.47, 47.45, 47.02, 47.36,
                      47.83, 48.15, 48.79, 48.94, 48.63, 49.59, 49.47, 49.02, 49.31, 50.03, 48.94, 49.96, 50.10, 50.21,
                      50.74, 48.36, 48.68, 50.24, 50.47, 50.66, 50.47, 50.66],
    'Re-Encryption_Max': [0.00, 11.48, 20.73, 25.85, 31.25, 31.84, 33.67, 33.87, 37.12, 37.70, 41.03, 41.48, 41.09,
                          40.25, 41.82, 43.43, 44.31, 44.77, 45.05, 46.49, 46.56, 47.54, 47.08, 47.24, 47.06, 47.41,
                          47.59, 47.70, 47.44, 48.10, 48.79, 48.63, 48.90, 49.06, 49.06, 49.91, 49.68, 50.03, 49.40,
                          48.75, 49.20, 50.77, 50.74, 48.36, 48.71, 50.44, 50.15, 50.66, 50.15, 50.66],
    'Client-Assisted_Max': [0.00, 12.58, 19.23, 26.08, 32.06, 32.80, 33.65, 34.27, 36.29, 38.69, 39.92, 40.41, 42.15,
                            41.90, 43.45, 43.67, 44.36, 46.26, 45.47, 46.06, 46.52, 47.08, 47.52, 46.29, 47.65, 47.74,
                            47.65, 47.44, 49.13, 48.31, 48.48, 48.90, 49.09, 50.09, 49.10, 49.74, 49.68, 50.03, 49.40,
                            49.36, 50.24, 50.77, 50.74, 48.71, 48.71, 50.44, 50.59, 50.46, 50.59, 50.46],
    'Encrypted Gradients_Max': [0.00, 12.74, 23.36, 27.07, 32.82, 32.80, 35.32, 35.93, 38.14, 40.09, 41.27, 41.84,
                                43.62, 44.34, 45.54, 45.54, 46.39, 46.26, 47.35, 48.06, 48.06, 48.72, 48.72, 48.05,
                                47.50, 47.92, 47.92, 48.61, 49.61, 50.13, 50.88, 50.88, 50.55, 50.75, 50.55, 50.36,
                                50.86, 50.27, 50.16, 50.58, 50.22, 50.32, 50.74, 48.36, 48.71, 50.19, 50.89, 50.18,
                                50.89, 50.18]
}

# Set the style for a scientific paper
plt.style.use('seaborn-v0_8-whitegrid')  # Clean, professional style
sns.set_context("paper", font_scale=1.2)  # Adjust font size for readability in a paper

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))  # Size suitable for a paper

# Use the "tab10" color palette for distinct, professional colors
colors = plt.cm.tab10(np.linspace(0, 1, 4))  # Select 4 colors from tab10
method_colors = {
    'Plaintext': colors[0],  # Blue
    'Re-Encryption': colors[1],  # Orange
    'Client-Assisted': colors[2],  # Green
    'Encrypted Gradients': colors[3]  # Red
}

# Plot lines with vertical bars for each method
methods = ['Plaintext', 'Re-Encryption', 'Client-Assisted', 'Encrypted Gradients']
for method in methods:
    min_vals = np.array(data[f'{method}_Min'])
    max_vals = np.array(data[f'{method}_Max'])
    iterations = np.array(data['Iteration'])

    # Calculate midpoints for the line
    midpoints = (min_vals + max_vals) / 2

    # Plot the line using midpoints
    ax.plot(iterations, midpoints, label=method, color=method_colors[method], linewidth=1.5)

    # Add vertical lines (error bars) from min to max at each iteration
    for i, (x, ymin, ymax) in enumerate(zip(iterations, min_vals, max_vals)):
        ax.vlines(x, ymin=ymin, ymax=ymax, color=method_colors[method], linewidth=1, alpha=0.7)

# Customize the plot
ax.set_xlabel('Iterations', fontsize=12)
ax.set_ylabel('Accuracy (%)', fontsize=12)  # Updated y-axis label
ax.set_title('Model Accuracy 2000 Rounds with Every 40 Rounds Averaged', fontsize=14, pad=15)  # Updated title

# Set the x-axis and y-axis ticks as specified
ax.set_xticks(range(0, 51, 5))  # X-axis ticks from 0 to 50 with a step of 5
ax.set_yticks(range(0, int(max([max(data[f'{method}_Max']) for method in methods]) + 10), 5))  # Y-axis ticks every 5

# Update the axis limits accordingly
ax.set_xlim(0, 50)  # Iterations from 0 to 50
ax.set_ylim(0, max([max(data[f'{method}_Max']) for method in methods]) + 5)  # Y-axis from 0 to max value + padding

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)  # Grid behind lines

# Add legend in the bottom right
ax.legend(loc='lower right')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot as a high-quality image for a paper
plt.savefig('model_accuracy_2000_rounds_every_40_rounds_averaged.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
