ARG BASE_IMAGE=${BASE_JAVA_IMAGE}
FROM ${BASE_IMAGE}

VOLUME /app

COPY target/namingServer-0.0.1-SNAPSHOT.jar namingserver.jar

EXPOSE 8761

ENTRYPOINT ["java", "-jar", "namingserver.jar"]