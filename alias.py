"""upscaling for aliasing"""

from scipy.io.wavfile import read, write
import numpy as np

def main(inputFilename, outputFilename):
    rate, data = read(inputFilename)
    newdata = np.array([], dtype=np.int16)
    print('starting')
    i = 0
    for p in data:
        newdata = np.append(newdata, [p, p, p, p])
        if i % rate == 0:
           print(',', end='', flush=True) 
        i += 1
    print('!')
    write(outputFilename, rate*4, newdata)

if __name__ == "__main__":
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", dest="inputfile",
                        help="input WAV", metavar="FILE")
    parser.add_argument("-o", "--output", dest="outputfile",
                        default="aliased.wav", help="output WAV",
                        metavar="FILE")
    args = parser.parse_args()
    main(args.inputfile, args.outputfile)
