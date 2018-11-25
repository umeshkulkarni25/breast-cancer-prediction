import numpy as np

class KNN:
	def __init__(self, k):
		#KNN state here
		#Feel free to add methods
		self.k = k

	def distance(self, featureA, featureB):
		diffs = (featureA - featureB)**2
		return np.sqrt(diffs.sum())

	def train(self, X, y):
		#training logic here
		#input is an array of features and labels
		self.samples = np.array(X)
		self.labels = np.array(y)
		None

	def predict(self, X):
		#Run model here
		#Return array of predictions where there is one prediction for each set of features
		prediction = np.array([])
		for x in X:
			distanceVector = self.getDistaceVector(x)
			kNearestNeighbours = self.getKNearestNeighbours(distanceVector)
			classification = self.classifyByMajorityVoting(kNearestNeighbours)
			prediction = np.append(prediction,[classification])
		return prediction

	def getDistaceVector(self,x):
		distances = np.array([self.distance(x, sample) for sample in self.samples])
		return zip(distances, self.labels)

	def getKNearestNeighbours(self, disatanceVector):
		disatanceVector = sorted(disatanceVector, key=lambda x: x[0])
		return disatanceVector[:self.k]

	def classifyByMajorityVoting(self, kNearestNeighbours):
		votingResults = {}
		for neighbour in kNearestNeighbours:
			label = neighbour[1]
			if label in votingResults:
				votingResults[label] += 1
			else:
				votingResults[label] = 1
		return max(votingResults, key=votingResults.get)
class ID3:
	def __init__(self, nbins, data_range):
		#Decision tree state here
		#Feel free to add methods
		self.bin_size = nbins
		self.range = data_range

	def preprocess(self, data):
		#Our dataset only has continuous data
		norm_data = (data - self.range[0]) / (self.range[1] - self.range[0])
		categorical_data = np.floor(self.bin_size*norm_data).astype(int)
		return categorical_data

	def train(self, X, y):
		#training logic here
		#input is array of features and labels
		categorical_data = self.preprocess(X)

	def predict(self, X):
		#Run model here
		#Return array of predictions where there is one prediction for each set of features
		categorical_data = self.preprocess(X)
		return None

class Perceptron:
	def __init__(self, w, b, lr):
		#Perceptron state here, input initial weight matrix
		#Feel free to add methods
		self.lr = lr
		self.w = w
		self.b = b

	def train(self, X, y, steps):
		#training logic here
		#input is array of features and labels
		correctlyClassified = 0;
		iterationCount = 0;
		while iterationCount < steps:
			trainingSample = X[iterationCount%len(X)]
			desiredOutput = y[iterationCount%len(y)]
			weightedSum = np.dot(trainingSample, self.w) + self.b
			perceptronOutput = 0 if weightedSum < 0 else 1
			if perceptronOutput != desiredOutput:
				self.w = self.w + self.lr * desiredOutput * trainingSample
				self.b = self.b + self.lr * desiredOutput
			iterationCount += 1
		None

	def predict(self, X):
		#Run model here
		#Return array of predictions where there is one prediction for each set of features
		predictions = []
		for testSample in X:
			predictions.append(0 if np.dot(testSample, self.w) + self.b < 0 else 1)
		return np.array(predictions)

class MLP:
	def __init__(self, w1, b1, w2, b2, lr):
		self.l1 = FCLayer(w1, b1, lr)
		self.a1 = Sigmoid()
		self.l2 = FCLayer(w2, b2, lr)
		self.a2 = Sigmoid()

	def MSE(self, prediction, target):
		return np.square(target - prediction).sum()

	def MSEGrad(self, prediction, target):
		return - 2.0 * (target - prediction)

	def shuffle(self, X, y):
		idxs = np.arange(y.size)
		np.random.shuffle(idxs)
		return X[idxs], y[idxs]

	def train(self, X, y, steps):
		for s in range(steps):
			i = s % y.size
			if(i == 0):
				X, y = self.shuffle(X,y)
			xi = np.expand_dims(X[i], axis=0)
			yi = np.expand_dims(y[i], axis=0)

			pred = self.l1.forward(xi)
			pred = self.a1.forward(pred)
			pred = self.l2.forward(pred)
			pred = self.a2.forward(pred)
			loss = self.MSE(pred, yi) 
			#print(loss)

			grad = self.MSEGrad(pred, yi)
			grad = self.a2.backward(grad)
			grad = self.l2.backward(grad)
			grad = self.a1.backward(grad)
			grad = self.l1.backward(grad)

	def predict(self, X):
		pred = self.l1.forward(X)
		pred = self.a1.forward(pred)
		pred = self.l2.forward(pred)
		pred = self.a2.forward(pred)
		pred = np.round(pred)
		return np.ravel(pred)

class FCLayer:

	def __init__(self, w, b, lr):
		self.lr = lr
		self.w = w	#Each column represents all the weights going into an output node
		self.b = b

	def forward(self, input):
		#Write forward pass here

	def backward(self, gradients):
		#Write backward pass herem

class Sigmoid:

	def __init__(self):
		None

	def forward(self, input):
		#Write forward pass here
		return self.activation

	def backward(self, gradients):
		#Write backward pass here