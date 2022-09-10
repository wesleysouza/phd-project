FROM ubuntu

WORKDIR /app
COPY ["gridlabd-4.3.0.x86_64.deb", "/app/gridlab.deb"]

#ADD GridLAB-D and iproute2
RUN apt-get update && apt-get install libxerces-c-dev iproute2 -y && dpkg -i gridlab.deb



