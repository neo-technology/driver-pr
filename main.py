import sys
import re
from os import getenv
from os.path import abspath
from subprocess import check_call, call, check_output

remote = "remote"


#def probe_driver_repo_for_name(driverRepoPath):
#    url = check_output(
#        ["git", "remote", "get-url", remote],
#        cwd=driverRepoPath, universal_newlines=True)
#    url = url.splitlines()[0]
#    match = re.search('neo4j-(?P<driverName>.*)-driver', url)
#    if not match:
#        return "unknown"
#    try:
#        return match.group('driverName')
#    except IndexError:
#        return "unknown"


def get_testkit_branch(driverName, driverTargetBranch):
    if driverName == "go" and driverTargetBranch in ['4.0', '4.1']:
        return "4.2"
    return driverTargetBranch


def main(testkitRepoPath, driverTargetBranch):
    testkitRepoPath = abspath(testkitRepoPath)
    driverRepoPath = abspath(driverRepoPath)
    driverName = getenv('TEST_DRIVER_NAME') #probe_driver_repo_for_name(driverRepoPath)
    print("Driver is {} and target branch is {}".format(
        driverName, driverTargetBranch))

    testkitBranch = get_testkit_branch(driverName, driverTargetBranch)
    print("Testkit branch is {}".format(testkitBranch))

    check_call(["git", "fetch", remote], cwd=testkitRepoPath)
    check_call(["git", "checkout", "{}/{}".format(remote, testkitBranch)], cwd=testkitRepoPath)


    # Position on master to be able to remove temp branch
    #call(["git", "checkout", "master"], cwd=testkitRepoPath)
    # Checkout the branch named as a temporary to avoid having to pull but
    # delete it first to make sure it is up to date with the remote.k
    #localBranch = "tempForPr"
    #call(["git", "branch", "-D", localBranch], cwd=testkitRepoPath)
    #remoteBranch = "{}/{}".format(remote, testkitBranch)
    #check_call(
    #    ["git", "checkout", "-b", localBranch, remoteBranch],
    #    cwd=testkitRepoPath)

    # Run testkit
    #testkitEnv = {
    #    "TEST_DRIVER_NAME":  driverName,
    #    "TEST_DRIVER_REPO":  driverRepoPath,
    #    "TEST_IN_TEAMCITY":  "1",
    #    "TEST_BRANCH":       testkitBranch,
    #    "TEAMCITY_USER":     getenv("TEAMCITY_USER"),
    #    "TEAMCITY_PASSWORD": getenv("TEAMCITY_PASSWORD"),
    #}
    #check_call(
    #    ["python3", "main.py"],
    #    env=testkitEnv, cwd=testkitRepoPath, universal_newlines=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
