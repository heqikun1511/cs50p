import emoji
def main():
    emo=input("Input:").strip()
    out=emoji.emojize(emo,language='alias')
    print(f"Output{out}")


main()
