# -*- coding: utf-8 -*-
"""
barcodeplot.py is part of Coquery.

Copyright (c) 2016, 2017 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License (v3).
For details, see the file LICENSE that you should have received along
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import print_function
from __future__ import unicode_literals

import matplotlib.pyplot as plt
import pandas as pd

from coquery.visualizer import visualizer as vis
from coquery import options
from coquery.gui.pyqt_compat import QtWidgets, QtCore

from coquery.visualizer.colorizer import (
    Colorizer, ColorizeByFactor, ColorizeByNum)


class BarcodePlot(vis.Visualizer):
    axes_style = "white"
    TOP = 0.975
    BOTTOM = 0.025
    COLOR = None

    name = "Barcode plot"
    icon = "Barcode_plot"

    DEFAULT_LABEL = "Corpus position"

    horizontal = True
    force_vertical = False

    def get_custom_widgets(self, *args, **kwargs):
        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QApplication.instance().translate(
                    "BarcodePlot", "Plot horizontal by default", None)
        button = QtWidgets.QApplication.instance().translate(
                    "Visualizer", "Apply", None)

        BarcodePlot.check_horizontal = QtWidgets.QCheckBox(label)
        BarcodePlot.check_horizontal.setCheckState(
            QtCore.Qt.Checked if BarcodePlot.horizontal else
            QtCore.Qt.Unchecked)

        BarcodePlot.button_apply = QtWidgets.QPushButton(button)
        BarcodePlot.button_apply.setDisabled(True)
        BarcodePlot.button_apply.clicked.connect(
            lambda: BarcodePlot.update_figure(
                self, BarcodePlot.check_horizontal.checkState()))

        BarcodePlot.check_horizontal.stateChanged.connect(
            lambda x: BarcodePlot.button_apply.setEnabled(True))

        layout.addWidget(BarcodePlot.check_horizontal)
        layout.addWidget(BarcodePlot.button_apply)
        layout.setStretch(0, 1)
        layout.setStretch(1, 0)
        return [layout]

    @classmethod
    def update_figure(cls, self, i):
        cls.horizontal = bool(i)
        BarcodePlot.button_apply.setDisabled(True)
        self.updateRequested.emit()

    def plot_facet(self,
                   data, color,
                   x=None, y=None, z=None,
                   levels_x=None, levels_y=None, levels_z=None,
                   range_x=None, range_y=None, range_z=None,
                   palette=None, color_number=None,
                   rug=None, rug_color="Black",
                   **kwargs):
        """
        Plot a barcode plot.

        In a barcode plot, each token is represented by a line drawn at the
        location of the corresponding corpus id.
        """

        self._xlab = self.DEFAULT_LABEL
        self._ylab = self.DEFAULT_LABEL

        corpus_id = data["coquery_invisible_corpus_id"]

        if x:
            val = data[x].apply(lambda val: levels_x.index(val))
        elif y:
            val = data[y].apply(lambda y: levels_y.index(y))
        else:
            # neither x nor y is specified, plot default
            val = pd.Series([0] * len(data), index=data.index)

        # Take care of a hue variable:
        if z:
            if data[z].dtype == object:
                self._colorizer = ColorizeByFactor(
                    palette, color_number, levels_z)
            else:
                self._colorizer = ColorizeByNum(
                    palette, color_number, data[z], vrange=range_z)
            cols = self._colorizer.get_hues(data=data[z])
        else:
            self._colorizer = Colorizer(palette, color_number, [])
            cols = self._colorizer.get_hues(n=len(data))

        self.legend_palette = self._colorizer.legend_palette()
        if not (z == x or z == y):
            self.legend_levels = self._colorizer.legend_levels()
        else:
            self.legend_levels = []

        if x and not y:
            BarcodePlot.force_vertical = True
            ax_kwargs = {"xticks": 0.5 + pd.np.arange(len(levels_x)),
                         "xticklabels": levels_x,
                         "xlim": (0, len(levels_x))}
            self._xlab = x
            func = plt.hlines

        elif y and not x:
            BarcodePlot.force_vertical = False
            ax_kwargs = {"yticks": 0.5 + pd.np.arange(len(levels_y)),
                         "yticklabels": levels_y,
                         "ylim": (0, len(levels_y))}
            self._ylab = y
            func = plt.vlines

        else:
            if BarcodePlot.horizontal:
                BarcodePlot.force_vertical = False
                ax_kwargs = {"yticklabels": []}
                self._ylab = ""
                func = plt.vlines

            else:
                BarcodePlot.force_vertical = True
                ax_kwargs = {"xticklabels": []}
                self._xlab = ""
                func = plt.hlines

        if rug:
            if "top" in rug:
                func(corpus_id, val + 0.9, val + 1, cols)
            if "bottom" in rug:
                func(corpus_id, val, val + 0.1, cols)
        else:
            func(corpus_id, val + self.BOTTOM, val + self.TOP, cols)

        self.legend_title = self._colorizer.legend_title(z)

        ax = kwargs.get("ax", plt.gca())
        ax.set(**ax_kwargs)

    def set_annotations(self, grid, values):
        lim = (0, self.session.Corpus.get_corpus_size())
        if BarcodePlot.horizontal and not BarcodePlot.force_vertical:
            grid.set(xlim=lim)
        else:
            grid.set(ylim=lim)
        vis.Visualizer.set_annotations(self, grid, values)

    @staticmethod
    def validate_data(data_x, data_y, data_z, df, session):
        cat, num, none = vis.Visualizer.count_parameters(
            data_x, data_y, data_z, df, session)

        if len(df) == 0:
            return False

        if len(num) > 0 or len(cat) > 1:
            return False
        return True


class HeatbarPlot(BarcodePlot):
    """
    Produce a heat bar instead of single bars.

    Assuming that 'matches' is an array containing the corpus ids of the
    tokens in the match, this code produces a heat bar:

    import numpy as np
    from matplotlib import pyplot as plt
    import statsmodels

    corpus_size = 50000
    matches = pd.np.unique(
                pd.np.concatenate(
                    (np.random.normal(1000, 250, 10).astype(int),
                     pd.np.random.normal(32500, 2000, 20).astype(int),
                     pd.np.random.uniform(0, corpus_size, 20).astype(int))))

    # KDE from statsmodels:
    from statsmodels.nonparametric.kde import KDEUnivariate
    kde = KDEUnivariate(matches.astype(float))
    kde.fit(bw="scott")

    # alternative KDE from scipy.stats:
    # from scipy.stats import gaussian_kde
    # kde = scipy.stats.gaussian_kde(matches, "silverman")

    values = kde.evaluate(range(corpus_size))
    #values =kde.density

    plt.pcolormesh([values], cmap="Blues_r")
    plt.vlines(matches, 0, 1)

    """

    name = "Heatbar plot"
    icon = "Barcode_plot"

    TOP = 0.05
    BOTTOM = 0.0
    COLOR = "Black"

    def __init__(self, *args, **kwargs):
        from statsmodels.nonparametric.kde import KDEUnivariate
        HeatbarPlot.kde = KDEUnivariate
        BarcodePlot.__init__(self, *args, **kwargs)

    def plot_facet(self, data, color, **kwargs):
        """
        Plot a HeatBar plot.

        A heatbar plot is like a barcode plot, only that there is also a
        heat map plotted under the lines.
        """

        x = kwargs.get("x", None)
        y = kwargs.get("y", None)
        levels_x = kwargs.get("levels_x", None)
        levels_y = kwargs.get("levels_y", None)

        corpus_size = self.session.Corpus.get_corpus_size()
        M = []
        if x and not y:
            self.horizontal = False
            for current_x in levels_x:
                dsub = data[data[x] == current_x]
                matches = dsub.coquery_invisible_corpus_id
                density = self.kde(matches.astype(float))
                density.fit(bw="scott")
                values = density.evaluate(range(corpus_size))[::-1]
                M.append(len(matches) * values)
            plt.imshow(pd.np.array(M).T,
                       aspect="auto", cmap="Greys",
                       extent=(0, len(levels_x), 0, corpus_size))
        elif y and not x:
            self.horizontal = True
            for current_y in levels_y:
                dsub = data[data[y] == current_y]
                matches = dsub.coquery_invisible_corpus_id
                density = self.kde(matches.astype(float))
                try:
                    density.fit(bw="scott")
                except:
                    values = pd.np.array([0] * corpus_size)
                else:
                    values = density.evaluate(range(corpus_size))
                    values = values / values.max()
                M.append(len(matches) * values)
            plt.imshow(pd.np.array(M),
                       aspect="auto", cmap="Greys",
                       extent=(0, corpus_size, 0, len(levels_y)))
        else:
            matches = data["coquery_invisible_corpus_id"]
            density = self.kde(matches.astype(float))
            density.fit(bw="scott")
            M = [density.evaluate(range(corpus_size))]
            plt.imshow(M,
                       aspect="auto", cmap="Greys",
                       extent=(0, corpus_size, 0, 1))
        super(HeatbarPlot, self).plot_facet(data, color,
                                            rug=["top", "bottom"],
                                            **kwargs)


provided_visualizations = [BarcodePlot]

if options.cfg.experimental:
    provided_visualizations.append(HeatbarPlot)
