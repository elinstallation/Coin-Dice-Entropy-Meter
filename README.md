# Shannon Entropy Simulator

An interactive dashboard for visualizing Shannon entropy across biased coins and loaded dice, built with Python and Matplotlib.

## Demo

https://github.com/user-attachments/assets/0f79264e-4dca-48b2-bcbf-b384c7e2098c


## What is Shannon Entropy?

Shannon entropy measures **uncertainty** in a probability distribution. The formula is:

```
H = -∑ p(x) · log₂(p(x))
```

The result is measured in **bits**. The higher the entropy, the more spread out and uncertain the distribution is.

- A **fair coin** (p = 0.5) has maximum entropy of **1.0 bit** — you have no idea what's coming
- A **biased coin** (p = 0.9) has lower entropy — heads is very likely, less surprise
- A **fair die** has maximum entropy of **~2.585 bits**
- A **loaded die** (one face dominates) has lower entropy

## Features

- **Coin curve** — plots H(p) from p=0 to p=1, with a live dot that tracks your slider
- **Die bar chart** — shows the probability of each face, updating as you drag the sliders
- **Live entropy readouts** — coin and die entropy update in real time
- **7 interactive sliders** — one for the coin probability, six for each die face
- Die sliders are automatically normalized so they always sum to 1

## Files

| File | Purpose |
|------|---------|
| `main.py` | All the math — entropy, normalization, coin/die helpers |
| `interface.py` | The interactive Matplotlib dashboard |

## Setup

**Install dependencies:**
```bash
pip install matplotlib
```

**Run:**
```bash
python interface.py
```

## How to Use

- Drag the **Coin Prob** slider to bias the coin — watch the dot move along the entropy curve
- Drag any **Die Face** slider to load the die — the bars and entropy readout update instantly
- The dashed line on the die chart marks the uniform (max entropy) reference

## Window Size

If the dashboard is too large for your screen, edit these two lines at the top of `interface.py`:

```python
fig = plt.figure(figsize=(8, 7), facecolor="#111111")  # width, height in inches
plt.rcParams["figure.dpi"] = 80                        # lower = smaller window
```

## Project Structure

```
.
├── main.py        # math module
├── interface.py   # dashboard
└── README.md
```
