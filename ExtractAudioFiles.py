from pathlib import Path
from shutil import rmtree, move

# Configure source and destination
source = Path.cwd() / "audioSource"
destination = Path.cwd() / "destination"
# source should have equivalent structure to ZOOM_R8/projects

print("source: ", source)
print("destination: ", destination)

for project in source.iterdir():
    if project.name != "PRJ000":
        print(project)
        if (project / "AUDIO").exists():
            count = 0
            try:
                for file in (project / "AUDIO").iterdir():
                    if file.name[-3:].upper() == "WAV":
                        count += 1
                        if count > 1:
                            newName = project.name + "_" + str(count) + ".wav"
                        else:
                            newName = project.name + ".wav"
                        newPath = destination / newName
                        move(file, newPath)
            except:
                print(project.name + " failed to copy")
            else:
                if count > 0:
                    rmtree(project)
