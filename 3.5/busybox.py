import docker


def main():
    client = docker.from_env()

    print("מוריד busybox אם צריך.")
    client.images.pull("busybox")

    print("מריץ קונטיינר עם sleep")
    container = client.containers.run(
        "busybox",
        ["sh", "-c", "sleep 3600"],
        name="python-docker-busybox",
        detach=True
    )

    print(f"Container started: {container.short_id}")

    print("מריץ hostname בתוך הקונטיינר")
    result = container.exec_run("hostname")

    hostname = result.output.decode().strip()
    print(f"Hostname: {hostname}")


if __name__ == "__main__":
    main()
