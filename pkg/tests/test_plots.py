
import numpy
import pandas
import matplotlib.pyplot
import wvu.util


# from:
# https://github.com/WinVector/wvu/blob/main/examples/example_graphs.ipynb
def test_graphs(monkeypatch):
    # https://stackoverflow.com/a/60127271/6901725
    monkeypatch.setattr(matplotlib.pyplot, 'show', lambda: None)

    d = pandas.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [False, False, True, True, False]
    })

    wvu.util.plot_roc(
        prediction=d['x'],
        istrue=d['y'],
        extra_points=pandas.DataFrame({
            'tpr': [0, 1],
            'fpr': [0, 1],
            'label': ['AAA', 'BBB']
        })
    )

    d = pandas.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [False, False, True, True, False]
    })

    wvu.util.dual_density_plot(
        probs=d['x'],
        istrue=d['y'],
    )

    d = pandas.DataFrame({
        'x': [.1, .2, .3, .4, .5],
        'y': [False, False, True, True, False]
    })

    wvu.util.dual_hist_plot(
        probs=d['x'],
        istrue=d['y'],
    )

    d = pandas.DataFrame({
        'x': [.1, .2, .3, .4, .5],
        'y': [0, 0, 1, 1, 0]
    })

    wvu.util.gain_curve_plot(
        prediction=d['x'],
        outcome=d['y'],
    )

    # %%

    d = pandas.DataFrame({
        'x': [.1, .2, .3, .4, .5],
        'y': [0, 0, 1, 1, 0]
    })

    wvu.util.lift_curve_plot(
        prediction=d['x'],
        outcome=d['y'],
    )

    # %%

    d = pandas.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [False, False, True, True, False]
    })

    wvu.util.threshold_plot(
        d,
        pred_var='x',
        truth_var='y',
        plotvars=("sensitivity", "specificity"),
    )

    d = pandas.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [False, False, True, True, False]
    })

    wvu.util.threshold_plot(
        d,
        pred_var='x',
        truth_var='y',
        plotvars=("precision", "recall", "accuracy"),
    )

    # %%

    d = pandas.DataFrame({
        'x': [.1, .2, .3, .4, .5],
        'y': [False, False, True, True, False]
    })
    d['x0'] = 1 - d['x']
    pmat = numpy.asarray(d.loc[:, ['x0', 'x']])

    wvu.util.dual_density_plot_proba1(
        probs=pmat,
        istrue=d['y'],
    )

    d = pandas.DataFrame({
        'x': [.1, .2, .3, .4, .5],
        'y': [False, False, True, True, False]
    })
    d['x0'] = 1 - d['x']
    pmat = numpy.asarray(d.loc[:, ['x0', 'x']])

    wvu.util.dual_hist_plot_proba1(
        probs=pmat,
        istrue=d['y'],
    )
