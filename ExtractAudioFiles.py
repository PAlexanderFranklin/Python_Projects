from pathlib import Path
from shutil import rmtree

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
                    if file.name[-3:] == "WAV":
                        count += 1
                        if count > 1:
                            newName = project.name + "_" + str(count) + ".wav"
                        else:
                            newName = project.name + ".wav"
                        with (destination / newName).open(mode="xb") as fid:
                            fid.write(file.read_bytes())
            except:
                print(project.name + " failed to copy")
            else:
                if count > 0:
                    rmtree(project)
