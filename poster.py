import matplotlib.pyplot
import sys

"""
usage:
python3 poster.py <graph_title> <file_1> <file_2> <file_3>...
ie python3 poster.py Flamingo flamingo_galaxy flamingo_blubold flamingo_ground_truth
creates graph with title flamingo
each input file should only have 1 confidence per line.
"""

def plot(X, Ys, labels):
    for confidences, title in zip(Ys, labels):
        matplotlib.pyplot.plot(X, confidences, label=title)
    matplotlib.pyplot.ylim(0, 1.1)
    matplotlib.pyplot.title(sys.argv[1])
    matplotlib.pyplot.legend(bbox_to_anchor=(1.01, 1.0), loc='upper left')
    matplotlib.pyplot.show()

def main():
    output = []  # Array of confidences for each phone
    labels = []  # type of phone
    smallest = float('inf') # conform to same length recording
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
        if (len(tripled) < smallest):
            smallest = len(tripled)
        output.append(tripled)
    # Make sure all array are same length, truncate if not
    for data in output:
        while len(data) > smallest:
            data.pop()
    # Plot confidences against seconds
    X = list(range(0, smallest))
    plot(X, output, labels)

if __name__ == "__main__":
    main()
