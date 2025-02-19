# Git and GitHub

This section explains how to set up Git and create the repository, as well as a brief tutorial on the most commonly used Git functionalities.
In [this](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners) link, there is a pretty good basic tutorial.

## Set up

Git comes pre-installed on Ubuntu, which is the OS of the VM where the project is developed. In any case, its installation would be done with:

```console
sudo apt update && sudo apt install git -y
```

If you want to use this repo as a template for developing future projects, you would clone the repo into the desired folder with:

```console
git clone https://github.com/mikel314/devproject.git
```

If, on the other hand, you want to create a repository from scratch, it is recommended to first create it on the GitHub website and then clone it locally to edit it. To do this:

1. **Create a Repository on GitHub**

- Go to GitHub and log in at https://github.com.
- Click on the "New" button.
- Create a name for your repository, for example: my-project.
- (Optional) Add a description.
- Choose the visibility (Public to use GitHub pages as documentation).
- Choose to create a README.md file.
- Choose to create a .gitignore file.
- Click on "Create repository".

2. **Clone the Repository on Linux**

   - Go to the folder where you want to clone the repository, for example:

   ```console
        cd ~/Projects
   ```

   - Clone the repository with `git clone`:

   ```console
        git clone https://github.com/your-username/my-project.git
   ```

3. **Confirm that the repository is properly cloned**

   - To verify that everything is correct, you can run `git status`.
   - If everything went well, you will see something like:

   ```console
        On branch main
        Your branch is up to date with 'origin/main'.

        nothing to commit, working tree clean
   ```

## Git repo structure

Although there is no fixed structure for ML projects, the following generally works well:

```
/project_name
│── data/                # Data (raw, processed)
│   ├── raw/             # Unprocessed data
│   ├── processed/       # Data after cleaning
│   └── external/        # Third-party data (optional)
│
│── notebooks/           # Jupyter Notebooks
│
│── src/                 # Project source code
│
│── models/              # Trained models (artifact)
│
│── reports/             # Reports and visualizations
│
│── tests/               # Unit tests
│
│── docs/                # Documentation
│
│── config/              # Configuration files
│
│── infra/               # Infrastructure as code
│
│── .gitignore           # Ignore files (large data, logs)
│── requirements.txt     # Project dependencies
│── README.md            # Project description
│── LICENSE              # Project license

```

## Basic commands

The basic functionality that will be used most often is to commit and push changes to the GitHub repository.

```console
git add files_or_folder
git commit -m "meaningful message"
git push
```

We can check the synchronization status with `git status`.

## Basic Branching and Merging

For a basic understanding of how to manage different branches and how to merge them an resolve conflicts, please visite the tutorial [Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

## Visual Studio code

Git can be managed directly from VS code interface. In the [Using Git source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview) tutorial you can learn how to add, commit, merge etc directly from the UI or how to interpret the info displayed.
