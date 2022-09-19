FROM python:3
EXPOSE 80/tcp
EXPOSE 80/udp

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install  iproute2 -y

COPY ["hems-app-client-socket.py", "hems-app-client-socket.py"]

CMD [ "python", "./hems-app-client-socket.py" ]