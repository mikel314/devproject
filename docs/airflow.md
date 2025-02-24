# Airflow

## Introducction

Apache Airflow is an open-source platform designed to programmatically author, schedule, and monitor workflows. It is widely used for orchestrating complex data pipelines and automating repetitive tasks. 

You can find a [Quick start guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html) and a [basic tuturial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html)

## Setup

Airflow is not compatible with the latest version of python (atm 3.13) so please make sure you check the comaptibility and use the proper Python version. You can find it in the [Airflow Quick start guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html)

In Apache Airflow, the "location" of the installation can refer to two main things: where the Airflow software itself is installed (e.g., the Python package and its dependencies) or where Airflow’s runtime files (like airflow.cfg, DAGs, logs, and the database) are stored. We want the runtime files to be under our repo so we can syinc with git.

To do so we just need to create the ``AIRFLOW_HOME`` Environment Variable and point it to our repo.

```console
export AIRFLOW_HOME=/home/mikel/devproject/airflow
```

And make it persistent by adding it to your shell profile:

```console
echo "export AIRFLOW_HOME=/home/mikel/devproject/airflow" >> ~/.bashrc
source ~/.bashrc
```

Now we are ready to install Airflow

```console
pip install apache-airflow
```

Once done we just need to create the dag folder and place a dag file there:

```console
mkdir /home/mikel/devproject/airflow/dags
touch /home/mikel/devproject/airflow/dags/devproject_dag.py
```

We can now luanch Aiflow with 

```console
airflow standalone
```
The airflow standalone command initializes the database, creates a user, and starts all components. If you want to run the individual parts of Airflow manually rather than using the all-in-one ``standalone`` command, you can instead run:

```console
airflow db migrate

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

airflow webserver --port 8080

airflow scheduler
```

Finally, it is recommended to add the airflow logs to the ``.gitignore``


