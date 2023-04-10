# NTP Viewer & Translator Description
The NTP Viewer & Translator has been designed as a single display & decode for the peerstats and the loopstats (future) log files.

The viewer will translate the various different fields (such as the Modified Julain Date & Timestamp) as well as the Peer Status Word to help with log review and troubleshooting.

# Future Updates

1. Searching & Filtering
2. Loopstats viewing & translating
3. Graphing capabilities

# Installation

```shell
git clone https://github.com/idarthjedi/ntpview
cd ntpview
poetry shell
python3 app.py
```