#!/usr/bin/env python3


import furuta_plot as fuplot
import logging
import matplotlib.pyplot as plt
import numpy as np
import sys

def main():
    fig = plt.figure(figsize=(16, 9))
    p = fuplot.FurutaPlotter(fig, (1,2))

    p.add_3D(span=1)

    p.add_linear(y="theta", x="t", span=2, color="orange",
                 x_label="t [s]",
                 y_label="cos($\\theta$)", y_transform=lambda y: np.cos(y))

    p.animate(fps=30,
              t=[float(i/30) for i in range(500)],
              phi=[float(2*np.pi * i/250) for i in range(500)],
              theta=[float(2*np.pi * i/50) for i in range(500)])


if __name__ == "__main__":
    loghandler = logging.StreamHandler(sys.stderr)
    loghandler.setFormatter(logging.Formatter("[%(asctime)s %(levelname)s] %(name)s:%(lineno)d: %(message)s"))
    logging.getLogger().addHandler(loghandler)
    logging.getLogger().setLevel(logging.INFO)

    main()
