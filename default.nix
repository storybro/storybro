{ pkgs ? import <nixpkgs> { } }:

with pkgs;

poetry2nix.mkPoetryApplication {
  projectDir = ./.;
  overrides = poetry2nix.overrides.withDefaults (self: super: {
    gsutil = super.gsutil.overridePythonAttrs
      (old: { nativeBuildInputs = [ self.importlib-metadata ]; });
    argcomplete = super.argcomplete.overridePythonAttrs
      (old: { nativeBuildInputs = [ self.importlib-metadata ]; });
    click-config-file = super.click-config-file.overridePythonAttrs
      (old: { nativeBuildInputs = [ self.pytest-runner ]; });
  });

}
