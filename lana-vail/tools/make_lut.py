"""Builds LANA_WarmPrint35 3D LUTs (.cube, 33^3, Rec.709/sRGB display in -> out).

Look target: warm 35mm print stock (Kodak Vision3 negative -> 2383 print feel),
in the spirit of night interiors in "Licorice Pizza" (2021): creamy warm skin,
softly lifted blacks, rolled-off highlights, olive greens, teal-leaning shadows,
subtractive density on saturated colours.
"""
import colorsys, sys
import numpy as np

N = 33

def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)

def look(rgb, strength=1.0):
    src = rgb.copy()
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    luma = 0.2126 * r + 0.7152 * g + 0.0722 * b

    # 1. Hue / saturation work in HSV
    hsv = np.stack(np.vectorize(colorsys.rgb_to_hsv)(r, g, b), -1)
    h, s, v = hsv[..., 0] * 360, hsv[..., 1], hsv[..., 2]
    # greens (75-165) -> toward olive, less saturated
    gw = smoothstep(60, 90, h) * (1 - smoothstep(150, 180, h))
    h = h - 18 * gw
    s = s * (1 - 0.35 * gw)
    # blues/cyans (180-250) -> toward teal, slightly muted
    bw = smoothstep(175, 200, h) * (1 - smoothstep(235, 260, h))
    h = h - 10 * bw
    s = s * (1 - 0.18 * bw)
    # magentas/purples muted (print stocks don't love them)
    mw = smoothstep(260, 285, h) * (1 - smoothstep(330, 350, h))
    s = s * (1 - 0.30 * mw)
    # skin (5-45 deg): protect, a touch richer and warmer
    sw = smoothstep(0, 12, h) * (1 - smoothstep(38, 55, h))
    h = h + 2.0 * sw
    s = s * (1 + 0.06 * sw)
    # global gentle desat of very saturated values (filmic compression)
    s = s - 0.12 * s * s
    h = np.mod(h, 360) / 360
    out = np.stack(np.vectorize(colorsys.hsv_to_rgb)(h, np.clip(s, 0, 1), v), -1)

    # 2. Subtractive density: saturated colours get darker, like print film
    mx, mn = out.max(-1), out.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    out = out * (1 - 0.10 * sat[..., None])

    # 3. Tone curve: soft S, lifted black, rolled highlight
    x = out
    lo, hi = 0.028, 0.95
    # filmic S around 0.42 mid
    k = 1.45
    sx = 1 / (1 + np.exp(-k * 4.2 * (x - 0.45)))
    s0 = 1 / (1 + np.exp(-k * 4.2 * (0 - 0.45)))
    s1 = 1 / (1 + np.exp(-k * 4.2 * (1 - 0.45)))
    sx = (sx - s0) / (s1 - s0)
    x = 0.30 * x + 0.70 * sx
    x = x ** 1.06  # slightly denser mids, print-like
    out = lo + (hi - lo) * x

    # 4. Split tone: cool-teal shadows, warm amber highlights
    l2 = 0.2126 * out[..., 0] + 0.7152 * out[..., 1] + 0.0722 * out[..., 2]
    shw = (1 - smoothstep(0.05, 0.45, l2))[..., None]
    hiw = smoothstep(0.45, 0.95, l2)[..., None]
    out = out + shw * np.array([-0.022, 0.004, 0.018])
    out = out + hiw * np.array([0.040, 0.014, -0.040])
    # overall warm white balance nudge (tungsten-ish print)
    out = out * np.array([1.03, 1.0, 0.93])

    out = np.clip(out, 0, 1)
    return src + strength * (out - src)

def write(path, strength, title):
    grid = np.linspace(0, 1, N)
    # .cube order: red fastest
    b, g, r = np.meshgrid(grid, grid, grid, indexing="ij")
    rgb = np.stack([r, g, b], -1).reshape(-1, 3)
    res = look(rgb, strength)
    with open(path, "w") as f:
        f.write(f'TITLE "{title}"\n')
        f.write("# Lana Vail project - warm 35mm print look. Input/Output: Rec.709 / sRGB display.\n")
        f.write(f"LUT_3D_SIZE {N}\nDOMAIN_MIN 0.0 0.0 0.0\nDOMAIN_MAX 1.0 1.0 1.0\n")
        for p in res:
            f.write(f"{p[0]:.6f} {p[1]:.6f} {p[2]:.6f}\n")

if __name__ == "__main__":
    d = sys.argv[1]
    write(f"{d}/LANA_WarmPrint35_full.cube", 1.0, "LANA WarmPrint35 full")
    write(f"{d}/LANA_WarmPrint35_60.cube", 0.6, "LANA WarmPrint35 60pct")
