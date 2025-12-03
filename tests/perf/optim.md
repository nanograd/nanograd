# generate llvm bytecode
codon build -release -llvm -o npbench.ll npbench.codon 

# link bytecode against openblas and apply native cpu optimizations with max performance mode (LTO)
clang npbench.bc -o npbench -flto=full -Ofast -march=native -funroll-loops -fno-exceptions -fno-rtti -L/path/to/openblas -lopenblas


# collect perf profile
perf record -e cycles:u -j any,u -o perf.data -- ./npbench
perf2bolt -o bolt.fdata perf.data

# run bolt with perf profile (PLO)
llvm-bolt ./npbench -o npbench.bolt \
  -data=bolt.fdata \
  -reorder-blocks=cache+ \
  -reorder-functions=hfsort+ \
  -split-functions \
  -relocs \
  -icf=1

# test performance
./npbench.bolt
