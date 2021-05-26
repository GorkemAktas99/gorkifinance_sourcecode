FROM ubuntu:20.04
COPY . /app
WORKDIR /app
RUN apt-get update -y && apt-get upgrade -y
RUN apt install python3-pip -y
RUN pip3 install matplotlib
RUN pip3 install pandas_datareader
RUN pip3 install mplfinance
RUN pip3 install mpld3
ENTRYPOINT ["python3"]
CMD ["./intro.py"]
