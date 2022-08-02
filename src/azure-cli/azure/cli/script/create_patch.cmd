cd "src\azure-cli\azure\cli\"
git diff dev..windows -- .\__main__.py > __main__.patch
git diff dev..windows -- .\fix\ > fix.patch
