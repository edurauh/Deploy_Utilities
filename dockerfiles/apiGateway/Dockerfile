ARG BASE_IMAGE=${BASE_JAVA_IMAGE}
FROM ${BASE_IMAGE}

VOLUME /app

COPY target/apiGateway-0.0.1-SNAPSHOT.jar apigateway.jar

#EXPOSE 8000

ENTRYPOINT ["java", "-jar", "apigateway.jar"]