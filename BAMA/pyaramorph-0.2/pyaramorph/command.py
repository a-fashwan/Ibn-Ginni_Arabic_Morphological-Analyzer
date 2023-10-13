# command.py
# Command line interface to pyaramorph

#import readline
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pyaramorph

def main():
    """ Read user input, analyze, output results. """
    analyzer = pyaramorph.Analyzer()
    print("Unicode Arabic Morphological Analyzer (press ctrl-d to exit)")
    while True:
        try:
            s = "الولد يحب مدرسته"
            results = analyzer.analyze_text(s)
        except EOFError:
            print("Goodbye!")
            break

        for analyses in results:
            for solution in analyses:
                print(solution)

        break
if __name__ == '__main__':
    main()

