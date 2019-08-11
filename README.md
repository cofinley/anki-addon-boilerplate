# anki-addon-boilerplate

An Anki add-on for getting started.

## Developing

- Helps to create a symlink to the anki plugin folder so you only have to edit one set of files
    - (As admin) `mklink /d <path to folder in anki addons> <path to actual addon/cloned folder>`
        - i.e. `mklink /d "C:\Users\me\AppData\Roaming\Anki2\addons21\anki-ff" "C:\Users\me\Documents\Code\anki-ff"`
- Run anki from the command line to view debug info easily
    - `anki-console.exe`
