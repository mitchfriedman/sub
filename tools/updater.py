import subprocess


def update():
    subprocess.run(["git", "pull"])
    subprocess.run(["make", "install"])


def main():
    subprocess.run(["git", "remote", "update"])
    status = subprocess.run(["git", "status"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if "behind" in status.stdout:
        update()


if __name__ == "__main__":
    main()