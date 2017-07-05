Sublime Ramda Repl
=========================
Try out Ramda functions from Sublime itself

Requirements
============
None. Well, other than Ramda :-)

Installation
------------
To install it **manually with Git:** Clone the repository in your Sublime Text 3 Packages directory:

    git clone https://github.com/bijoythomas/sublime-ramda-repl ramdarepl


The "Packages" directory should be located at:

* OS X:

    ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/

* Linux:

    ~/.Sublime\ Text\ 3/Packages/
    or
    ~/.config/sublime-text-3/Packages/

* Windows:

    %APPDATA%/Sublime Text 3/Packages/


The plugin should be picked up automatically. If not, restart Sublime Text.

Usage
-----
Simply use Ctrl-n or Cmd-n to open a new tab in Sublime, type in your JS code
and hit ctrl+shift+r

The plugin adds the following key bindings.

```
[
  {
    "keys": ["ctrl+shift+r"], "command": "ramda_repl"
  }
]
```

You can tweak the plugin settings to provide the path to the ramda lib and
optionally include ramda-fantasy

```
{
  // Absolutle path to the dir containing the ramda lib
  // Examples:
  //    /Users/me/project/node_modules
  "node_modules_path": "/Users/bijoythomas/Zulu/SchedulingMVP/node_modules",
  "ramda-fantasy" : true
}
```

Screenshot
---------
