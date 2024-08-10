import os
tiles_dir_name = input("Tiles directory name?: ")

for file in os.listdir(tiles_dir_name):
    if file[-4:] == ".bin":
        os.remove(fr"{tiles_dir_name}/{file}")
    elif file[-4:] == ".xml":
        new_file = ""
        xml_file = open(fr"{tiles_dir_name}/{file}", 'r').read()
        try:
            for area in xml_file.split("<edit_areas>")[1].split("</edit_areas>")[0].split("</edit_area>"):

                try:
                    if "edit" in area.split('id=')[1].split(' ')[0]:
                        before_area = area + "</edit_area>"
                        before_area = before_area[1:]
                        before_size = area.split("<size ")[1].split("/>")[0]
                        before_grid_size = before_area.split('grid_size="')[1].split('"')[0]
                        new_area = area.replace(before_size, 'x="255" y="255" z="255"') + "</edit_area>"
                        new_area = new_area.replace(f'grid_size="{before_grid_size}"', 'grid_size="0"')
                        new_area = new_area[1:]

                        xml_file = xml_file.replace(before_area, new_area)
                except IndexError:
                    pass
            xml_file = open(fr"{tiles_dir_name}/{file}", 'w').write(xml_file)
        except IndexError:
            os.remove(fr"{tiles_dir_name}/{file}")

        """ 
            with open(fr"{tiles_dir_name}/{file}", 'w') as f:
                print(new_file)
                f.write(new_file)
            """
