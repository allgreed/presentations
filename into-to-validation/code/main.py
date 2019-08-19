import matplotlib.pyplot as plt


bars = [
    ("a", 30),
    ("b", 50),
    ("dupa", 70),
    ("fuj", 100),
]

some_stages = [
    ("stage#0", 0),
    ("stage#1", 0),
    ("stage#...", 0),
    ("stage#n", 0),
]

some_sdlc_stages = [
    ("stage#0", 0),
    ("stage#1", 0),
    ("stage#...", 0),
    ("production", 0),
]

thisor = [
    ("other stages", 25),
    ("production", 75),
]

thator = [
    ("other stages", 75),
    ("production", 25),
]

def plot_bars(bars):
    names = list(map(lambda t: t[0], bars))
    values = list(map(lambda t: t[1], bars))

    with plt.xkcd():
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_color('none')
        ax.set_yticks([])
        ax.xaxis.set_ticks_position('bottom')

        x_positions = list(map(lambda x: x / 2, range(len(names))))
        max_x_position = max(x_positions)

        ax.bar(x_positions, values, 0.25)
        # TODO: How to controll the bars colour
        
        ax.set_xticks(x_positions)
        ax.set_xticklabels(names)

        ax.set_ylim([0, 110])
        ax.set_xlim([-0.25, max_x_position + 0.25])

        ax.set_title("CLAIMS OF SUPERNATURAL POWERS")

    plt.show()

#plot_bars(just_stages)
plot_bars(thisor)
#plot_bars(thator)
