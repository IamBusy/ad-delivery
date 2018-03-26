package main

import (
	"github.com/julienschmidt/httprouter"
	"github.com/BurntSushi/toml"
	"log"
	"github.com/coreos/etcd/client"
	"time"
	"net/http"
	"encoding/base64"
	"context"
	"fmt"
)

type Config struct{
	Etcd struct {
		Host string
		Port int
	}
}



func main()  {
	var conf Config
	if _, err := toml.DecodeFile("./db.toml", &conf); err != nil {
		log.Fatal(err)
	}
	cfg := client.Config{
		Endpoints: []string{fmt.Sprintf("http://%s:%d", conf.Etcd.Host, conf.Etcd.Port)},
		Transport: client.DefaultTransport,
		HeaderTimeoutPerRequest: time.Second * 3,
	}
	c, err := client.New(cfg)
	if err != nil {
		log.Fatal(err)
	}
	kapi := client.NewKeysAPI(c)
	router := httprouter.New()
	if err != nil {
		log.Fatal(err)
	}

	router.GET("/write", func(writer http.ResponseWriter, request *http.Request, params httprouter.Params) {
		queryValues := request.URL.Query()
		k := queryValues.Get("key")
		v := queryValues.Get("value")

		debug := queryValues.Get("debug")
		if debug != "true" {
			tmpK,_ := base64.StdEncoding.DecodeString(k)
			tmpV,_ := base64.StdEncoding.DecodeString(v)
			k = string(tmpK)
			v = string(tmpV)

		}
		log.Println(k, v)
		if len(k) == 0 || len(v) == 0 {
			return
		}
		kapi.Set(context.Background(), k, v, nil)
		writer.Write([]byte("Successfully"))
	})
	log.Fatal(http.ListenAndServe(":8080", router))
}

