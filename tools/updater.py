import subprocess
import os


def update():
    subprocess.run(["git", "pull"], cwd=os.environ["_OAK_ROOT"])
    subprocess.run(["make", "install"], cwd=os.environ["_OAK_ROOT"])


def main():
    subprocess.run(["git", "remote", "update"], cwd=os.environ["_OAK_ROOT"])
    status = subprocess.run(
        ["git", "status"],
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.environ["_OAK_ROOT"],
    )
    if "behind" in status.stdout:
        update()


if __name__ == "__main__":
    main()
