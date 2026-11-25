"""Write one best-advice sentence to the grader's output directory."""

import os


ADVICE = (
    "After I yelled at my son, Dad gave me the best advice I've had: "
    "say sorry without making him comfort you; "
    "he's sixteen now and still tells me when he's scared."
)


def main():
    text = ADVICE + "\n"
    if not ADVICE.strip() or len(text) > 200:
        raise SystemExit("Entry must contain 1-200 characters including its newline.")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as entry:
        entry.write(text)


if __name__ == "__main__":
    main()
