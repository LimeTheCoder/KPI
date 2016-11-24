import matplotlib.pyplot as plt
import numpy as np


def plot_history(hist, title):
    # Alternatives include bmh, fivethirtyeight, ggplot,
    # dark_background, seaborn-deep, etc
    plt.style.use('ggplot')
    plt.title(title, fontname='Ubuntu', fontsize=16,
              fontstyle='italic', fontweight='bold')

    plt.plot(list(range(len(hist))), hist, linewidth=2.0)
    plt.xlabel('Iteration')
    plt.ylabel('Value of x')
    step = 0.2
    plt.yticks(np.arange(np.min(hist) - step, np.max(hist) + step, step))
    plt.show()