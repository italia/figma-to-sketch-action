# GitHub Docker container action template

[![Join the #publiccode channel](https://img.shields.io/badge/Slack%20channel-%23publiccode-blue.svg?logo=slack)](https://developersitalia.slack.com/messages/CAM3F785T)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)

This is a template repository for [creating a GitHub Docker container action](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-a-docker-container-action).

Click `Use this template` button to create your action based on this template.

A sample action to get GitHub star counts and license from a given repository.

## Inputs

The following inputs briefly explained here are fully declared and documented in the [action.yaml](action.yaml):

* `repo` [**Required**] - GitHub repository to fetch (default `${{ github.repository }}`)

* `github_token` [**Optional**] - GitHub token to interact with GitHub API (default `${{ github.token }}`)

## Examples

Include this action in your repo by creating 
`.github/workflows/docker-action-template.yml`and edit where needed:

```yml
on: [push, pull_request]

jobs:
  examplejob:
    runs-on: ubuntu-latest
    name: Get Stars and License
    steps:
    - uses: actions/checkout@v2
    - uses: italia/docker-action-template@v1
      with:
        repo: "italia/publiccode-parser-action"
```

## Contributing

Contributing is always appreciated.
Feel free to open issues, fork or submit a Pull Request.
If you want to know more about how to add new fields, check out [CONTRIBUTING.md](CONTRIBUTING.md).
In order to support other country-specific extensions in addition to Italy some
refactoring might be needed.

## Maintainers

This software is maintained by the
[Developers Italia](https://developers.italia.it/) team.

## License

© 2021 Dipartimento per la Trasformazione Digitale - Presidenza del Consiglio dei
Ministri

Licensed under the EUPL.
The version control system provides attribution for specific lines of code.

## Remarks

This GitHub Action is published in the Github Marketplace.
As such, you can find the [Terms of Service here](https://docs.github.com/en/free-pro-team@latest/github/site-policy/github-marketplace-terms-of-service).
Also, [here](https://docs.github.com/en/free-pro-team@latest/github/site-policy/github-marketplace-developer-agreement)
you can find the GitHub Marketplace Developer Agreement.
