﻿#Remove-Item –path ./ –recurse
& java -jar swagger-codegen-cli-2.4.5.jar generate -i https://api.cloudmersive.com/swagger/api/ocr -l python -c packageconfig.json
$extrasetup = (Get-Content ./extrasetup.py) -join "`n"
Write-Host $extrasetup
(Get-Content ./setup.py).replace('# http://pypi.python.org/pypi/setuptools', $extrasetup) | Set-Content ./setup.py
(Get-Content ./setup.py).replace('"""\', "long_description,`n    long_description_content_type='text/markdown'") | Set-Content ./setup.py
(Get-Content ./setup.py).replace('The powerful Optical Character Recognition (OCR) APIs let you convert scanned images of pages into recognized text.  # noqa: E501', '') | Set-Content ./setup.py
(Get-Content ./setup.py).replace('    """', '') | Set-Content ./setup.py
Write-Host "Done."