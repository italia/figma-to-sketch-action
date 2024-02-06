# GitHub action to convert Figma files to Sketch ones

[![Join the #publiccode channel](https://img.shields.io/badge/Slack%20channel-%23publiccode-blue.svg?logo=slack)](https://developersitalia.slack.com/messages/CAM3F785T)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)

## Inputs

The following inputs briefly explained here are fully declared and documented in the [action.yaml](action.yaml):

* `files` [**Required**] - Figma files to convert separated by `|` (default `*.fig*`)
* `output_files` [**Required**] - Sketch files produced separated by `|` (default `*.sketch*`)

## Examples

Include this action in your repo by creating 
`.github/workflows/fig2sketch.yml`and edit where needed:

```yml
jobs:
  examplejob:
    runs-on: ubuntu-latest
    name: Convert Figma files to Sketch ones
    steps:
    - uses: actions/checkout@v2
    - uses: italia/figma-to-sketch-action@v1
      with:
        files: "my_ui.fig"
        output_files: "my_ui.sketch"
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

© 2024 Dipartimento per la Trasformazione Digitale - Presidenza del Consiglio dei
Ministri

Licensed under the EUPL.
The version control system provides attribution for specific lines of code.

## Remarks

This GitHub Action is published in the Github Marketplace.
As such, you can find the [Terms of Service here](https://docs.github.com/en/free-pro-team@latest/github/site-policy/github-marketplace-terms-of-service).
Also, [here](https://docs.github.com/en/free-pro-team@latest/github/site-policy/github-marketplace-developer-agreement)
you can find the GitHub Marketplace Developer Agreement.
