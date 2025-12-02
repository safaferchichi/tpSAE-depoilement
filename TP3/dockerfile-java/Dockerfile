# Étape 1 : compilation
FROM eclipse-temurin:21-jdk AS build

WORKDIR /app
COPY Hello.java .
RUN javac Hello.java

# Étape 2 : exécution
FROM eclipse-temurin:21-jre

WORKDIR /app
COPY --from=build /app/Hello.class .

CMD ["java", "Hello"]

