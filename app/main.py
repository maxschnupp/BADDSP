import sys
import train

if __name__ == "__main__":
    try:
        startup_param = str(sys.argv[1])
        if startup_param == "--train":
            try:
                audio_folder_path = str(sys.argv[2])
                train.train(audio_folder_path)
            except IndexError:
                print("train expects exactly one argument   <audio_folder_path>\n"
                      + "   recieved 0")
    except:
        print("script expects at least one parameter: \n"
              + "--train <audio_folder_path>:\n"
              + "     to train solo insturment on audio at given location ")
