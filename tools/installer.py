import os
import subprocess


def find_go_modules():
    go_code_path = os.path.join(os.path.dirname(os.path.abspath(os.path.basename(__file__))), "src", "go")
    return [root for root, _, files in os.walk(go_code_path) if "go.mod" in files]


def install_module(mod_path):
    subprocess.run(["make", "install"], cwd=mod_path)


def main():
    for mod_path in find_go_modules():
        install_module(mod_path)


if __name__ == "__main__":
    main()