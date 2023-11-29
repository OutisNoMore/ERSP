import matplotlib.pyplot
import numpy
import sys

"""
usage:
python3 poster.py <graph_title> <bird_to_graph> <Ground_truth> <file_1> <file_2> <file_3>...
ie python3 poster.py "Flamingo" flamingo_ground_truth flamingo_galaxy flamingo_blubold 
creates graph with title Flamingo
Files should have just a 0 or 1 for confidence per line
"""


def plot(X, Ys, labels):
    matplotlib.pyplot.figure(figsize=(4, 3))
    for confidences, title in zip(Ys, labels):
        matplotlib.pyplot.plot(X, confidences, label=title)
    matplotlib.pyplot.xlabel("Time (s)")
    matplotlib.pyplot.ylabel("Confidence")
    matplotlib.pyplot.ylim(0, 1.1)
    #matplotlib.pyplot.title(sys.argv[1])
    matplotlib.pyplot.legend(bbox_to_anchor=(0.05, 1.32), loc='upper left', ncols=2)
    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.grid(axis='y', linestyle='dashed', color='#D3D3D3')
    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.savefig(sys.argv[1])
    matplotlib.pyplot.show()


def main():
    output = []  # Array of confidences for each phone
    labels = []  # type of phone
    X = []
    smallest = float('inf') # conform to same length recording
    # Extend data for 3 second intervals
    for dataFile in sys.argv[2:]:
        tripled = []
        labels.append(dataFile)
        with open(dataFile, 'r') as confidences:
            for confidence in confidences:
                tripled.append(float(confidence))
                tripled.append(float(confidence))
                tripled.append(float(confidence))
        if len(tripled) < smallest:
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
