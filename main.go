package main

import (
	"fmt"

	//. "github.com/Arturo0911/CloudLearning/lacto"
	"github.com/Arturo0911/CloudLearning/model"
	"github.com/sjwhitworth/golearn/base"
)

func yogurtPrediction() {
	rawData, err := base.ParseCSVToInstances("neural_model/data/data_regression_set.csv", true)
	if err != nil {
		panic(err)
	}
	fmt.Println(rawData)
}

func main() {
	//yogurtPrediction()
	//GetXYMat()
	model.LinearModel()
}
