FROM python:2.7-slim
LABEL "purpose"="clean environment for webapp development"

# workaround for apt-get
ENV DEBIAN_FRONTEND noninteractive

# having a requirements.txt would mean rerunning apt-get as docker cannot reuse apt-get when it is after VOLUME
RUN apt-get update -qq && apt-get install -qqy \
		gcc build-essential \
		sqlite3 libjpeg-dev zlib1g-dev \
		python python-pip python2.7-dev python-imaging \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

# keep all non-RUN commands at the end
VOLUME ["/kanvas"]
COPY . /kanvas
WORKDIR /kanvas
EXPOSE 8085

RUN pip install -q -r requirements.txt

ENTRYPOINT ["/kanvas/entrypoint.sh"]