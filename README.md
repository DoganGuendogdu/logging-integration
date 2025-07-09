# Ideas

## Prometheus Metric integration with Alert manager
## All the metrics Crtical, ERROR integrated
## More complex metrics, example, more than 5 Authentication error or Critical errors in a minute -> hacking in progress -> ALERT!
## Grafana integration
## Grafana or Prometheus integration in the Streamlit UI

# Configuration
## Email notification
- Use email notification service by Prometheus.
- Please reference following link to register an application to your Google Account: [Register app to Gmail account](https://www.youtube.com/watch?v=a6Gh01-Rldw).
- After that, add the missing information to the `alertmanager.yml` file in dir `/alertmanager`. 

## Create alerts
- To use updated values from the UI to set alert thresholds and values , you need to ensure that the bash script is executable.
- `chmod +x backend/bin/create-prometheus-alerts.sh`

## Access Grafana dashboard
- Default username and password to login.
- `username: user`
- `password: password123 `
- To change username and password, edit the `.env` file in the root directory. 
-  Make sure to delete the corresponding docker volume `logging-integration_grafana-storage` first, so the changes of the `.env` file can take effect after rebuilding.
- Rebuild the application with `docker compose build --no-cache`.

## Running the application
- `docker compose up`

