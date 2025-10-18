#!/usr/bin/env python3
"""
Generate a figure illustrating the temporal windows used in the monarch butterfly analysis.
Shows both 30-minute lag windows and the sunset window analysis approach.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates as mdates

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 6))

# Define time range (2 days)
start_time = datetime(2024, 1, 1, 0, 0)  # Arbitrary date
hours = np.arange(0, 48, 0.5)  # Every 30 minutes for 2 days
times = [start_time + timedelta(hours=h) for h in hours]

# Define sunrise/sunset times (approximate for California winter)
day1_sunrise = 7.0  # 7:00 AM
day1_sunset = 17.5  # 5:30 PM
day2_sunrise = 31.0  # 7:00 AM next day (24 + 7)
day2_sunset = 41.5  # 5:30 PM next day (24 + 17.5)

# Create gradient background for day/night
for i in range(len(hours) - 1):
    hour = hours[i]

    # Determine color based on time of day
    if (day1_sunrise <= hour <= day1_sunset) or (day2_sunrise <= hour <= day2_sunset):
        # Daytime - calculate gradient based on position in day
        if hour < 24:  # Day 1
            day_progress = (hour - day1_sunrise) / (day1_sunset - day1_sunrise)
        else:  # Day 2
            day_progress = (hour - day2_sunrise) / (day2_sunset - day2_sunrise)

        # Peak brightness at midday
        if day_progress < 0.5:
            brightness = 0.3 + 0.7 * (day_progress * 2)
        else:
            brightness = 0.3 + 0.7 * (2 - day_progress * 2)

        # Light yellow at peak, transitioning to light blue at edges
        r = 1.0
        g = 0.95 + 0.05 * (1 - brightness)
        b = 0.85 + 0.15 * (1 - brightness)
        color = (r, g, b, 0.3)  # Semi-transparent
    else:
        # Nighttime - darker blue/gray
        color = (0.7, 0.75, 0.85, 0.2)

    # Draw background rectangle
    rect = patches.Rectangle((times[i], -0.1),
                            timedelta(hours=0.5), 1.2,
                            facecolor=color, edgecolor='none')
    ax.add_patch(rect)

# Add observation points (only during daytime)
observation_y = 0.5
observation_times = []
for i, hour in enumerate(hours):
    if (day1_sunrise <= hour <= day1_sunset) or (day2_sunrise <= hour <= day2_sunset):
        ax.plot(times[i], observation_y, 'ko', markersize=6, zorder=5)
        observation_times.append((times[i], hour))

# Add 30-minute lag windows (show 5 examples from midday of day 1)
lag_y = 0.35
example_start_idx = 16  # Start around noon of day 1
for i in range(5):
    if example_start_idx + i + 1 < len(observation_times):
        t1 = observation_times[example_start_idx + i][0]
        t2 = observation_times[example_start_idx + i + 1][0]

        # Draw bracket using matplotlib's native bracket annotation
        ax.annotate('', xy=(mdates.date2num(t1), lag_y),
                   xytext=(mdates.date2num(t2), lag_y),
                   arrowprops=dict(arrowstyle='|-|', color='darkblue',
                                 linewidth=1.5, shrinkA=0, shrinkB=0))

        # Add small arrows
        ax.annotate('', xy=(t1, observation_y), xytext=(t1, lag_y + 0.05),
                   arrowprops=dict(arrowstyle='-', color='darkblue',
                                 linewidth=1, linestyle='dashed'))
        ax.annotate('', xy=(t2, observation_y), xytext=(t2, lag_y + 0.05),
                   arrowprops=dict(arrowstyle='-', color='darkblue',
                                 linewidth=1, linestyle='dashed'))

# Add sunset window
# Find maximum count time for day 1 (let's say around 2 PM)
day1_max_hour = 14.0  # 2:00 PM
day1_max_time = start_time + timedelta(hours=day1_max_hour)

# Last observation of day 2
day2_last_hour = day2_sunset
day2_last_time = start_time + timedelta(hours=day2_last_hour)

# Draw sunset window bracket
sunset_y = 0.75
ax.annotate('', xy=(mdates.date2num(day1_max_time), sunset_y),
           xytext=(mdates.date2num(day2_last_time), sunset_y),
           arrowprops=dict(arrowstyle='|-|', color='darkred',
                         linewidth=2, shrinkA=0, shrinkB=0))

# Add arrows for sunset window
ax.annotate('', xy=(day1_max_time, observation_y), xytext=(day1_max_time, sunset_y - 0.05),
           arrowprops=dict(arrowstyle='-', color='darkred',
                         linewidth=1.5, linestyle='dashed'))
ax.annotate('', xy=(day2_last_time, observation_y), xytext=(day2_last_time, sunset_y - 0.05),
           arrowprops=dict(arrowstyle='-', color='darkred',
                         linewidth=1.5, linestyle='dashed'))

# Add labels
ax.text(observation_times[example_start_idx + 2][0], lag_y - 0.15,
        '30-minute window',
        fontsize=11, ha='center', color='darkblue', weight='bold')

# Calculate midpoint of sunset window for label
sunset_midpoint = day1_max_time + (day2_last_time - day1_max_time) / 2
ax.text(sunset_midpoint, sunset_y + 0.05,
        'Sunset window',
        fontsize=11, ha='center', color='darkred', weight='bold')

# Add day/night labels
ax.text(start_time + timedelta(hours=3), 0.95, 'Night',
        fontsize=10, ha='center', style='italic', color='gray')
ax.text(start_time + timedelta(hours=(day1_sunrise + day1_sunset)/2), 0.95, 'Day 1',
        fontsize=10, ha='center', weight='bold')
ax.text(start_time + timedelta(hours=24), 0.95, 'Night',
        fontsize=10, ha='center', style='italic', color='gray')
ax.text(start_time + timedelta(hours=(day2_sunrise + day2_sunset)/2), 0.95, 'Day 2',
        fontsize=10, ha='center', weight='bold')
ax.text(start_time + timedelta(hours=45), 0.95, 'Night',
        fontsize=10, ha='center', style='italic', color='gray')

# Sunrise/sunset indicators removed for cleaner appearance

# Add legend for observation points
ax.plot([], [], 'ko', markersize=6, label='Camera observations (30-min intervals)')
ax.legend(loc='upper left', fontsize=10)

# Format the plot
ax.set_xlim(times[0], times[-1])
ax.set_ylim(-0.1, 1.1)

# Format x-axis
ax.xaxis.set_major_locator(mdates.HourLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:00'))
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=3))

# Labels
ax.set_xlabel('Time (hours)', fontsize=12)

# Remove y-axis
ax.set_yticks([])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add day labels below x-axis
ax.text(start_time + timedelta(hours=12), -0.25, 'Day 1',
        fontsize=11, ha='center', weight='bold', transform=ax.get_xaxis_transform())
ax.text(start_time + timedelta(hours=36), -0.25, 'Day 2',
        fontsize=11, ha='center', weight='bold', transform=ax.get_xaxis_transform())

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('temporal_windows.pdf', dpi=300, bbox_inches='tight')
plt.savefig('temporal_windows.png', dpi=300, bbox_inches='tight')

print("Figure saved as temporal_windows.pdf and temporal_windows.png")
plt.show()