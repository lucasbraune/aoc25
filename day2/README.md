# C++ Project Template

## Building and running

Initialize vcpkg submodule and generate build system (once):

```shell
git submodule update --init
mkdir -p build && cmake -B build
```

Build, test and run:

```shell
make test
make run
```

This regenerates the build system and downloads dependencies if necessary.

## LLVM tools

This project uses `clang-tidy` and `clang-format`, which can be installed on MacOS as follows:

```shell
brew install llvm
ln -s "$(brew --prefix llvm)/bin/clang-format" "/usr/local/bin/clang-format"
ln -s "$(brew --prefix llvm)/bin/git-clang-format" "/usr/local/bin/git-clang-format"
ln -s "$(brew --prefix llvm)/bin/clang-tidy" "/usr/local/bin/clang-tidy"
```

To reformat all source files, run

```shell
clang-format -i src/*
```

The build process runs `clang-tidy` with the appropriate options. Unfortunately,
running `clang-tidy src/* -p build` yields errors.
