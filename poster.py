import matplotlib.pyplot
import numpy
import sys

"""
usage:
python3 poster.py <graph_title> <bird_to_graph> <Ground_truth> <file_1> <file_2> <file_3>...
ie python3 poster.py "Flamingo" "Greater Flamingo" flamingo_ground_truth flamingo_galaxy flamingo_blubold 
creates graph with title Flamingo
input files should be csv as output by AudioBird app
Except for ground truth file - this should have just a 0 or 1 for confidence per line
"""


def plot(X, Ys, labels):
    matplotlib.pyplot.figure(figsize=(4, 3))
    for confidences, title in zip(Ys, labels):
        matplotlib.pyplot.plot(X, confidences, label=title)
    matplotlib.pyplot.xlabel("Time (s)")
    matplotlib.pyplot.ylabel("Confidence")
    matplotlib.pyplot.ylim(0, 1.1)
    matplotlib.pyplot.title(sys.argv[1])
    matplotlib.pyplot.legend(bbox_to_anchor=(0.5, 1.0), loc='upper left')
    matplotlib.pyplot.tight_layout()
    #matplotlib.pyplot.savefig(sys.argv[1])
    matplotlib.pyplot.show()


def main():
    output = []  # Array of confidences for each phone
    labels = []  # type of phone
    smallest = float('inf') # conform to same length recording
    bird_name = sys.argv[2] # name of bird to plot
    # Extend data for 3 second intervals
    tripled = []
    X = []
    with open(sys.argv[3], 'r') as confidences:
        labels.append(sys.argv[3])
        for confidence in confidences:
            tripled.append(float(confidence))
            tripled.append(float(confidence))
            tripled.append(float(confidence))
        #if len(tripled) < smallest:
         #   smallest = len(tripled)
        output.append(tripled)
    for dataFile in sys.argv[4:]:
        tripled = []
        labels.append(dataFile)
        confidences = numpy.loadtxt(dataFile, dtype='str', delimiter=',', skiprows=1)
        #with open(dataFile, 'r') as confidences:
        confidence = 0 
        for i in range(len(confidences)):
            if bird_name in confidences[i][2]:
                # found bird 
                confidence = float(confidences[i][3])
            if i == len(confidences) - 1 or confidences[i][0] != confidences[i + 1][0]:
                # reached end of interval - plot confidence of bird
                tripled.append(float(confidence))
                tripled.append(float(confidence))
                tripled.append(float(confidence))
                confidence = 0
                if dataFile == sys.argv[-1]:
                    X.append(int(confidences[i][0]) + 0)
                    X.append(int(confidences[i][0]) + 1)
                    X.append(int(confidences[i][0]) + 2)
        if len(tripled) < smallest:
            smallest = len(tripled)
        output.append(tripled)
    # Make sure all array are same length, truncate if not
    for data in output:
        while len(data) > smallest:
            data.pop()
    while len(X) > smallest:
        X.pop()
    # Plot confidences against seconds
    #X = list(range(0, smallest))
    plot(X, output, labels)

if __name__ == "__main__":
    main()
