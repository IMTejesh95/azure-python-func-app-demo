# Azure Function App Demo Project
---
## Local Environment Setup (MacOS M1/ARM Architecture )

***Azure Function local environment for Python runtime not yet supported on arm64 architecture.<br> Here is the workaround for it...***

### Install *Rosetta*
*Rosetta* emulates `x86_64` architecture on Apple Silicon chip.

- To install Rosetta
```bash
$ softwareupdate --install-rosetta --agree-to-license
```
- Create duplicate (call it `rosettaTerm`) of *Terminal* or *iTerm* to open it using Rosetta, which should provide `x86_64` arch environment.

![alt text](./images/duplicate.png "Duplicate terminal App")
![alt text](./images/getinfo.png "Duplicate terminal App")
![alt text](./images/openusingrosetta.png "Duplicate terminal App")


### Install required packages
Open `rosettaTerm` and follow along...


