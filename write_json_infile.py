with open("{}/Cloud_DA/PyQUBO4FDAU/notebook_files/{}".format(my_machine_path, file_to_execute),
                      "w+") as nf:
                json.dump(notebook_data, nf)
