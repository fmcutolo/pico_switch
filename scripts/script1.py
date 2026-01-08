#exec(open("scripts\script1.py").read())
import pcbnew
import csv
import os

# Get the current board
board = pcbnew.GetBoard()

# Set the output CSV file path
board_file = board.GetFileName()
if board_file:
    folder = os.path.dirname(board_file)
else:
    folder = os.getcwd()
csv_file_path = os.path.join(folder, "component_list.csv")

# Open CSV file for writing
with open(csv_file_path, mode='wb') as csv_file:  # 'wb' for Python 2
    writer = csv.writer(csv_file)
    
    # Write header
    writer.writerow(["Reference", "Value", "Footprint", "Position X (mm)", "Position Y (mm)"])
    
    # Iterate all footprints (modules)
    for module in board.GetModules():
        ref = module.GetReference()
        value = module.GetValue()
        footprint = module.GetFPID().GetLibItemName()
        pos = module.GetPosition()
        pos_mm = (pcbnew.ToMM(pos.x), pcbnew.ToMM(pos.y))
        
        # Write row using format()
        writer.writerow([ref, value, footprint, "%.2f" % pos_mm[0], "%.2f" % pos_mm[1]])

print("Component list exported to:\n%s" % csv_file_path)
