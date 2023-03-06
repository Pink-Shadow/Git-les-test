# Opdracht: Verzin een unieke banner text en pas dit aan!

def print_banner(text):
    ''' This function is used to display banner text in the console'''
    print(f"-{'-'*15}{'-'*len(text)}{'-'*15}-")
    print(f"-{' '*15}{text}{' '*15}-")
    print(f"-{'-'*15}{'-'*len(text)}{'-'*15}-")


if __name__ == "__main__":
    print_banner("<voer hier uw banner text in>")

