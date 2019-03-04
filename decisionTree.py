# import libraries
import sys, csv, math, copy

# Node class for the tree
class Node:
    # Create a new node with the attribute to split on or hold the prediction, left node , right node
    def __init__(self,attribute,left,right,isNode = False):
        self.attribute = attribute
        self.left = left
        self.right = right
        self.isNode = isNode

def doLog(val):
    #Return 0 if the input is 0
    if val > 0:
        return math.log(val,2)
    else:
        return 0

def splitOnAttribute(data,attribute,expected):
    matchedDataset, unmatchedDataset = [], []
    for row in data:
        if checkCondition(row,attributes.index(attribute),expected):
            matchedDataset.append(row)
        else:
            unmatchedDataset.append(row)
    # print("For " + attribute + " = " + expected +":\n")
    # print(matchedDataset)
    # print(unmatchedDataset)
    return matchedDataset, unmatchedDataset

def checkCondition(row,attribute,expected):
    return (row[attribute] == expected)

def majorityVote1(dataset):
    votes = {}
    # Get the count of all classes
    for line in dataset:
        if line[-1] not in votes:
            votes[line[-1]] = 1
        else:
            votes[line[-1]] += 1
    return str(votes)
def majorityVote(dataset):
    votes = {}
    # Get the count of all classes
    for line in dataset:
        if line[-1] not in votes:
            votes[line[-1]] = 1
        else:
            votes[line[-1]] += 1
    ans = ""
    largest = -1
    # Find the class with the maximum votes
    for val in votes.keys():
        if(votes[val] > largest):
            ans = val
            largest = votes[val]
    return ans

def entropy():
    global entropyVal
    #Calculate entropy
    for val in classes.values():
        entropyVal += (val/totalEntries) * math.log(val/totalEntries,2)
    entropyVal = -entropyVal
    
def error():
    global errorVal
    errorVal = min(classes.values())/totalEntries

def conditionalProbability(matchedDataset,unmatchedDataset):
    #Calculate conditional probability
    total = len(matchedDataset) + len(unmatchedDataset)
    matchCount = 0
    unmatchCount = 0
    for line in matchedDataset:
        if line[-1] == hy:
            matchCount += 1
    for line in unmatchedDataset:
        if line[-1] == hy:
            unmatchCount += 1
    matchProb = matchCount/len(matchedDataset)
    revMatchProb = (len(matchedDataset) - matchCount)/len(matchedDataset)
    unmatchProb = unmatchCount/len(unmatchedDataset)
    revUnmatchProb = (len(unmatchedDataset) - unmatchCount)/len(unmatchedDataset)
    condProb = - (
                    ((matchProb * doLog(matchProb))
                    + (revMatchProb * doLog(revMatchProb))) * len(matchedDataset)/total
                    + ((revUnmatchProb * doLog(revUnmatchProb))
                    + (unmatchProb * doLog(unmatchProb))) * len(unmatchedDataset)/total
                )
    # print(condProb)
    return condProb

def findBestAttribute(dataset,remAttributes):
    bestCondProb = 1
    bestAttribute = None
    #find the best attribute from the current list
    for val in remAttributes:
        possibleValue = attributeValues[val][0]
        matchedDataset, unmatchedDataset = splitOnAttribute(dataset,val,possibleValue)
        #print("Cond Prob for" + val + " = " + possibleValue)
        # Return None as this would be a leaf node
        if(len(matchedDataset) == 0 or len(unmatchedDataset) == 0):
            continue
        condProb = conditionalProbability(matchedDataset,unmatchedDataset)
        #print(condProb)
        # Store the best attribute and expected value
        if condProb < bestCondProb:
            bestCondProb = condProb
            bestAttribute = val
    # print("bestAttribute : " + str(bestAttribute) + str(bestCondProb))
    return bestAttribute

