FROM python:3.12-alpine

# app directory
WORKDIR /app

# demo user
ARG USER_ID=1000 
ARG GROUP_ID=1000 

RUN addgroup -g ${GROUP_ID} demo \
 && adduser -D demo -u ${USER_ID} -g demo -G demo -s /bin/sh

# COPY FILES
COPY --chown=demo:demo . .

# Install dependencies
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
 && pip install --no-cache-dir -r requirements.txt \
 && apk del .build-deps gcc libc-dev make

USER demo

EXPOSE 8080 

# entrypoint 
CMD ["uvicorn","app.main:app","--proxy-headers","--host","0.0.0.0","--port","8080"]
