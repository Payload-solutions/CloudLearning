package main

import (
	"fmt"
	"os"

	"github.com/kniren/gota/dataframe"
)

func getXYMat() { //(*mat.Dense, *mat.Dense) {
	file, err := os.Open("neural_model/data/data_regression_set.csv")
	if err != nil {
		//return nil, nil
		return
	}
	defer file.Close()
	df := dataframe.ReadCSV(file)
	yData := df.Col("quality_product")
	fmt.Println(yData)

}

func main() {
	getXYMat()
}
