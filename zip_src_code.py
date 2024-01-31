# coding: utf-8

"""
Script to zip BRSiOP 2

ignores a predefined list of folders and files
"""

import os
import pathlib
import zipfile


PACKAGING_ROOT = pathlib.Path(__file__).parent.parent.resolve()
version_name = "1.0.1"
zip_filename = f'brsiop2_{version_name}.zip'


# Insert full path
folders_to_ignore_from_root = [
]

folders_to_include = [
    os.path.join(".", "keycloak"),

    # os.path.join(".", "namingServer"),
    # os.path.join(".", "apiGateway"),
    # os.path.join(".", "storage"),

    os.path.join(".", "DB_Service"),
    os.path.join(".", "Algo_Management"),
    os.path.join(".", "CurveGen_Service"),
    os.path.join(".", "ExternalDataProvider_Service"),
    os.path.join(".", "Opt_Service"),

    # os.path.join(".", "frontend"),
    # todo: we should pack only what is needed instead of the entire src code
    os.path.join(".", "frontend", "static_homologation"),
]

empty_folders_to_include = [
    os.path.join(".", "DB_Service", "logs/"),
]

files_to_include = [
    os.path.join(".", "apiGateway", "target", "apiGateway-0.0.1-SNAPSHOT.jar"),
    os.path.join(".", "storage", "target", "storage-0.0.1-SNAPSHOT.jar"),
    os.path.join(".", "namingServer", "target", "namingServer-0.0.1-SNAPSHOT.jar"),

    os.path.join(".", "docker-compose_frontend_npm.yml"),
    os.path.join(".", "docker-compose_frontend_static.yml"),
    os.path.join(".", ".env"),
    os.path.join(".", "development.env"),
    os.path.join(".", "homologation.env"),

    os.path.join(".", "storage", "Dockerfile"),
    os.path.join(".", "apiGateway", "Dockerfile"),
    os.path.join(".", "namingServer", "Dockerfile"),
    os.path.join(".", "frontend", "Dockerfile_uvicorn"),
    os.path.join(".", "frontend", "Dockerfile_npm"),

    os.path.join(".", "frontend", "serve_frontend.py"),
    os.path.join(".", "frontend", "requirements.txt")
]

folders_to_ignore_everywhere = [
    "__pycache__",
    ".idea",
    ".git",
]

files_to_ignore = [
    ".gitignore",
    ".gitmodules"
]

extensions_to_ignore = [
    "zip",
    "log",
    "mr2"
]


def ignore_folder_from_root(dir_path=str()):
    if dir_path in folders_to_ignore_from_root:
        return True
    return False


def ignore_file(filename):
    if filename in files_to_ignore:
        return True
    if filename.split(".")[-1] in extensions_to_ignore:
        return True
    return False


def remove_ignored_folders_from_dirs_list(dirs):
    for ignored in folders_to_ignore_everywhere:
        if ignored in dirs:
            dirs.remove(ignored)


# Declare the function to return all file paths of a particular directory
def retrieve_file_paths(source_dir):
    filePaths = []

    # Read all directory, subdirectories and file lists
    for here, dirs, files in os.walk(source_dir):
        if ignore_folder_from_root(here):
            dirs[:] = []        # Prevents os.walk from descending further into the current dir if we already know we can ignore it
            continue
        remove_ignored_folders_from_dirs_list(dirs)
        for filename in files:
            # If not to filter files and folders, add to list
            if not ignore_file(filename):
                # Create the full filepath by using os module.
                filePath = os.path.join(here, filename)
                filePaths.append(filePath)
    return filePaths


def generate_zip_file():
    source = PACKAGING_ROOT
    target = os.path.join(PACKAGING_ROOT, zip_filename)

    print(f"Zipping contents of {source} to {target}")
    # Remove old zip files
    try:
        os.remove(target)
    except FileNotFoundError:
        pass

    os.chdir(source)
    source = "."

    list_paths = []
    #list_paths = list_paths + retrieve_file_paths(source)
    for folder in folders_to_include:
        files_in_folder = retrieve_file_paths(folder)
        list_paths = list_paths + files_in_folder
    list_paths = list_paths + files_to_include

    with zipfile.ZipFile(target, mode='w', compression=zipfile.ZIP_DEFLATED, strict_timestamps=False) as zf:
        for path in list_paths:
            zf.write(path)

        for dir_name in empty_folders_to_include:
            zif = zipfile.ZipInfo(dir_name)
            zf.writestr(zif, "")

    print(f"Zipping finished!")


if __name__ == "__main__":
    ZIP_DESTINATION = os.path.join(PACKAGING_ROOT, zip_filename)
    generate_zip_file()
