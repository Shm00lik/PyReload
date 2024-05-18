import os
import time
import subprocess
import sys

SCRIPT_NAME = "python"


class PyReload:
    def __init__(self, interval: float = 1) -> None:
        self.interval = interval
        self.last_time_modified = time.time()

        if not (len(sys.argv) >= 2):
            raise ValueError("You must provide file to run")

        self.filename, self.args = sys.argv[1], sys.argv[2:]
        self.current_subprocess: subprocess.Popen | None = None

        if self.is_valid_input():
            self.loop()
        else:
            raise FileNotFoundError(self.filename)

    def is_valid_input(self) -> bool:
        return os.path.isfile(self.filename)

    def get_modified_time(self) -> float:
        return os.stat(self.filename).st_mtime

    def modified(self) -> bool:
        return self.get_modified_time() != self.last_time_modified

    def run_script(self) -> subprocess.Popen:
        args = [SCRIPT_NAME, self.filename] + self.args
        return subprocess.Popen(args)

    def stop_current_subprocess(self) -> bool:
        if self.current_subprocess != None:
            self.current_subprocess.kill()
            return True

        return False

    def loop(self):
        while True:
            time.sleep(self.interval)

            if self.modified():
                self.last_time_modified = self.get_modified_time()
                self.stop_current_subprocess()
                self.current_subprocess = self.run_script()


if __name__ == "__main__":
    pyreload = PyReload()
