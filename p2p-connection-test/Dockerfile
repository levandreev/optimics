FROM registry.access.redhat.com/redhat-openjdk-18/openjdk18-openshift:1.12

COPY target/p2p-connection-test-1.0-SNAPSHOT-jar-with-dependencies.jar ./p2p-conn-test.jar

ENTRYPOINT ["java", "-jar", "p2p-conn-test.jar"]