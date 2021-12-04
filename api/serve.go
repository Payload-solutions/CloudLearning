package api

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

func Serve() {

	router := gin.Default()
	Router(router)

	serve := &http.Server{
		Addr:    ":8000",
		Handler: router,
	}

	if err := serve.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		log.Fatalf("Error trying yo connect with the server")
		return
	}
	fmt.Println("Listening in http://127.0.0.1:8000/regression")
}
