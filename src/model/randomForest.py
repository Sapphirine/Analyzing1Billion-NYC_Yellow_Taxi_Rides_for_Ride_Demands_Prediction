# This script is sythesized from the following resources 
# 1) Apache official documents on Ensembles example https://spark.apache.org/docs/latest/mllib-ensembles.html#regression
# 2) Apache official documents on the class "pyspark.mllib.tree.RandomForestModel" 
# https://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#pyspark.mllib.tree.RandomForestModel
# 3) Github repo on Random Forest regressoin https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/random_forest_regression_example.py
# 4) how to tune parameters http://stats.stackexchange.com/questions/53240/practical-questions-on-tuning-random-forests

from __future__ import print_function

from pyspark import SparkContext

from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

from pyspark.ml import Pipeline
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import RegressionEvaluator

from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils

import math



cat_var_dic = {}
cat_var_dic[0] = 18
#cat_var_dic[1] = 24
cat_var_dic[2] = 2
cat_var_dic[3] = 3
#cat_var_dic[4] = 10


def train_model(filename='final_tip_all.txt', test_portion=0.2, cat_var=cat_var_dic, n_tree=250, mode_feature_strat='auto', max_deep=5, max_bin=32):
	# Train a RandomForest model.
	#  Empty categoricalFeaturesInfo indicates all features are continuous.
	#  Note: Use larger numTrees in practice.
	#  Setting featureSubsetStrategy="auto" lets the algorithm choose

	sc = SparkContext()


	sqlContext = SQLContext(sc)




	spark = SparkSession.builder.appName("RandomForestRegressor").getOrCreate()


	# Load and parse the data file into an RDD of LabeledPoint.
	data = MLUtils.loadLibSVMFile(sc, filename)


	# Split the data into training and test sets (30% held out for testing)
	(trainingData, testData) = data.randomSplit([1-test_portion, test_portion])
	

	##### TREAT TEMP AS CONTINUOUS #### 
	model = RandomForest.trainRegressor(trainingData, categoricalFeaturesInfo=cat_var,
	                                    numTrees=n_tree, featureSubsetStrategy=mode_feature_strat,
	                                    impurity='variance', maxDepth=max_deep, maxBins=max_bin)

	


	

	############ prediction !!!! #### 
	# Evaluate model on test instances and compute test error
	predictions = model.predict(testData.map(lambda x: x.features))
	labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
	testMSE = labelsAndPredictions.map(lambda (v, p): (v - p) * (v - p)).sum() / float(testData.count())
	testRMSE = math.sqrt(testMSE)


	#predictions.takeSample(withReplacement = False, num = 5)
	# convert the rdd object to dataframe as follows
	df_predictions = predictions.map(lambda x: (x, )).toDF()
	df_predictions.cache()
	#df_predictions.show(5, False)
	

	#print('Learned regression forest model:')
	#print(model.toDebugString())
	print('Test Root Mean Squared Error on ' + filename + ' = ' + str(testRMSE))



	# Save and load model
	#model.save(sc, "./savedModel")
	#sameModel = RandomForestModel.load(sc, "./savedModel")


	#Select example prediction rows to display.
	# This predictions is an RDD object 
	# predictions.cache()
	# convert the rdd object to dataframe as follows
	#df_predictions = predictions.map(lambda x: (x, )).toDF()
	#df_predictions.cache()
	#df_predictions.show(5, False)
















if __name__ == "__main__":

	
	# # pass parameters 
	# filename = 'final_count_2015-12.txt'
	# test_portion = 0.2
	# cat_var = {}
	# cat_var[0] = 18
	# #cat_var[1] = 24
	# cat_var[2] = 2
	# cat_var[3] = 3
	# #cat_var[4] = 10
	# n_tree = 250
	# max_deep = 5
	# ################



	train_model()

	









