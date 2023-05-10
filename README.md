# fakelogger

fakelogger is a simple and useful Python script to test Elastic and Kibana. It generates random fake logs and sends them to Elastic.

# Usage 

 - Usage is also pretty simple. Clone the repo. Update `ELASTIC_URL` and `LOG_DURATION` environment variables in the `docker-compose.yaml` according to your environment and scenario.

 - `ELASTIC_URL` represents the Elastic endpoint
 - `LOG_DURATION` represents the period of sending logs to Elastic.

 - To run fakelogger at full capacity, you can set the `LOG_DURATION`  to 0 or simply not specify it. Otherwise, fakelogger will wait for the specified duration in seconds before sending logs.

 - After making the changes,

 ```
 docker compose up -d
 ```

# Tips

- If Elasticsearch is also running as a Docker container, you may not be able to access it at localhost:9200. In this case, you can modify the Docker Compose file to run Elasticsearch, Kibana, and Fakelogger on the same network, or alternatively, try using the server IP instead of localhost.

- Instead of creating an index for fakelogger, you can define the `ELASTIC_URL` as `<elasticendpoint>/fakeloggerindex/customlog` to enable Kibana to create an index.

- Go to `<kibanaendpoint>/app/management/kibana/indexPatterns`, click on Create Index Pattern, and create fakeloggerindex.




