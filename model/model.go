package model

import (
	"fmt"
	"log"

	"github.com/sjwhitworth/golearn/base"
	"github.com/sjwhitworth/golearn/evaluation"
	"github.com/sjwhitworth/golearn/knn"
)

func LinearModel() {
	fmt.Println("Loading our csv data")
	rawData, err := base.ParseCSVToInstances("neural_model/data/milk-properties.csv", true)
	if err != nil {
		log.Fatal("Something went wrong at the moment of read the file")
	}
	//fmt.Println(rawData)

	cls := knn.NewKnnClassifier("euclidean", "linear", 2)

	trainData, testData := base.InstancesTrainTestSplit(rawData, 0.5)
	cls.Fit(trainData)

	fmt.Println("Calculate the euclidian distance and return the most popular label")
	predictions, err := cls.Predict(testData)
	if err != nil {
		log.Fatal("Error in the predictions step")
	}

	fmt.Println(predictions)

	confusionMat, err := evaluation.GetConfusionMatrix(testData, predictions)
	if err != nil {
		panic(fmt.Sprintf("Unable to get confusion matrix: %s", err.Error()))
	}
	fmt.Println(evaluation.GetSummary(confusionMat))

}
