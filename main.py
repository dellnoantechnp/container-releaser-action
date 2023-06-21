import os
# import requests  # noqa We are just importing this to prove the dependency installed correctly
from dockerfile_parse import DockerfileParser


def main():
    dockerfile = os.environ["INPUT_DOCKERFILE"]

    # github_home = "/github/home"
    # dockerfile = github_home + "/" + dockerfile.lstrip("/")

    docker = DockerfileParser(fileobj=open(dockerfile, "r"))

    version = docker.labels.get("org.opencontainers.image.version", "latest")

    print(f"version={version}")


if __name__ == "__main__":
    main()
