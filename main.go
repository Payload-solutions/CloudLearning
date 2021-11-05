package main

import (
	"fmt"

	"github.com/sjwhitworth/golearn/base"
)

//"github.com/sjwhitworth/golearn/base"

// func getXYMat() { //(*mat.Dense, *mat.Dense) {
// 	file, err := os.Open("neural_model/data/data_regression_set.csv")
// 	if err != nil {
// 		//return nil, nil
// 		return
// 	}
// 	defer file.Close()
// 	df := dataframe.ReadCSV(file)
// 	yData := df.Col("quality_product")
// 	fmt.Println(yData)
// }

func yogurtPrediction() {
	rawData, err := base.ParseCSVToInstances("neural_model/data/data_regression_set.csv", true)
	if err != nil {
		panic(err)
	}
	fmt.Println(rawData)
}

func main() {
	yogurtPrediction()
}
