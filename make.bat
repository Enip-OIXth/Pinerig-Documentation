@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.\manual
set BUILDDIR=build


%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

if "%1" == "setup" (
	python -m venv ".venv"
	".venv\Scripts\pip" install pip --upgrade
	".venv\Scripts\pip" install -r "requirements.txt" --upgrade
	goto EOF
)

if "%1" == "latexpdf" (
	%SPHINXBUILD% -b latex %SPHINXOPTS% %O% "%SOURCEDIR%" "%BUILDDIR%\latex"
	cd "%BUILDDIR%\latex"
	make all-pdf
	cd %~dp0
	echo To view, run:
	echo   start "%BUILDDIR%\html\blender_manual.pdf"
	goto EOF
)

if "%1" == "check_syntax" (
	python tools\check_source\check_syntax.py --kbd --long
	goto EOF
)

if "%1" == "check_spelling" (
	python tools\check_source\check_spelling.py
	goto EOF
)



%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end


if "%1" == "" (
	%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
)

:end
popd
