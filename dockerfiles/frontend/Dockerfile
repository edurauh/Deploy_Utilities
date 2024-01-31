# Stage 1: Build the application
ARG BASE_IMAGE=${BASE_NODE_IMAGE}

FROM ${BASE_IMAGE} as build-stage

# reads arguments and sends environment variables from them
ARG VUE_APP_DBSERVICE_URL
ENV VUE_APP_DBSERVICE_URL $VUE_APP_DBSERVICE_URL
ARG VUE_APP_GATEWAY_STORAGE_URL
ENV VUE_APP_GATEWAY_STORAGE_URL $VUE_APP_GATEWAY_STORAGE_URL
ARG VUE_APP_GATEWAY_ALGMAN_URL
ENV VUE_APP_GATEWAY_ALGMAN_URL $VUE_APP_GATEWAY_ALGMAN_URL
ARG VUE_APP_LOGIN_URL
ENV VUE_APP_LOGIN_URL $VUE_APP_LOGIN_URL
ARG VUE_APP_LOGIN_CLIENT_ID
ENV VUE_APP_LOGIN_CLIENT_ID $VUE_APP_LOGIN_CLIENT_ID
ARG VUE_APP_LOGIN_CLIENT_SECRET
ENV VUE_APP_LOGIN_CLIENT_SECRET $VUE_APP_LOGIN_CLIENT_SECRET

VOLUME /app
WORKDIR /app

COPY package*.json ./
RUN npm set strict-ssl false
RUN npm config set proxy http://EYC5:brsiop2024!@inet-sys.petrobras.com.br:804
RUN npm config set https-proxy http://EYC5:brsiop2024!@inet-sys.petrobras.com.br:804
RUN npm install
COPY . .
RUN npm run build
RUN npm set strict-ssl true

# Stage 2: Serve the application using Node.js http-server
FROM ${BASE_IMAGE} as production-stage

# Set the working directory
WORKDIR /usr/src/app

# Copy the built files from the build stage
COPY --from=build-stage /app/dist ./dist

# Install http-server globally
RUN npm set strict-ssl false
RUN npm config set proxy http://EYC5:brsiop2024!@inet-sys.petrobras.com.br:804
RUN npm config set https-proxy http://EYC5:brsiop2024!@inet-sys.petrobras.com.br:804
RUN npm cache clean --force && \
    npm install -g npm@8.19.2 && \
    npm install
RUN npm install -g http-server
RUN npm set strict-ssl true

# Expose the port you want to use for serving the application
EXPOSE 8013

# Command to start the HTTP server and serve the built application
CMD [ "http-server", "dist" ,"-p8013"]