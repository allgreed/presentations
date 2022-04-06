let
  nixpkgs = builtins.fetchGit {
    # 2021-08-24
    url = "https://github.com/nixos/nixpkgs/";
    ref = "refs/heads/nixos-unstable";
    rev = "253aecf69ed7595aaefabde779aa6449195bebb7";
    # obtain via `git ls-remote https://github.com/nixos/nixpkgs nixos-unstable`
  };
  pkgs = import nixpkgs { config = {}; };
in
pkgs.mkShell {
  buildInputs =
  with pkgs;
  [
    nodejs
    yarn
    git
    gnumake
  ];
}
