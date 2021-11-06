package lacto

import (
	"fmt"
	"os"

	"github.com/kniren/gota/dataframe"
	"github.com/kniren/gota/series"
	"gonum.org/v1/gonum/mat"
)

func GetXYMat() (*mat.Dense, *mat.Dense) {
	file, err := os.Open("neural_model/data/data_regression_set.csv")
	if err != nil {
		return nil, nil
	}
	defer file.Close()
	df := dataframe.ReadCSV(file)
	yData := df.Col("quality_product")
	xData := df.Drop([]string{"quality_product", "lactobacillus_final_cfu_ml", "streptococcus_final_cfu_ml"})
	//fmt.Println(yData)
	fmt.Println(xData)

	toValue := func(s series.Series) series.Series {
		records := s.Records()
		floats := make([]float64, len(records))

		for i, r := range records {
			switch r {
			case "Low fat yogurt":
				floats[i] = 1
			case "Regular yogurt":
				floats[i] = 2
			case "Non fat yogurt":
				floats[i] = 3
			}
		}
	}
}
