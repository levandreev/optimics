/*
* (c) Copyright IBM Corporation 2018
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

package com.ibm.clientengineering;

import javax.jms.Destination;
import javax.jms.JMSContext;
import javax.jms.JMSProducer;

import java.text.SimpleDateFormat;
import java.util.Date;

import com.ibm.mq.jms.MQConnectionFactory;
import com.ibm.msg.client.wmq.WMQConstants;

/**
 * A minimal and simple application for Point-to-point messaging.
 *
 * Application makes use of fixed literals, any customisations will require
 * re-compilation of this source file. Application assumes that the named queue
 * is empty prior to a run.
 *
 * Notes:
 *
 * API type: JMS API (v2.0, simplified domain)
 *
 * Messaging domain: Point-to-point
 *
 * Provider type: IBM MQ
 *
 * Connection mode: Client connection
 *
 * JNDI in use: No
 *
 */
public class JmsProducerThread extends Thread {

    private static final String DATE_PATTERN = "HH:mm:ss.SSSZ";
    private static final SimpleDateFormat SDF = new SimpleDateFormat(DATE_PATTERN);

    private String name;

    public JmsProducerThread(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        System.out.println("[" + this.name + "] starting...");

        // JMS Variables
        JMSContext context = null;
        Destination destination = null;
        JMSProducer producer = null;

        try {
            // Create a connection factory
            MQConnectionFactory cf = new MQConnectionFactory();

            // Set the properties
            cf.setConnectionNameList(JmsProducerMain.CONN_NAME);
            cf.setChannel(JmsProducerMain.CHANNEL);
            cf.setTransportType(WMQConstants.WMQ_CM_CLIENT);
            cf.setStringProperty(WMQConstants.WMQ_QUEUE_MANAGER, JmsProducerMain.QMGR);
            cf.setStringProperty(WMQConstants.WMQ_APPLICATIONNAME, "JmsProducer");
            cf.setBooleanProperty(WMQConstants.USER_AUTHENTICATION_MQCSP, true);
            cf.setStringProperty(WMQConstants.USERID, JmsProducerMain.APP_USER);
            cf.setStringProperty(WMQConstants.PASSWORD, JmsProducerMain.APP_PASSWORD);
            // cf.setClientReconnectOptions(WMQConstants.WMQ_CLIENT_RECONNECT);
            // cf.setClientReconnectTimeout(600);
            // cf.setStringProperty(WMQConstants.WMQ_SSL_CIPHER_SUITE, "*TLS12");

            // Create JMS objects

            Date beforeConnection = new Date();
            context = cf.createContext();
            destination = context.createQueue("queue:///" + JmsProducerMain.QUEUE_NAME);

            producer = context.createProducer();
            Date readyToSend = new Date();

            producer.send(destination, JmsProducerMain.MSG);
            Date afterSend = new Date();

            System.out.println("[" + this.name + "]: beforeConn=" + SDF.format(beforeConnection) + ", readyToSend="
                    + SDF.format(readyToSend) + ", afterSend=" + SDF.format(afterSend));

        } catch (Exception e) {
            System.out.println("[" + this.name + "] ERROR - " + e.getMessage());

        } finally {
            try {
                context.close();
            } catch (Exception e) {
                // I know
            }
        }
    }

}