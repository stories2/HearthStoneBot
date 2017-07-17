# Project Title

Hearthstone deck tracking and simulate.

[![Sample program running](./Sample.png)](https://www.youtube.com/embed/YM4Zv0CeJSY)

## Getting Started

### Prerequisites

This project only working mac os.
You should be an hearthstone player.

### Installing

[Check this](https://github.com/stories2/HearthStoneBot/wiki/Workspace-setting)

## Running the tests

### Realtime test

In Runner.py, disable or delete this line.

```FileIO.StaticLoader()```

And enable or write this.

```FileIO.RealtimeLoader("/Users/" + DefineManager.COMPUTER_USER_NAME + "/Library/Preferences/Blizzard/Hearthstone/Logs/" + DefineManager.LOG_FILE_NAME)```

In Settings/DefineManager.py, set `COMPUTER_USER_NAME` your username.

### Static test

In Runner.py, disable or delete this line.

```FileIO.RealtimeLoader("/Users/" + DefineManager.COMPUTER_USER_NAME + "/Library/Preferences/Blizzard/Hearthstone/Logs/" + DefineManager.LOG_FILE_NAME)```

And enable or write this.

```FileIO.StaticLoader()```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details