import numpy

with open("demo-result.csv", 'a') as demo:
    confidences = numpy.loadtxt("aligned-goaway-audiomoth1-result.csv", dtype='str', delimiter=',', skiprows=1)
    for confidence in confidences:
        confidence[0] = str(int(confidence[0]) + 30)
        confidence[1] = str(int(confidence[1]) + 30)
        demo.write(confidence[0] + "," + confidence[1] + "," + confidence[2] + "," + confidence[3] + "\n")

