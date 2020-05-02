from pathlib import Path
from shutil import rmtree

# Configure source and destination
source = Path.cwd() / 'audioSource'
destination = Path.cwd() / 'destination'
# source should have equivalent structure to ZOOM_R8/projects

print('source: ', source)
print('destination: ', destination)

for project in source.iterdir():
    print(project)
    if (project / 'AUDIO').exists():
        count = 0
        try:
            for file in (project / 'AUDIO').iterdir():
                count += 1
                if file.name[-3:] == 'WAV':
                    if count > 1:
                        newName = project.name + '_' + str(count) + '.WAV'
                    else:
                        newName = project.name + '.WAV'
                    with (destination / newName).open(mode='xb') as fid:
                        fid.write(file.read_bytes())
        except:
            print(project.name + ' failed to copy')
        else:
            rmtree(project)
