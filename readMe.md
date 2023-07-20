# Attendance system

## Adding faces
    - run the ['encode_faces.py'] program
    - pass in the parameters: --datasets for the folder containing the images to be added, 
      each named with the title/unique name for that person in the image.
      and --encodings for the file path of the pickle file generated for the encodings
    - each time this is run, it replaces the pickle file with another one. 
      so, when adding a new person's face, the face should be added to folder with the other earlier faces.
    
## Recognise faces and check them in for attendance
    - run the interface.py file.
    - the code runs in continuos loop, each time checking for a fage, 
      recognising it and attempting to check it in if not already checked in.
    - the attendance will be a txt file containing two items in each line, a name and a timestamp 
    - the program assumes the encoding file in ./encodings/encordings.pickle
      and the attendance file is generated at ./attendance/attendance.txt.
