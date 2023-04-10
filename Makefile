.PHONY: all build run push

name = metart-streamlit:latest
image = xatier/$(name)
registry = ghcr.io/xatier

all: build push

build:
	podman build --squash --no-cache -t $(image) .

run:
	podman run --rm -it \
		--name metart \
		-p 127.0.0.1:8000:8000 \
		$(image)

push:
	podman images $(image)
	podman tag $(shell podman images $(image) -q) $(registry)/$(name)
	podman push $(registry)/$(name)
