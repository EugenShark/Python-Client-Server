import yaml

data = {'list': ['l', 'i', 's', 't'], 'integer': 582, 'dict': {'a': '12€', 'b': 38}}
with open('file.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)
with open('file.yaml') as f_n:
    f_n_content = yaml.safe_load(f_n)
print(f_n_content)
