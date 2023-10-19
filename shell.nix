{ sources ? import ./nix/sources.nix, rsources ? import (sources.mutwo-nix.outPath + "/nix/sources.nix"), pkgs ? import rsources.nixpkgs {}}:

let

  mutwo-ekmelily = import (sources.mutwo-nix.outPath + "/mutwo.ekmelily/default.nix") {};

  mypython = pkgs.python310.buildEnv.override {
    extraLibs = with pkgs.python310Packages; [
      mutwo-ekmelily
    ];
  };

in

  pkgs.mkShell {
      buildInputs = with pkgs; [
          mypython
          lilypond-with-fonts
      ];
  }
