#exec(open(r"scripts\text_over_via_check.py").read())
import pcbnew
def bbox(item):
    return item.GetBoundingBox()

board = pcbnew.GetBoard()
vias = [
    item for item in board.GetTracks()
    if isinstance(item, pcbnew.VIA)
]

silk_text = [
    d for d in board.GetDrawings()
    if isinstance(d, pcbnew.TEXTE_PCB)
    and d.GetLayer() in (pcbnew.F_SilkS, pcbnew.B_SilkS)
]
overlaps = []

for via in vias:
    via_box = bbox(via)
    for txt in silk_text:
        if via_box.Intersects(bbox(txt)):
            overlaps.append((via, txt))


for via, txt in overlaps:
    pos = via.GetPosition()
    print("Silkscreen overlaps via at",
          pcbnew.ToMM(pos.x), pcbnew.ToMM(pos.y),
          "Text:", txt.GetText())

if not overlaps:
    print("Success! There are no overlaps, i.e. text over vias")
