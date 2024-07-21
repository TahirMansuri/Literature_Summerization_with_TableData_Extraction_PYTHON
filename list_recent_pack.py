import os
import site
import datetime

def get_site_packages_path():
    return site.getsitepackages()[0]

def get_packages_installation_dates(site_packages_path):
    packages = []
    for root, dirs, files in os.walk(site_packages_path):
        for name in dirs:
            package_path = os.path.join(root, name)
            try:
                mtime = os.path.getmtime(package_path)
                install_date = datetime.datetime.fromtimestamp(mtime)
                packages.append((name, install_date))
            except Exception as e:
                print(f"Could not get install date for {name}: {e}")
    return packages

def list_recent_packages():
    site_packages_path = get_site_packages_path()
    packages = get_packages_installation_dates(site_packages_path)
    packages.sort(key=lambda x: x[1], reverse=True)

    for pkg, date in packages:
        print(f"{pkg}: {date}")

if __name__ == '__main__':
    list_recent_packages()
