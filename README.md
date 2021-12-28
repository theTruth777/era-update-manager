# ERA Update Manager
This is the official update manager used in the ERA app (see [era.sh](https://era.sh))

## How it works
Once a new version of ERA is available, the app launches this small program, that will
handle the entire update process. This includes:

- Closing the running ERA app
- Downloading the new version for the running operating system
- Setting file permissions
- Deleting the old version of ERA
- Launching the new version of ERA

## Building a standalone executable
In order to build this small program into an executable, pyinstaller is
being used. 

The build parameters are:
```bash
$ pyinstaller --onefile --windowed __main__.py
```