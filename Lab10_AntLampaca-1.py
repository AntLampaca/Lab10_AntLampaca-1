"""
Program Name: Lab10_AntLampaca-1.py
Author: Antoni Labsz
Purpose: Program Analyzes the word frequencies of a given text and Sorts them alphabetically.
Starter Code: None
Date: March 29, 2026
"""

from pathlib import Path
import string

class WordAnalyzer:
    """
    This class analyzes a text file and counts word frequencies.

    Attributes:
        _path (Path): Path to the file being analyzed
        _frequencies (dict): Stores word frequency counts
        _stop_words (set): Words to ignore durning analysis.
    """
    def __init__(self, filepath, stop_words=None):
        """
        Initializes the Word Analyzer with a file path and optional stop words

        Args:
            filepath (str or Path): Path to the text file
            stop_words (iterable, optional): Words to exclude from counting
        """
        self._path = Path(filepath)
        self._frequencies = {}
        self._stop_words = set(stop_words) if stop_words else set()

    def process_file(self):
        try:
            """
            Reads the file, processes text, and counts word frequencies.

            Returns:
                True if processing succeeds, False if file is not found.
            """
            if not self._path.exists():
                raise FileNotFoundError
            
            #Creates translation table to remove punctuation
            translator = str.maketrans('', '', string.punctuation)
            with self._path.open('r', encoding='utf-8') as file:
                for line in file:
                    #Normalizes text
                    line = line.lower().translate(translator)
                    words = line.split()

                    for word in words:
                        #skip stop words if provided
                        if word in self._stop_words:
                            continue
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1

            return True
        except FileNotFoundError:
            print(f"Error: File '{self._path}' not found.")
            return False
        
    def print_report(self):
        """
        Prints the word frequency report in alphabetical order.
        """
        for word in sorted(self._frequencies.keys()):
            print(f"{word:<10} :: {self._frequencies[word]}")
        
def main():
    """
    Runs the menu interface for selecting and analyzing text files.
    """

    #Base directory
    base_dir = Path("texts")

    #file menu directionary
    files = {
        "1": ("Monte Cristo", base_dir / "monte_cristo.txt"),
        "2": ("Princess Mars", base_dir / "princess_mars.txt"),
        "3": ("Tarzan", base_dir / "tarzan.txt"),
        "4": ("Treasure Island", base_dir / "treasure_island.txt"),
        "5": ("Exit", None),
    }

    #Optional stop words
    stop_words = {"The", "and", "a", "of", "to", "in", "it"}

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze: ")

        for key, (name, _) in files.items():
            print(f"{key}. {name}")
            
        choice = input ("\nEnter your choice (1-5): ").strip()

        if choice not in files:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")
            continue

        if choice == "5":
            print("\nGoodbye!")
            break

        file_name, file_path = files[choice]

        print(f"\nProcessing '{file_path.name}'...\n")

        analyzer = WordAnalyzer(file_path, stop_words)
        success = analyzer.process_file()

        if success:
            analyzer.print_report()

        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()