package helper

import (
	"fmt"
	"os"

	"github.com/kniren/gota/dataframe"
)

func TransformStuct(pathFile string) error {

	file, err := os.Open(pathFile)
	if err != nil {
		return err
	}

	dataset := dataframe.ReadCSV(file)
	fmt.Println(dataset)
	return nil
}
