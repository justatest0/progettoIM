import argparse
import time

#This function interpret some values as boolean True or False
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

#This is the way the object parser is created
parser = argparse.ArgumentParser()

#These are the mandatory arguments (watch out, no dash!)
#parser.add_argument('nameOfMandatoryArgument', help='this is the help related to the mandatory argument', type=int)

#This are the optional arguments (watch out, dashes here!)
parser.add_argument('-p', '--protocol', help="Select the protocol to use", type=str, choices=['UDP', 'udp', 'TCP', 'tcp'], default='TCP', dest='protocol')
parser.add_argument('-o', '--outputVideo', help="Select the name of the file you want to create. This will be create in a subdirectory", nargs='?', const='E64E093307615569593609618F2FBBC53A28A59452D156F8D8827B465289B18C', dest='outputVideo')



#Mutual exclusive input, path for video or webcam index
groupVideoInput = parser.add_mutually_exclusive_group()
groupVideoInput.add_argument('-w', '--webcamInputIndex', help="Select the index of the webcam to use", type=int, dest='webcamInputIndex')
groupVideoInput.add_argument('-v', '--videoInputPath', help="Select the path of the file to analyze", type=str, dest='videoInputPath')




#This variable encapsulate all the information gathered from parser
args = parser.parse_args()

#Store the argument passed in a variable
protocol = args.protocol.upper()
webcamInputIndex = args.webcamInputIndex
videoInputPath = args.videoInputPath
outputVideo = args.outputVideo
