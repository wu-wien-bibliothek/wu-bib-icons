import os
# import cairosvg
import re
import subprocess
import yaml

inkscape = 'inkscape'
output_primo = '../../png/180x210_primo/'
output_leganto = '../../png/180x210_leganto/'
input_file = ''

with open("../../resources/material_types.yml", 'r') as stream:
    material_types = yaml.safe_load(stream)

cmd_list = ["inkscape",  "--help"]
cmd_list_primo = [ inkscape, #'-z', 
             '--export-png', output_primo,
             '--export-width', 180,
             # '--export-height', 210,
             input_file ]

cmd_list_leganto = [ inkscape, '-z', 
             '--export-png', output_leganto,
             '--export-width', 180,
             '--export-height', 210,
             '--export-background', 'ffffffff',
             input_file ]

for file in os.listdir('.'):
    if file.endswith(".svg") == False:
        continue

    name = file.split('.svg')[0]

    if name in material_types:
        for system in material_types[name]:
            for output_file in material_types[name][system]:
                args = [ 
                        inkscape, 
                        '-z', 
                        '--export-width', '180', 
                        file]
                if system == 'primo':
                    args.extend([
                        '--export-filename', output_primo + output_file])
                elif system == 'leganto':
                    args.extend([
                        '--export-filename', output_leganto + output_file,
                        '--export-background', 'ffffffff'])
                else:
                    continue

                p = subprocess.Popen( 
                        args,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE )

# Below, < out > and < err > are strings or < None >, derived from stdout and stderr.
                out, err = p.communicate()      # Waits for process to terminate

# Maybe do something with stdout output that is in < out >
# Maybe do something with stderr output that is in < err >

                if p.returncode:
                    raise Exception( 'Inkscape error: ' + (err or '?')  )

        # cairosvg.svg2png(url=name+'.svg',write_to='icon_'+name+'.png',parent_width=180,dpi=96) 
