#exec(open("scripts\drill_hole_sizes.py").read())
import pcbnew
name = raw_input("Enter your name: ")
print("Hello", name)


board = pcbnew.GetBoard()

def nm_to_mm(nm):
    return nm / 1e6

print("Drill Sizes on PCB (Interior holes):")
print("%-15s %10s" % ("Pad/Via", "Drill (mm)"))
print("-" * 28)

# Pads: iterate over all footprints
for module in board.GetModules():
    ref = module.GetReference()  # e.g., U2, R5, J1
    for pad in module.Pads():
        drill_size_vec = pad.GetDrillSize()  # returns (x, y) in nm
        if drill_size_vec[0] > 0 and drill_size_vec[1] > 0:
            drill_size = min(drill_size_vec)  # use smaller dimension for non-circular holes
            print("%-15s %10.3f" % (ref + "-" + pad.GetName(), nm_to_mm(drill_size)))

# Vias: iterate over all tracks and find vias
for track in board.GetTracks():
    if isinstance(track, pcbnew.VIA):
        drill_size = track.GetWidth()
        if drill_size > 0:
            print("%-15s %10.3f" % ("Via", nm_to_mm(drill_size)))
