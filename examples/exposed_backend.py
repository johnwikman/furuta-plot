#!/usr/bin/env python3

import furuta_plot as fuplot
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig = plt.figure(figsize=(18, 6))
    fig.clear()

    ax1 = fig.add_subplot(1, 3, (1, 1), projection="3d")
    ax2 = fig.add_subplot(1, 3, (2, 2), projection="3d")
    ax3 = fig.add_subplot(1, 3, (3, 3), projection="3d")

    ax1.clear()
    fuplot.backend.plot_3D_axes(ax1, phi=0.0, theta=0.0, render_margin=0.2)
    ax1.legend()

    ax2.clear()
    fuplot.backend.plot_3D_axes(ax2, phi=1.0, theta=1.0, render_margin=0.2)
    ax2.legend()

    ax3.clear()
    fuplot.backend.plot_3D_axes(ax3, phi=-0.1, theta=-np.pi/3, render_margin=0.2)
    ax3.legend()

    plt.show()


if __name__ == "__main__":
    main()
