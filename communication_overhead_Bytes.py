import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Input Data
data = {
    "Encrypted Gradients": {
        "Bytes Sent 1st round - Client": 10000000,
        "Bytes Sent 1st round - Server": 29920980,
        "Bytes Sent per round - Client": 34822660,
        "Bytes Sent per round - Server": 22863684
    },
    "Client-Assisted": {
        "Bytes Sent 1st round - Client": 86341961,
        "Bytes Sent 1st round - Server": 23639913.67,
        "Bytes Sent per round - Client": 31570590,
        "Bytes Sent per round - Server": 23639620
    },
    "Re-Encryption": {
        "Bytes Sent 1st round - Client": 39265771,
        "Bytes Sent 1st round - Server": 29920980,
        "Bytes Sent per round - Client": 34822660,
        "Bytes Sent per round - Server": 22863684
    },
    "Plaintext": {
        "Bytes Sent 1st round - Client": 1052546,
        "Bytes Sent 1st round - Server": 1051966,
        "Bytes Sent per round - Client": 1052558,
        "Bytes Sent per round - Server": 1051966
    }
}

# Step 2: Format DataFrame
df = pd.DataFrame(data).T
df = df.reset_index().rename(columns={"index": "Method"})
df_melt = df.melt(id_vars="Method", var_name="Phase", value_name="Bytes")

# Step 3: Split and clean Round/Role
split_cols = df_melt["Phase"].str.split(" - ", expand=True)
df_melt["Round"] = split_cols[0].str.replace("Bytes Sent ", "").str.strip()
df_melt["Role"] = split_cols[1].str.strip()

# Step 4: Create custom y-axis positions
y_order = [
    ("1st round", "Client"),
    ("1st round", "Server"),
    ("per round", "Client"),
    ("per round", "Server")
]

positions = {key: i for i, key in enumerate(y_order)}
bar_width = 0.18
offsets = [-1.5, -0.5, 0.5, 1.5]  # for 4 methods

# Step 5: Set method colors (matching screenshot)
colors = {
    "Encrypted Gradients": "#00B0F0",
    "Client-Assisted": "#548235",
    "Re-Encryption": "#ED7D31",
    "Plaintext": "#2F75B5"
}

# Step 6: Plotting
fig, ax = plt.subplots(figsize=(10, 5.5))
bar_positions = []
bar_heights = []
bar_colors = []

for i, method in enumerate(colors.keys()):
    subset = df_melt[df_melt["Method"] == method]
    for _, row in subset.iterrows():
        y_pos = positions[(row["Round"], row["Role"])] + offsets[i] * bar_width
        bar_positions.append(y_pos)
        bar_heights.append(row["Bytes"])
        bar_colors.append(colors[method])

ax.barh(bar_positions, bar_heights, height=bar_width, color=bar_colors)

# Step 7: Y-axis labeling
yticks = [positions[key] for key in y_order]
yticklabels = [f"{key[1]}" for key in y_order]  # Client or Server only

ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)

# Step 8: Add group labels manually
ax.text(-1e7, 0.5, "Bytes Sent\n1st round", va='center', ha='right', fontsize=10, rotation=90)
ax.text(-1e7, 2.5, "Bytes Sent\nper round", va='center', ha='right', fontsize=10, rotation=90)

# Step 9: Final touches
ax.set_xlabel("Bytes Sent")
ax.set_title("Communication Overhead (Average Bytes)")
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors.values()]
ax.legend(handles, colors.keys(), title="Method Strategy", loc="upper right", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig("communication_overhead_Bytes_labeled.png", dpi=300)
plt.show()



