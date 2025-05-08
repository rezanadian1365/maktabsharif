import os
import platform
import subprocess
import shutil
import glob
import sys
import argparse

def system_monitor(verbose=False):
    print("Running system monitor...")
    if verbose:
        print("\n=== Verbose System Info ===")
        print(f"System: {platform.system()}")
        print(f"Node Name: {platform.node()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Machine: {platform.machine()}")
        print(f"Processor: {platform.processor()}\n")

        try:
            subprocess.run(["lscpu"], check=True)
            subprocess.run(["free", "-h"], check=True)
        except FileNotFoundError:
            print("One of the system commands (lscpu, free) was not found.")

def backup_dir(source, destination):
    print(f"Backing up from {source} to {destination}")
    if not os.path.exists(source):
        print("Source directory does not exist.")
        return
    if not os.path.exists(destination):
        os.makedirs(destination)
    try:
        shutil.copytree(source, os.path.join(destination, os.path.basename(source)), dirs_exist_ok=True)
        print("Backup completed.")
    except Exception as e:
        print(f"Error during backup: {e}")

def delete_empty(target_dir, recursive=False):
    print(f"Deleting empty directories in: {target_dir} (recursive={recursive})")
    if not os.path.isdir(target_dir):
        print("Target is not a directory.")
        return
    if recursive:
        for dirpath, dirnames, _ in os.walk(target_dir, topdown=False):
            for dirname in dirnames:
                full_path = os.path.join(dirpath, dirname)
                if not os.listdir(full_path):
                    os.rmdir(full_path)
                    print(f"Deleted: {full_path}")
    else:
        for entry in os.listdir(target_dir):
            full_path = os.path.join(target_dir, entry)
            if os.path.isdir(full_path) and not os.listdir(full_path):
                os.rmdir(full_path)
                print(f"Deleted: {full_path}")

def list_py(directory):
    print(f"Listing .py files in {directory}")
    pattern = os.path.join(directory, "*.py")
    for filepath in glob.glob(pattern):
        print(filepath)

def sys_info():
    print("System Information Summary:")
    print(f"Platform: {platform.platform()}")
    print(f"System: {platform.system()}")
    print(f"Python Version: {sys.version}")
    print(f"Executable: {sys.executable}")
    print(f"User: {os.getlogin()}")

def main():
    parser = argparse.ArgumentParser(description="Sysadmin Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # system-monitor
    monitor_parser = subparsers.add_parser("system-monitor")
    monitor_parser.add_argument("--verbose", action="store_true")

    # backup-dir
    backup_parser = subparsers.add_parser("backup-dir")
    backup_parser.add_argument("source")
    backup_parser.add_argument("destination")

    # delete-empty
    delete_parser = subparsers.add_parser("delete-empty")
    delete_parser.add_argument("target_dir")
    delete_parser.add_argument("--recursive", action="store_true")

    # list-py
    list_parser = subparsers.add_parser("list-py")
    list_parser.add_argument("directory")

    # sys-info
    subparsers.add_parser("sys-info")

    args = parser.parse_args()

    # Dispatch commands
    if args.command == "system-monitor":
        system_monitor(verbose=args.verbose)
    elif args.command == "backup-dir":
        backup_dir(args.source, args.destination)
    elif args.command == "delete-empty":
        delete_empty(args.target_dir, recursive=args.recursive)
    elif args.command == "list-py":
        list_py(args.directory)
    elif args.command == "sys-info":
        sys_info()

if __name__ == "__main__":
    main()
