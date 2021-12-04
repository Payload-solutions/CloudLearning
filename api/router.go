package api

import (
	//. "github.com/Arturo0911/CloudLearning/api/controllers"
	"github.com/gin-gonic/gin"
)

func Router(router *gin.Engine) *gin.Engine {

	//controller :=
	router.Group("/regression").
		GET("/")

	return router
}
