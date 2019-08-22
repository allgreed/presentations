from collections import namedtuple

import matplotlib.pyplot as plt


Plot = namedtuple('Plot', 'name title bars')
Plot.__new__.__defaults__ = ("", "", [])
Bar = namedtuple('Bar', 'label value')


def generate_plot(plot):
    bars = plot.bars

    labels = list(map(lambda t: t.label, bars))
    values = list(map(lambda t: t.value, bars))

    with plt.xkcd():
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_color('none')
        ax.set_yticks([])
        ax.xaxis.set_ticks_position('bottom')

        x_positions = list(map(lambda x: x / 2, range(len(labels))))
        max_x_position = max(x_positions)

        ax.bar(x_positions, values, 0.25)
        # TODO: How to controll the bars colour
        
        ax.set_xticks(x_positions)
        ax.set_xticklabels(labels)

        ax.set_ylim([0, 110])
        ax.set_xlim([-0.25, max_x_position + 0.25])

        ax.set_title(plot.title)

    #plt.show()
    plt.savefig("../gen/" + plot.name)
