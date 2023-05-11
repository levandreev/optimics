# Point to Point Connection tester

A simple java app to test P2P communication by creating a thread every second (configurable).

## Build with dependencies

```bash
mvn assembly:assembly -DdescriptorId=jar-with-dependencies
```

## Run

```bash
java -jar target/p2p-connection-test-1.0-SNAPSHOT-jar-with-dependencies.jar
```

## Environment variables

| Env            | Description                                         | Default Value            |
| -------------- | --------------------------------------------------- | ------------------------ |
| `CONN_NAME`    | Connection name list                                | `"165.72.169.236(1427)"` |
| `CHANNEL`      | Channel name                                        | `"DEV.APP.SVRCONN"`      |
| `QMGR`         | Queue manager name                                  | `"QMPS1"`                |
| `APP_USER`     | User name that application uses to connect to MQ    | `"app"`                  |
| `APP_PASSWORD` | Password that the application uses to connect to MQ | `"w1r3$p33d"`            |
| `QUEUE_NAME`   | Queue that the application uses to put messages to  | `"QUEUE1"`               |
| `RATE`         | Sleep time between messages                         | `1000`                   |

## Example

Above `Run` command needs to be modified based on variables.
Below is the example how to generate load for QM `MYMQ061`.
Remaining values stay as default.

```bash
java -jar -DQMGR="MYMQ061" -DQUEUE_NAME="APAMA.BPM.SDCM" target/p2p-connection-test-1.0-SNAPSHOT-jar-with-dependencies.jar
```
