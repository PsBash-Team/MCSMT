# code from https://www.geeksforgeeks.org/create-a-watchdog-in-python-to-look-for-filesystem-changes/

# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class OnMyWatch:
    # Set the directory on watch
    watchDirectory = "."
    def __init__(self):
        self.observer = Observer()
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        print("WatchDog FileSystemEventHandler found a event. regenerating client.json.")
        os.system('python server.py')

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()