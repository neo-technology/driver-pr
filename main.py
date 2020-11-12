import sys
import re
from os import getenv
from os.path import abspath
from subprocess import check_call, call, check_output

remote = "remote"


def get_testkit_branch(driverName, driverTargetBranch):
    if driverName == "go" and driverTargetBranch in ['4.0', '4.1']:
        return "4.2"
    return driverTargetBranch


def main(testkitRepoPath, driverTargetBranch):
    testkitRepoPath = abspath(testkitRepoPath)
    driverName = getenv('TEST_DRIVER_NAME')
    print("Driver is {} and target branch is {}".format(
        driverName, driverTargetBranch))

    testkitBranch = get_testkit_branch(driverName, driverTargetBranch)
    print("Testkit branch is {}".format(testkitBranch))

    check_call(["git", "fetch", remote], cwd=testkitRepoPath)
    check_call(["git", "checkout", "{}/{}".format(remote, testkitBranch)], cwd=testkitRepoPath)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
