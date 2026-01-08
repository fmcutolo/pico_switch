#exec(open("change_drill_holes_on_a_footprint.py").read())
import pcbnew

footprint = pcbnew.GetCurrentFootprint()  # currently open in Footprint Editor
new_drill_mm = 1.0

for pad in footprint.Pads():
    pad.SetDrill(nm=new_drill_mm*1e6)

print("Updated all pads drill size to", new_drill_mm, "mm")
