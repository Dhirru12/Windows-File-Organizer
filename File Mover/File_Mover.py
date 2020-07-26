import os
import shutil
import pathlib

print('Proccess may take awhile, please stand by...')

############################################################
#Place full destination of folder/destination you'd like sorted
#Paste it in between the quotes in the exact format of the example below
sourcepath='Your path here'
#Example: "C:\\Users\\coolguy\\Downloads\\"
############################################################
sourcefiles = os.listdir(sourcepath)
destinationpath = sourcepath

for file in sourcefiles:
    try:
        if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.gif') or file.endswith('.jpg')or file.endswith('.webp')or file.endswith('.jfif')or file.endswith('.JPG'):
            pathlib.Path(destinationpath +'Pictures').mkdir(parents=True, exist_ok=True) 
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Pictures',file))

        elif file.endswith('.mp4')or file.endswith('.avi')or file.endswith('.mov'):
            pathlib.Path(destinationpath +'Videos').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Videos',file))

        elif file.endswith('.ai') or file.endswith('.psd') or file.endswith('.aep'):
            pathlib.Path(destinationpath +'Adobe Projects').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Adobe Projects',file))

        elif file.endswith('.zip') or file.endswith('.rar')or file.endswith('.7z'):
            pathlib.Path(destinationpath +'Zip Files').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Zip Files',file))

        elif file.endswith('.exe'):
            pathlib.Path(destinationpath +'Executables').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Executables',file))

        elif file.endswith('.xlsx'):
            pathlib.Path(destinationpath +'Excel Files').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Excel Files',file))

        elif file.endswith('.pptx')or file.endswith('.PPTM'):
            pathlib.Path(destinationpath +'Powerpoint').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Powerpoint',file))

        elif file.endswith('.docx'):
            pathlib.Path(destinationpath +'Microsoft Word').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Microsoft Word',file))

        elif file.endswith('.txt'):
            pathlib.Path(destinationpath +'Text Files').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Text Files',file))

        elif file.endswith('.pdf')or file.endswith('.PDF'):  
            pathlib.Path(destinationpath +'PDFs').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'PDFs',file))

        elif file.endswith('.ipa'):
            pathlib.Path(destinationpath +'IPAs').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'IPAs',file))

        elif file.endswith('.mp3'):
            pathlib.Path(destinationpath +'MP3 Files').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'MP3 Files',file))

        elif os.path.isdir(sourcepath + file):
            if not file=='Folders'and not file=="Other" and not file=='Pictures'and not file=='Videos'and not file=='Adobe Projects'and not file=='MP3 FIles'and not file=='IPAs'and not file=='PDFs'and not file=='Text Files'and not file=='Microsoft Word'and not file=='Powerpoint'and not file=='Excel Files'and not file=='Executables':
                pathlib.Path(destinationpath +'Folders').mkdir(parents=True, exist_ok=True)
                shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Folders',file))
            else:
                print("No need to move " + file+ " folder, ignore moved message")
        else:
            pathlib.Path(destinationpath +'Other').mkdir(parents=True, exist_ok=True)
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath +'Other',file))

        print(file + " moved")
    except:
        print(file+" movement failed")

