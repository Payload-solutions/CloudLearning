FROM golang:1.17.2

WORKDIR $GOPATH/src/github.com/Arturo0911/CloudLearning

COPY . .

RUN go get -d -v ./...

RUN go install -v ./...

CMD ["CloudLearning"]
