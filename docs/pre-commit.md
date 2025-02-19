# Pre-commit hooks

`pre-commit` is a tool that runs hooks before making a commit in Git. It is used to automatically apply checks and formatting to the code, ensuring quality and consistency before it is saved in the repository.

# Set up

It is easily installed with:

```console
pip install pre-commit
```

Then, it must be initialized in the repository by running in the root:

```console
pre-commit install
```

This creates a `.pre-commit-config.yaml` file, where the hooks are configured.
An example configuration file could be:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace # Removes unnecessary whitespace
      - id: end-of-file-fixer # Ensures files end with a blank line
      - id: check-yaml # Checks that YAML files are valid
      - id: check-ast # Checks that Python files are syntactically correct

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black # Formats Python files with Black
```

In this file, all the hooks that we want to run before making a commit are added. The version (rev) can be updated with `pre-commit autoupdate` as explained below.

## Running the hooks

All hooks will be automatically executed when a `git commit` is made, which will output the test results to the terminal. If any hook fails (due to incorrect formatting, for example), the commit will not be carried out.

Some hooks (the formatting ones) will change the problematic file, which will need to be added again with `git add` before executing the commit again.

If you want to run the hooks before the commit to manually ensure that everything is okay, you can do so with:

```console
pre-commit run --all-files
```

The first time a hook is run, the system installs it and it takes a while. It also creates a cache folder in the repository, `node_modules`, to speed up subsequent runs. It is advisable to add this folder to `.gitignore`.

## Updating the hooks

To update to the latest version of each hook, you can run

```console
pre-commit autoupdate
```

This is especially useful the first time we add a hook to the configuration file if we do not know what the latest version is.