def createDecisionTree(dataset,remAttributes,depth):
    if(max_depth == 0 or max_depth <= depth):
        b = majorityVote1(dataset)
        print(b)
        return Node(majorityVote(dataset),None,None,True)
    # iterate through all attributes and find the best attribute to split on every advancement in depth
    # limit it by max depth and handle the 0 stump case
    bestAttribute = findBestAttribute(dataset,remAttributes)
    # If we can't classify anymore or reached maxdepth
    if bestAttribute is None:
        b = majorityVote1(dataset)
        print(b)
        # Make a leaf node
        return Node(majorityVote(dataset),None,None,True)
    else:
        depth += 1
        remAttributes.remove(bestAttribute)
        # Split the data on the nest attribute and expected value
        leftNodeData, rightNodeData = splitOnAttribute(dataset,bestAttribute,attributeValues[bestAttribute][0])
        print(" |" + str(bestAttribute) + " = " + attributeValues[bestAttribute][0] + " " + majorityVote1(dataset))
        # Generate the tree on the left side
        leftNode = createDecisionTree(leftNodeData,copy.deepcopy(remAttributes),depth)
        # Generate the tree on the right side
        rightNode = createDecisionTree(rightNodeData,copy.deepcopy(remAttributes),depth)
        # Return the current node
        return Node(bestAttribute, leftNode, rightNode)

def inspect(input):
    global attributes
    global hy
    global totalEntries
    global csvData
    global attributeValues
    global dataset
    # Open and read the input file
    inputFile = open(input, "r")
    csvData = csv.reader(inputFile)
    line_count = 0
    # Iterate through the csv file
    for line in csvData:
        if line_count != 0:
            dataset.append(line)
            if line[-1] not in classes:
                classes[line[-1]] = 1
            else:
                classes[line[-1]] += 1
            # Store a list of possible values for each attribute
            for att in attributes:
                if line[attributes.index(att)] not in attributeValues[att]:
                    attributeValues[att].append(line[attributes.index(att)])
        else:
            # Store attributes
            attributes = (line[0:-1])
            # Generate a list of possible values for each attribute
            for att in attributes:
                attributeValues[att] =  []
        line_count += 1
    inputFile.close()
    # Compute entropy and error values
    totalEntries = sum(classes.values())
    largest = -1
    for val in classes.keys():
        if(classes[val] > largest):
            hy = val
            largest = classes[val]

def printTree(root,spaces = 0):
    print("| " * spaces + str(root.attribute))
    if(root.left != None and root.right != None):
        printTree(root.left,spaces + 1)
        printTree(root.right,spaces + 1)
        if(root.isNode):
            print(spaces + str(root.attribute))

def predict(dataset,tree):
    if(tree.right == None and tree.left == None):
        return tree.attribute
    elif(dataset[attributes.index(tree.attribute)] == attributeValues[tree.attribute][0]):
        return predict(dataset,tree.left)
    else:
        return predict(dataset,tree.right)

def performPredictions(dataset,tree):
    for line in dataset:
        print(str(predict(line,tree)))

def predictTestData(test_input,test_out,tree):
    correct = 0
    total = 0
    # Open and read the test file
    testFile = open(test_input, "r")
    next(testFile)
    csvTestData = csv.reader(testFile)
    # Open label file to write
    predictionFile = open(test_out, "w")
    for line in csvTestData:
        # Perform prediction
        prediction = predict(line,tree)
        # Calculate error rate
        if(prediction != line[-1]):
            correct +=1
        predictionFile.write(prediction+"\n")
        total+=1
    testFile.close()
    predictionFile.close()
    return correct/total

def writeErrors(trainError,testError):
    metricFile = open(metrics_out,"w")
    metricFile.write("error(train): " + str(trainError) + "\nerror(test): " + str(testError))
    metricFile.close()

# Main flow
# Input variables
train_input = sys.argv[1]
test_input = sys.argv[2]
max_depth = int(sys.argv[3])
train_out = sys.argv[4]
test_out = sys.argv[5]
metrics_out = sys.argv[6]

# Global variables
classes = {} # The classes available for classification
attributes = [] # Attributes on which decisions can be made
attributeValues = {} # List of values an attribute can have
remainingAttributes = [] # List of attributes left for finding the next best attribute to split on
entropyVal = 0 # Entropy of the dataset
totalEntries = 0 # Total number of entries in the dataset
hy = "" #H(Y) = Party
dataset = [] #csvData
depth = 0 # Depth of the decision tree

# Load all the data
inspect(train_input)
remainingAttributes = list(attributes)

# Calculate the entropy
entropy()
# Calculate the error
error()

tree = createDecisionTree(dataset,list(remainingAttributes),0)
printTree(tree)
trainError = predictTestData(train_input,train_out,tree)
testError = predictTestData(test_input,test_out,tree)
writeErrors(trainError, testError)