import re #regular expression module for text pattern matching


class SpellChecker:

    def __init__(self):
        """
        Initialize the SCOWL .
        """
        # Load SCOWL word list into a Python set for fast lookup
        with open("en_US-large.txt", "r") as f:
            self.word_set = set(word.strip().lower() for word in f)


    def tokenize_text(self, text):
        """Split text into words"""
        words = re.findall(r"[a-zA-Z']+", text) # Uses regex to split text into words
        return [word.lower() for word in words]

    def check_text(self, text):
        """
        Check a text for spelling errors.
        """
        words = self.tokenize_text(text)
        misspellings = []

        for word in words:
            if word not in self.word_set:
                misspellings.append(word)

        return misspellings

    def highlight_errors(self, text):
        """
        Return the original text with misspelled words highlighted.
        """
        words = self.tokenize_text(text)
        misspellings = self.check_text(text)

        highlighted = []

        for word in words:
            if word in misspellings:
                highlighted.append("**" + word + "**")
            else:
                highlighted.append(word)

        return ' '.join(highlighted)




# Example usage
if __name__ == "__main__":
    checker = SpellChecker()

    """Main application loop"""
    print("\nSpell Checker Application")
    print("Type 'exit' to quit the program\n")
    
    while True:
        text = input("Enter text to check: ")
        
        if text.lower() == 'exit':
            print("\nGoodbye!")
            break
            
        if not text:
            print("Please enter some text.\n")
            continue
            
        errors = checker.check_text(text)
        
        if not errors:
            print("\n✓ No spelling errors found!\n")
        else:
            print("\nMisspelled words found:")
            for word in errors:
                print(f"- {word}")

            print("\nText with errors highlighted:")
            print(checker.highlight_errors(text)) 
            print()  # Add extra space for better readability
