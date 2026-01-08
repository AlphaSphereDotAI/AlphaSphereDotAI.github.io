{
  pkgs,
  lib,
  ...
}: let
  yamllint_config = ".github/lint/.yamllint.yaml";
in {
  files.${yamllint_config}.yaml = {
    extends = "default";
    rules = {
      document-start = "disable";
      truthy = "disable";
      comments = "disable";
    };
  };
  # https://devenv.sh/basics/
  env = {
    UV_PYTHON_DOWNLOADS = lib.mkDefault "automatic";
    UV_PYTHON_PREFERENCE = lib.mkDefault "managed";
  };

  # https://devenv.sh/packages/
  packages = [];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    # version = "3.14";
    uv = {
      enable = true;
      sync.enable = true;
    };
  };

  # https://devenv.sh/processes/
  # processes.dev.exec = "${lib.getExe pkgs.watchexec} -n -- ls -la";

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/scripts/
  scripts = {
    build-web.exec = ''
      ${lib.getExe pkgs.uv} --version
      ${lib.getExe pkgs.python313Packages.reflex} --version
      ${lib.getExe pkgs.python313Packages.reflex} export --frontend-only --no-zip --env prod
    '';
    compatibility-check.exec = ''
      echo "Checking compatibility"
      ${lib.getExe pkgs.uv} sync --frozen --no-install-project
    '';
  };

  # https://devenv.sh/basics/
  enterShell = ''
    git --version # Use packages
  '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/git-hooks/
  git-hooks.hooks = {
    action-validator.enable = true;
    actionlint.enable = true;
    alejandra.enable = true;
    check-added-large-files.enable = true;
    check-builtin-literals.enable = true;
    check-case-conflicts.enable = true;
    check-docstring-first.enable = true;
    check-json.enable = true;
    check-merge-conflicts.enable = true;
    check-python.enable = true;
    check-toml.enable = true;
    check-vcs-permalinks.enable = true;
    check-xml.enable = true;
    check-yaml.enable = true;
    comrak.enable = true;
    deadnix.enable = true;
    detect-private-keys.enable = true;
    lychee.enable = true;
    markdownlint.enable = true;
    mixed-line-endings.enable = true;
    name-tests-test.enable = true;
    prettier.enable = true;
    python-debug-statements.enable = true;
    ripsecrets.enable = true;
    ruff.enable = true;
    ruff-format.enable = true;
    statix.enable = true;
    taplo.enable = true;
    trim-trailing-whitespace.enable = true;
    trufflehog.enable = true;
    uv-check.enable = true;
    # uv-export.enable = true;
    uv-lock.enable = true;
    yamllint = {
      enable = true;
      settings.configPath = yamllint_config;
    };
  };
  # See full reference at https://devenv.sh/reference/options/

  difftastic.enable = true;
}
