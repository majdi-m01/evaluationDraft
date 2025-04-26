import matplotlib.pyplot as plt
import numpy as np

# Data converted to minutes
methods = ['Plaintext', 'Re-Encryption', 'Client-Assisted', 'Encrypted Gradients']
times_in_minutes = [178.19, 171.62, 173.52, 195.76]  # Total time in minutes

# Define colors for each method
colors = ['skyblue', 'lightgreen', 'salmon', 'plum']

# Create a wider horizontal bar graph
plt.figure(figsize=(12, 6))  # Increased the width to make the graph wider
bars = plt.barh(methods, times_in_minutes, color=colors, edgecolor='black')

# Add labels and title
plt.xlabel('Total Time (minutes)', fontsize=12)
plt.ylabel('Method', fontsize=12)
plt.title('Total Time of Federated Learning Across Different Methods', fontsize=14, pad=15)

# Add value labels next to each bar for clarity (bold values)
for bar in bars:
    xval = bar.get_width()
    plt.text(xval + 2, bar.get_y() + bar.get_height()/2, f'{xval:.2f}',
             va='center', ha='left', fontsize=10, fontweight='bold')

# Adjust x-axis to give some space for the labels
plt.xlim(0, max(times_in_minutes) + 20)

# Add grid for better readability
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Improve layout to avoid label cutoff
plt.tight_layout()

# Save the plot as a high-quality image suitable for an academic paper
plt.savefig('FL_Process_Total_Time.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
