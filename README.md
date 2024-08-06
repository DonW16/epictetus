# epictetus

## Build pod
```bash
podman build -t epictetus .
```

## Run pod
```bash
podman run --network host -e DISCORD_BOT_TOKEN="yourtokenhere" --read-only --cap-drop=ALL --security-opt=no-new-privileges -d --replace --name epictetus-container epictetus
```