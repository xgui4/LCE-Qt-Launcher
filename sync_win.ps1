$version = $args[1]

$env:SETUPTOOLS_SCM_PRETEND_VERSION=$version; uv sync; $env:SETUPTOOLS_SCM_PRETEND_VERSION=$null