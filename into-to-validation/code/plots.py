from plt_gen import Plot, Bar, generate_plot

plots = [
    Plot(name="thisor", title="A", bars=[
        Bar(label="other stages", value=25),
        Bar(label="production", value=75),
    ]),
    Plot(name="thator", title="B", bars=[
        Bar(label="other stages", value=75),
        Bar(label="production", value=25),
    ]),
    Plot(name="crap", bars=[
        Bar(label="other stages", value=0),
        Bar(label="production", value=100),
    ]),
    Plot(name="hehfix", title="", bars=[
        Bar(label="stage 1 .. n-1", value=0),
        Bar(label="stage n", value=100),
        Bar(label="production", value=0),
    ]),
    Plot(name="realhehfix", title="", bars=[
        Bar(label="stage 1 .. n-1", value=0),
        Bar(label="stage n", value=80),
        Bar(label="production", value=20),
    ]),
    Plot(name="desired", title="", bars=[
        Bar(label="stage 0", value=80),
        Bar(label="stage 1 .. n-1", value=0),
        Bar(label="stage n", value=0),
        Bar(label="production", value=20),
    ]),
    Plot(name="real", title="", bars=[
        Bar(label="0", value=5),
        Bar(label="1", value=10),
        Bar(label="2 .. n-2", value=60),
        Bar(label="n-1", value=10),
        Bar(label="n", value=5),
        Bar(label="production", value=20),
    ]),
]

some_sdlc_stages = [
    ("stage#0", 0),
    ("stage#1", 0),
    ("stage#...", 0),
    ("production", 0),
]

for plot in plots:
    generate_plot(plot)
