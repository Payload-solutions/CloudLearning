package api

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

const DataSetPath = "neural_model/data/data_regression_set.csv"

type JSONResponse struct {
	Success bool   `json:"success"`
	Error   string `json:"error,omitempty"`
	Message string `json:"message,omitempty"`
}

func errorHandling(c *gin.Context, message string) {
	c.JSON(http.StatusBadRequest, JSONResponse{Success: false, Error: message})
	c.Abort()
}
