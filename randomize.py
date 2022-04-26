import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mtplt

import os
import cv2
from PIL import Image

low_data = 13
high_data = 40

mu_1, sigma_1 = high_data, 1
mu_3, sigma_3 = low_data, 1


data_number_1 = 30
data_number_2 = 20
data_number_3 = 30

depth_starting = 100

deltaHigh = np.random.randint(low=0, high=30, size=1)[0]
deltaMid = np.random.randint(low=0, high=10, size=1)[0]
deltaLow = np.random.randint(low=0, high=60, size=1)[0]

higher_range_start = depth_starting
higher_range_ends = higher_range_start + deltaHigh

mid_range_starts = higher_range_ends
mid_range_ends = mid_range_starts + deltaMid

low_range_starts = mid_range_ends
low_range_ends = low_range_starts + deltaLow


# -----------------------------------------------------------------------------------------------------------
tx1 = np.sort(np.random.normal(mu_1, sigma_1, data_number_1))
np.random.shuffle(tx1)
ty1 = np.linspace(higher_range_start, higher_range_ends, data_number_1)


# -----------------------------------------------------------------------------------------------------------
tx2 = np.sort(np.random.uniform(low=low_data, high=high_data, size=data_number_2))
tx2 = tx2[::-1]
ty2 = np.linspace(mid_range_starts, mid_range_ends, data_number_2)

# -----------------------------------------------------------------------------------------------------------
tx3 = np.sort(np.random.normal(mu_3, sigma_3, data_number_3))
np.random.shuffle(tx3)
ty3 = np.linspace(low_range_starts, low_range_ends, data_number_3)


# -----------------------------------------------------------------------------------------------------------
x = np.concatenate((tx1, tx2, tx3))
y = np.concatenate((ty1, ty2, ty3))


# Plotting
plt.figure(figsize=(5, 20))
plt.plot(x, y, label="line 1")
plt.gca().invert_yaxis()
plt.xlim(0, 100)
plt.xticks(np.arange(0, 100, 10.0))
plt.yticks(np.arange(min(y), max(y)+1, 5.0))
plt.grid(True)
plt.show()
















import numpy as np
import matplotlib.pyplot as plt
import tkinter
import random
import math
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tkinter.Tk()
root.wm_title("GR Log Generator")

x = []
side_x = []
y = []


mean_median_module = False
crazy_random_shape_module = False

number_based_on_depth = 1
starting = random.randint(100, 2000)

number_of_segments = random.randint(2, 5)
for i in range(0, number_of_segments):
    temp_depth = random.randint(5, 50)
    temp_array = starting+np.arange(0, temp_depth,)
    temp = temp_array[:-1]
    y.extend(temp[:])

    number_of_y = temp_depth / number_based_on_depth
    number_of_x = int(number_of_y)

    possibility = random.randint(0, 10)
    if possibility > 8:
        crazy_random_shape_module = True
        mean_median_module = False
    else:
        crazy_random_shape_module = False
        mean_median_module = True

    if mean_median_module:
        random_mean = random.randint(5, 95)
        if random_mean > 80:
            random_sigma = random.uniform(5, 15)
        else:
            random_sigma = random.uniform(0, 5)

        temp_x = np.random.normal(random_mean, random_sigma, number_of_x)
        x_temp = temp_x[:-1]
        x.extend(x_temp)
    elif crazy_random_shape_module:
        random_mean = random.randint(95, 120)
        random_sigma = random.uniform(15, 25)
        temp_x = np.random.normal(random_mean, random_sigma, number_of_x)
        x_temp = temp_x[:-1]
        x.extend(x_temp)

    starting = max(temp_array)
for i in range(0, len(x)):
    side_x.extend([x[i]-100])


# Plotting
fig = Figure(figsize=(1, 20))

ax = plt.plot(x, y, 'b')
plt.plot(side_x, y, 'b', alpha=0.5)

plt.gca().invert_yaxis()
plt.xlim(0, 100)
plt.xticks(np.arange(0, 101, 10.0))
major_ticks = np.arange(math.floor(min(y)/5)*5, max(y), 5)
plt.yticks(major_ticks)
plt.title("GR Log")
plt.grid(b=True, which='major', color='#666666', linestyle='-', linewidth=1)
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-',  alpha=0.5)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)


tkinter.mainloop()
