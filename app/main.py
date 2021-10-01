import sys
import train
import transfer_timbre

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
                transfer_timbre.transfer_timbre(source_audio_file_name, target_path)
            except IndexError:
                print(
                    "--transfer expects exactly two arguments \n" + 
                    " <source_audio_file_name> <target_path>")

    except:
        print("script expects at least one parameter: \n"
              + "--train <audio_folder_path>:\n"
              + "     to train solo insturment on audio at given location\n "
              + "--transfer <source_audio_file_name> <target_path>\n"
              + "     to transfer timbre from /assets/audioIn/<source_audio_file_name>"
              + "     to <target_path>")
