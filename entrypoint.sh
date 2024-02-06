#!/bin/sh
set -e

if [ -n "${GITHUB_WORKSPACE}" ]; then
  cd "${GITHUB_WORKSPACE}" || exit
fi

get_repo() {
  if [ -n "${INPUT_GITHUB_TOKEN}" ]; then
    echo "Use INPUT_GITHUB_TOKEN to get release data." >&2
    curl -s -H "Authorization: token ${INPUT_GITHUB_TOKEN}" "https://api.github.com/repos/${INPUT_REPO}"
  else
    echo "INPUT_GITHUB_TOKEN is not available. Subsequent GitHub API call may fail due to API limit." >&2
    curl -s "https://api.github.com/repos/${INPUT_REPO}"
  fi
}

STARS_COUNT=$(get_repo | jq -r '.stargazers_count')
if [ -z "${STARS_COUNT}" ] || [ "${STARS_COUNT}" = "null" ]; then
  echo "cannot get star count from ${INPUT_REPO}"
  exit 1
fi

LICENSE=$(get_repo | jq -r '.license.name')
if [ -z "${LICENSE}" ] || [ "${LICENSE}" = "null" ]; then
  echo "cannot get license from ${INPUT_REPO}"
  exit 1
fi

echo "Repo has ${STARS_COUNT} ⭐️ and is released under ${LICENSE} license"

echo "::set-output name=stars::${STARS_COUNT}"
echo "::set-output name=license::${LICENSE}"
