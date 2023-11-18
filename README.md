# Xbox360-Game-Database
Index of Xbox 360 game titles, title IDs, and Xbox filesystem compliant names.

The accompanying Python script can be used to organize game folders if they are named with Title IDs, as they are after being processed with ISO2GoD.

This:
```bash
-Directory
--Title ID
---Game files
--Title ID
---Game files
```
will become this:
```bash
-Directory
--Game Title
---Title ID
----Game files
--Game Title
---Title ID
----Game files
```

##Usage
```bash
python3 organize.py <Path to directory of game folders>
```
