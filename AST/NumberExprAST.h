#pragma once
#include "ExprAST.h"


class NumberExprAST: public ExprAST
    double val;
public:
    explicit NumberExprAST(double val): val(val) {}
};


