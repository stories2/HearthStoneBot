# Project Title

Hearthstone deck tracking and simulate.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project only working mac os.

### Installing

[Check this](https://github.com/stories2/HearthStoneBot/wiki/Workspace-setting)

## Running the tests

In Runner.py, disable or delete this line.

```FileIO.StaticLoader()```

And enable or write this.

```FileIO.RealtimeLoader("/Users/" + DefineManager.COMPUTER_USER_NAME + "/Library/Preferences/Blizzard/Hearthstone/Logs/" + DefineManager.LOG_FILE_NAME)```

In Settings/DefineManager.py, set `COMPUTER_USER_NAME` your username.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details