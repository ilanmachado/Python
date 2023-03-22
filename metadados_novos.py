from importlib import metadata

# print(metadata.version('pip'))
#
# metadados_pip = metadata.metadata('pip')
#
# print(metadados_pip['Project-URL'])
#
# print(list(metadados_pip))

# print(len(metadata.files('pip')))

print(metadata.requires('django'))

