#Remove-Item –path ./ –recurse
& java -jar swagger-codegen-cli-2.4.5.jar generate -i https://api.cloudmersive.com/swagger/api/ocr -l python -c packageconfig.json
(Get-Content ./setup.py).replace('# http://pypi.python.org/pypi/setuptools', (Get-Content ./extrasetup.py)) | Set-Content ./setup.py