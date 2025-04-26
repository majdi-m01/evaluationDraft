import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Plot styling for academic look
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "figure.dpi": 300
})

# Data
data = {
    "Method": ["Plaintext", "Re-Encryption", "Client-Assisted", "Encrypted Gradients"],
    "Training": [26.6481, 32.266, 31.027, 36.32],
    "Preparing Parameters": [0.00545, 2.0152, 1.2512, 3.2935],
    "Loading Parameters": [0.00665, 2.3553, 0.2974, 0.4493]
}

df = pd.DataFrame(data)
df.set_index("Method", inplace=True)

# Calculate maximum total time
max_total_time = df.sum(axis=1).max()

# Create plot with increased width and height
fig, ax = plt.subplots(figsize=(14, 6))

# Colors per phase
colors = ["#4C72B0", "#55A868", "#C44E52"]

# Horizontal stacked bars with phase labels
left = [0] * len(df)
for idx, phase in enumerate(df.columns):
    bars = ax.barh(df.index, df[phase], left=left, label=phase, color=colors[idx])

    # Add labels for each segment
    for i, bar in enumerate(bars):
        width = bar.get_width()
        x_pos = bar.get_x() + width / 2
        y_pos = bar.get_y() + bar.get_height() / 2
        method = df.index[i]

        # Special handling for Plaintext method's small segments
        if method == "Plaintext" and idx > 0:
            # For Preparing Parameters (idx=1)
            if idx == 1:
                ax.text(
                    bar.get_x() + width + 0.5,
                    y_pos - 0.15,  # Position below center
                    f"{width:.3f}",
                    ha="left",
                    va="center",
                    fontsize=9,
                    color="#55A868",  # Green for Preparing Parameters
                    fontweight='bold',  # Bold as requested
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1)
                )
            # For Loading Parameters (idx=2)
            elif idx == 2:
                ax.text(
                    bar.get_x() + width + 0.5,
                    y_pos + 0.15,  # Position above center
                    f"{width:.3f}",
                    ha="left",
                    va="center",
                    fontsize=9,
                    color="#C44E52",  # Red for Loading Parameters
                    fontweight='bold',  # Bold as requested
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1)
                )
            # Draw connecting line for both
            ax.plot([bar.get_x() + width, bar.get_x() + width + 0.5],
                    [y_pos, y_pos], 'k-', linewidth=0.8)
        # Special handling for Loading Parameters in Client-Assisted and Encrypted Gradients
        elif phase == "Loading Parameters" and (method == "Client-Assisted" or method == "Encrypted Gradients"):
            offset = 0.5
            ax.plot([bar.get_x() + width, bar.get_x() + width + offset],
                    [y_pos, y_pos], 'k-', linewidth=0.8)
            ax.text(
                bar.get_x() + width + offset + 0.2,
                y_pos,
                f"{width:.3f}",
                ha="left",
                va="center",
                fontsize=9,
                color="#C44E52",  # Red for Loading Parameters
                fontweight='bold',  # Bold as requested
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1)
            )
        # Place small segment labels outside the bar with a line for other methods
        elif width < 1:
            # Add a small offset to prevent overlap
            offset = 0.5 if idx == 0 else 1.0 if idx == 1 else 1.5
            ax.plot([bar.get_x() + width, bar.get_x() + width + offset],
                    [y_pos, y_pos], 'k-', linewidth=0.8)
            ax.text(
                bar.get_x() + width + offset + 0.2,
                y_pos,
                f"{width:.3f}",
                ha="left",
                va="center",
                fontsize=8,
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1)
            )
        # Place large segment labels inside the bar
        else:
            ax.text(
                x_pos,
                y_pos,
                f"{width:.2f}",
                ha="center",
                va="center",
                color="white",
                fontsize=9,
                fontweight='bold'
            )

    left = [i + j for i, j in zip(left, df[phase])]

# Set x-axis limits and ticks with more padding
ax.set_xlim(0, max_total_time + 12)  # Increased padding for labels
tick_step = 5
max_tick = np.ceil(max_total_time / tick_step) * tick_step
ax.set_xticks(np.arange(0, max_tick + tick_step, tick_step))

# Add grid lines
ax.grid(True, axis="x", linestyle="--", alpha=0.7)

# Labels and title
ax.set_xlabel("Time (seconds)")
ax.set_title("Client Computation Overhead by Phase")
ax.legend(title="Phase", loc="lower right")

# Add more space on the right for the labels
plt.subplots_adjust(right=0.85)

# Adjust layout
plt.tight_layout()

# Save and show
plt.savefig("client_computation_overhead.png", dpi=300, bbox_inches="tight")
plt.show()