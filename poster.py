import matplotlib.pyplot
import sys

"""
usage:
python3 poster.py <output_file_name> <file_1> <file_2> <file_3>...
ie python3 poster.py flamingo flamingo_galaxy flamingo_blubold flamingo_ground_truth
creates flamingo.png with plot
each csv file should only have 1 confidence per line.
"""

def plot(X, Ys, labels):
    for confidences, title in zip(Ys, labels):
        matplotlib.pyplot.plot(X, confidences, label=title)
    matplotlib.pyplot.legend()
    matplotlib.pyplot.savefig(sys.argv[1])
    matplotlib.pyplot.show()

def main():
    output = []  # Array of confidences for each phone
    labels = []  # type of phone
    greatest = 0 # if not the same length
    # Extend data for 3 second intervals
    for dataFile in sys.argv:
        if dataFile == sys.argv[0] or dataFile == sys.argv[1]:
            continue
        tripled = []
        labels.append(dataFile)
        with open(dataFile, 'r') as confidences:
            for confidence in confidences:
                tripled.append(float(confidence))
                tripled.append(float(confidence))
                tripled.append(float(confidence))
        if len(tripled) > greatest:
            greatest = len(tripled)
        output.append(tripled)
    # Make sure all array are same length
    for data in output:
        while len(data) != greatest:
            data.append(0.0)
    # Plot confidences against seconds
    X = list(range(0, greatest))
    plot(X, output, labels)

if __name__ == "__main__":
    main()
