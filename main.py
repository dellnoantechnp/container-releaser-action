import os
# import requests  # noqa We are just importing this to prove the dependency installed correctly
from dockerfile_parse import DockerfileParser
import subprocess
import lookup_latest_tag


def run_command(command: str) -> str:
    proc = subprocess.Popen(command,
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                            )
    stdout_value, stderr_value = proc.communicate()
    return stdout_value.decode().strip()


def main():
    dockerfile = os.environ["INPUT_DOCKERFILE"]

    # github_home = "/github/home"
    # dockerfile = github_home + "/" + dockerfile.lstrip("/")

    docker = DockerfileParser(fileobj=open(dockerfile, "r"))

    version = docker.labels.get("org.opencontainers.image.version", "latest")

    print(f"version={version}")


if __name__ == "__main__":
    main()
