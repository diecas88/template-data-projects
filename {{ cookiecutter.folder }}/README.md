# {{ cookiecutter.project_name }} 

By: {{ cookiecutter.project_author_name }}.

Version: {{ cookiecutter.project_version }}

{{ cookiecutter.project_description }}

## Prerequisites

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate {{ cookiecutter.folder }}
```

or 

```bash
mamba env create -f environment.yml
activate {{ cookiecutter.folder }}
```

## Project organization

    {{ cookiecutter.folder }}
        ├── data
        │   ├── {{ cookiecutter.docs }}         <- The final, canonical data sets for modeling.
        │   └── {{ cookiecutter.src }}          <- The original, immutable data dump.
        │   ├── processed                       <- The final, canonical data sets for modeling.
        │   └── raw                             <- The original, immutable data dump.
        │
        ├── notebooks                           <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                                           the creator's initials, and a short `-` delimited description, e.g.
        │                                           ``.
        │
        ├── .gitignore                          <- Files to ignore by `git`.
        │
        ├── environment.yml                     <- The requirements file for reproducing the analysis environment.
        │
        └── README.md                           <- The top-level README for developers using this project.

---
