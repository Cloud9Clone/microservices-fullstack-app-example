# Product Likes App

A fullstack web application demonstrating the combination of microservice architecture pattern and the communication between its actors.

## Description

The core idea of the current app is on the one hand to present a list of products where a user can mark favourite products by liking them and on the other hand to display the number of likes for each particular product in an admin panel. For building the admin back-end functionality is used the Django web framework with a MySQL database, all wrapped in Docker containers. In a similar way is built the other microservice but with the only difference that it is written in the Spring Boot framework. On the client-side is used the Angular framework with the Bootstrap library. As a communication method between the microservices is chosen the AMQP with one of the most famous libraries for it, namely the RabbitMQ.