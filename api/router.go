package api

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func Router(router *gin.Engine) *gin.Engine {

	router.Group("/regression", GetAllParameters).
		GET("/")

	router.Use(func(c *gin.Context) {
		c.JSON(http.StatusNotFound, JSONResponse{
			Success: false,
			Message: "resource not found!",
		})
	})

	return router
}
