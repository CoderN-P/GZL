#pragma once
#include "PrototypeExprAST.h"

class FunctionAST {
    std::unique_ptr<PrototypeExprAST> proto;
    std::unique_ptr<ExprAST> body;
public:
    FunctionAST(std::unique_ptr<PrototypeExprAST> proto, std::unique_ptr<ExprAST> body)
        : proto(std::move(proto)), body(std::move(body)) {}
};

