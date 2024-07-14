import pkg_resources

# Get a list of all installed packages
installed_packages = pkg_resources.working_set

# Print each package name and its version
for package in installed_packages:
    print(f"{package.key}=={package.version}")
