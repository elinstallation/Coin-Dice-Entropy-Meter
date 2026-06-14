import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import * 

from main import coin_curve, coin_entropy, normalise, die_entropy, max_entropy

coin_init = 0.5
die_init = [1/6] * 6
coin_max = max_entropy(2)
die_max = max_entropy(6)

p_vals, h_vals = coin_curve(num_points=300)

fig = plt.figure(figsize=(7, 7), facecolor="#111111")
fig.suptitle("Entropy Dashboard", color="white", fontsize=16, y=0.98)
plt.rcParams["figure.dpi"] = 70

gs = gridspec.GridSpec(
    nrows=4, ncols=1,
    height_ratios=[3, 3, 0.6, 2],
    hspace=0.5,
    top=0.93, bottom=0.03, left=0.1, right=0.95,
)
 
ax_coin = fig.add_subplot(gs[0])
ax_die  = fig.add_subplot(gs[1])
ax_info = fig.add_subplot(gs[2])
 
gs_sliders = gridspec.GridSpecFromSubplotSpec(
    nrows=7, ncols=3,
    subplot_spec=gs[3],
    hspace=0.3,
    width_ratios=[2, 6, 1],
)
DARK   = "#111111"
MID    = "#1e1e1e"
BLUE   = "#4a90d9"
WHITE  = "#dddddd"
GREY   = "#555555"
GREEN  = "#4caf50"
 
def style_ax(ax, xlabel, ylabel):
    ax.set_facecolor(MID)
    ax.tick_params(colors=GREY, labelsize=9)
    ax.set_xlabel(xlabel, color=GREY, fontsize=9)
    ax.set_ylabel(ylabel, color=GREY, fontsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor(GREY)
        spine.set_linewidth(0.5)
    ax.grid(color="#2a2a2a", linewidth=0.5)
 
def make_slider_ax(row):
    label_ax  = fig.add_subplot(gs_sliders[row, 0])
    slider_ax = fig.add_subplot(gs_sliders[row, 1])
    value_ax  = fig.add_subplot(gs_sliders[row, 2])
    for a in [label_ax, value_ax]:
        a.axis("off")
    slider_ax.set_facecolor(DARK)
    return label_ax, slider_ax, value_ax

style_ax(ax_coin, "Probability (p) →", "Entropy (bits) ↑")
ax_coin.set_xlim(0, 1)
ax_coin.set_ylim(0, 1.2)
 
ax_coin.plot(p_vals, h_vals, color=GREY, linewidth=2)
ax_coin.axhline(y=1.0, color=GREEN, linewidth=0.8, linestyle="--")
ax_coin.text(0.98, 1.02, "Max = 1 bit", color=GREEN,
             fontsize=8, ha="right", transform=ax_coin.get_xaxis_transform())
 
coin_dot,  = ax_coin.plot([coin_init], [coin_entropy(coin_init)],
                           "o", color="white", markersize=10, zorder=5)
coin_label = ax_coin.text(coin_init, coin_entropy(coin_init) + 0.06,
                           f"H={coin_entropy(coin_init):.2f}",
                           color="white", fontsize=10, ha="center")
 

style_ax(ax_die, "Die Face →", "Probability ↑")
ax_die.set_ylim(0, 1.05)
ax_die.set_xticks(range(6))
ax_die.set_xticklabels(["1","2","3","4","5","6"], color=GREY)
 
probs_init = normalise(die_init)
bars = ax_die.bar(range(6), probs_init, color=BLUE, width=0.5)
 
ax_die.axhline(y=1/6, color=GREY, linewidth=0.8, linestyle="--")
ax_die.text(5.4, 1/6 + 0.02, "Uniform (Max Entropy)",
            color=GREY, fontsize=8, ha="right")
 
ax_info.axis("off")
ax_info.set_facecolor(DARK)
 
coin_info_text = ax_info.text(
    0.25, 0.5,
    f"Coin Entropy\n{coin_entropy(coin_init):.3f} bits",
    color="white", fontsize=12, ha="center", va="center",
    transform=ax_info.transAxes,
)
die_info_text = ax_info.text(
    0.75, 0.5,
    f"Die Entropy\n{die_entropy(die_init):.3f} bits",
    color="white", fontsize=12, ha="center", va="center",
    transform=ax_info.transAxes,
)
 
slider_style = dict(color="#4a90d9", track_color="#2a2a2a")
 
lax, sax, vax = make_slider_ax(0)
lax.text(0.9, 0.5, "Coin Prob (p)", color=WHITE, fontsize=9,
         ha="right", va="center", transform=lax.transAxes)
sl_coin = Slider(sax, "", 0.0, 1.0, valinit=coin_init, **slider_style)
val_coin = vax.text(0.1, 0.5, f"{coin_init:.2f}", color=WHITE,
                    fontsize=9, va="center", transform=vax.transAxes)
 
sl_die  = []
val_die = []
for i in range(6):
    lax, sax, vax = make_slider_ax(i + 1)
    lax.text(0.9, 0.5, f"Die Face {i+1}", color=WHITE, fontsize=9,
             ha="right", va="center", transform=lax.transAxes)
    sl = Slider(sax, "", 0.01, 1.0, valinit=1/6, **slider_style)
    vt = vax.text(0.1, 0.5, f"{probs_init[i]:.2f}", color=WHITE,
                  fontsize=9, va="center", transform=vax.transAxes)
    sl_die.append(sl)
    val_die.append(vt)
 
def update_coin(val):
    p = sl_coin.val
    h = coin_entropy(p)
 
    coin_dot.set_data([p], [h])
    coin_label.set_position((p, h + 0.06))
    coin_label.set_text(f"H={h:.2f}")
 
    val_coin.set_text(f"{p:.2f}")
    coin_info_text.set_text(f"Coin Entropy\n{h:.3f} bits")
    fig.canvas.draw_idle()
 
 
def update_die(val):
    weights = [sl.val for sl in sl_die]
    probs   = normalise(weights)
    h       = die_entropy(weights)
 
    for bar, prob in zip(bars, probs):
        bar.set_height(prob)
 
    for vt, prob in zip(val_die, probs):
        vt.set_text(f"{prob:.2f}")
 
    die_info_text.set_text(f"Die Entropy\n{h:.3f} bits")
    fig.canvas.draw_idle()
 
 
sl_coin.on_changed(update_coin)
for sl in sl_die:
    sl.on_changed(update_die)

plt.show()