# import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("place_5.csv")

df['Date'] = pd.to_datetime(df['date'])

new_df = (
    df.groupby([pd.Grouper(key='Date', freq='W-SAT'), 'color'])
        .size()
        .to_frame(name='count')
)
print(df)
print(new_df)
import matplotlib.ticker as ticker

# pivot to wide format
plot_df = (
    new_df.reset_index().pivot(index='Date', columns='color', values='count')
)
# Plot Bar
ax = plot_df.plot(kind='bar', rot=0, ylabel='count')
# Format X-axis ticks
# ax.xaxis.set_major_formatter(
#     ticker.FixedFormatter(plot_df.index.strftime('%Y-%m-%d'))
# )
plt.show()