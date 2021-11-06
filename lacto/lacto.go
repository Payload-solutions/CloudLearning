package lacto

import (
	"fmt"
	"os"

	"github.com/kniren/gota/dataframe"
	"gonum.org/v1/gonum/mat"
)

func GetXYMat() (*mat.Dense, *mat.Dense) {
	file, err := os.Open("neural_model/data/data_regression_set.csv")
	if err != nil {
		return nil, nil
	}
	defer file.Close()
	df := dataframe.ReadCSV(file)
	yData := df.Col("lactobacillus_initial_strain_cfu_ml")
	xData := df.Drop([]string{"streptococcus_initial_strain_cfu_ml",
		"lactobacillus_initial_strain_cfu_ml", "quality_product", "lactobacillus_final_cfu_ml", "streptococcus_final_cfu_ml"})
	//fmt.Println(yData)
	fmt.Println(xData)
}
