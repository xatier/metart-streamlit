FROM ghcr.io/xatier/arch-dev:latest

USER root
RUN pacman -Syuu --noconfirm --needed \
    python

WORKDIR /app
RUN chown xatier:xatier /app

USER xatier

COPY ./requirements.txt /app/requirements.txt
COPY ./server.py /app/server.py
COPY ./sites.py /app/sites.py
COPY ./credentials.toml /home/xatier/.streamlit/credentials.toml
COPY ./config.toml /home/xatier/.streamlit/config.toml

RUN python -m venv venv && \
    source venv/bin/activate && \
    pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "source venv/bin/activate && streamlit run server.py"]
