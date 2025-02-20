
# configurator.py

def configure_tone():
    """
    Configure the tone of STARNEX AI, adjusting its personality and behavior.
    """
    print("Configuring AI tone...")
    tone_choice = input("Choose AI tone (1) Formal (2) Casual: ")
    if tone_choice == "1":
        set_formal_tone()
    elif tone_choice == "2":
        set_casual_tone()
    else:
        print("Invalid choice, defaulting to formal.")

def set_formal_tone():
    """
    Sets a formal tone for AI responses.
    """
    print("AI set to formal tone. Expect precise and professional responses.")

def set_casual_tone():
    """
    Sets a casual tone for AI responses.
    """
    print("AI set to casual tone. Expect friendly and relaxed responses.")

if __name__ == "__main__":
    configure_tone()
