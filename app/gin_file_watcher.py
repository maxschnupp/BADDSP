from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import constants
import time
import threading 
import bucketAPI

def on_created(event):
    filename = event.src_path.split("/")[-1]
    print("hey this file {} was created".format(filename))
    try: 
        bucketAPI.upload_to_gin_bucket(filename, constants.TAG)
    except:
        print("error uploading file")


    


def run_watchdog_observer():
    print("\n\nobserver started\n\n")

    my_event_handler = PatternMatchingEventHandler(
        patterns = ["*.gin", "ckpt"], 
        ignore_patterns = None, 
        ignore_directories = False, 
        case_sensitive = True
    )

    my_event_handler.on_created = on_created

    path = constants.SAVE_DIR

    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=True)
    my_observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

def get_watchdog_thread() -> threading.Thread:
    watchdog_thread = threading.Thread(target = run_watchdog_observer, args=())
    watchdog_thread.daemon = True
    return watchdog_thread
