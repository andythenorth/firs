import sys
import os

currentdir = os.curdir
import shutil

from polar_fox import git_info


def copy_docs_from_current_project():
    project_name = sys.argv[1]
    tag_name = git_info.get_tag_exact_match()
    print("Copying current docs to grf.farm src dir as", "'" + project_name + '/' + tag_name + "'")
    common_parent_path = os.path.dirname(os.path.dirname(os.path.abspath(currentdir)))
    grf_farm_path = os.path.join(common_parent_path, "grf.farm", "src", project_name)

    shutil.copytree(
        os.path.join(currentdir, "docs"), os.path.join(currentdir, tag_name)
    )
    try:
        shutil.move(os.path.join(currentdir, tag_name), grf_farm_path)
    except:
        # clean up local dir if moving failed
        shutil.rmtree(os.path.join(currentdir, tag_name))
        raise


def main():
    copy_docs_from_current_project()


if __name__ == "__main__":
    main()
