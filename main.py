import os

import shutil

do = os.listdir(r"c:\Users\moiz3\Downloads")

for a in do:

    if a.endswith(".jpg") or a.endswith(".png"):

        shutil.move(

            os.path.join(r"C:\Users\moiz3\Downloads", a),

            r"C:\Users\moiz3\OneDrive\Pictures"

        )

    elif a.endswith(".mp3"):

        shutil.move(

            os.path.join(r"C:\Users\moiz3\Downloads", a),

            r"c:\Users\moiz3\Music"

        )

    elif a.endswith(".mp4"):

        shutil.move(

            os.path.join(r"C:\Users\moiz3\Downloads", a),

            r"c:\Users\moiz3\Videos"

        )