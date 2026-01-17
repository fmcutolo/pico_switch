#exec(open("scripts\create_component_list.py").read())
#import pcbnew
import csv
import os

# Get the current board

path = "scratch"

if not os.path.isdir(path):
    print("creating the directory: %s" %path)
    os.makedirs(path)
    
csv_file_location = path + "\component_list.csv"




board = pcbnew.GetBoard()
csv_file_location =  "scratch\component_list.csv"

# Set the output CSV file path
board_file = board.GetFileName()
print("board_file=%s" %board_file)

if board_file:
    folder = os.path.dirname(board_file)
    print("folder=%s" % folder)
    csv_file_path = os.path.join(folder, "scratch\component_list.csv")

    # Open CSV file for writing
    with open(csv_file_path, mode='wb') as csv_file_path:  # 'wb' for Python 2
        writer = csv.writer(csv_file_path)
        
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
