package api

import (
	"fmt"
	"log"
	"net/http"
	"os"

	//. "github.com/Arturo0911/CloudLearning/api"
	"github.com/gin-gonic/gin"
)

type RegressionControllers struct {
	StreptococcusInitial float64 `json:"streptococcus_initial_strain_cfu_ml"`
	LactobacillusInitial float64 `json:"lactobacillus_initial_strain_cfu_ml"`
	Temperature          float64 `json:"ideal_temperature_c"`
	MilkProteins         float64 `json:"minimum_milk_proteins"`
	TritatableAcidity    float64 `json:"titratable_acidity"`
	PhMilkSour           float64 `json:"pH_milk_sour_"`
	FatMilk              float64 `json:"fat_milk_over_100mg_"`
	QualityProduct       string  `json:"quality_product"`
	LactobacillusFinal   float64 `json:"lactobacillus_final_cfu_ml"`
	StreptococcusFinal   float64 `json:"streptococcus_final_cfu_ml"`
}

type ResponseBody struct {
	JSONResponse
	Result interface{} `json:"result"`
}

func GetAllParameters(c *gin.Context) {

	file, err := os.Open(DataSetPath)
	if err != nil {
		log.Fatalf("Error by %s", err)
	}
	defer file.Close()

	dataset := dataframe
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

	fmt.Println(dataReader)
	c.JSON(http.StatusOK, RegressionControllers{})
}
