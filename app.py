

# STEP 1: PRESS TO PLAY


while True:
    from mic2 import recording_flag
    if recording_flag:
        print("Recording is ongoing")
    else:
        print("Recording is not ongoing")