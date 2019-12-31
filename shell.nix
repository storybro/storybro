with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "storybro";
  buildInputs = [
    readline
    which
    gcc
    binutils
    openssl
    libxml2
    libxslt

    aria2
    python36Packages.poetry
  ];
  src = null;
  PIPENV_VENV_IN_PROJECT=1;

  shellHook = ''
    # Allow the use of wheels.
    SOURCE_DATE_EPOCH=$(date +%s)

    # Augment the dynamic linker path
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${R}/lib/R/lib:${readline}/lib
  '';
}
