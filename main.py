import os

LINE_1 = "Don't take the last bus home on the night of June 14, 2019 \u2014 stay at the hospital until your father wakes up."
LINE_2 = "That was the last night he was awake enough to tell you he was proud of you, and every decision you made after that was an attempt to live up to those words."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE_1 + "\n")
        f.write(LINE_2 + "\n")


if __name__ == "__main__":
    main()
