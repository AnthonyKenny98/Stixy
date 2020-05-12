# Repository Setup

This folder contains the necessary scripts to setup and customize a project repo when using this template repo.

## setup.py

```setup.py``` will customize your repo quickly by replacing all Markdown placeholders with the details of the new repository.

Usage:
```
PythonTemplate User$ python3 scripts/setup/repo/setup.py
```

## Repository details
To input your repository details, simply fill in the ```.txt``` files with the name of the placeholder. There are 2 types of place holders:

1. Repository Name: "PythonTemplate" will be replaced by the name of your repository. This will default to the top level directory name, but can be overridden by putting a value in the ```RepoName.txt``` file.

2. Variable Placeholders: Variable placeholders are wrapped in Markdown comments like so:

```

<!--- (DO NOT REMOVE) Begin:PlaceholderName --->
This is what will be replaced with your value

<!-- (DO NOT REMOVE) End:PlaceholderName --->
```

The content between these comments will be replaced with the contents of the ```PlaceholderName.txt``` file. If the file is empty, the placeholder text will remain. This script can be run repeatedly to update your values. 