import sys
import train
import transfer_timbre
import constants

if __name__ == "__main__":
    try:
        startup_param = str(sys.argv[1])
        if startup_param == "--train":
            try:
                audio_folder_name = str(sys.argv[2])
                train.train(audio_folder_name)
            except IndexError:
                print("train expects exactly one argument   <audio_folder_path>\n"
                      + "   recieved 0")
        elif startup_param == "--transfer":
            try:
                source_audio_file_name = str(sys.argv[2])
                target_path = str(sys.argv[3])
                label = str(sys.argv[4])
                transfer_timbre.transfer_timbre(source_audio_file_name, target_path, label)
            except IndexError:
                print(
                    "--transfer expects exactly three arguments \n" + 
                    " <source_audio_file_name> <target_file_name> <label>")
        elif startup_param == "--trasnfer_all":
            try:
                label = str(sys.argv[2])
                directory = constants.AUDIO_INPUT
                if (3 < len(sys.argv)):
                    directory = directory
                transfer_timbre.transfer_all(label, directory)
            except IndexError:
                print(
                    "--transfer_all expects at least one argument \n" + 
                    " <label> <direcotry>\n" + 
                    "label - label to be prepended to output file names\n" +
                    "direcotry (optional) - directory to transfer files from defaults to ./assets/audioIn")

    except:
        print("script expects at least one parameter: \n"
              + "--train <audio_folder_path>:\n"
              + "     to train solo insturment on audio at given location\n "
              + "--transfer <source_audio_file_name> <target_file_name>\n"
              + "     to transfer timbre from /assets/audioIn/<source_audio_file_name>"
              + "     to assets/audioOut/<target_file_name>")
