#pragma once
#include "ExprAST.h"

class CallExprAST : public ExprAST {
    std::string callee;
    std::vector<std::unique_ptr<ExprAST>> args;
public:
    CallExprAST(std::string callee, std::vector<std::unique_ptr<ExprAST>> args)
        : callee(std::move(callee)), args(std::move(args)) {}
};

