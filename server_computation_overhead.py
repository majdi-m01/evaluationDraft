import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data from the table
methods = ['Plaintext', 'Re-Encryption', 'Client-Assisted', 'Encrypted Gradients']
agg_serialization = [0.0105, 1.5793, 0.2066, 1.0357]
deserialization = [0.00553, 0.6213, 0.4384, 0.6142]

# Set the style for a scientific paper
plt.style.use('seaborn-v0_8-whitegrid')  # Clean, professional style
sns.set_context("paper", font_scale=1.2)  # Adjust font size for readability in a paper

# Create the horizontal bar chart with a wider figure
fig, ax = plt.subplots(figsize=(10, 5))  # Increased width from 8 to 10

# Bar height and positions
bar_height = 0.35
y = np.arange(len(methods))

# Plot horizontal bars
bars1 = ax.barh(y + bar_height/2, agg_serialization, bar_height, label='Aggregation + Serialization', color='skyblue', edgecolor='black')
bars2 = ax.barh(y - bar_height/2, deserialization, bar_height, label='Deserialization', color='lightcoral', edgecolor='black')

# Add labels on the bars
for bar in bars1:
    width = bar.get_width()
    ax.text(x=width + 0.02, y=bar.get_y() + bar.get_height()/2, s=f'{width:.4f}',
            ha='left', va='center', fontsize=10)

for bar in bars2:
    width = bar.get_width()
    ax.text(x=width + 0.02, y=bar.get_y() + bar.get_height()/2, s=f'{width:.4f}',
            ha='left', va='center', fontsize=10)

# Customize the plot
ax.set_ylabel('Method Strategy', fontsize=12)
ax.set_xlabel('Average Time Taken (sec)', fontsize=12)
ax.set_title('Server Computational Overhead', fontsize=14, pad=15)
ax.set_yticks(y)
ax.set_yticklabels(methods)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)  # Grid behind bars

# Set x-axis limit to accommodate the largest value and its label
max_value = max(max(agg_serialization), max(deserialization))  # Largest value is 1.5793
ax.set_xlim(0, max_value + 0.2)  # Add padding (0.2) for the label

# Add legend in the bottom right
ax.legend(loc='lower right')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot as a high-quality image for a paper
plt.savefig('server_computational_overhead_plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()