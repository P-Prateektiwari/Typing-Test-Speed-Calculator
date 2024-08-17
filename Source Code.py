import time

def typing_test():
    # Sample text for the typing test
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text as fast as you can:")
    print(text)
    input("Press Enter to start...")

    start_time = time.time()  # Record the start time
    typed_text = input("Start typing here: ")
    end_time = time.time()  # Record the end time

    # Calculate the time taken
    time_taken = end_time - start_time

    # Calculate the number of words typed
    word_count = len(typed_text.split())

    # Calculate words per minute (WPM)
    wpm = (word_count / time_taken) * 60

    # Calculate accuracy
    correct_chars = sum(1 for typed, original in zip(typed_text, text) if typed == original)
    accuracy = (correct_chars / len(text)) * 100

    print("\nResults:")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Words Typed: {word_count}")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test()
