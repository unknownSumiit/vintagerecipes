"""The Vintage Recipe Box logo kit. Text is converted to outlines so it looks the same everywhere.
Fonts: Lora (OFL), Inter (OFL)."""
import os, re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
TEAL, CHERRY, CREAM, INK, BUTTER = "#2e6e6a", "#b3322e", "#fffaf0", "#2a2522", "#f6dfa3"

lora = instantiateVariableFont(TTFont("/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"), {"wght": 700})
inter = TTFont("/usr/share/fonts/opentype/inter/Inter-Bold.otf")


class Font:
    def __init__(self, tt):
        self.gs, self.cmap, self.hmtx, self.upm = tt.getGlyphSet(), tt.getBestCmap(), tt["hmtx"], tt["head"].unitsPerEm

    def text(self, s, x, y, size, tracking=0.0):
        sc, pen, cx = size / self.upm, SVGPathPen(self.gs), x
        for ch in s:
            name = self.cmap[ord(ch)]
            self.gs[name].draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
            cx += self.hmtx[name][0] * sc + tracking * size
        return pen.getCommands(), cx - x - tracking * size


LORA, INTER = Font(lora), Font(inter)


def mark(card=CREAM, edge=TEAL, line=CHERRY, faint=TEAL, heart=CHERRY):
    """A recipe card with a heart pinned to its corner."""
    return f'''
  <rect x="9" y="24" width="78" height="60" rx="7" fill="{card}" stroke="{edge}" stroke-width="6"/>
  <path d="M19 42 H77" stroke="{line}" stroke-width="3" stroke-linecap="round"/>
  <path d="M19 55 H66 M19 67 H58" stroke="{faint}" stroke-width="3" stroke-linecap="round" opacity=".45"/>
  <path d="M76 36 C62 27 60 18 65 13.5 C69.5 9.8 74 11.5 76 15.3 C78 11.5 82.5 9.8 87 13.5 C92 18 90 27 76 36 Z" fill="{heart}" stroke="{card}" stroke-width="3" stroke-linejoin="round"/>'''


def lockup(word=INK, small=TEAL, card=CREAM, edge=TEAL):
    top_d, top_w = INTER.text("THE VINTAGE", 124, 40, 17, tracking=0.32)
    main_d, main_w = LORA.text("Recipe Box", 122, 82, 50)
    W = int(122 + max(top_w, main_w) + 8)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" width="{W * 3}" height="300">'
            f'<g transform="translate(4 2)">{mark(card=card, edge=edge)}</g>'
            f'<path d="{top_d}" fill="{small}"/><path d="{main_d}" fill="{word}"/></svg>'), W


def icon(bg=CREAM, rx=22):
    back = f'<rect width="100" height="100" rx="{rx}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">{back}<g transform="translate(1 3) scale(.98)">{mark()}</g></svg>'


logo, W = lockup()
open(os.path.join(OUT, "vintage-recipe-box-logo.svg"), "w").write(logo)
open(os.path.join(OUT, "vintage-recipe-box-logo-white.svg"), "w").write(lockup(word="#ffffff", small=BUTTER, card=CREAM, edge="#8fcfc6")[0])
open(os.path.join(OUT, "vintage-recipe-box-icon.svg"), "w").write(icon())
open(os.path.join(OUT, "vintage-recipe-box-icon-square.svg"), "w").write(icon(rx=0))
print("width", W)
