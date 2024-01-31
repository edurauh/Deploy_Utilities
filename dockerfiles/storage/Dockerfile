ARG BASE_IMAGE=${BASE_JAVA_IMAGE}
FROM ${BASE_IMAGE}

VOLUME /app

COPY target/storage-0.0.1-SNAPSHOT.jar storage.jar

EXPOSE 8081

ENTRYPOINT ["java", "-jar", "storage.jar"]