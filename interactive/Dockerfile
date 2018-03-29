FROM williamwxl/go-dep:1.9.0-alpine AS build-env
ADD . /go/src/app
WORKDIR /go/src/app
RUN dep ensure && go build -o target main.go

FROM alpine:3.6
RUN apk add -U tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
COPY --from=build-env /go/src/app/target /usr/local/bin/app-server
ADD db.toml /
EXPOSE 8080
CMD ["app-server"]