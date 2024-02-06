# GitHub action to convert Figma files to Sketch ones

[![Join the #design-system channel](https://img.shields.io/badge/Slack%20channel-%23designers-blue.svg?logo=slack)](https://developersitalia.slack.com/messages/C7VPAUVB3)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)

This action converts Figma files to Sketch ones using [fig2sketch utility](https://github.com/sketch-hq/fig2sketch).

## Inputs

The following inputs briefly explained here are fully declared and documented in the [action.yaml](action.yaml):

* `files` [**Required**] - Figma files to convert separated by `|`.
* `output_files` [**Required**] - Sketch files produced separated by `|`.

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
    - uses: italia/figma-to-sketch-action@v0.1.3
      with:
        files: "my_ui.fig|my_best.fig"
        output_files: "my_ui.sketch|my_best.sketch"
```

## Development

You can test this action creating a `test_files` folder, ann `.env` file

```sh
INPUT_FILES=./test_files/test-ui.fig
INPUT_OUTPUT_FILES=./test_files/test-ui.sketch
```

and a `docker-compose.yml`

```yml
version: '3.3'

services:
  build:
    image: italia/figma-to-sketch-action
    container_name: figma2sketch-action
    build:
      context: ./
      dockerfile: Dockerfile
    env_file:
      - .env
    volumes:
      - ./test_files:/test_files
    networks:
      - overlay

networks:
  overlay:
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
