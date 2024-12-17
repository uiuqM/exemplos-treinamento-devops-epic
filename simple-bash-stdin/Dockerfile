FROM alpine

WORKDIR /src

COPY app.sh /src

RUN chmod +x app.sh
RUN apk add --no-cache bash

CMD bash ./app.sh