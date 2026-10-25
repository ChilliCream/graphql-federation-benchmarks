#!/usr/bin/env bash
# Publishes benchmark results to the branch the run was started on, while the
# job itself stays checked out at the run's commit (github.sha).
#
#   results-branch.sh checkout <dir>          worktree of the branch tip at <dir>
#   results-branch.sh push <dir> <message>    commit all changes in <dir> and push
#
# The branch defaults to GITHUB_REF_NAME and can be overridden with RESULTS_BRANCH.
set -euo pipefail

BRANCH="${RESULTS_BRANCH:-${GITHUB_REF_NAME:?GITHUB_REF_NAME or RESULTS_BRANCH must be set}}"
REMOTE_REF="refs/remotes/origin/$BRANCH"

fetch_branch() {
  git fetch --quiet --depth=1 origin "+refs/heads/$BRANCH:$REMOTE_REF"
}

usage() {
  echo "Usage: results-branch.sh checkout <dir> | push <dir> <message>" >&2
  exit 2
}

[[ $# -ge 2 ]] || usage
command="$1"
dir="$2"

case "$command" in
  checkout)
    [[ $# -eq 2 ]] || usage
    fetch_branch
    git worktree add --quiet --detach "$dir" "$REMOTE_REF"
    git -C "$dir" config user.name "github-actions[bot]"
    git -C "$dir" config user.email "github-actions[bot]@users.noreply.github.com"
    ;;
  push)
    [[ $# -eq 3 ]] || usage
    message="$3"
    git -C "$dir" add -A
    if git -C "$dir" diff --cached --quiet; then
      echo "No changes to publish."
      exit 0
    fi
    git -C "$dir" commit --quiet -m "$message"
    commit="$(git -C "$dir" rev-parse HEAD)"
    for attempt in 1 2 3 4 5; do
      if git -C "$dir" push --quiet origin "HEAD:refs/heads/$BRANCH"; then
        echo "Published $commit to $BRANCH."
        exit 0
      fi
      if [[ "$attempt" -eq 5 ]]; then
        break
      fi
      echo "Push rejected (attempt $attempt); replaying onto the new $BRANCH tip."
      sleep $((attempt * 5))
      fetch_branch
      git -C "$dir" reset --quiet --hard "$REMOTE_REF"
      git -C "$dir" cherry-pick "$commit"
      commit="$(git -C "$dir" rev-parse HEAD)"
    done
    echo "Error: could not push results to $BRANCH." >&2
    exit 1
    ;;
  *)
    usage
    ;;
esac
