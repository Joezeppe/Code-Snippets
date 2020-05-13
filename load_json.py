
### Example of loading JSON file into python dictionary

package_path = f"../../pypi_packages/{package_name}"
print(package_path)
with open(package_path,"r" ) as pck:
    package_dict = json.load(pck)
    print(package_dict)
