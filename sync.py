import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitAutoSync(FileSystemEventHandler):
    def on_modified(self, event):
        if '.git' not in event.src_path:
            self.sync()

    def on_created(self, event):
        if '.git' not in event.src_path:
            self.sync()

    def on_deleted(self, event):
        if '.git' not in event.src_path:
            self.sync()

    def sync(self):
        print("🔄 Alteração detectada! Sincronizando...")
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'auto-sync: alteração detectada'])
        subprocess.run(['git', 'push', 'origin', 'main'])
        print("✅ Sincronizado com GitHub!")

path = "."
observer = Observer()
observer.schedule(GitAutoSync(), path, recursive=True)
observer.start()
print("👀 Monitorando alterações em data-science-portfolio...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()