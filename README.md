# Prometheus Django

Instrumenting a Django server with [Prometheus](https://prometheus.io/).

## Motivation

Prometheus is a monitoring and visualization tool that can easily be used to instrument Kubernetes.

This follows on from my [Cloud Django](https://github.com/mramshaw/Cloud_Django) exercise.

## Prometheus Installation

1. Download the [latest stable release for your platform](https://prometheus.io/download/).

    [At the time of writing this is `prometheus-2.1.0.linux-amd64.tar.gz`]

2. Note the checksum.

    [At the time of writing this is `f181f619c9a8e0750c1ac940eb00a0881cc50386d896f06f159e9a5b68db60a0`]

3. Verify the checksum (SHA 256 Checksum):

    $ sha256sum prometheus-2.1.0.linux-amd64.tar.gz

4. Uncompress it (using `tar` or `ark` or whatever floats your boat).

There is also a [Docker image](https://hub.docker.com/r/prom/prometheus/):

    prom/prometheus:v2.1.0

## Install Django dependencies

As usual, I do not recommend global installs:

    $ pip install --user prometheus_client

Verify the version:

    $ pip list --format=legacy | grep prometheus-client

[0.1.1]

    $ pip install --user 

[Replace `pip` with `pip3` for Python3.]

Or simply use the `requirements.txt` file:

    $ pip install --user -r requirements.txt

## Launch Prometheus

Run it as follows:

    $ ./prometheus-2.1.0.linux-amd64/prometheus --config.file=prometheus.yaml

[This will create a `data` directory for the prometheus stats.]

## Prometheus best practices:

Naming:

    https://prometheus.io/docs/practices/naming/

Instrumentation:

    https://prometheus.io/docs/practices/instrumentation/

## Advanced Tutorials

    https://www.digitalocean.com/community/tutorials/how-to-query-prometheus-on-ubuntu-14-04-part-1

    https://www.digitalocean.com/community/tutorials/how-to-query-prometheus-on-ubuntu-14-04-part-2

## To Do

## Credits

Based on:

    https://github.com/korfuri/django-prometheus

And:

    https://github.com/prometheus/client_python
