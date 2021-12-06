package main

import (
	"fmt"
	"log"
	"os"

	//. "github.com/Arturo0911/CloudLearning/api"
	"github.com/kniren/gota/dataframe"
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
	//model.LinearModel()
	//Serve()
	file, err := os.Open("neural_model/data/data_regression_set.csv")
	if err != nil {
		log.Fatalf("Error by %s", err)
	}
	defer file.Close()

	dataset := dataframe.ReadCSV(file)
	// reader := csv.NewReader(file)
	// dataReader, err := reader.ReadAll()
	// if err != nil {
	// 	log.Fatalf("Error by %s", err)
	// }

	// for i, data := range dataReader {
	// 	if i == 0 {
	// 		continue
	// 	}
	// 	fmt.Println(data)
	// 	break
	// }

	//fmt.Println(dataset)
	for id, data := range dataset.Records() {

		if id == 0 {
			continue
		}
		fmt.Println(data)
		break
	}
}
