from main import run_command


fetch = "git fetch --tags"
run_command(fetch)

latest_tag = "git describe --tags --abbrev=0 HEAD~"

latest_commitID = "git rev-list --max-parents=0 --first-parent HEAD"

if len(run_command(latest_tag)) > 0:
    tag = run_command((latest_tag))
